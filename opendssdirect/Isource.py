# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all ISource names"""
    return CheckForError(get_string_array(lib.ISources_Get_AllNames))


def Amps(*args):
    """Magnitude of the ISource in amps"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ISources_Get_Amps())

    # Setter
    Value, = args
    CheckForError(lib.ISources_Set_Amps(Value))


def AngleDeg(*args):
    """Phase angle for ISource, degrees"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ISources_Get_AngleDeg())

    # Setter
    Value, = args
    CheckForError(lib.ISources_Set_AngleDeg(Value))


def Count():
    """(read-only) Number of ISources"""
    return CheckForError(lib.ISources_Get_Count())


def First():
    """Set first ISource active; returns 0 if none."""
    return CheckForError(lib.ISources_Get_First())


def Frequency(*args):
    """The present frequency of the ISource, Hz"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ISources_Get_Frequency())

    # Setter
    Value, = args
    CheckForError(lib.ISources_Set_Frequency(Value))


def Name(*args):
    """
    Get/set the name of the active ISource
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.ISources_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.ISources_Set_Name(Value))


def Next():
    """Sets next ISource active; returns 0 if no more."""
    return CheckForError(lib.ISources_Get_Next())


def Idx(*args):
    """
    Get/set active ISource by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ISources_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.ISources_Set_idx(Value))


_columns = ["Amps", "AngleDeg", "Frequency", "Name", "Idx"]
__all__ = [
    "AllNames",
    "Amps",
    "AngleDeg",
    "Count",
    "First",
    "Frequency",
    "Name",
    "Next",
    "Idx",
]
