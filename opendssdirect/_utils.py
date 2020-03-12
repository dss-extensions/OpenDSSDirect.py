# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Import dss_python, exposing only OpenDSS v7 while v8 is still considered
# experimental (at least with Free Pascal)
import dss as dss_py
import numpy as np
import warnings

# Bind to the FFI module instance. This should be refined in a future version,
# especially after DSS C-API 0.11 is fully released.
lib = dss_py.v7.api_util.lib
ffi = dss_py.v7.api_util.ffi
api_util = dss_py.v7.api_util
codec = api_util.codec
CheckForError = dss_py.v7.DSS_IR.CheckForError
DSSException = dss_py._cffi_api_util.DSSException

# Currently, we prefer the functions that return lists (suffix 2)
# to keep higher compatibility with previous versions of OpenDSSDirect.py.

get_string = api_util.get_string
get_float64_array = api_util.get_float64_array2
get_int32_array = api_util.get_int32_array2
get_int8_array = api_util.get_int8_array2
get_string_array = api_util.get_string_array2
prepare_float64_array = api_util.prepare_float64_array
prepare_int32_array = api_util.prepare_int32_array
prepare_string_array = api_util.prepare_string_array
