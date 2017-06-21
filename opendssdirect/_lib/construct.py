from __future__ import absolute_import, print_function
from builtins import open
import os
import sys
import json
from collections import OrderedDict
from functools import partial
import ctypes

from ..compat import ModuleType

from .core import load_library
from .core import VArg, VarArray, is_x64, is_delphi


# Global modules and classes that can be populated by functions
modules = OrderedDict()
functions = OrderedDict()


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


def construct():

    library = load_library()

    create_modules()

    create_functions(library)

    for name, f in functions.items():
        module_name = '.'.join(name.split('.')[:-1])
        function_name = name.split('.')[-1]
        setattr(modules[module_name], function_name, f)

    for name, m in modules.items():
        sys.modules[name] = m

    return modules, library


def create_modules():

    for m in interface['modules']:
        name = 'opendssdirect.' + (m['name'])
        modules[name] = ModuleType(name)


def create_functions(library):

    for m in interface['modules']:

        module_name = 'opendssdirect.' + (m['name'])
        for function in m['functions']:

            f = getattr(library, function['library_function_name'])

            f = generate_function(f, function)

            f.__name__ = function['name']
            f.__module__ = module_name
            f.__doc__ = function['doc']

            functions[f.__module__ + '.' + f.__name__] = f


def generate_function(f, function):
    if function['args'][-1] is None:
        f = partial(caller_function, f=f)
    else:
        f = partial(f, *function['args'])
    return f


def caller_function(f):

    varg = VArg(0, None, 0, 0)

    p = ctypes.POINTER(VArg)(varg)

    f(0, p)

    var_arr = ctypes.cast(varg.p, ctypes.POINTER(VarArray)).contents

    l = list()

    if varg.dtype == 0x2008:

        data = ctypes.cast(var_arr.data, ctypes.POINTER(POINTER * var_arr.length))

        for s in data.contents:

            length = ctypes.cast(s - HEADER_SIZE, ctypes.POINTER(ctypes.c_uint8)).contents.value

            s = ctypes.cast(s, ctypes.POINTER(ctypes.c_int16 * length))

            l.append(''.join([chr(x).decode('ascii') for x in s.contents[:]]))

    else:

        import warnings
        warnings.warn("Unsupported dtype. Contact developer")

    return l
