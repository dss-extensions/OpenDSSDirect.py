# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    get_string,
    get_string_array,
    get_int32_array,
    prepare_int32_array,
)
from ._utils import codec


def AddStep():
    return lib.Capacitors_AddStep() != 0


def Close():
    lib.Capacitors_Close()


def Open():
    lib.Capacitors_Open()


def SubtractStep():
    return lib.Capacitors_SubtractStep() != 0


def AllNames():
    """(read-only) Array of strings with all Capacitor names in the circuit."""
    return get_string_array(lib.Capacitors_Get_AllNames)


def AvailableSteps():
    """(read-only) Number of Steps available in cap bank to be switched ON."""
    return lib.Capacitors_Get_AvailableSteps()


def Count():
    """(read-only) Number of Capacitor objects in active circuit."""
    return lib.Capacitors_Get_Count()


def First():
    """(read-only) Sets the first Capacitor active. Returns 0 if no more."""
    return lib.Capacitors_Get_First()


def IsDelta(*args):
    """Delta connection or wye?"""
    # Getter
    if len(args) == 0:
        return lib.Capacitors_Get_IsDelta() != 0

    # Setter
    Value, = args
    lib.Capacitors_Set_IsDelta(Value)


def Name(*args):
    """Sets the active Capacitor by Name."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Capacitors_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Capacitors_Set_Name(Value)


def Next():
    """(read-only) Sets the next Capacitor active. Returns 0 if no more."""
    return lib.Capacitors_Get_Next()


def NumSteps(*args):
    """Number of steps (default 1) for distributing and switching the total bank kVAR."""
    # Getter
    if len(args) == 0:
        return lib.Capacitors_Get_NumSteps()

    # Setter
    Value, = args
    lib.Capacitors_Set_NumSteps(Value)


def States(*args):
    """
    (read) A array of  integer [0..numsteps-1] indicating state of each step. If value is -1 an error has occurred.
    (write) Array of integer [0 ..numSteps-1] indicating the state of each step
    """
    # Getter
    if len(args) == 0:
        return get_int32_array(lib.Capacitors_Get_States)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_int32_array(Value)
    lib.Capacitors_Set_States(ValuePtr, ValueCount)


def kV(*args):
    """Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase."""
    # Getter
    if len(args) == 0:
        return lib.Capacitors_Get_kV()

    # Setter
    Value, = args
    lib.Capacitors_Set_kV(Value)


def kvar(*args):
    """Total bank KVAR, distributed equally among phases and steps."""
    # Getter
    if len(args) == 0:
        return lib.Capacitors_Get_kvar()

    # Setter
    Value, = args
    lib.Capacitors_Set_kvar(Value)


_columns = ["AvailableSteps", "IsDelta", "Name", "NumSteps", "States", "kV", "kvar"]
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
]
