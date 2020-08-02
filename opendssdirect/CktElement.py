# -*- coding: utf-8 -*-
from __future__ import absolute_import
import warnings
from ._utils import (
    lib,
    ffi,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_int32_array,
    get_string_array,
    prepare_string_array,
    DSSException,
)


def Close(Term, Phs):
    CheckForError(lib.CktElement_Close(Term, Phs))


def Controller(idx):
    """(read-only) Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range"""
    return get_string(CheckForError(lib.CktElement_Get_Controller(idx)))


def Variable(MyVarName, Code=None):
    """
    If the active element is a PCElement, get the value of a variable by name.
    Otherwise, an exception is raised.
    """
    if Code is not None:
        warnings.warn(
            "The Code parameter is deprecated and unused. It will be removed in a future version."
        )

    if type(MyVarName) is not bytes:
        MyVarName = MyVarName.encode(codec)
    Code = ffi.new("int32_t*")
    result = lib.CktElement_Get_Variable(MyVarName, Code)
    if Code[0] != 0:
        raise DSSException(Code[0], "No variable by this name or not a PCelement.")

    return result


def Variablei(Idx, Code=None):
    """
    If the active element is a PCElement, get the value of a variable by its integer index.
    Otherwise, an exception is raised.
    """
    if Code is not None:
        warnings.warn(
            "The Code parameter is deprecated and unused. It will be removed in a future version."
        )

    Code = ffi.new("int32_t*")
    result = lib.CktElement_Get_Variablei(Idx, Code)
    if Code[0] != 0:
        raise DSSException(Code[0], "No variable by this index or not a PCelement.")

    return result


def IsOpen(Term, Phs):
    return CheckForError(lib.CktElement_IsOpen(Term, Phs)) != 0


def Open(Term, Phs):
    CheckForError(lib.CktElement_Open(Term, Phs))


def AllPropertyNames():
    """(read-only) Array containing all property names of the active device."""
    return CheckForError(get_string_array(lib.CktElement_Get_AllPropertyNames))


def AllVariableNames():
    """(read-only) Array of strings listing all the published variable names, if a PCElement. Otherwise, null string."""
    return CheckForError(get_string_array(lib.CktElement_Get_AllVariableNames))


def AllVariableValues():
    """(read-only) Array of doubles. Values of state variables of active element if PC element."""
    return get_float64_array(lib.CktElement_Get_AllVariableValues)


def BusNames(*args):
    """
    Array of strings. Get  Bus definitions to which each terminal is connected. 0-based array.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string_array(lib.CktElement_Get_BusNames))

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_string_array(Value)
    CheckForError(lib.CktElement_Set_BusNames(ValuePtr, ValueCount))


def CplxSeqCurrents():
    """(read-only) Complex double array of Sequence Currents for all conductors of all terminals of active circuit element."""
    return get_float64_array(lib.CktElement_Get_CplxSeqCurrents)


def CplxSeqVoltages():
    """(read-only) Complex double array of Sequence Voltage for all terminals of active circuit element."""
    return get_float64_array(lib.CktElement_Get_CplxSeqVoltages)


def Currents():
    """(read-only) Complex array of currents into each conductor of each terminal"""
    return get_float64_array(lib.CktElement_Get_Currents)


def CurrentsMagAng():
    """(read-only) Currents in magnitude, angle format as a array of doubles."""
    return get_float64_array(lib.CktElement_Get_CurrentsMagAng)


def DisplayName(*args):
    """Display name of the object (not necessarily unique)"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.CktElement_Get_DisplayName()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.CktElement_Set_DisplayName(Value))


def EmergAmps(*args):
    """Emergency Ampere Rating for PD elements"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CktElement_Get_EmergAmps())

    # Setter
    Value, = args
    CheckForError(lib.CktElement_Set_EmergAmps(Value))


def Enabled(*args):
    """Boolean indicating that element is currently in the circuit."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CktElement_Get_Enabled()) != 0

    # Setter
    Value, = args
    CheckForError(lib.CktElement_Set_Enabled(Value))


def EnergyMeter():
    """(read-only) Name of the Energy Meter this element is assigned to."""
    return get_string(CheckForError(lib.CktElement_Get_EnergyMeter()))


def GUID():
    """(read-only) globally unique identifier for this object"""
    return get_string(CheckForError(lib.CktElement_Get_GUID()))


def Handle():
    """(read-only) Pointer to this object"""
    return CheckForError(lib.CktElement_Get_Handle())


def HasOCPDevice():
    """(read-only) True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection"""
    return CheckForError(lib.CktElement_Get_HasOCPDevice()) != 0


def HasSwitchControl():
    """(read-only) This element has a SwtControl attached."""
    return CheckForError(lib.CktElement_Get_HasSwitchControl()) != 0


def HasVoltControl():
    """(read-only) This element has a CapControl or RegControl attached."""
    return CheckForError(lib.CktElement_Get_HasVoltControl()) != 0


def Losses():
    """(read-only) Total losses in the element: two-element complex array"""
    return get_float64_array(lib.CktElement_Get_Losses)


def Name():
    """(read-only) Full Name of Active Circuit Element"""
    return get_string(CheckForError(lib.CktElement_Get_Name()))


