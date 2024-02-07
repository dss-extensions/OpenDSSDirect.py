# Import dss_python
import dss as dss_py
import os

# Integrate "Use environment variable for numpy version" from @kdheepak
# https://github.com/dss-extensions/OpenDSSDirect.py/pull/103/
OPENDSSDIRECT_PY_USE_NUMPY = os.environ.get("OPENDSSDIRECT_PY_USE_NUMPY", "0").upper() in ("1", "TRUE")

# Bind to the FFI module instance. This should be refined in a future version
lib = dss_py.prime_api_util.lib
ffi = dss_py.prime_api_util.ffi

api_util = dss_py.prime_api_util
DSSException = dss_py.DSSException
