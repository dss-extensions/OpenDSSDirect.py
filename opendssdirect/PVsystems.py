# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array, get_float64_array
from ._utils import codec


def AllNames():
    """(read-only) Vairant array of strings with all PVSystem names"""
    return get_string_array(lib.PVSystems_Get_AllNames)


def Count():
    """(read-only) Number of PVSystems"""
    return lib.PVSystems_Get_Count()


def First():
    """(read-only) Set first PVSystem active; returns 0 if none."""
    return lib.PVSystems_Get_First()


def Irradiance(*args):
    """
    (read) Get the present value of the Irradiance property in W/sq-m
    (write) Set the present Irradiance value in W/sq-m
    """
    # Getter
    if len(args) == 0:
        return lib.PVSystems_Get_Irradiance()

    # Setter
    Value, = args
    lib.PVSystems_Set_Irradiance(Value)


def Name(*args):
    """
    (read) Get the name of the active PVSystem
    (write) Set the name of the active PVSystem
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.PVSystems_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.PVSystems_Set_Name(Value)


def Next():
    """(read-only) Sets next PVSystem active; returns 0 if no more."""
    return lib.PVSystems_Get_Next()


def pf(*args):
    """
    (read) Get Power factor
    (write) Set PF
    """
    # Getter
    if len(args) == 0:
        return lib.PVSystems_Get_PF()

    # Setter
    Value, = args
    lib.PVSystems_Set_PF(Value)


def RegisterNames():
    """(read-only) Variant Array of PVSYSTEM energy meter register names"""
    return get_string_array(lib.PVSystems_Get_RegisterNames)


def RegisterValues():
    """(read-only) Array of doubles containing values in PVSystem registers."""
    return get_float64_array(lib.PVSystems_Get_RegisterValues)


def Idx(*args):
    """
    (read) Get/set active PVSystem by index;  1..Count
    (write) Get/Set Active PVSystem by index:  1.. Count
    """
    # Getter
    if len(args) == 0:
        return lib.PVSystems_Get_idx()

    # Setter
    Value, = args
    lib.PVSystems_Set_idx(Value)


def kVARated(*args):
    """
    (read) Get Rated kVA of the PVSystem
    (write) Set kva rated
    """
    # Getter
    if len(args) == 0:
        return lib.PVSystems_Get_kVArated()

    # Setter
    Value, = args
    lib.PVSystems_Set_kVArated(Value)


def kW():
    """(read-only) get kW output"""
    return lib.PVSystems_Get_kW()


def kvar(*args):
    """
    (read) Get kvar value
    (write) Set kvar output value
    """
    # Getter
    if len(args) == 0:
        return lib.PVSystems_Get_kvar()

    # Setter
    Value, = args
    lib.PVSystems_Set_kvar(Value)


_columns = [
    "Irradiance",
    "Name",
    "pf",
    "RegisterNames",
    "RegisterValues",
    "Idx",
    "kVARated",
    "kW",
    "kvar",
]
__all__ = [
    "AllNames",
    "Count",
    "First",
    "Irradiance",
    "Name",
    "Next",
    "pf",
    "RegisterNames",
    "RegisterValues",
    "Idx",
    "kVARated",
    "kW",
    "kvar",
]
