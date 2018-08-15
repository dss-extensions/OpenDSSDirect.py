# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def AllNames():
    """(read-only) Array of strings containing names of all Relay elements"""
    return get_string_array(lib.Relays_Get_AllNames)


def Count():
    """(read-only) Number of Relays in circuit"""
    return lib.Relays_Get_Count()


def First():
    """(read-only) Set First Relay active. If none, returns 0."""
    return lib.Relays_Get_First()


def MonitoredObj(*args):
    """Full name of object this Relay is monitoring."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Relays_Get_MonitoredObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Relays_Set_MonitoredObj(Value)


def MonitoredTerm(*args):
    """Number of terminal of monitored element that this Relay is monitoring."""
    # Getter
    if len(args) == 0:
        return lib.Relays_Get_MonitoredTerm()

    # Setter
    Value, = args
    lib.Relays_Set_MonitoredTerm(Value)


def Name(*args):
    """
    (read) Get name of active relay.
    (write) Set Relay active by name
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Relays_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Relays_Set_Name(Value)


def Next():
    """(read-only) Advance to next Relay object. Returns 0 when no more relays."""
    return lib.Relays_Get_Next()


def SwitchedObj(*args):
    """Full name of element that will be switched when relay trips."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Relays_Get_SwitchedObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Relays_Set_SwitchedObj(Value)


def SwitchedTerm(*args):
    """Terminal number of the switched object that will be opened when the relay trips."""
    # Getter
    if len(args) == 0:
        return lib.Relays_Get_SwitchedTerm()

    # Setter
    Value, = args
    lib.Relays_Set_SwitchedTerm(Value)


def Idx(*args):
    """
    (read) Get/Set active Relay by index into the Relay list. 1..Count
    (write) Get/Set Relay active by index into relay list. 1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.Relays_Get_idx()

    # Setter
    Value, = args
    lib.Relays_Set_idx(Value)


_columns = [
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
__all__ = [
    "AllNames",
    "Count",
    "First",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
