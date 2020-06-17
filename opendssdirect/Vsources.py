# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all Vsource names"""
    return get_string_array(lib.Vsources_Get_AllNames)


def AngleDeg(*args):
    """Phase angle of first phase in degrees"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_AngleDeg()

    # Setter
    Value, = args
    lib.Vsources_Set_AngleDeg(Value)
    CheckForError()


def BasekV(*args):
    """Source voltage in kV"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_BasekV()

    # Setter
    Value, = args
    lib.Vsources_Set_BasekV(Value)
    CheckForError()


def Count():
    """(read-only) Number of Vsources"""
    return lib.Vsources_Get_Count()


def First():
    """Set first Vsource active; returns 0 if none."""
    return lib.Vsources_Get_First()


def Frequency(*args):
    """Source frequency in Hz"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_Frequency()

    # Setter
    Value, = args
    lib.Vsources_Set_Frequency(Value)
    CheckForError()


def Name(*args):
    """
    Get/set the name of the active Vsource
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Vsources_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Vsources_Set_Name(Value))


def Next():
    """Sets next Vsource active; returns 0 if no more."""
    return lib.Vsources_Get_Next()


def Phases(*args):
    """Number of phases"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_Phases()

    # Setter
    Value, = args
    lib.Vsources_Set_Phases(Value)
    CheckForError()


def PU(*args):
    """
    (read) Source pu voltage.
    (write) Per-unit value of source voltage based on kV
    """
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_pu()

    # Setter
    Value, = args
    lib.Vsources_Set_pu(Value)
    CheckForError()


def Idx(*args):
    """
    Get/set active Vsource by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.Vsources_Set_idx(Value))


_columns = ["AngleDeg", "BasekV", "Frequency", "Name", "Phases", "PU", "Idx"]
__all__ = [
    "AllNames",
    "AngleDeg",
    "BasekV",
    "Count",
    "First",
    "Frequency",
    "Name",
    "Next",
    "Phases",
    "PU",
    "Idx",
]
