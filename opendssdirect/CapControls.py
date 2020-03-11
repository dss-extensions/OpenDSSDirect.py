# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def Reset():
    lib.CapControls_Reset()


def AllNames():
    """(read-only) List of strings with all CapControl names"""
    return get_string_array(lib.CapControls_Get_AllNames)


def CTRatio(*args):
    """Transducer ratio from pirmary current to control current."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_CTratio()

    # Setter
    Value, = args
    lib.CapControls_Set_CTratio(Value)
    CheckForError()


def Capacitor(*args):
    """Name of the Capacitor that is controlled."""
    # Getter
    if len(args) == 0:
        return get_string(lib.CapControls_Get_Capacitor())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.CapControls_Set_Capacitor(Value)
    CheckForError()


def Count():
    """(read-only) Number of CapControls"""
    return lib.CapControls_Get_Count()


def DeadTime(*args):
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_DeadTime()

    # Setter
    Value, = args
    lib.CapControls_Set_DeadTime(Value)
    CheckForError()


def Delay(*args):
    """Time delay [s] to switch on after arming.  Control may reset before actually switching."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Delay()

    # Setter
    Value, = args
    lib.CapControls_Set_Delay(Value)
    CheckForError()


def DelayOff(*args):
    """Time delay [s] before swithcing off a step. Control may reset before actually switching."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_DelayOff()

    # Setter
    Value, = args
    lib.CapControls_Set_DelayOff(Value)
    CheckForError()


def First():
    """Set first CapControl active; returns 0 if none."""
    return lib.CapControls_Get_First()


def Mode(*args):
    """Type of automatic controller."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Mode()

    # Setter
    Value, = args
    lib.CapControls_Set_Mode(Value)
    CheckForError()


def MonitoredObj(*args):
    """Full name of the element that PT and CT are connected to."""
    # Getter
    if len(args) == 0:
        return get_string(lib.CapControls_Get_MonitoredObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.CapControls_Set_MonitoredObj(Value)
    CheckForError()


def MonitoredTerm(*args):
    """Terminal number on the element that PT and CT are connected to."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_MonitoredTerm()

    # Setter
    Value, = args
    lib.CapControls_Set_MonitoredTerm(Value)
    CheckForError()


def Name(*args):
    """
    Get/set the name of the active CapControl
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.CapControls_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.CapControls_Set_Name(Value))


def Next():
    """Sets next CapControl active; returns 0 if no more."""
    return lib.CapControls_Get_Next()


def OFFSetting(*args):
    """Threshold to switch off a step. See Mode for units."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_OFFSetting()

    # Setter
    Value, = args
    lib.CapControls_Set_OFFSetting(Value)
    CheckForError()


def ONSetting(*args):
    """Threshold to arm or switch on a step.  See Mode for units."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_ONSetting()

    # Setter
    Value, = args
    lib.CapControls_Set_ONSetting(Value)
    CheckForError()


def PTRatio(*args):
    """Transducer ratio from primary feeder to control voltage."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_PTratio()

    # Setter
    Value, = args
    lib.CapControls_Set_PTratio(Value)
    CheckForError()


def UseVoltOverride(*args):
    """Enables Vmin and Vmax to override the control Mode"""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_UseVoltOverride() != 0

    # Setter
    Value, = args
    lib.CapControls_Set_UseVoltOverride(Value)
    CheckForError()


def Vmax(*args):
    """With VoltOverride, swtich off whenever PT voltage exceeds this level."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Vmax()

    # Setter
    Value, = args
    lib.CapControls_Set_Vmax(Value)
    CheckForError()


def Vmin(*args):
    """With VoltOverride, switch ON whenever PT voltage drops below this level."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Vmin()

    # Setter
    Value, = args
    lib.CapControls_Set_Vmin(Value)
    CheckForError()


def Idx(*args):
    """
    Get/set active CapControl by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.CapControls_Set_idx(Value))


_columns = [
    "CTRatio",
    "Capacitor",
    "DeadTime",
    "Delay",
    "DelayOff",
    "Mode",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "OFFSetting",
    "ONSetting",
    "PTRatio",
    "UseVoltOverride",
    "Vmax",
    "Vmin",
    "Idx",
]
__all__ = [
    "Reset",
    "AllNames",
    "CTRatio",
    "Capacitor",
    "Count",
    "DeadTime",
    "Delay",
    "DelayOff",
    "First",
    "Mode",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "OFFSetting",
    "ONSetting",
    "PTRatio",
    "UseVoltOverride",
    "Vmax",
    "Vmin",
    "Idx",
]
