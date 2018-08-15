# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def AllNames():
    """(read-only) Names of all Vsource objects in the circuit"""
    return get_string_array(lib.Vsources_Get_AllNames)


def AngleDeg(*args):
    """
    (read) Phase angle of first phase in degrees
    (write) phase angle in degrees
    """
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_AngleDeg()

    # Setter
    Value, = args
    lib.Vsources_Set_AngleDeg(Value)


def BasekV(*args):
    """Source voltage in kV"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_BasekV()

    # Setter
    Value, = args
    lib.Vsources_Set_BasekV(Value)


def Count():
    """(read-only) Number of Vsource Object"""
    return lib.Vsources_Get_Count()


def First():
    """(read-only) Sets the first VSOURCE to be active; Returns 0 if none"""
    return lib.Vsources_Get_First()


def Frequency(*args):
    """Source frequency in Hz"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_Frequency()

    # Setter
    Value, = args
    lib.Vsources_Set_Frequency(Value)


def Name(*args):
    """
    (read) Get Active VSOURCE name
    (write) Set Active VSOURCE by Name
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Vsources_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Vsources_Set_Name(Value)


def Next():
    """(read-only) Sets the next VSOURCE object to be active; returns zero if no more"""
    return lib.Vsources_Get_Next()


def Phases(*args):
    """Number of phases"""
    # Getter
    if len(args) == 0:
        return lib.Vsources_Get_Phases()

    # Setter
    Value, = args
    lib.Vsources_Set_Phases(Value)


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


_columns = ["AngleDeg", "BasekV", "Frequency", "Name", "Phases", "PU"]
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
]
