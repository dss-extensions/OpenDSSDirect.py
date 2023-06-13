# Import dss_python
import dss as dss_py
import numpy as np
import warnings

# Bind to the FFI module instance. This should be refined in a future version
lib = dss_py.prime_api_util.lib
ffi = dss_py.prime_api_util.ffi
api_util = dss_py.prime_api_util
codec = api_util.codec
CheckForError = dss_py.DSS_GR.CheckForError
DSSException = dss_py._cffi_api_util.DSSException
Base = dss_py._cffi_api_util.Base

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
