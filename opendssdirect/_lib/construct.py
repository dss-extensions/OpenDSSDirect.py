from __future__ import absolute_import, print_function
from builtins import open
import os
import sys
import json
from collections import OrderedDict
from functools import partial

from ..compat import ModuleType

from .core import load_library


# Global modules and classes that can be populated by functions
modules = OrderedDict()
functions = OrderedDict()


# Use dir_path to locate interface.json
dir_path = os.path.dirname(os.path.realpath(__file__))


# Read interface.json and create interfaces
with open(os.path.join(dir_path, 'interface.json'), encoding='utf-8') as f:
    interface = json.loads(f.read())


library = None


def construct():

    global library

    library = load_library()

    create_modules()

    create_functions(library)

    for name, f in functions.items():
        module_name = '.'.join(name.split('.')[:-1])
        function_name = name.split('.')[-1]
        setattr(modules[module_name], function_name, f)

    for name, m in modules.items():
        sys.modules[name] = m

    return modules


def create_modules():

    for m in interface['modules']:
        name = 'opendssdirect.' + (m['name'])
        modules[name] = ModuleType(name)


def create_functions(library):

    for m in interface['modules']:

        module_name = 'opendssdirect.' + (m['name'])
        for function in m['functions']:

            f = getattr(library, function['library_function_name'])

            f = partial(f, *function['args'])

            f.__name__ = function['name']
            f.__module__ = module_name
            f.__doc__ = function['doc']

            functions[f.__module__ + '.' + f.__name__] = f


def caller_function(f, *args):
    return f(*args)
