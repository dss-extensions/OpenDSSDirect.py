# Import dss_python
import dss as dss_py
from .Iterable import Iterable, Base

# Bind to the FFI module instance. This should be refined in a future version
lib = dss_py.prime_api_util.lib
ffi = dss_py.prime_api_util.ffi
api_util = dss_py.prime_api_util
codec = api_util.codec
CheckForError = dss_py.DSS_GR.CheckForError
DSSException = dss_py._cffi_api_util.DSSException
