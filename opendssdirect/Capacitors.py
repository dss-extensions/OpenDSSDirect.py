# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_int32_array,
    get_string_array,
    prepare_int32_array,
)


def AddStep():
    return CheckForError(lib.Capacitors_AddStep()) != 0


def Close():
    CheckForError(lib.Capacitors_Close())


def Open():
    CheckForError(lib.Capacitors_Open())


def SubtractStep():
    return CheckForError(lib.Capacitors_SubtractStep()) != 0


def AllNames():
    """(read-only) List of strings with all Capacitor names"""
    return CheckForError(get_string_array(lib.Capacitors_Get_AllNames))


def AvailableSteps():
    """(read-only) Number of Steps available in cap bank to be switched ON."""
    return CheckForError(lib.Capacitors_Get_AvailableSteps())


def Count():
    """(read-only) Number of Capacitors"""
    return CheckForError(lib.Capacitors_Get_Count())


def First():
    """Set first Capacitor active; returns 0 if none."""
    return CheckForError(lib.Capacitors_Get_First())


def IsDelta(*args):
    """Delta connection or wye?"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Capacitors_Get_IsDelta()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Capacitors_Set_IsDelta(Value))


def Name(*args):
    """
    Get/set the name of the active Capacitor
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Capacitors_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Capacitors_Set_Name(Value))


def Next():
    """Sets next Capacitor active; returns 0 if no more."""
    return CheckForError(lib.Capacitors_Get_Next())


def NumSteps(*args):
    """Number of steps (default 1) for distributing and switching the total bank kVAR."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Capacitors_Get_NumSteps())

    # Setter
    Value, = args
    CheckForError(lib.Capacitors_Set_NumSteps(Value))


def States(*args):
    """A array of  integer [0..numsteps-1] indicating state of each step. If the read value is -1 an error has occurred."""
    # Getter
    if len(args) == 0:
        return get_int32_array(lib.Capacitors_Get_States)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_int32_array(Value)
    CheckForError(lib.Capacitors_Set_States(ValuePtr, ValueCount))


def kV(*args):
    """Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Capacitors_Get_kV())

    # Setter
    Value, = args
    CheckForError(lib.Capacitors_Set_kV(Value))


def kvar(*args):
    """Total bank KVAR, distributed equally among phases and steps."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Capacitors_Get_kvar())

    # Setter
    Value, = args
    CheckForError(lib.Capacitors_Set_kvar(Value))


def Idx(*args):
    """
    Get/set active Capacitor by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Capacitors_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Capacitors_Set_idx(Value))


_columns = [
    "AvailableSteps",
    "IsDelta",
    "Name",
    "NumSteps",
    "States",
    "kV",
    "kvar",
    "Idx",
]
__all__ = [
    "AddStep",
    "Close",
    "Open",
    "SubtractStep",
    "AllNames",
    "AvailableSteps",
    "Count",
    "First",
    "IsDelta",
    "Name",
    "Next",
    "NumSteps",
    "States",
    "kV",
    "kvar",
    "Idx",
]
