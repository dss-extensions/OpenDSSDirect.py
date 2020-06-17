# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all TSData names"""
    return get_string_array(lib.TSData_Get_AllNames)


def Count():
    """(read-only) Number of TSDatas"""
    return lib.TSData_Get_Count()


def Idx(*args):
    """
    Get/set active TSData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.TSData_Set_idx(Value))


def First():
    """Set first TSData active; returns 0 if none."""
    return lib.TSData_Get_First()


def Next():
    """Sets next TSData active; returns 0 if no more."""
    return lib.TSData_Get_Next()


def Name(*args):
    """
    Get/set the name of the active TSData
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.TSData_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    CheckForError(lib.TSData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_EmergAmps()

    # Setter
    Value, = args
    lib.TSData_Set_EmergAmps(Value)
    CheckForError()


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_NormAmps()

    # Setter
    Value, = args
    lib.TSData_Set_NormAmps(Value)
    CheckForError()


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_Rdc()

    # Setter
    Value, = args
    lib.TSData_Set_Rdc(Value)
    CheckForError()


def Rac(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_Rac()

    # Setter
    Value, = args
    lib.TSData_Set_Rac(Value)
    CheckForError()


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_GMRac()

    # Setter
    Value, = args
    lib.TSData_Set_GMRac(Value)
    CheckForError()


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_GMRUnits()

    # Setter
    Value, = args
    lib.TSData_Set_GMRUnits(Value)
    CheckForError()


def Radius(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_Radius()

    # Setter
    Value, = args
    lib.TSData_Set_Radius(Value)
    CheckForError()


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_RadiusUnits()

    # Setter
    Value, = args
    lib.TSData_Set_RadiusUnits(Value)
    CheckForError()


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_ResistanceUnits()

    # Setter
    Value, = args
    lib.TSData_Set_ResistanceUnits(Value)
    CheckForError()


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_Diameter()

    # Setter
    Value, = args
    lib.TSData_Set_Diameter(Value)
    CheckForError()


def EpsR(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_EpsR()

    # Setter
    Value, = args
    lib.TSData_Set_EpsR(Value)
    CheckForError()


def InsLayer(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_InsLayer()

    # Setter
    Value, = args
    lib.TSData_Set_InsLayer(Value)
    CheckForError()


def DiaIns(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_DiaIns()

    # Setter
    Value, = args
    lib.TSData_Set_DiaIns(Value)
    CheckForError()


def DiaCable(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_DiaCable()

    # Setter
    Value, = args
    lib.TSData_Set_DiaCable(Value)
    CheckForError()


def DiaShield(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_DiaShield()

    # Setter
    Value, = args
    lib.TSData_Set_DiaShield(Value)
    CheckForError()


def TapeLayer(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_TapeLayer()

    # Setter
    Value, = args
    lib.TSData_Set_TapeLayer(Value)
    CheckForError()


def TapeLap(*args):
    # Getter
    if len(args) == 0:
        return lib.TSData_Get_TapeLap()

    # Setter
    Value, = args
    lib.TSData_Set_TapeLap(Value)
    CheckForError()


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
