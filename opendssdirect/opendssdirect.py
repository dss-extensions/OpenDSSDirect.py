# import ctypes
# import numpy as np
# 
# from ._lib import load_library
# from ._lib import setup_class as __s_c
# 
# 
# class OpenDSSDirect(object):
# 
#     _lib= load_library()
# 
#     def getI(self):
# 
#         library = self._lib
# 
#         z = ctypes.POINTER(ctypes.c_double * 2)()
# 
#         library.getIpointer(z)
# 
#         data = np.ctypeslib.as_array((ctypes.c_double * 2 * (library.CircuitI(2, 0) + 1)).from_address(ctypes.addressof(z.contents)))
#         arr = np.vectorize(complex)(data[..., 0], data[..., 1])
# 
#         return arr
# 
# 
# __s_c(OpenDSSDirect)
