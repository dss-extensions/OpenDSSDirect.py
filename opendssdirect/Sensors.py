# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    get_string,
    get_string_array,
    get_float64_array,
    prepare_float64_array,
)
from ._utils import codec


def Reset():
    lib.Sensors_Reset()


def ResetAll():
    lib.Sensors_ResetAll()


def AllNames():
    """(read-only) Array of Sensor names."""
    return get_string_array(lib.Sensors_Get_AllNames)


def Count():
    """(read-only) Number of Sensors in Active Circuit."""
    return lib.Sensors_Get_Count()


def Currents(*args):
    """Array of doubles for the line current measurements; don't use with kWS and kVARS."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Sensors_Get_Currents)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Sensors_Set_Currents(ValuePtr, ValueCount)


def First():
    """(read-only) Sets the first sensor active. Returns 0 if none."""
    return lib.Sensors_Get_First()


def IsDelta(*args):
    """True if measured voltages are line-line. Currents are always line currents."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_IsDelta() != 0

    # Setter
    Value, = args
    lib.Sensors_Set_IsDelta(Value)


def MeteredElement(*args):
    """Full Name of the measured element"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Sensors_Get_MeteredElement())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Sensors_Set_MeteredElement(Value)


def MeteredTerminal(*args):
    """Number of the measured terminal in the measured element."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_MeteredTerminal()

    # Setter
    Value, = args
    lib.Sensors_Set_MeteredTerminal(Value)


def Name(*args):
    """
    (read) Name of the active sensor.
    (write) Set the active Sensor by name.
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.Sensors_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Sensors_Set_Name(Value)


def Next():
    """(read-only) Sets the next Sensor active. Returns 0 if no more."""
    return lib.Sensors_Get_Next()


def PctError(*args):
    """Assumed percent error in the Sensor measurement. Default is 1."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_PctError()

    # Setter
    Value, = args
    lib.Sensors_Set_PctError(Value)


def ReverseDelta(*args):
    """True if voltage measurements are 1-3, 3-2, 2-1."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_ReverseDelta() != 0

    # Setter
    Value, = args
    lib.Sensors_Set_ReverseDelta(Value)


def Weight(*args):
    """Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_Weight()

    # Setter
    Value, = args
    lib.Sensors_Set_Weight(Value)


def kvar(*args):
    """Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Sensors_Get_kVARS)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Sensors_Set_kVARS(ValuePtr, ValueCount)


def kVS(*args):
    """Array of doubles for the LL or LN (depending on Delta connection) voltage measurements."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Sensors_Get_kVS)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Sensors_Set_kVS(ValuePtr, ValueCount)


def kVBase(*args):
    """Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors."""
    # Getter
    if len(args) == 0:
        return lib.Sensors_Get_kVbase()

    # Setter
    Value, = args
    lib.Sensors_Set_kVbase(Value)


def kW(*args):
    """Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Sensors_Get_kWS)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Sensors_Set_kWS(ValuePtr, ValueCount)


_columns = [
    "Currents",
    "IsDelta",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "PctError",
    "ReverseDelta",
    "Weight",
    "kvar",
    "kVS",
    "kVBase",
    "kW",
]
__all__ = [
    "Reset",
    "ResetAll",
    "AllNames",
    "Count",
    "Currents",
    "First",
    "IsDelta",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "Next",
    "PctError",
    "ReverseDelta",
    "Weight",
    "kvar",
    "kVS",
    "kVBase",
    "kW",
]
