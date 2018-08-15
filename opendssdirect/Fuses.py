# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def Close():
    lib.Fuses_Close()


def IsBlown():
    return lib.Fuses_IsBlown() != 0


def Open():
    lib.Fuses_Open()


def AllNames():
    """(read-only) Array of strings containing names of all Fuses in the circuit"""
    return get_string_array(lib.Fuses_Get_AllNames)


def Count():
    """(read-only) Number of Fuse elements in the circuit"""
    return lib.Fuses_Get_Count()


def Delay(*args):
    """
    (read) A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
    (write) Fixed delay time in seconds added to the fuse blowing time to represent fuse clear or other delay.
    """
    # Getter
    if len(args) == 0:
        return lib.Fuses_Get_Delay()

    # Setter
    Value, = args
    lib.Fuses_Set_Delay(Value)


def First():
    """(read-only) Set the first Fuse to be the active fuse. Returns 0 if none."""
    return lib.Fuses_Get_First()


def MonitoredObj(*args):
    """Full name of the circuit element to which the fuse is connected."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Fuses_Get_MonitoredObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Fuses_Set_MonitoredObj(Value)


def MonitoredTerm(*args):
    """
    (read) Terminal number to which the fuse is connected.
    (write) Number of the terminal to which the fuse is connected
    """
    # Getter
    if len(args) == 0:
        return lib.Fuses_Get_MonitoredTerm()

    # Setter
    Value, = args
    lib.Fuses_Set_MonitoredTerm(Value)


def Name(*args):
    """
    (read) Get the name of the active Fuse element
    (write) Set the active Fuse element by name.
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Fuses_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Fuses_Set_Name(Value)


def Next():
    """(read-only) Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses."""
    return lib.Fuses_Get_Next()


def NumPhases():
    """(read-only) Number of phases, this fuse. """
    return lib.Fuses_Get_NumPhases()


def RatedCurrent(*args):
    """
    (read) Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.  Multipliy current values of TCC curve by this to get actual amps.
    (write) Multiplier or actual fuse amps for the TCC curve. Defaults to 1.0. Has to correspond to the Current axis of TCCcurve object.
    """
    # Getter
    if len(args) == 0:
        return lib.Fuses_Get_RatedCurrent()

    # Setter
    Value, = args
    lib.Fuses_Set_RatedCurrent(Value)


def SwitchedObj(*args):
    """
    (read) Full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.
    (write) Full name of the circuit element switch that the fuse controls. Defaults to MonitoredObj.
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Fuses_Get_SwitchedObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Fuses_Set_SwitchedObj(Value)


def SwitchedTerm(*args):
    """
    (read) Number of the terminal containing the switch controlled by the fuse.
    (write) Number of the terminal of the controlled element containing the switch controlled by the fuse.
    """
    # Getter
    if len(args) == 0:
        return lib.Fuses_Get_SwitchedTerm()

    # Setter
    Value, = args
    lib.Fuses_Set_SwitchedTerm(Value)


def TCCCurve(*args):
    """Name of the TCCcurve object that determines fuse blowing."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Fuses_Get_TCCcurve())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Fuses_Set_TCCcurve(Value)


def Idx(*args):
    """
    (read) Get/set active fuse by index into the list of fuses. 1 based: 1..count
    (write) Set Fuse active by index into the list of fuses. 1..count
    """
    # Getter
    if len(args) == 0:
        return lib.Fuses_Get_idx()

    # Setter
    Value, = args
    lib.Fuses_Set_idx(Value)


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
