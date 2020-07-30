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


def Capacity(Start, Increment):
    return CheckForError(lib.Circuit_Capacity(Start, Increment))


def Disable(Name):
    if type(Name) is not bytes:
        Name = Name.encode(codec)
    CheckForError(lib.Circuit_Disable(Name))


def Enable(Name):
    if type(Name) is not bytes:
        Name = Name.encode(codec)
    CheckForError(lib.Circuit_Enable(Name))


def EndOfTimeStepUpdate():
    CheckForError(lib.Circuit_EndOfTimeStepUpdate())


def FirstElement():
    return CheckForError(lib.Circuit_FirstElement())


def FirstPCElement():
    return CheckForError(lib.Circuit_FirstPCElement())


def FirstPDElement():
    return CheckForError(lib.Circuit_FirstPDElement())


def AllNodeDistancesByPhase(Phase):
    """(read-only) Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties."""
    return CheckForError(
        get_float64_array(lib.Circuit_Get_AllNodeDistancesByPhase, Phase)
    )


def AllNodeNamesByPhase(Phase):
    """(read-only) Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties."""
    return CheckForError(get_string_array(lib.Circuit_Get_AllNodeNamesByPhase, Phase))


def AllNodeVmagByPhase(Phase):
    """(read-only) Returns Array of doubles represent voltage magnitudes for nodes on the specified phase."""
    return CheckForError(get_float64_array(lib.Circuit_Get_AllNodeVmagByPhase, Phase))


def AllNodeVmagPUByPhase(Phase):
    """(read-only) Returns array of per unit voltage magnitudes for each node by phase"""
    return CheckForError(get_float64_array(lib.Circuit_Get_AllNodeVmagPUByPhase, Phase))


def NextElement():
    return CheckForError(lib.Circuit_NextElement())


def NextPCElement():
    return CheckForError(lib.Circuit_NextPCElement())


def NextPDElement():
    return CheckForError(lib.Circuit_NextPDElement())


def Sample():
    CheckForError(lib.Circuit_Sample())


def SaveSample():
    CheckForError(lib.Circuit_SaveSample())


def SetActiveBus(BusName):
    if type(BusName) is not bytes:
        BusName = BusName.encode(codec)
    return CheckForError(lib.Circuit_SetActiveBus(BusName))


def SetActiveBusi(BusIndex):
    return CheckForError(lib.Circuit_SetActiveBusi(BusIndex))


def SetActiveClass(ClassName):
    if type(ClassName) is not bytes:
        ClassName = ClassName.encode(codec)
    return CheckForError(lib.Circuit_SetActiveClass(ClassName))


def SetActiveElement(FullName):
    if type(FullName) is not bytes:
        FullName = FullName.encode(codec)
    return CheckForError(lib.Circuit_SetActiveElement(FullName))


def UpdateStorage():
    CheckForError(lib.Circuit_UpdateStorage())


def AllBusDistances():
    """(read-only) Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames."""
    return get_float64_array(lib.Circuit_Get_AllBusDistances)


def AllBusNames():
    """(read-only) Array of strings containing names of all buses in circuit (see AllNodeNames)."""
    return CheckForError(get_string_array(lib.Circuit_Get_AllBusNames))


def AllBusVMag():
    """(read-only) Array of magnitudes (doubles) of voltages at all buses"""
    return get_float64_array(lib.Circuit_Get_AllBusVmag)


def AllBusMagPu():
    """(read-only) Double Array of all bus voltages (each node) magnitudes in Per unit"""
    return get_float64_array(lib.Circuit_Get_AllBusVmagPu)


def AllBusVolts():
    """(read-only) Complex array of all bus, node voltages from most recent solution"""
    return get_float64_array(lib.Circuit_Get_AllBusVolts)


def AllElementLosses():
    """(read-only) Array of total losses (complex) in each circuit element"""
    return get_float64_array(lib.Circuit_Get_AllElementLosses)


def AllElementNames():
    """(read-only) Array of strings containing Full Name of all elements."""
    return CheckForError(get_string_array(lib.Circuit_Get_AllElementNames))


