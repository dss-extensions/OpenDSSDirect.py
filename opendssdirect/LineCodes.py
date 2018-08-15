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


def AllNames():
    """(read-only) Array of strings with names of all devices"""
    return get_string_array(lib.LineCodes_Get_AllNames)


def C0(*args):
    """Zero-sequence capacitance, nF per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_C0()

    # Setter
    Value, = args
    lib.LineCodes_Set_C0(Value)


def C1(*args):
    """Positive-sequence capacitance, nF per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_C1()

    # Setter
    Value, = args
    lib.LineCodes_Set_C1(Value)


def Cmatrix(*args):
    """Capacitance matrix, nF per unit length"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineCodes_Get_Cmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount)


def Count():
    """(read-only) Number of LineCodes"""
    return lib.LineCodes_Get_Count()


def EmergAmps(*args):
    """Emergency ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_EmergAmps()

    # Setter
    Value, = args
    lib.LineCodes_Set_EmergAmps(Value)


def First():
    return lib.LineCodes_Get_First()


def IsZ1Z0():
    """(read-only) Flag denoting whether impedance data were entered in symmetrical components"""
    return lib.LineCodes_Get_IsZ1Z0() != 0


def Name(*args):
    """Name of active LineCode"""
    # Getter
    if len(args) == 0:
        return get_string(lib.LineCodes_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.LineCodes_Set_Name(Value)


def Next():
    return lib.LineCodes_Get_Next()


def NormAmps(*args):
    """Normal Ampere rating"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_NormAmps()

    # Setter
    Value, = args
    lib.LineCodes_Set_NormAmps(Value)


def Phases(*args):
    """Number of Phases"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_Phases()

    # Setter
    Value, = args
    lib.LineCodes_Set_Phases(Value)


def R0(*args):
    """Zero-Sequence Resistance, ohms per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_R0()

    # Setter
    Value, = args
    lib.LineCodes_Set_R0(Value)


def R1(*args):
    """Positive-sequence resistance ohms per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_R1()

    # Setter
    Value, = args
    lib.LineCodes_Set_R1(Value)


def Rmatrix(*args):
    """Resistance matrix, ohms per unit length"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineCodes_Get_Rmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount)


def Units(*args):
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_Units()

    # Setter
    Value, = args
    lib.LineCodes_Set_Units(Value)


def X0(*args):
    """Zero Sequence Reactance, Ohms per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_X0()

    # Setter
    Value, = args
    lib.LineCodes_Set_X0(Value)


def X1(*args):
    """Posiive-sequence reactance, ohms per unit length"""
    # Getter
    if len(args) == 0:
        return lib.LineCodes_Get_X1()

    # Setter
    Value, = args
    lib.LineCodes_Set_X1(Value)


def Xmatrix(*args):
    """Reactance matrix, ohms per unit length"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LineCodes_Get_Xmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount)


_columns = [
    "C0",
    "C1",
    "Cmatrix",
    "EmergAmps",
    "IsZ1Z0",
    "Name",
    "NormAmps",
    "Phases",
    "R0",
    "R1",
    "Rmatrix",
    "Units",
    "X0",
    "X1",
    "Xmatrix",
]
__all__ = [
    "AllNames",
    "C0",
    "C1",
    "Cmatrix",
    "Count",
    "EmergAmps",
    "First",
    "IsZ1Z0",
    "Name",
    "Next",
    "NormAmps",
    "Phases",
    "R0",
    "R1",
    "Rmatrix",
    "Units",
    "X0",
    "X1",
    "Xmatrix",
]
