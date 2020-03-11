# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all CNData names"""
    return get_string_array(lib.CNData_Get_AllNames)


def Count():
    """(read-only) Number of CNDatas"""
    return lib.CNData_Get_Count()


def Idx(*args):
    """
    Get/set active CNData by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.CNData_Set_idx(Value))


def First():
    """Set first CNData active; returns 0 if none."""
    return lib.CNData_Get_First()


def Next():
    """Sets next CNData active; returns 0 if no more."""
    return lib.CNData_Get_Next()


def Name(*args):
    """
    Get/set the name of the active CNData
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.CNData_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    CheckForError(lib.CNData_Set_Name(Value))


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_EmergAmps()

    # Setter
    Value, = args
    lib.CNData_Set_EmergAmps(Value)
    CheckForError()


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_NormAmps()

    # Setter
    Value, = args
    lib.CNData_Set_NormAmps(Value)
    CheckForError()


def Rdc(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_Rdc()

    # Setter
    Value, = args
    lib.CNData_Set_Rdc(Value)
    CheckForError()


def Rac(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_Rac()

    # Setter
    Value, = args
    lib.CNData_Set_Rac(Value)
    CheckForError()


def GMRac(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_GMRac()

    # Setter
    Value, = args
    lib.CNData_Set_GMRac(Value)
    CheckForError()


def GMRUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_GMRUnits()

    # Setter
    Value, = args
    lib.CNData_Set_GMRUnits(Value)
    CheckForError()


def Radius(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_Radius()

    # Setter
    Value, = args
    lib.CNData_Set_Radius(Value)
    CheckForError()


def RadiusUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_RadiusUnits()

    # Setter
    Value, = args
    lib.CNData_Set_RadiusUnits(Value)
    CheckForError()


def ResistanceUnits(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_ResistanceUnits()

    # Setter
    Value, = args
    lib.CNData_Set_ResistanceUnits(Value)
    CheckForError()


def Diameter(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_Diameter()

    # Setter
    Value, = args
    lib.CNData_Set_Diameter(Value)
    CheckForError()


def EpsR(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_EpsR()

    # Setter
    Value, = args
    lib.CNData_Set_EpsR(Value)
    CheckForError()


def InsLayer(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_InsLayer()

    # Setter
    Value, = args
    lib.CNData_Set_InsLayer(Value)
    CheckForError()


def DiaIns(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_DiaIns()

    # Setter
    Value, = args
    lib.CNData_Set_DiaIns(Value)
    CheckForError()


def DiaCable(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_DiaCable()

    # Setter
    Value, = args
    lib.CNData_Set_DiaCable(Value)
    CheckForError()


def k(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_k()

    # Setter
    Value, = args
    lib.CNData_Set_k(Value)
    CheckForError()


def DiaStrand(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_DiaStrand()

    # Setter
    Value, = args
    lib.CNData_Set_DiaStrand(Value)
    CheckForError()


def GmrStrand(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_GmrStrand()

    # Setter
    Value, = args
    lib.CNData_Set_GmrStrand(Value)
    CheckForError()


def RStrand(*args):
    # Getter
    if len(args) == 0:
        return lib.CNData_Get_RStrand()

    # Setter
    Value, = args
    lib.CNData_Set_RStrand(Value)
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
