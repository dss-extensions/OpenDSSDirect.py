import os
import ctypes
import sys
import struct
import json
import logging


logger = logging.getLogger('opendssdirect.core')

dir_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

with open(os.path.join(dir_path, 'schema.json')) as f:
    schema = json.loads(f.read())


class SAFEARRAYBOUND(ctypes.Structure):
    _fields_ = [
        ('cElements', ctypes.c_uint32),
        ('lLbound', ctypes.c_long),
    ]


class SAFEARRAY(ctypes.Structure):
    _fields_ = [
        ('cDims', ctypes.c_ushort),
        ('fFeatures', ctypes.c_ushort),
        ('cbElements', ctypes.c_uint32),
        ('cLocks', ctypes.c_uint32),
        ('pvData', ctypes.c_void_p),
        ('rgsabound', SAFEARRAYBOUND * 1),
    ]


class VArg(ctypes.Structure):
    _fields_ = [
        ('dtype', ctypes.c_uint64),
        ('p', ctypes.POINTER(None)),
        ('dum1', ctypes.c_uint64),
        ('dum2', ctypes.c_uint64),
    ]


class VarArray(ctypes.Structure):
    _fields_ = [
        ('dimcount', ctypes.c_uint8),
        ('flags', ctypes.c_uint8),
        ('elementsize', ctypes.c_uint32),
        ('lockcount', ctypes.c_uint32),
        ('data', ctypes.POINTER(None)),
        ('length', ctypes.c_uint),
        ('lbound', ctypes.c_uint),
    ]


mapping = {
    u'longint': ctypes.c_int32,
    u'longword': ctypes.c_uint32,
    u'pansichar': ctypes.c_char_p,
    u'double': ctypes.c_double,
    u'integer': ctypes.c_int,
    u'pcomplexarray': ctypes.POINTER(ctypes.POINTER(ctypes.c_double * 2)),
    u'pintegerarray': ctypes.POINTER(ctypes.POINTER(ctypes.c_double * 2)),
    u'pnodevarray': ctypes.POINTER(ctypes.POINTER(ctypes.c_double * 2)),
    u'variant': ctypes.POINTER(VArg),
}


def is_delphi():
    if 'darwin' in sys.platform or 'linux' in sys.platform:
        return False
    else:
        return True


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

    setup_library(library)

    return library


def check_library(library):

    # Start DSS engine
    success = library.DSSI(3, 0)

    if not success == 1:
        error_description = library.ErrorDesc()
        raise ImportError("Could not start OpenDSS: " + error_description)

    # Set forms to False
    library.DSSI(8, 0)

    # Verify forms are False
    if library.DSSI(7) != 1:
        raise ImportError("Unable to turn off forms")


def setup_library(library):
    for f in schema['interface']:
        if f['return_type']:
            getattr(library, f['name']).restype = mapping[f['return_type'].lower()]
        else:
            getattr(library, f['name']).restype = None

        if f['args']:
            getattr(library, f['name']).argtypes = tuple(mapping[arg.lower()] for arg in f['args'])

    directory = os.path.abspath(os.path.expanduser(os.getenv('OPENDSSDIRECTPY_DATAPATH', '.')))
    if not os.path.exists(directory):
        os.makedirs(directory)
    logger.debug("Setting datapath for OpenDSS to {}".format(directory))
    library.DSSS(3, directory.encode('ascii'))


def is_x64():
    return 8 * struct.calcsize("P") == 64
