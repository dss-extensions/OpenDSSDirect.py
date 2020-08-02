# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_string_array,
)


def Close():
    CheckForError(lib.Reclosers_Close())


def Open():
    CheckForError(lib.Reclosers_Open())


def AllNames():
    """(read-only) List of strings with all Recloser names"""
    return CheckForError(get_string_array(lib.Reclosers_Get_AllNames))


def Count():
    """(read-only) Number of Reclosers"""
    return CheckForError(lib.Reclosers_Get_Count())


def First():
    """Set first Recloser active; returns 0 if none."""
    return CheckForError(lib.Reclosers_Get_First())


def GroundInst(*args):
    """Ground (3I0) instantaneous trip setting - curve multipler or actual amps."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_GroundInst())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_GroundInst(Value))


def GroundTrip(*args):
    """Ground (3I0) trip multiplier or actual amps"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_GroundTrip())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_GroundTrip(Value))


def MonitoredObj(*args):
    """Full name of object this Recloser to be monitored."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reclosers_Get_MonitoredObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reclosers_Set_MonitoredObj(Value))


def MonitoredTerm(*args):
    """Terminal number of Monitored object for the Recloser"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_MonitoredTerm())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_MonitoredTerm(Value))


def Name(*args):
    """
    Get/set the name of the active Recloser
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Reclosers_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reclosers_Set_Name(Value))


def Next():
    """Sets next Recloser active; returns 0 if no more."""
    return CheckForError(lib.Reclosers_Get_Next())


def NumFast(*args):
    """Number of fast shots"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_NumFast())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_NumFast(Value))


def PhaseInst(*args):
    """Phase instantaneous curve multipler or actual amps"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_PhaseInst())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_PhaseInst(Value))


def PhaseTrip(*args):
    """Phase trip curve multiplier or actual amps"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_PhaseTrip())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_PhaseTrip(Value))


def RecloseIntervals():
    """(read-only) Array of Doubles: reclose intervals, s, between shots."""
    return get_float64_array(lib.Reclosers_Get_RecloseIntervals)


def Shots(*args):
    """Number of shots to lockout (fast + delayed)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_Shots())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_Shots(Value))


def SwitchedObj(*args):
    """Full name of the circuit element that is being switched by the Recloser."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reclosers_Get_SwitchedObj()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reclosers_Set_SwitchedObj(Value))


def SwitchedTerm(*args):
    """Terminal number of the controlled device being switched by the Recloser"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_SwitchedTerm())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_SwitchedTerm(Value))


def Idx(*args):
    """
    Get/set active Recloser by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reclosers_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Reclosers_Set_idx(Value))


_columns = [
    "GroundInst",
    "GroundTrip",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "NumFast",
    "PhaseInst",
    "PhaseTrip",
    "RecloseIntervals",
    "Shots",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
__all__ = [
    "Close",
    "Open",
    "AllNames",
    "Count",
    "First",
    "GroundInst",
    "GroundTrip",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NumFast",
    "PhaseInst",
    "PhaseTrip",
    "RecloseIntervals",
    "Shots",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
