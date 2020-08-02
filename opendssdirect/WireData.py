# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all WireData names"""
    return CheckForError(get_string_array(lib.WireData_Get_AllNames))


def Count():
    """(read-only) Number of WireDatas"""
    return CheckForError(lib.WireData_Get_Count())


def Idx(*args):
    """
    Get/set active WireData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_idx(Value))


def First():
    """Set first WireData active; returns 0 if none."""
    return CheckForError(lib.WireData_Get_First())


def Next():
    """Sets next WireData active; returns 0 if no more."""
    return CheckForError(lib.WireData_Get_Next())


def Name(*args):
    """
    Get/set the name of the active WireData
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.WireData_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.WireData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_EmergAmps())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_EmergAmps(Value))


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_NormAmps())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_NormAmps(Value))


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_Rdc())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_Rdc(Value))


def Rac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_Rac())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_Rac(Value))


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_GMRac())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_GMRac(Value))


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_GMRUnits())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_GMRUnits(Value))


def Radius(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_Radius())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_Radius(Value))


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_RadiusUnits())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_RadiusUnits(Value))


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_ResistanceUnits())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_ResistanceUnits(Value))


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.WireData_Get_Diameter())

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_Diameter(Value))


_columns = [
    "Name",
    "Idx",
    "NormAmps",
    "EmergAmps",
    "Rdc",
    "Rac",
    "ResistanceUnits",
    "GMRac",
    "GMRUnits",
    "Radius",
    "Diameter",
    "RadiusUnits",
]
__all__ = [
    "EmergAmps",
    "NormAmps",
    "Rdc",
    "Rac",
    "GMRac",
    "GMRUnits",
    "Radius",
    "RadiusUnits",
    "ResistanceUnits",
    "Diameter",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