def AllNodeDistances():
    """(read-only) Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence."""
    return get_float64_array(lib.Circuit_Get_AllNodeDistances)


def AllNodeNames():
    """(read-only) Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc."""
    return CheckForError(get_string_array(lib.Circuit_Get_AllNodeNames))


def LineLosses():
    """(read-only) Complex total line losses in the circuit"""
    return get_float64_array(lib.Circuit_Get_LineLosses)


def Losses():
    """(read-only) Total losses in active circuit, complex number (two-element array of double)."""
    return get_float64_array(lib.Circuit_Get_Losses)


def Name():
    """(read-only) Name of the active circuit."""
    return get_string(CheckForError(lib.Circuit_Get_Name()))


def NumBuses():
    """(read-only) Total number of Buses in the circuit."""
    return CheckForError(lib.Circuit_Get_NumBuses())


def NumCktElements():
    """(read-only) Number of CktElements in the circuit."""
    return CheckForError(lib.Circuit_Get_NumCktElements())


def NumNodes():
    """(read-only) Total number of nodes in the circuit."""
    return CheckForError(lib.Circuit_Get_NumNodes())


def ParentPDElement():
    """(read-only) Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable."""
    return CheckForError(lib.Circuit_Get_ParentPDElement())


def SubstationLosses():
    """(read-only) Complex losses in all transformers designated to substations."""
    return get_float64_array(lib.Circuit_Get_SubstationLosses)


def SystemY():
    """
    (read-only) System Y matrix (after a solution has been performed). 
    This is deprecated as it returns a dense matrix. Only use it for small systems.
    For large scale systems, prefer YMatrix.GetCompressedYMatrix.
    """
    return get_float64_array(lib.Circuit_Get_SystemY)


def TotalPower():
    """(read-only) Total power, watts delivered to the circuit"""
    return get_float64_array(lib.Circuit_Get_TotalPower)


def YCurrents():
    """(read-only) Array of doubles containing complex injection currents for the present solution. Is is the "I" vector of I=YV"""
    return get_float64_array(lib.Circuit_Get_YCurrents)


def YNodeOrder():
    """(read-only) Array of strings containing the names of the nodes in the same order as the Y matrix"""
    return CheckForError(get_string_array(lib.Circuit_Get_YNodeOrder))


def YNodeVArray():
    """(read-only) Complex array of actual node voltages in same order as SystemY matrix."""
    return get_float64_array(lib.Circuit_Get_YNodeVarray)


_columns = [
    "LineLosses",
    "Losses",
    "Name",
    "NumBuses",
    "NumCktElements",
    "NumNodes",
    "SubstationLosses",
    "TotalPower",
    "YCurrents",
    "YNodeOrder",
    "YNodeVArray",
    "AllBusDistances",
    "AllBusNames",
    "AllBusVMag",
    "AllBusMagPu",
    "AllBusVolts",
    "AllNodeNames",
    "AllNodeDistances",
    "AllElementNames",
    "AllElementLosses",
]
__all__ = [
    "Capacity",
    "Disable",
    "Enable",
    "EndOfTimeStepUpdate",
    "FirstElement",
    "FirstPCElement",
    "FirstPDElement",
    "AllNodeDistancesByPhase",
    "AllNodeNamesByPhase",
    "AllNodeVmagByPhase",
    "AllNodeVmagPUByPhase",
    "NextElement",
    "NextPCElement",
    "NextPDElement",
    "Sample",
    "SaveSample",
    "SetActiveBus",
    "SetActiveBusi",
    "SetActiveClass",
    "SetActiveElement",
    "UpdateStorage",
    "AllBusDistances",
    "AllBusNames",
    "AllBusVMag",
    "AllBusMagPu",
    "AllBusVolts",
    "AllElementLosses",
    "AllElementNames",
    "AllNodeDistances",
    "AllNodeNames",
    "LineLosses",
    "Losses",
    "Name",
    "NumBuses",
    "NumCktElements",
    "NumNodes",
    "ParentPDElement",
    "SubstationLosses",
    "SystemY",
    "TotalPower",
    "YCurrents",
    "YNodeOrder",
    "YNodeVArray",
]
