# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def Reset():
    lib.CapControls_Reset()


def AllNames():
    """(read-only) Array of strings with all CapControl names."""
    return get_string_array(lib.CapControls_Get_AllNames)


def CTRatio(*args):
    """Transducer ratio from pirmary current to control current."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_CTratio()

    # Setter
    Value, = args
    lib.CapControls_Set_CTratio(Value)


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


def Count():
    """(read-only) Number of CapControls in Active Circuit"""
    return lib.CapControls_Get_Count()


def DeadTime(*args):
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_DeadTime()

    # Setter
    Value, = args
    lib.CapControls_Set_DeadTime(Value)


def Delay(*args):
    """Time delay [s] to switch on after arming.  Control may reset before actually switching."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Delay()

    # Setter
    Value, = args
    lib.CapControls_Set_Delay(Value)


def DelayOff(*args):
    """Time delay [s] before swithcing off a step. Control may reset before actually switching."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_DelayOff()

    # Setter
    Value, = args
    lib.CapControls_Set_DelayOff(Value)


def First():
    """(read-only) Sets the first CapControl as active. Return 0 if none."""
    return lib.CapControls_Get_First()


def Mode(*args):
    """Type of automatic controller."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Mode()

    # Setter
    Value, = args
    lib.CapControls_Set_Mode(Value)


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


def MonitoredTerm(*args):
    """Terminal number on the element that PT and CT are connected to."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_MonitoredTerm()

    # Setter
    Value, = args
    lib.CapControls_Set_MonitoredTerm(Value)


def Name(*args):
    """Sets a CapControl active by name."""
    # Getter
    if len(args) == 0:
        return get_string(lib.CapControls_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.CapControls_Set_Name(Value)


def Next():
    """(read-only) Gets the next CapControl in the circut. Returns 0 if none."""
    return lib.CapControls_Get_Next()


def OFFSetting(*args):
    """Threshold to switch off a step. See Mode for units."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_OFFSetting()

    # Setter
    Value, = args
    lib.CapControls_Set_OFFSetting(Value)


def ONSetting(*args):
    """Threshold to arm or switch on a step.  See Mode for units."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_ONSetting()

    # Setter
    Value, = args
    lib.CapControls_Set_ONSetting(Value)


def PTRatio(*args):
    """Transducer ratio from primary feeder to control voltage."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_PTratio()

    # Setter
    Value, = args
    lib.CapControls_Set_PTratio(Value)


def UseVoltOverride(*args):
    """Enables Vmin and Vmax to override the control Mode"""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_UseVoltOverride() != 0

    # Setter
    Value, = args
    lib.CapControls_Set_UseVoltOverride(Value)


def Vmax(*args):
    """With VoltOverride, swtich off whenever PT voltage exceeds this level."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Vmax()

    # Setter
    Value, = args
    lib.CapControls_Set_Vmax(Value)


def Vmin(*args):
    """With VoltOverride, switch ON whenever PT voltage drops below this level."""
    # Getter
    if len(args) == 0:
        return lib.CapControls_Get_Vmin()

    # Setter
    Value, = args
    lib.CapControls_Set_Vmin(Value)


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
]
