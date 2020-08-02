# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def Close():
    CheckForError(lib.Fuses_Close())


def IsBlown():
    return CheckForError(lib.Fuses_IsBlown()) != 0


def Open():
    CheckForError(lib.Fuses_Open())


def AllNames():
    """(read-only) List of strings with all Fuse names"""
    return CheckForError(get_string_array(lib.Fuses_Get_AllNames))


def Count():
    """(read-only) Number of Fuses"""
    return CheckForError(lib.Fuses_Get_Count())


def Delay(*args):
    """
    A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
    This represents a fuse clear or other delay.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Fuses_Get_Delay())

    # Setter
    Value, = args
    CheckForError(lib.Fuses_Set_Delay(Value))


def First():
    """Set first Fuse active; returns 0 if none."""
    return CheckForError(lib.Fuses_Get_First())


def MonitoredObj(*args):
    """Full name of the circuit element to which the fuse is connected."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Fuses_Get_MonitoredObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Fuses_Set_MonitoredObj(Value))


def MonitoredTerm(*args):
    """Terminal number to which the fuse is connected."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Fuses_Get_MonitoredTerm())

    # Setter
    Value, = args
    CheckForError(lib.Fuses_Set_MonitoredTerm(Value))


def Name(*args):
    """
    Get/set the name of the active Fuse
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Fuses_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Fuses_Set_Name(Value))


def Next():
    """Sets next Fuse active; returns 0 if no more."""
    return CheckForError(lib.Fuses_Get_Next())


def NumPhases():
    """(read-only) Number of phases, this fuse."""
    return CheckForError(lib.Fuses_Get_NumPhases())


def RatedCurrent(*args):
    """
    Multiplier or actual amps for the TCCcurve object. Defaults to 1.0. 
    Multiply current values of TCC curve by this to get actual amps.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Fuses_Get_RatedCurrent())

    # Setter
    Value, = args
    CheckForError(lib.Fuses_Set_RatedCurrent(Value))


def SwitchedObj(*args):
    """
    Full name of the circuit element switch that the fuse controls. 
    Defaults to the MonitoredObj.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Fuses_Get_SwitchedObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Fuses_Set_SwitchedObj(Value))


def SwitchedTerm(*args):
    """
    Number of the terminal of the controlled element containing the switch controlled by the fuse.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Fuses_Get_SwitchedTerm())

    # Setter
    Value, = args
    CheckForError(lib.Fuses_Set_SwitchedTerm(Value))


def TCCCurve(*args):
    """Name of the TCCcurve object that determines fuse blowing."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Fuses_Get_TCCcurve()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Fuses_Set_TCCcurve(Value))


def Idx(*args):
    """
    Get/set active Fuse by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Fuses_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Fuses_Set_idx(Value))


_columns = [
    "IsBlown",
    "Delay",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "NumPhases",
    "RatedCurrent",
    "SwitchedObj",
    "SwitchedTerm",
    "TCCCurve",
    "Idx",
]
__all__ = [
    "Close",
    "IsBlown",
    "Open",
    "AllNames",
    "Count",
    "Delay",
    "First",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NumPhases",
    "RatedCurrent",
    "SwitchedObj",
    "SwitchedTerm",
    "TCCCurve",
    "Idx",
]
