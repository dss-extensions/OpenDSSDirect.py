import os
import ctypes
import sys
import struct


dir_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))


def load_library():

    curdir = os.path.abspath(os.curdir)

    if is_x64():
        architecture = 'x64'
    else:
        architecture = 'x32'

    if 'darwin' in sys.platform:
        platform = 'darwin'
        libklusolve = '../libklusolve.dylib'
        libopendssdirect = 'libopendssdirect.dylib'
        DLL = ctypes.CDLL

    elif 'linux' in sys.platform:
        platform = 'linux'
        libklusolve = None
        libopendssdirect = 'libopendssdirect.so'
        DLL = ctypes.CDLL

    elif 'win' in sys.platform:
        platform = 'windows'
        libklusolve = 'KLUSolve.dll'
        libopendssdirect = 'OpenDSSDirect.dll'
        DLL = ctypes.WinDLL

    else:
        raise ImportError("Unsupported platform: {}".format(sys.platform))

    if libklusolve is not None:
        libklusolve = os.path.abspath(os.path.join(dir_path, platform, architecture, libklusolve))
        DLL(libklusolve)

    libopendssdirect = os.path.abspath(os.path.join(dir_path, platform, architecture, libopendssdirect))
    library = DLL(libopendssdirect)

    os.chdir(curdir)

    check_library(library)

    return library


def check_library(library):

    success = int(library.DSSI(ctypes.c_int32(3), ctypes.c_int32(0)))
    library.ErrorDesc.restype = ctypes.c_char_p

    if not success == 1:
        error_description = ctypes.c_char_p(library.ErrorDesc()).value
        raise ImportError("Could not start OpenDSS: " + error_description)


def is_x64():
    return 8 * struct.calcsize("P") == 64
