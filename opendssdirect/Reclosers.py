# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array, get_float64_array
from ._utils import codec


def Close():
    lib.Reclosers_Close()


def Open():
    lib.Reclosers_Open()


def AllNames():
    """(read-only) Array of strings with names of all Reclosers in Active Circuit"""
    return get_string_array(lib.Reclosers_Get_AllNames)


def Count():
    """(read-only) Number of Reclosers in active circuit."""
    return lib.Reclosers_Get_Count()


def First():
    """(read-only) Set First Recloser to be Active Ckt Element. Returns 0 if none."""
    return lib.Reclosers_Get_First()


def GroundInst(*args):
    """
    (read) Ground (3I0) instantaneous trip setting - curve multipler or actual amps.
    (write) Ground (3I0) trip instantaneous multiplier or actual amps
    """
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_GroundInst()

    # Setter
    Value, = args
    lib.Reclosers_Set_GroundInst(Value)


def GroundTrip(*args):
    """Ground (3I0) trip multiplier or actual amps"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_GroundTrip()

    # Setter
    Value, = args
    lib.Reclosers_Set_GroundTrip(Value)


def MonitoredObj(*args):
    """
    (read) Full name of object this Recloser is monitoring.
    (write) Set monitored object by full name.
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Reclosers_Get_MonitoredObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Reclosers_Set_MonitoredObj(Value)


def MonitoredTerm(*args):
    """Terminal number of Monitored object for the Recloser """
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_MonitoredTerm()

    # Setter
    Value, = args
    lib.Reclosers_Set_MonitoredTerm(Value)


def Name(*args):
    """Get Name of active Recloser or set the active Recloser by name."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Reclosers_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Reclosers_Set_Name(Value)


def Next():
    """(read-only) Iterate to the next recloser in the circuit. Returns zero if no more."""
    return lib.Reclosers_Get_Next()


def NumFast(*args):
    """Number of fast shots"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_NumFast()

    # Setter
    Value, = args
    lib.Reclosers_Set_NumFast(Value)


def PhaseInst(*args):
    """Phase instantaneous curve multipler or actual amps"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_PhaseInst()

    # Setter
    Value, = args
    lib.Reclosers_Set_PhaseInst(Value)


def PhaseTrip(*args):
    """
    (read) Phase trip curve multiplier or actual amps
    (write) Phase Trip multiplier or actual amps
    """
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_PhaseTrip()

    # Setter
    Value, = args
    lib.Reclosers_Set_PhaseTrip(Value)


def RecloseIntervals():
    """(read-only) Variant Array of Doubles: reclose intervals, s, between shots."""
    return get_float64_array(lib.Reclosers_Get_RecloseIntervals)


def Shots(*args):
    """Number of shots to lockout (fast + delayed)"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_Shots()

    # Setter
    Value, = args
    lib.Reclosers_Set_Shots(Value)


def SwitchedObj(*args):
    """Full name of the circuit element that is being switched by the Recloser."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Reclosers_Get_SwitchedObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Reclosers_Set_SwitchedObj(Value)


def SwitchedTerm(*args):
    """Terminal number of the controlled device being switched by the Recloser"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_SwitchedTerm()

    # Setter
    Value, = args
    lib.Reclosers_Set_SwitchedTerm(Value)


def Idx(*args):
    """Get/Set the active Recloser by index into the recloser list.  1..Count"""
    # Getter
    if len(args) == 0:
        return lib.Reclosers_Get_idx()

    # Setter
    Value, = args
    lib.Reclosers_Set_idx(Value)


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
