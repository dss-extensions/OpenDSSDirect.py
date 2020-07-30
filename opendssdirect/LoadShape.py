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


def New(Name):
    if type(Name) is not bytes:
        Name = Name.encode(codec)
    return CheckForError(lib.LoadShapes_New(Name))


def Normalize():
    CheckForError(lib.LoadShapes_Normalize())


def AllNames():
    """(read-only) List of strings with all LoadShape names"""
    return CheckForError(get_string_array(lib.LoadShapes_Get_AllNames))


def Count():
    """(read-only) Number of LoadShapes"""
    return CheckForError(lib.LoadShapes_Get_Count())


def First():
    """Set first LoadShape active; returns 0 if none."""
    return CheckForError(lib.LoadShapes_Get_First())


def HrInterval(*args):
    """Fixed interval time value, hours."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_HrInterval())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_HrInterval(Value))


def MinInterval(*args):
    """Fixed Interval time value, in minutes"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_MinInterval())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_MinInterval(Value))


def Name(*args):
    """
    Get/set the name of the active LoadShape
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.LoadShapes_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.LoadShapes_Set_Name(Value))


def Next():
    """Sets next LoadShape active; returns 0 if no more."""
    return CheckForError(lib.LoadShapes_Get_Next())


def Npts(*args):
    """Get/set Number of points in active Loadshape."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_Npts())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_Npts(Value))


def PBase(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_PBase())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_PBase(Value))


def PMult(*args):
    """Array of doubles for the P multiplier in the Loadshape."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_Pmult)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount))


def QBase(*args):
    """Base for normalizing Q curve. If left at zero, the peak value is used."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_Qbase())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_Qbase(Value))


def QMult(*args):
    """Array of doubles containing the Q multipliers."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_Qmult)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount))


def TimeArray(*args):
    """Time array in hours correscponding to P and Q multipliers when the Interval=0."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_TimeArray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount))


def UseActual(*args):
    """Boolean flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_UseActual()) != 0

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_UseActual(Value))


def SInterval(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_sInterval())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_Sinterval(Value))


def Idx(*args):
    """
    Get/set active LoadShape by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LoadShapes_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.LoadShapes_Set_idx(Value))


_columns = [
    "HrInterval",
    "MinInterval",
    "Name",
    "Npts",
    "PBase",
    "PMult",
    "QBase",
    "QMult",
    "TimeArray",
    "UseActual",
    "SInterval",
    "Idx",
]
__all__ = [
    "New",
    "Normalize",
    "AllNames",
    "Count",
    "First",
    "HrInterval",
    "MinInterval",
    "Name",
    "Next",
    "Npts",
    "PBase",
    "PMult",
    "QBase",
    "QMult",
    "TimeArray",
    "UseActual",
    "SInterval",
    "Idx",
]
