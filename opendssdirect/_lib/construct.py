from __future__ import absolute_import, print_function
from builtins import open
import os
import sys
import json
from collections import OrderedDict
from functools import partial
import ctypes
import logging

from .._compat import ModuleType, is_py2

from .core import load_library
from .core import VArg, VarArray, is_x64, is_delphi


logger = logging.getLogger('opendssdirect.core')

try:
    import pandas as pd
    import numpy as np
except ImportError:
    logger.warning("Unable to import pandas and numpy. Monitors.ByteStream may not work as expected")


# Global modules and classes that can be populated by functions
g_modules = OrderedDict()
g_functions = OrderedDict()


# Use dir_path to locate interface.json
dir_path = os.path.dirname(os.path.realpath(__file__))


# Read interface.json and create interfaces
with open(os.path.join(dir_path, 'interface.json'), encoding='utf-8') as f:
    interface = json.loads(f.read())


if is_delphi():
    HEADER_SIZE = 4  # Windows
else:
    HEADER_SIZE = 8  # OSX and LINUX

if is_x64():
    POINTER = ctypes.c_int64
else:
    POINTER = ctypes.c_int32


def construct(modules=None, functions=None):
    if modules is None:
        modules = g_modules
    if functions is None:
        functions = g_functions

    library = load_library()

    create_modules(modules)

    create_functions(library, functions)

    module = populate_modules(modules, functions)

    module.dss_lib = library

    return(module, modules)


def populate_modules(modules, functions):
    for name, f in functions.items():
        module_name = '.'.join(name.split('.')[:-1])
        function_name = name.split('.')[-1]
        logger.debug(
            "Populating {module_name} with {function_name}".format(
                module_name=module_name,
                function_name=function_name
            )
        )
        setattr(modules[module_name], function_name, f)

    module = modules['opendssdirect.dss'] = ModuleType('opendssdirect.dss')

    for name, m in modules.items():
        module_name = name.split('.')[-1]
        setattr(module, module_name, m)

    return module


def update_sys_modules(modules):
    for name, m in modules.items():
        if not is_py2:
            sys.modules[name] = m


def create_modules(modules):

    for m in interface['modules']:
        name = 'opendssdirect.dss.' + (m['name'])
        modules[name] = ModuleType(name)


def create_functions(library, functions):

    for m in interface['modules']:

        module_name = 'opendssdirect.dss.' + (m['name'])
        for function in m['functions']:

            if function['enabled'] is True:

                f = generate_function(library, function, module_name)

                f.__name__ = function['name']
                f.__module__ = module_name
                f.__doc__ = function['doc']

                functions[f.__module__ + '.' + f.__name__] = f


def generate_function(library, function, module_name):

    if is_py2:
        name = function['name'].encode('ascii')
    else:
        name = function['name']

    klass = type(
        name,
        (FunctionMocker, ),
        {
            '__module__': module_name,
            '__doc__': function['doc'],
            '__name__': function['name'],
        }
    )

    c = klass(library, function)

    return c


class FunctionMocker(object):

    def __init__(self, library, function):

        self.__function = function
        self.__handle = getattr(library, function['library_function_name'])
        self.__args = function['args']

        self.__setup_callback()

    def __setup_callback(self):

        if self.__function['function_type'] == 'VarArrayFunction':
            mode = 0
            self.__callback = partial(
                VarArrayFunction,
                f=self.__handle,
                mode=self.__function['args'][mode]['dss_args'][0],
                optional=self.__function['args'][mode]['dss_args'][-1],  # Use last element, since it can be null or 0, for those optional 3 argument functions
                name=self.__function['library_function_name']
            )

        else:
            modes = [a['dss_args'][0] for a in self.__function['args']]
            args = [a['dss_args'][1] for a in self.__function['args']]
            self.__callback = partial(
                CtypesFunction,
                f=self.__handle,
                modes=modes,
                args=args,
                name=self.__function['library_function_name'],
            )

        self.__max_user_args = max([x['user_args'] for x in self.__function['args']])
        self.__min_user_args = min([x['user_args'] for x in self.__function['args']])

    def __repr__(self):

        return '<function {module_name}.{function_name}>'.format(
            module_name=self.__class__.__module__,
            function_name=self.__name__
        )

    def __call__(self, *args, **kwargs):
        if len(args) > self.__max_user_args or len(args) < self.__min_user_args:
            if self.__max_user_args == self.__min_user_args:
                error_msg = 'Expected {user_args} number of arguments'.format(
                    user_args=self.__max_user_args,
                )
            else:
                error_msg = 'Expected {min_user_args} <= number of arguments <= {max_user_args}'.format(
                    min_user_args=self.__min_user_args,
                    max_user_args=self.__max_user_args,
                )
            logger.warn("Incorrect calling signature for {name}. {error_msg} but received {length} (args={args}).".format(
                name=self.__name__,
                error_msg=error_msg,
                length=len(args),
                args=args,
            ))

        r = self.__callback(*args)

        return r


