# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_string_array,
    prepare_float64_array,
)


def AllNames():
    """(read-only) List of strings with all Reactor names"""
    return CheckForError(get_string_array(lib.Reactors_Get_AllNames))


def Count():
    """(read-only) Number of Reactors"""
    return CheckForError(lib.Reactors_Get_Count())


def Idx(*args):
    """
    Get/set active Reactor by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_idx(Value))


def First():
    """Set first Reactor active; returns 0 if none."""
    return CheckForError(lib.Reactors_Get_First())


def Next():
    """Sets next Reactor active; returns 0 if no more."""
    return CheckForError(lib.Reactors_Get_Next())


def Name(*args):
    """
    Get/set the name of the active Reactor
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Reactors_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reactors_Set_Name(Value))


def SpecType():
    """
    How the reactor data was provided: 1=kvar, 2=R+jX, 3=R and X matrices, 4=sym components.
    Depending on this value, only some properties are filled or make sense in the context.
    """
    return CheckForError(lib.Reactors_Get_SpecType())


def IsDelta(*args):
    """Delta connection or wye?"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_IsDelta()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_IsDelta(Value))


def Parallel(*args):
    """Indicates whether Rmatrix and Xmatrix are to be considered in parallel."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_Parallel()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_Parallel(Value))


def LmH(*args):
    """Inductance, mH. Alternate way to define the reactance, X, property."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_LmH())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_LmH(Value))


def kV(*args):
    """For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_kV())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_kV(Value))


def kvar(*args):
    """Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_kvar())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_kvar(Value))


def Phases(*args):
    """Number of phases."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_Phases())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_Phases(Value))


def Bus1(*args):
    """
    Name of first bus.
    Bus2 property will default to this bus, node 0, unless previously specified.
    Only Bus1 need be specified for a Yg shunt reactor.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reactors_Get_Bus1()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reactors_Set_Bus1(Value))


def Bus2(*args):
    """
    Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.
    Not necessary to specify for delta (LL) connection
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reactors_Get_Bus2()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reactors_Set_Bus2(Value))


def LCurve(*args):
    """Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property. L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reactors_Get_LCurve()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reactors_Set_LCurve(Value))


def RCurve(*args):
    """Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Reactors_Get_RCurve()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Reactors_Set_RCurve(Value))


def R(*args):
    """Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_R())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_R(Value))


def X(*args):
    """Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_X())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_X(Value))


def Rp(*args):
    """Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Reactors_Get_Rp())

    # Setter
    Value, = args
    CheckForError(lib.Reactors_Set_Rp(Value))


def Rmatrix(*args):
    """Resistance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Rmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Rmatrix(ValuePtr, ValueCount))


def Xmatrix(*args):
    """Reactance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Xmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Xmatrix(ValuePtr, ValueCount))


def Z(*args):
    """Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Z)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Z(ValuePtr, ValueCount))


def Z1(*args):
    """
    Positive-sequence impedance, ohms, as a 2-element array representing a complex number.

    If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR.

    Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

    Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.
    """
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Z1)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Z1(ValuePtr, ValueCount))


def Z2(*args):
    """
    Negative-sequence impedance, ohms, as a 2-element array representing a complex number.

    Used to define the impedance matrix of the REACTOR if Z1 is also specified.

    Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.
    """
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Z2)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Z2(ValuePtr, ValueCount))


def Z0(*args):
    """
    Zero-sequence impedance, ohms, as a 2-element array representing a complex number.

    Used to define the impedance matrix of the REACTOR if Z1 is also specified.

    Note: Z0 defaults to Z1 if it is not specifically defined.
    """
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Reactors_Get_Z0)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Reactors_Set_Z0(ValuePtr, ValueCount))


_columns = [
    "Name",
    "Idx",
    "Phases",
    "Bus1",
    "Bus2",
    "SpecType",
    "kV",
    "kvar",
    "IsDelta",
    "Parallel",
    "LCurve",
    "RCurve",
    "R",
    "Rp",
    "X",
    "Z0",
    "Z1",
    "Z2",
    "Z",
    "Rmatrix",
    "Xmatrix",
]
__all__ = [
    "SpecType",
    "IsDelta",
    "Parallel",
    "LmH",
    "kV",
    "kvar",
    "Phases",
    "Bus1",
    "Bus2",
    "LCurve",
    "RCurve",
    "R",
    "X",
    "Rp",
    "Rmatrix",
    "Xmatrix",
    "Z",
    "Z1",
    "Z2",
    "Z0",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
