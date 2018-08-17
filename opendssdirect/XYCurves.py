# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_float64_array, prepare_float64_array
from ._utils import codec


def Count():
    """(read-only) Number of XYCurve Objects"""
    return lib.XYCurves_Get_Count()


def First():
    """(read-only) Sets first XYcurve object active; returns 0 if none."""
    return lib.XYCurves_Get_First()


def Name(*args):
    """
    (read) Name of active XYCurve Object
    (write) Get Name of active XYCurve Object
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.XYCurves_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.XYCurves_Set_Name(Value)


def Next():
    """(read-only) Advances to next XYCurve object; returns 0 if no more objects of this class"""
    return lib.XYCurves_Get_Next()


def Npts(*args):
    """Get/Set Number of points in X-Y curve"""
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_Npts()

    # Setter
    Value, = args
    lib.XYCurves_Set_Npts(Value)


def XArray(*args):
    """Get/Set X values as a Array of doubles. Set Npts to max number expected if setting"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.XYCurves_Get_Xarray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.XYCurves_Set_Xarray(ValuePtr, ValueCount)


def XScale(*args):
    """Factor to scale X values from original curve"""
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_Xscale()

    # Setter
    Value, = args
    lib.XYCurves_Set_Xscale(Value)


def XShift(*args):
    """Amount to shift X value from original curve"""
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_Xshift()

    # Setter
    Value, = args
    lib.XYCurves_Set_Xshift(Value)


def YArray(*args):
    """Get/Set Y values in curve; Set Npts to max number expected if setting"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.XYCurves_Get_Yarray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.XYCurves_Set_Yarray(ValuePtr, ValueCount)


def YScale(*args):
    """
    (read) Factor to scale Y values from original curve
    (write) Amount to scale Y values from original curve. Represents a curve shift.
    """
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_Yscale()

    # Setter
    Value, = args
    lib.XYCurves_Set_Yscale(Value)


def YShift(*args):
    """amount to shift Y valiue from original curve"""
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_Yshift()

    # Setter
    Value, = args
    lib.XYCurves_Set_Yshift(Value)


def X(*args):
    """Set X value or get interpolated value after setting Y"""
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_x()

    # Setter
    Value, = args
    lib.XYCurves_Set_x(Value)


def Y(*args):
    """
    (read) Y value for present X or set this value then get corresponding X
    (write) Set Y value or get interpolated Y value after setting X
    """
    # Getter
    if len(args) == 0:
        return lib.XYCurves_Get_y()

    # Setter
    Value, = args
    lib.XYCurves_Set_y(Value)


_columns = [
    "Name",
    "Npts",
    "XArray",
    "XScale",
    "XShift",
    "YArray",
    "YScale",
    "YShift",
    "X",
    "Y",
]
__all__ = [
    "Count",
    "First",
    "Name",
    "Next",
    "Npts",
    "XArray",
    "XScale",
    "XShift",
    "YArray",
    "YScale",
    "YShift",
    "X",
    "Y",
]
