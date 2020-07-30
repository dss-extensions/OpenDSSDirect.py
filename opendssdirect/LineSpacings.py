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


def AllNames():
    """(read-only) List of strings with all LineSpacing names"""
    return CheckForError(get_string_array(lib.LineSpacings_Get_AllNames))


def Count():
    """(read-only) Number of LineSpacings"""
    return CheckForError(lib.LineSpacings_Get_Count())


def Idx(*args):
    """
    Get/set active LineSpacing by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LineSpacings_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.LineSpacings_Set_idx(Value))


def First():
    """Set first LineSpacing active; returns 0 if none."""
    return CheckForError(lib.LineSpacings_Get_First())


def Next():
    """Sets next LineSpacing active; returns 0 if no more."""
    return CheckForError(lib.LineSpacings_Get_Next())


def Name(*args):
    """
    Get/set the name of the active LineSpacing
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.LineSpacings_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.LineSpacings_Set_Name(Value))


def Phases(*args):
    """Number of Phases"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LineSpacings_Get_Phases())

    # Setter
    Value, = args
    CheckForError(lib.LineSpacings_Set_Phases(Value))


def Nconds(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LineSpacings_Get_Nconds())

    # Setter
    Value, = args
    CheckForError(lib.LineSpacings_Set_Nconds(Value))


def Units(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.LineSpacings_Get_Units())

    # Setter
    Value, = args
    CheckForError(lib.LineSpacings_Set_Units(Value))


def Xcoords(*args):
    """Get/Set the X (horizontal) coordinates of the conductors"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineSpacings_Get_Xcoords)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount))


def Ycoords(*args):
    """Get/Set the Y (vertical/height) coordinates of the conductors"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineSpacings_Get_Ycoords)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount))


_columns = ["Name", "Idx", "Nconds", "Phases", "Units", "Xcoords", "Ycoords"]
__all__ = [
    "Phases",
    "Nconds",
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
