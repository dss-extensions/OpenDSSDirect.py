from __future__ import absolute_import, print_function
from builtins import open
import os
import sys
import json
from collections import OrderedDict

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

    create_functions()

    for name, m in modules.items():
        sys.modules[name] = m


def create_modules():

    for m in interface['modules']:
        modules[m['name']] = ModuleType('opendssdirect.' + (m['name']))


def create_functions():

    pass
