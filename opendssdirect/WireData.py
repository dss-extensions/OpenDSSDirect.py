# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all WireData names"""
    return get_string_array(lib.WireData_Get_AllNames)


def Count():
    """(read-only) Number of WireDatas"""
    return lib.WireData_Get_Count()


def Idx(*args):
    """
    Get/set active WireData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.WireData_Set_idx(Value))


def First():
    """Set first WireData active; returns 0 if none."""
    return lib.WireData_Get_First()


def Next():
    """Sets next WireData active; returns 0 if no more."""
    return lib.WireData_Get_Next()


def Name(*args):
    """
    Get/set the name of the active WireData
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.WireData_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    CheckForError(lib.WireData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_EmergAmps()

    # Setter
    Value, = args
    lib.WireData_Set_EmergAmps(Value)
    CheckForError()


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_NormAmps()

    # Setter
    Value, = args
    lib.WireData_Set_NormAmps(Value)
    CheckForError()


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_Rdc()

    # Setter
    Value, = args
    lib.WireData_Set_Rdc(Value)
    CheckForError()


def Rac(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_Rac()

    # Setter
    Value, = args
    lib.WireData_Set_Rac(Value)
    CheckForError()


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_GMRac()

    # Setter
    Value, = args
    lib.WireData_Set_GMRac(Value)
    CheckForError()


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_GMRUnits()

    # Setter
    Value, = args
    lib.WireData_Set_GMRUnits(Value)
    CheckForError()


def Radius(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_Radius()

    # Setter
    Value, = args
    lib.WireData_Set_Radius(Value)
    CheckForError()


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_RadiusUnits()

    # Setter
    Value, = args
    lib.WireData_Set_RadiusUnits(Value)
    CheckForError()


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_ResistanceUnits()

    # Setter
    Value, = args
    lib.WireData_Set_ResistanceUnits(Value)
    CheckForError()


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return lib.WireData_Get_Diameter()

    # Setter
    Value, = args
    lib.WireData_Set_Diameter(Value)
    CheckForError()


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
