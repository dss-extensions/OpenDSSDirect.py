# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def AllNames():
    """(read-only) List of strings with all Relay names"""
    return CheckForError(get_string_array(lib.Relays_Get_AllNames))


def Count():
    """(read-only) Number of Relays"""
    return CheckForError(lib.Relays_Get_Count())


def First():
    """Set first Relay active; returns 0 if none."""
    return CheckForError(lib.Relays_Get_First())


def MonitoredObj(*args):
    """Full name of object this Relay is monitoring."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Relays_Get_MonitoredObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Relays_Set_MonitoredObj(Value))


def MonitoredTerm(*args):
    """Number of terminal of monitored element that this Relay is monitoring."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Relays_Get_MonitoredTerm())

    # Setter
    Value, = args
    CheckForError(lib.Relays_Set_MonitoredTerm(Value))


def Name(*args):
    """
    Get/set the name of the active Relay
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Relays_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Relays_Set_Name(Value))


def Next():
    """Sets next Relay active; returns 0 if no more."""
    return CheckForError(lib.Relays_Get_Next())


def SwitchedObj(*args):
    """Full name of element that will be switched when relay trips."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Relays_Get_SwitchedObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Relays_Set_SwitchedObj(Value))


def SwitchedTerm(*args):
    """Terminal number of the switched object that will be opened when the relay trips."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Relays_Get_SwitchedTerm())

    # Setter
    Value, = args
    CheckForError(lib.Relays_Set_SwitchedTerm(Value))


def Idx(*args):
    """
    Get/set active Relay by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Relays_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Relays_Set_idx(Value))


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
