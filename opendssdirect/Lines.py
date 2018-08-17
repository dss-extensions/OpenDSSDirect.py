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


def New(Name):
    if type(Name) is not bytes:
        Name = Name.encode(codec)

    return lib.Lines_New(Name)


def AllNames():
    """(read-only) Names of all Line Objects"""
    return get_string_array(lib.Lines_Get_AllNames)


def Bus1(*args):
    """Name of bus for terminal 1."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_Bus1())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_Bus1(Value)


def Bus2(*args):
    """Name of bus for terminal 2."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_Bus2())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_Bus2(Value)


def C0(*args):
    """Zero Sequence capacitance, nanofarads per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_C0()

    # Setter
    Value, = args
    lib.Lines_Set_C0(Value)


def C1(*args):
    """Positive Sequence capacitance, nanofarads per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_C1()

    # Setter
    Value, = args
    lib.Lines_Set_C1(Value)


def CMatrix(*args):
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Lines_Get_Cmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Lines_Set_Cmatrix(ValuePtr, ValueCount)


def Count():
    """(read-only) Number of Line objects in Active Circuit."""
    return lib.Lines_Get_Count()


def EmergAmps(*args):
    """Emergency (maximum) ampere rating of Line."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_EmergAmps()

    # Setter
    Value, = args
    lib.Lines_Set_EmergAmps(Value)


def First():
    """(read-only) Invoking this property sets the first element active.  Returns 0 if no lines.  Otherwise, index of the line element."""
    return lib.Lines_Get_First()


def Geometry(*args):
    """Line geometry code"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_Geometry())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_Geometry(Value)


def Length(*args):
    """Length of line section in units compatible with the LineCode definition."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Length()

    # Setter
    Value, = args
    lib.Lines_Set_Length(Value)


def LineCode(*args):
    """Name of LineCode object that defines the impedances."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_LineCode())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_LineCode(Value)


def Name(*args):
    """Specify the name of the Line element to set it active."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_Name(Value)


def Next():
    """(read-only) Invoking this property advances to the next Line element active.  Returns 0 if no more lines.  Otherwise, index of the line element."""
    return lib.Lines_Get_Next()


def NormAmps(*args):
    """Normal ampere rating of Line."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_NormAmps()

    # Setter
    Value, = args
    lib.Lines_Set_NormAmps(Value)


def NumCust():
    """(read-only) Number of customers on this line section."""
    return lib.Lines_Get_NumCust()


def Parent():
    """(read-only) Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails."""
    return lib.Lines_Get_Parent()


def Phases(*args):
    """Number of Phases, this Line element."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Phases()

    # Setter
    Value, = args
    lib.Lines_Set_Phases(Value)


def R0(*args):
    """Zero Sequence resistance, ohms per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_R0()

    # Setter
    Value, = args
    lib.Lines_Set_R0(Value)


def R1(*args):
    """Positive Sequence resistance, ohms per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_R1()

    # Setter
    Value, = args
    lib.Lines_Set_R1(Value)


def Rg(*args):
    """Earth return resistance value used to compute line impedances at power frequency"""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Rg()

    # Setter
    Value, = args
    lib.Lines_Set_Rg(Value)


def Rho(*args):
    """Earth Resistivity, m-ohms"""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Rho()

    # Setter
    Value, = args
    lib.Lines_Set_Rho(Value)


def RMatrix(*args):
    """Resistance matrix (full), ohms per unit length. Array of doubles."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Lines_Get_Rmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Lines_Set_Rmatrix(ValuePtr, ValueCount)


def Spacing(*args):
    """Line spacing code"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Lines_Get_Spacing())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Lines_Set_Spacing(Value)


def TotalCust():
    """(read-only) Total Number of customers served from this line section."""
    return lib.Lines_Get_TotalCust()


def Units(*args):
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Units()

    # Setter
    Value, = args
    lib.Lines_Set_Units(Value)


def X0(*args):
    """Zero Sequence reactance ohms per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_X0()

    # Setter
    Value, = args
    lib.Lines_Set_X0(Value)


def X1(*args):
    """Positive Sequence reactance, ohms per unit length."""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_X1()

    # Setter
    Value, = args
    lib.Lines_Set_X1(Value)


def Xg(*args):
    """Earth return reactance value used to compute line impedances at power frequency"""
    # Getter
    if len(args) == 0:
        return lib.Lines_Get_Xg()

    # Setter
    Value, = args
    lib.Lines_Set_Xg(Value)


def XMatrix(*args):
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Lines_Get_Xmatrix)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Lines_Set_Xmatrix(ValuePtr, ValueCount)


def Yprim(*args):
    """Yprimitive: Does Nothing at present on Put; Dangerous"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Lines_Get_Yprim)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Lines_Set_Yprim(ValuePtr, ValueCount)


_columns = [
    "Bus1",
    "Bus2",
    "C0",
    "C1",
    "CMatrix",
    "EmergAmps",
    "Geometry",
    "Length",
    "LineCode",
    "Name",
    "NormAmps",
    "NumCust",
    "Parent",
    "Phases",
    "R0",
    "R1",
    "Rg",
    "Rho",
    "RMatrix",
    "Spacing",
    "TotalCust",
    "Units",
    "X0",
    "X1",
    "Xg",
    "XMatrix",
    "Yprim",
]
__all__ = [
    "New",
    "AllNames",
    "Bus1",
    "Bus2",
    "C0",
    "C1",
    "CMatrix",
    "Count",
    "EmergAmps",
    "First",
    "Geometry",
    "Length",
    "LineCode",
    "Name",
    "Next",
    "NormAmps",
    "NumCust",
    "Parent",
    "Phases",
    "R0",
    "R1",
    "Rg",
    "Rho",
    "RMatrix",
    "Spacing",
    "TotalCust",
    "Units",
    "X0",
    "X1",
    "Xg",
    "XMatrix",
    "Yprim",
]
