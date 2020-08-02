# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all CNData names"""
    return CheckForError(get_string_array(lib.CNData_Get_AllNames))


def Count():
    """(read-only) Number of CNDatas"""
    return CheckForError(lib.CNData_Get_Count())


def Idx(*args):
    """
    Get/set active CNData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_idx(Value))


def First():
    """Set first CNData active; returns 0 if none."""
    return CheckForError(lib.CNData_Get_First())


def Next():
    """Sets next CNData active; returns 0 if no more."""
    return CheckForError(lib.CNData_Get_Next())


def Name(*args):
    """
    Get/set the name of the active CNData
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.CNData_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.CNData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_EmergAmps())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_EmergAmps(Value))


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_NormAmps())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_NormAmps(Value))


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_Rdc())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_Rdc(Value))


def Rac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_Rac())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_Rac(Value))


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_GMRac())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_GMRac(Value))


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_GMRUnits())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_GMRUnits(Value))


def Radius(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_Radius())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_Radius(Value))


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_RadiusUnits())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_RadiusUnits(Value))


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_ResistanceUnits())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_ResistanceUnits(Value))


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_Diameter())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_Diameter(Value))


def EpsR(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_EpsR())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_EpsR(Value))


def InsLayer(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_InsLayer())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_InsLayer(Value))


def DiaIns(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_DiaIns())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_DiaIns(Value))


def DiaCable(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_DiaCable())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_DiaCable(Value))


def k(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_k())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_k(Value))


def DiaStrand(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_DiaStrand())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_DiaStrand(Value))


def GmrStrand(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_GmrStrand())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_GmrStrand(Value))


def RStrand(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CNData_Get_RStrand())

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_RStrand(Value))


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
    "EpsR",
    "InsLayer",
    "DiaIns",
    "DiaCable",
    "DiaStrand",
    "RStrand",
    "k",
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
    "k",
    "DiaStrand",
    "GmrStrand",
    "RStrand",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
