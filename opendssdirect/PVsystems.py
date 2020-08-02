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


def AllNames():
    """(read-only) List of strings with all PVSystem names"""
    return CheckForError(get_string_array(lib.PVSystems_Get_AllNames))


def Count():
    """(read-only) Number of PVSystems"""
    return CheckForError(lib.PVSystems_Get_Count())


def First():
    """Set first PVSystem active; returns 0 if none."""
    return CheckForError(lib.PVSystems_Get_First())


def Irradiance(*args):
    """Get/set the present value of the Irradiance property in W/m²"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_Irradiance())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_Irradiance(Value))


def Name(*args):
    """
    Get/set the name of the active PVSystem
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.PVSystems_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_Name(Value))


def Next():
    """Sets next PVSystem active; returns 0 if no more."""
    return CheckForError(lib.PVSystems_Get_Next())


def pf(*args):
    """Get/set the power factor for the active PVSystem"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_PF())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_PF(Value))


def RegisterNames():
    """(read-only) Array of PVSYSTEM energy meter register names"""
    return CheckForError(get_string_array(lib.PVSystems_Get_RegisterNames))


def RegisterValues():
    """(read-only) Array of doubles containing values in PVSystem registers."""
    return get_float64_array(lib.PVSystems_Get_RegisterValues)


def Idx(*args):
    """
    Get/set active PVSystem by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_idx(Value))


def kVARated(*args):
    """Get/set Rated kVA of the PVSystem"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_kVArated())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_kVArated(Value))


def kW():
    """(read-only) get kW output"""
    return CheckForError(lib.PVSystems_Get_kW())


def kvar(*args):
    """Get/set kvar output value"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_kvar())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_kvar(Value))


def daily(*args):
    """Name of the loadshape for a daily PVSystem profile."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_daily()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_daily(Value))


def duty(*args):
    """
    Name of the load shape to use for duty cycle dispatch simulations such as
    for solar ramp rate studies. Must be previously defined as a Loadshape
    object. Typically would have time intervals of 1-5 seconds.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_duty()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_duty(Value))


def yearly(*args):
    """
    Dispatch shape to use for yearly simulations. Must be previously defined
    as a Loadshape object. If this is not specified, the Daily dispatch shape,
    if any, is repeated during Yearly solution modes. In the default dispatch
    mode, the PVSystem element uses this loadshape to trigger State changes.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_yearly()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_yearly(Value))


def Tdaily(*args):
    """
    Temperature shape to use for daily simulations. Must be previously defined
    as a TShape object of 24 hrs, typically. The PVSystem element uses this
    TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
    with the Pmpp vs T curve.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_Tdaily()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_Tdaily(Value))


def Tduty(*args):
    """
    Temperature shape to use for duty cycle dispatch simulations such as for
    solar ramp rate studies. Must be previously defined as a TShape object.
    Typically would have time intervals of 1-5 seconds. Designate the number
    of points to solve using the Set Number=xxxx command. If there are fewer
    points in the actual shape, the shape is assumed to repeat. The PVSystem
    model uses this TShape to determine the Pmpp from the Pmpp vs T curve.
    Units must agree with the Pmpp vs T curve.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_Tduty()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_Tduty(Value))


def Tyearly(*args):
    """
    Temperature shape to use for yearly simulations. Must be previously defined
    as a TShape object. If this is not specified, the Daily dispatch shape, if
    any, is repeated during Yearly solution modes. The PVSystem element uses
    this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
    agree with the Pmpp vs T curve.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PVSystems_Get_Tyearly()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PVSystems_Set_Tyearly(Value))


def IrradianceNow():
    """
    Returns the current irradiance value for the active PVSystem. Use it to 
    know what's the current irradiance value for the PV during a simulation.
    """
    return CheckForError(lib.PVSystems_Get_IrradianceNow())


def Pmpp(*args):
    """
    Gets/sets the rated max power of the PV array for 1.0 kW/sq-m irradiance 
    and a user-selected array temperature of the active PVSystem.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PVSystems_Get_Pmpp())

    # Setter
    Value, = args
    CheckForError(lib.PVSystems_Set_Pmpp(Value))


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
    "IrradianceNow",
    "Pmpp",
    "daily",
    "duty",
    "yearly",
    "Tdaily",
    "Tduty",
    "Tyearly",
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
    "daily",
    "duty",
    "yearly",
    "Tdaily",
    "Tduty",
    "Tyearly",
    "IrradianceNow",
    "Pmpp",
]
