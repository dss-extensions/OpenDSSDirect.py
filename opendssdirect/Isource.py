# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def AllNames():
    """(read-only) Array of strings containing names of all ISOURCE elements."""
    return get_string_array(lib.ISources_Get_AllNames)


def Amps(*args):
    """Magnitude of the ISOURCE in amps"""
    # Getter
    if len(args) == 0:
        return lib.ISources_Get_Amps()

    # Setter
    Value, = args
    lib.ISources_Set_Amps(Value)


def AngleDeg(*args):
    """Phase angle for ISOURCE, degrees"""
    # Getter
    if len(args) == 0:
        return lib.ISources_Get_AngleDeg()

    # Setter
    Value, = args
    lib.ISources_Set_AngleDeg(Value)


def Count():
    """(read-only) Count: Number of ISOURCE elements."""
    return lib.ISources_Get_Count()


def First():
    """(read-only) Set the First ISOURCE to be active; returns Zero if none."""
    return lib.ISources_Get_First()


def Frequency(*args):
    """The present frequency of the ISOURCE, Hz"""
    # Getter
    if len(args) == 0:
        return lib.ISources_Get_Frequency()

    # Setter
    Value, = args
    lib.ISources_Set_Frequency(Value)


def Name(*args):
    """
    (read) Get name of active ISOURCE
    (write) Set Active ISOURCE by name
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.ISources_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.ISources_Set_Name(Value)


def Next():
    """(read-only) Sets the next ISOURCE element to be the active one. Returns Zero if no more."""
    return lib.ISources_Get_Next()


_columns = ["Amps", "AngleDeg", "Frequency", "Name"]
__all__ = [
    "AllNames",
    "Amps",
    "AngleDeg",
    "Count",
    "First",
    "Frequency",
    "Name",
    "Next",
]
