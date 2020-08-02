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


def CloseAllDIFiles():
    CheckForError(lib.Meters_CloseAllDIFiles())


def DoReliabilityCalc(AssumeRestoration):
    CheckForError(lib.Meters_DoReliabilityCalc(AssumeRestoration))


def OpenAllDIFiles():
    CheckForError(lib.Meters_OpenAllDIFiles())


def Reset():
    CheckForError(lib.Meters_Reset())


def ResetAll():
    CheckForError(lib.Meters_ResetAll())


def Sample():
    CheckForError(lib.Meters_Sample())


def SampleAll():
    CheckForError(lib.Meters_SampleAll())


def Save():
    CheckForError(lib.Meters_Save())


def SaveAll():
    CheckForError(lib.Meters_SaveAll())


def SetActiveSection(SectIdx):
    CheckForError(lib.Meters_SetActiveSection(SectIdx))


def AllBranchesInZone():
    """(read-only) Wide string list of all branches in zone of the active energymeter object."""
    return CheckForError(get_string_array(lib.Meters_Get_AllBranchesInZone))


def AllEndElements():
    """(read-only) Array of names of all zone end elements."""
    return CheckForError(get_string_array(lib.Meters_Get_AllEndElements))


def AllNames():
    """(read-only) List of strings with all Meter names"""
    return CheckForError(get_string_array(lib.Meters_Get_AllNames))


def AllocFactors(*args):
    """Array of doubles: set the phase allocation factors for the active meter."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Meters_Get_AllocFactors)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))


def AvgRepairTime():
    """(read-only) Average Repair time in this section of the meter zone"""
    return CheckForError(lib.Meters_Get_AvgRepairTime())


def CalcCurrent(*args):
    """Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Meters_Get_CalcCurrent)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))


def Count():
    """(read-only) Number of Meters"""
    return CheckForError(lib.Meters_Get_Count())


def CountBranches():
    """(read-only) Number of branches in Active energymeter zone. (Same as sequencelist size)"""
    return CheckForError(lib.Meters_Get_CountBranches())


def CountEndElements():
    """(read-only) Number of zone end elements in the active meter zone."""
    return CheckForError(lib.Meters_Get_CountEndElements())


def CustInterrupts():
    """(read-only) Total customer interruptions for this Meter zone based on reliability calcs."""
    return CheckForError(lib.Meters_Get_CustInterrupts())


def DIFilesAreOpen():
    """(read-only) Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened."""
    return CheckForError(lib.Meters_Get_DIFilesAreOpen()) != 0


def FaultRateXRepairHrs():
    """(read-only) Sum of Fault Rate time Repair Hrs in this section of the meter zone"""
    return CheckForError(lib.Meters_Get_FaultRateXRepairHrs())


def First():
    """Set first Meter active; returns 0 if none."""
    return CheckForError(lib.Meters_Get_First())


def MeteredElement(*args):
    """Set Name of metered element"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Meters_Get_MeteredElement()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Meters_Set_MeteredElement(Value))


def MeteredTerminal(*args):
    """set Number of Metered Terminal"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Meters_Get_MeteredTerminal())

    # Setter
    Value, = args
    CheckForError(lib.Meters_Set_MeteredTerminal(Value))


def Name(*args):
    """
    Get/set the name of the active Meter
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Meters_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Meters_Set_Name(Value))


def Next():
    """Sets next Meter active; returns 0 if no more."""
    return CheckForError(lib.Meters_Get_Next())


def NumSectionBranches():
    """(read-only) Number of branches (lines) in this section"""
    return CheckForError(lib.Meters_Get_NumSectionBranches())


def NumSectionCustomers():
    """(read-only) Number of Customers in the active section."""
    return CheckForError(lib.Meters_Get_NumSectionCustomers())


def NumSections():
    """(read-only) Number of feeder sections in this meter's zone"""
    return CheckForError(lib.Meters_Get_NumSections())


def OCPDeviceType():
    """(read-only) Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay"""
    return CheckForError(lib.Meters_Get_OCPDeviceType())


