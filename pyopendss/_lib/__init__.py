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

    return library


def is_x64():
    return 8 * struct.calcsize("P") == 64
