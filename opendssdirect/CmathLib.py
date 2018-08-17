# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_float64_array


def cabs(realpart, imagpart):
    """(read-only) Return abs value of complex number given in real and imag doubles"""
    return lib.CmathLib_Get_cabs(realpart, imagpart)


def cdang(RealPart, ImagPart):
    """(read-only) Returns the angle, in degrees, of a complex number specified as two doubles: Realpart and imagpart."""
    return lib.CmathLib_Get_cdang(RealPart, ImagPart)


def cdiv(a1, b1, a2, b2):
    """(read-only) Divide two complex number: (a1, b1)/(a2, b2). Returns array of two doubles representing complex result."""
    return get_float64_array(lib.CmathLib_Get_cdiv, a1, b1, a2, b2)


def cmplx(RealPart, ImagPart):
    """(read-only) Convert real and imaginary doubles to Array of doubles"""
    return get_float64_array(lib.CmathLib_Get_cmplx, RealPart, ImagPart)


def cmul(a1, b1, a2, b2):
    """(read-only) Multiply two complex numbers: (a1, b1) * (a2, b2). Returns result as a array of two doubles."""
    return get_float64_array(lib.CmathLib_Get_cmul, a1, b1, a2, b2)


def ctopolardeg(RealPart, ImagPart):
    """(read-only) Convert complex number to magnitude and angle, degrees. Returns array of two doubles."""
    return get_float64_array(lib.CmathLib_Get_ctopolardeg, RealPart, ImagPart)


def pdegtocomplex(magnitude, angle):
    """(read-only) Convert magnitude, angle in degrees to a complex number. Returns Array of two doubles."""
    return get_float64_array(lib.CmathLib_Get_pdegtocomplex, magnitude, angle)


_columns = []
__all__ = ["cabs", "cdang", "cdiv", "cmplx", "cmul", "ctopolardeg", "pdegtocomplex"]
