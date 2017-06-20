# -*- coding: utf-8 -*-

"""
ditto.core.compat
This module handles compatibility issues between Python 2 and Python 3.
"""

import types


import sys

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)


if is_py2:
    def ModuleType(m):
        return types.ModuleType(m.encode('utf-8'))

else:
    def ModuleType(m):
        return types.ModuleType(m)
