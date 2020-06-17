# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_int32_array,
    get_string_array,
    prepare_float64_array,
    prepare_int32_array,
)


def AllNames():
    """(read-only) List of strings with all LineGeometrie names"""
    return get_string_array(lib.LineGeometries_Get_AllNames)


def Count():
    """(read-only) Number of LineGeometries"""
    return lib.LineGeometries_Get_Count()


def Idx(*args):
    """
    Get/set active LineGeometrie by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.LineGeometries_Set_idx(Value))


def First():
    """Set first LineGeometrie active; returns 0 if none."""
    return lib.LineGeometries_Get_First()


def Next():
    """Sets next LineGeometrie active; returns 0 if no more."""
    return lib.LineGeometries_Get_Next()


def Name(*args):
    """
    Get/set the name of the active LineGeometrie
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.LineGeometries_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    CheckForError(lib.LineGeometries_Set_Name(Value))


def Conductors():
    """(read-only) Array of strings with names of all conductors in the active LineGeometry object"""
    return get_string_array(lib.LineGeometries_Get_Conductors)


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_EmergAmps()

    # Setter
    Value, = args
    lib.LineGeometries_Set_EmergAmps(Value)
    CheckForError()


def NormAmps(*args):
    """Normal ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_NormAmps()

    # Setter
    Value, = args
    lib.LineGeometries_Set_NormAmps(Value)
    CheckForError()


def RhoEarth(*args):
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_RhoEarth()

    # Setter
    Value, = args
    lib.LineGeometries_Set_RhoEarth(Value)
    CheckForError()


def Reduce(*args):
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_Reduce() != 0

    # Setter
    Value, = args
    lib.LineGeometries_Set_Reduce(Value)
    CheckForError()


def Phases(*args):
    """Number of Phases"""
    # Getter
    if len(args) == 0:
        return lib.LineGeometries_Get_Phases()

    # Setter
    Value, = args
    lib.LineGeometries_Set_Phases(Value)
    CheckForError()


def Rmatrix(Frequency, Length, Units):
    """(read-only) Resistance matrix, ohms"""
    return get_float64_array(lib.LineGeometries_Get_Rmatrix, Frequency, Length, Units)


def Xmatrix(Frequency, Length, Units):
    """(read-only) Reactance matrix, ohms"""
    return get_float64_array(lib.LineGeometries_Get_Xmatrix, Frequency, Length, Units)


def Zmatrix(Frequency, Length, Units):
    """(read-only) Complex impedance matrix, ohms"""
    return get_float64_array(lib.LineGeometries_Get_Zmatrix, Frequency, Length, Units)


def Cmatrix(Frequency, Length, Units):
    """(read-only) Capacitance matrix, nF"""
    return get_float64_array(lib.LineGeometries_Get_Cmatrix, Frequency, Length, Units)


def Units(*args):
    # Getter
    if len(args) == 0:
        return get_int32_array(lib.LineGeometries_Get_Units)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_int32_array(Value)
    lib.LineGeometries_Set_Units(ValuePtr, ValueCount)
    CheckForError()


def Xcoords(*args):
    """Get/Set the X (horizontal) coordinates of the conductors"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineGeometries_Get_Xcoords)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount)
    CheckForError()


def Ycoords(*args):
    """Get/Set the Y (vertical/height) coordinates of the conductors"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineGeometries_Get_Ycoords)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount)
    CheckForError()


_columns = [
    "Name",
    "Idx",
    "Phases",
    "RhoEarth",
    "Reduce",
    "Units",
    "Conductors",
    "Xcoords",
    "Ycoords",
    "Rmatrix",
    "Xmatrix",
    "Zmatrix",
    "NormAmps",
    "EmergAmps",
]
__all__ = [
    "Conductors",
    "EmergAmps",
    "NormAmps",
    "RhoEarth",
    "Reduce",
    "Phases",
    "Rmatrix",
    "Xmatrix",
    "Zmatrix",
    "Cmatrix",
    "Units",
    "Xcoords",
    "Ycoords",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
