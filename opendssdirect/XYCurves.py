# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_string_array,
    prepare_float64_array,
)


def Count():
    """(read-only) Number of XYCurves"""
    return CheckForError(lib.XYCurves_Get_Count())


def First():
    """Set first XYCurve active; returns 0 if none."""
    return CheckForError(lib.XYCurves_Get_First())


def Name(*args):
    """
    Get/set the name of the active XYCurve
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.XYCurves_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.XYCurves_Set_Name(Value))


def Next():
    """Sets next XYCurve active; returns 0 if no more."""
    return CheckForError(lib.XYCurves_Get_Next())


def Npts(*args):
    """Get/Set Number of points in X-Y curve"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_Npts())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_Npts(Value))


def XArray(*args):
    """Get/set X values as a Array of doubles. Set Npts to max number expected if setting"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.XYCurves_Get_Xarray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.XYCurves_Set_Xarray(ValuePtr, ValueCount))


def XScale(*args):
    """Factor to scale X values from original curve"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_Xscale())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_Xscale(Value))


def XShift(*args):
    """Amount to shift X value from original curve"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_Xshift())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_Xshift(Value))


def YArray(*args):
    """Get/Set Y values in curve; Set Npts to max number expected if setting"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.XYCurves_Get_Yarray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.XYCurves_Set_Yarray(ValuePtr, ValueCount))


def YScale(*args):
    """Factor to scale Y values from original curve"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_Yscale())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_Yscale(Value))


def YShift(*args):
    """Amount to shift Y valiue from original curve"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_Yshift())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_Yshift(Value))


def X(*args):
    """Set X value or get interpolated value after setting Y"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_x())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_x(Value))


def Y(*args):
    """Set Y value or get interpolated Y value after setting X"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_y())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_y(Value))


def AllNames():
    """(read-only) List of strings with all XYCurve names"""
    return CheckForError(get_string_array(lib.XYCurves_Get_AllNames))


def Idx(*args):
    """
    Get/set active XYCurve by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.XYCurves_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.XYCurves_Set_idx(Value))


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
    "Idx",
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
    "Idx",
    "AllNames",
]
