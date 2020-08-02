# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all TSData names"""
    return CheckForError(get_string_array(lib.TSData_Get_AllNames))


def Count():
    """(read-only) Number of TSDatas"""
    return CheckForError(lib.TSData_Get_Count())


def Idx(*args):
    """
    Get/set active TSData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_idx(Value))


def First():
    """Set first TSData active; returns 0 if none."""
    return CheckForError(lib.TSData_Get_First())


def Next():
    """Sets next TSData active; returns 0 if no more."""
    return CheckForError(lib.TSData_Get_Next())


def Name(*args):
    """
    Get/set the name of the active TSData
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.TSData_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.TSData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_EmergAmps())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_EmergAmps(Value))


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_NormAmps())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_NormAmps(Value))


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_Rdc())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_Rdc(Value))


def Rac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_Rac())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_Rac(Value))


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_GMRac())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_GMRac(Value))


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_GMRUnits())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_GMRUnits(Value))


def Radius(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_Radius())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_Radius(Value))


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_RadiusUnits())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_RadiusUnits(Value))


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_ResistanceUnits())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_ResistanceUnits(Value))


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_Diameter())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_Diameter(Value))


def EpsR(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_EpsR())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_EpsR(Value))


def InsLayer(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_InsLayer())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_InsLayer(Value))


def DiaIns(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_DiaIns())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_DiaIns(Value))


def DiaCable(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_DiaCable())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_DiaCable(Value))


def DiaShield(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_DiaShield())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_DiaShield(Value))


def TapeLayer(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_TapeLayer())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_TapeLayer(Value))


def TapeLap(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.TSData_Get_TapeLap())

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_TapeLap(Value))


_columns = [
    "Name",
    "Idx",
    "NormAmps",
    "EmergAmps",
    "Rdc",
    "Rac",
    "GMRac",
    "GMRUnits",
    "Radius",
    "RadiusUnits",
    "ResistanceUnits",
    "Diameter",
    "TapeLayer",
    "TapeLap",
    "DiaShield",
    "DiaCable",
    "DiaIns",
    "InsLayer",
    "EpsR",
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
    "EpsR",
    "InsLayer",
    "DiaIns",
    "DiaCable",
    "DiaShield",
    "TapeLayer",
    "TapeLap",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
