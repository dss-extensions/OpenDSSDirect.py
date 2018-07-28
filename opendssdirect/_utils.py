from __future__ import absolute_import

# Exposing only v7 while v8 is still considered experimental
from dss._dss_capi_v7 import ffi, lib

from dss._cffi_api_util import *
import numpy as np
import warnings

# Bind to the FFI module instance
# Currently, we prefer list to keep higher compatibility with previous 
# versions of OpenDSSDirect.py. 

api_util = CffiApiUtil(ffi, lib)
get_string = api_util.get_string
get_float64_array = api_util.get_float64_array2
get_int32_array = api_util.get_int32_array2
get_int8_array = api_util.get_int8_array2
get_string_array = api_util.get_string_array2
prepare_float64_array = api_util.prepare_float64_array
prepare_int32_array = api_util.prepare_int32_array
prepare_string_array = api_util.prepare_string_array