def NodeOrder():
    """(read-only) Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal."""
    return get_int32_array(lib.CktElement_Get_NodeOrder)


def NormalAmps(*args):
    """Normal ampere rating for PD Elements"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.CktElement_Get_NormalAmps())

    # Setter
    Value, = args
    CheckForError(lib.CktElement_Set_NormalAmps(Value))


def NumConductors():
    """(read-only) Number of Conductors per Terminal"""
    return CheckForError(lib.CktElement_Get_NumConductors())


def NumControls():
    """
    (read-only) Number of controls connected to this device. 
    Use to determine valid range for index into Controller array.
    """
    return CheckForError(lib.CktElement_Get_NumControls())


def NumPhases():
    """(read-only) Number of Phases"""
    return CheckForError(lib.CktElement_Get_NumPhases())


def NumProperties():
    """(read-only) Number of Properties this Circuit Element."""
    return CheckForError(lib.CktElement_Get_NumProperties())


def NumTerminals():
    """(read-only) Number of Terminals this Circuit Element"""
    return CheckForError(lib.CktElement_Get_NumTerminals())


def OCPDevIndex():
    """(read-only) Index into Controller list of OCP Device controlling this CktElement"""
    return CheckForError(lib.CktElement_Get_OCPDevIndex())


def OCPDevType():
    """(read-only) 0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device"""
    return CheckForError(lib.CktElement_Get_OCPDevType())


def PhaseLosses():
    """(read-only) Complex array of losses by phase"""
    return get_float64_array(lib.CktElement_Get_PhaseLosses)


def Powers():
    """(read-only) Complex array of powers into each conductor of each terminal"""
    return get_float64_array(lib.CktElement_Get_Powers)


def Residuals():
    """(read-only) Residual currents for each terminal: (mag, angle)"""
    return get_float64_array(lib.CktElement_Get_Residuals)


def SeqCurrents():
    """(read-only) Double array of symmetrical component currents into each 3-phase terminal"""
    return get_float64_array(lib.CktElement_Get_SeqCurrents)


def SeqPowers():
    """(read-only) Double array of sequence powers into each 3-phase teminal"""
    return get_float64_array(lib.CktElement_Get_SeqPowers)


def SeqVoltages():
    """(read-only) Double array of symmetrical component voltages at each 3-phase terminal"""
    return get_float64_array(lib.CktElement_Get_SeqVoltages)


def Voltages():
    """(read-only) Complex array of voltages at terminals"""
    return get_float64_array(lib.CktElement_Get_Voltages)


def VoltagesMagAng():
    """(read-only) Voltages at each conductor in magnitude, angle form as array of doubles."""
    return get_float64_array(lib.CktElement_Get_VoltagesMagAng)


def YPrim():
    """(read-only) YPrim matrix, column order, complex numbers (paired)"""
    return get_float64_array(lib.CktElement_Get_Yprim)


def IsIsolated():
    """
    Returns true if the current active element is isolated.
    Note that this only fetches the current value. See also the Topology interface.
    """
    return CheckForError(lib.CktElement_Get_IsIsolated()) != 0


_columns = [
    "BusNames",
    "CplxSeqCurrents",
    "CplxSeqVoltages",
    "Currents",
    "CurrentsMagAng",
    "DisplayName",
    "EmergAmps",
    "Enabled",
    "EnergyMeter",
    "GUID",
    "Handle",
    "HasOCPDevice",
    "HasSwitchControl",
    "HasVoltControl",
    "Losses",
    "Name",
    "NodeOrder",
    "NormalAmps",
    "NumConductors",
    "NumControls",
    "NumPhases",
    "NumProperties",
    "NumTerminals",
    "OCPDevIndex",
    "OCPDevType",
    "PhaseLosses",
    "Powers",
    "Residuals",
    "SeqCurrents",
    "SeqPowers",
    "SeqVoltages",
    "Voltages",
    "VoltagesMagAng",
    "YPrim",
    "IsIsolated",
    "AllPropertyNames",
    "AllVariableValues",
    "AllVariableNames",
]
__all__ = [
    "Close",
    "Controller",
    "Variable",
    "Variablei",
    "IsOpen",
    "Open",
    "AllPropertyNames",
    "AllVariableNames",
    "AllVariableValues",
    "BusNames",
    "CplxSeqCurrents",
    "CplxSeqVoltages",
    "Currents",
    "CurrentsMagAng",
    "DisplayName",
    "EmergAmps",
    "Enabled",
    "EnergyMeter",
    "GUID",
    "Handle",
    "HasOCPDevice",
    "HasSwitchControl",
    "HasVoltControl",
    "Losses",
    "Name",
    "NodeOrder",
    "NormalAmps",
    "NumConductors",
    "NumControls",
    "NumPhases",
    "NumProperties",
    "NumTerminals",
    "OCPDevIndex",
    "OCPDevType",
    "PhaseLosses",
    "Powers",
    "Residuals",
    "SeqCurrents",
    "SeqPowers",
    "SeqVoltages",
    "Voltages",
    "VoltagesMagAng",
    "YPrim",
    "IsIsolated",
]