def PeakCurrent(*args):
    """Array of doubles to set values of Peak Current property"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Meters_Get_Peakcurrent)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    CheckForError(lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))


def RegisterNames():
    """(read-only) Array of strings containing the names of the registers."""
    return CheckForError(get_string_array(lib.Meters_Get_RegisterNames))


def RegisterValues():
    """(read-only) Array of all the values contained in the Meter registers for the active Meter."""
    return get_float64_array(lib.Meters_Get_RegisterValues)


def SAIDI():
    """(read-only) SAIDI for this meter's zone. Execute DoReliabilityCalc first."""
    return CheckForError(lib.Meters_Get_SAIDI())


def SAIFI():
    """(read-only) Returns SAIFI for this meter's Zone. Execute Reliability Calc method first."""
    return CheckForError(lib.Meters_Get_SAIFI())


def SAIFIkW():
    """(read-only) SAIFI based on kW rather than number of customers. Get after reliability calcs."""
    return CheckForError(lib.Meters_Get_SAIFIKW())


def SectSeqidx():
    """(read-only) SequenceIndex of the branch at the head of this section"""
    return CheckForError(lib.Meters_Get_SectSeqIdx())


def SectTotalCust():
    """(read-only) Total Customers downline from this section"""
    return CheckForError(lib.Meters_Get_SectTotalCust())


def SeqListSize():
    """(read-only) Size of Sequence List"""
    return CheckForError(lib.Meters_Get_SeqListSize())


def SequenceList(*args):
    """Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Meters_Get_SequenceIndex())

    # Setter
    Value, = args
    CheckForError(lib.Meters_Set_SequenceIndex(Value))


def SumBranchFltRates():
    """(read-only) Sum of the branch fault rates in this section of the meter's zone"""
    return CheckForError(lib.Meters_Get_SumBranchFltRates())


def TotalCustomers():
    """(read-only) Total Number of customers in this zone (downline from the EnergyMeter)"""
    return CheckForError(lib.Meters_Get_TotalCustomers())


def Totals():
    """(read-only) Totals of all registers of all meters"""
    return get_float64_array(lib.Meters_Get_Totals)


def Idx(*args):
    """
    Get/set active Meter by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Meters_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Meters_Set_idx(Value))


_columns = [
    "AvgRepairTime",
    "CalcCurrent",
    "CountBranches",
    "CountEndElements",
    "CustInterrupts",
    "FaultRateXRepairHrs",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "NumSectionBranches",
    "NumSectionCustomers",
    "NumSections",
    "OCPDeviceType",
    "PeakCurrent",
    "RegisterNames",
    "RegisterValues",
    "SAIDI",
    "SAIFI",
    "SAIFIkW",
    "SectSeqidx",
    "SectTotalCust",
    "SeqListSize",
    "SequenceList",
    "SumBranchFltRates",
    "TotalCustomers",
    "Totals",
    "AllocFactors",
    "AllEndElements",
    "AllBranchesInZone",
]
__all__ = [
    "CloseAllDIFiles",
    "DoReliabilityCalc",
    "OpenAllDIFiles",
    "Reset",
    "ResetAll",
    "Sample",
    "SampleAll",
    "Save",
    "SaveAll",
    "SetActiveSection",
    "AllBranchesInZone",
    "AllEndElements",
    "AllNames",
    "AllocFactors",
    "AvgRepairTime",
    "CalcCurrent",
    "Count",
    "CountBranches",
    "CountEndElements",
    "CustInterrupts",
    "DIFilesAreOpen",
    "FaultRateXRepairHrs",
    "First",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "Next",
    "NumSectionBranches",
    "NumSectionCustomers",
    "NumSections",
    "OCPDeviceType",
    "PeakCurrent",
    "RegisterNames",
    "RegisterValues",
    "SAIDI",
    "SAIFI",
    "SAIFIkW",
    "SectSeqidx",
    "SectTotalCust",
    "SeqListSize",
    "SequenceList",
    "SumBranchFltRates",
    "TotalCustomers",
    "Totals",
    "Idx",
]