def CtypesFunction(dss_arg=None, f=None, modes=None, args=None, name=None, user_args=0):

    if dss_arg is None:
        # First mode should be used
        dss_arg = args[0]
        mode = modes[0]
    else:
        # Second mode should be used
        mode = modes[-1]

    logger.debug("Calling function {} with arguments {}".format(name, (mode, dss_arg)))

    if isinstance(dss_arg, str):
        dss_arg = dss_arg.encode('ascii')

    r = f(mode, dss_arg)

    if isinstance(r, bytes):
        r = r.decode('ascii')

    return r


def VarArrayFunction(f, mode, name, optional):

    varg = VArg(0, None, 0, 0)

    p = ctypes.POINTER(VArg)(varg)

    if optional is not None:
        f(mode, p, optional)
    else:
        logger.debug("Calling function {} with arguments {}".format(name, (mode, p)))
        f(mode, p)

    logger.debug("Successively called and returned from function {}".format(name))

    var_arr = ctypes.cast(varg.p, ctypes.POINTER(VarArray)).contents

    l = list()

    if varg.dtype == 0x2008 and var_arr.length != 0:  # CString

        data = ctypes.cast(var_arr.data, ctypes.POINTER(POINTER * var_arr.length))

        for s in data.contents:

            if s == 0:
                continue
            else:
                length = ctypes.cast(s - HEADER_SIZE, ctypes.POINTER(ctypes.c_uint8)).contents.value
                if is_delphi():
                    length = int(length / 2)
                s = ctypes.cast(s, ctypes.POINTER(ctypes.c_int16 * length))
                s = u''.join([chr(x) for x in s.contents[:]])
                if s.lower() != 'none':
                    l.append(s)

    elif varg.dtype == 0x2005 and var_arr.length != 0:  # Float64

        data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_double * var_arr.length))

        # Converting CFloat to Python float, more efficiency could be gained by using NumPy
        # TODO: Consider making numpy/pandas a dependency?
        for i in data.contents:
            l.append(i)

    elif varg.dtype == 0x2003 and var_arr.length != 0:  # Int32

        data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32 * var_arr.length))

        # Converting CInt32 to Python float, more efficiency could be gained by using NumPy
        # TODO: Consider making numpy/pandas a dependency?
        for i in data.contents:
            l.append(i)

    elif varg.dtype == 0x2011 and var_arr.length != 0:

        signature = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32)).contents.value

        if signature != 43756:
            logger.warning("ByteStream did not contain expected signature. Found {} but expected 43756".format(signature))
        else:
            # data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32 * 4))
            # signature, version, size, mode = data.contents

            p = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32))

            a_ptr = ctypes.cast(p, ctypes.c_void_p)

            a_ptr.value += ctypes.sizeof(p._type_)
            version = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value

            a_ptr.value += ctypes.sizeof(p._type_)
            size = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value

            a_ptr.value += ctypes.sizeof(p._type_)
            mode = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value

            logger.debug("version={version}, size={size}, mode={mode}".format(version=version, size=size, mode=mode))

            a_ptr.value += ctypes.sizeof(p._type_)
            header = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_char * 256)).contents.value
            header = [i.strip() for i in header.decode('ascii').strip().rstrip(',').split(',')]

            a_ptr.value = a_ptr.value + 256 * ctypes.sizeof(ctypes.c_char)
            count = (var_arr.length - 272) / 4 / (size + 2)

            if int(count) != count:
                logger.error(
                    "Expected count to be integer but found count={count}".format(
                        count=count,
                    )
                )
            else:
                count = int(count)

            data = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_float * (size + 2) * count))

            for row in data.contents[:]:
                for i, v in enumerate(row[:]):
                    l.append(v)

            try:
                l = np.array(l).reshape([-1, len(header)])
                l = pd.DataFrame(l, columns=header)
            except NameError:
                l = [l, header]

    elif var_arr.length == 0:

        logger.warning("Empty var_arr found")

    else:

        logger.warning("Unsupported dtype {} returned for {}. Please contact developer".format(varg.dtype, name))

    return l
