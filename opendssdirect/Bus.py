# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    CheckForError,
    get_string,
    get_float64_array,
    get_int32_array,
    get_string_array,
)


def GetUniqueNodeNumber(StartNumber):
    return CheckForError(lib.Bus_GetUniqueNodeNumber(StartNumber))


def ZscRefresh():
    return CheckForError(lib.Bus_ZscRefresh()) != 0


def Coorddefined():
    """(read-only) False=0 else True. Indicates whether a coordinate has been defined for this bus"""
    return CheckForError(lib.Bus_Get_Coorddefined()) != 0


def CplxSeqVoltages():
    """(read-only) Complex Double array of Sequence Voltages (0, 1, 2) at this Bus."""
    return get_float64_array(lib.Bus_Get_CplxSeqVoltages)


def Cust_Duration():
    """(read-only) Accumulated customer outage durations"""
    return CheckForError(lib.Bus_Get_Cust_Duration())


def Cust_Interrupts():
    """(read-only) Annual number of customer-interruptions from this bus"""
    return CheckForError(lib.Bus_Get_Cust_Interrupts())


def Distance():
    """(read-only) Distance from energymeter (if non-zero)"""
    return CheckForError(lib.Bus_Get_Distance())


def Int_Duration():
    """(read-only) Average interruption duration, hr."""
    return CheckForError(lib.Bus_Get_Int_Duration())


def Isc():
    """(read-only) Short circuit currents at bus; Complex Array."""
    return get_float64_array(lib.Bus_Get_Isc)


def Lambda():
    """(read-only) Accumulated failure rate downstream from this bus; faults per year"""
    return CheckForError(lib.Bus_Get_Lambda())


def N_Customers():
    """(read-only) Total numbers of customers served downline from this bus"""
    return CheckForError(lib.Bus_Get_N_Customers())


def N_interrupts():
    """(read-only) Number of interruptions this bus per year"""
    return CheckForError(lib.Bus_Get_N_interrupts())


def Name():
    """(read-only) Name of Bus"""
    return get_string(CheckForError(lib.Bus_Get_Name()))


def Nodes():
    """(read-only) Integer Array of Node Numbers defined at the bus in same order as the voltages."""
    return get_int32_array(lib.Bus_Get_Nodes)


def NumNodes():
    """(read-only) Number of Nodes this bus."""
    return CheckForError(lib.Bus_Get_NumNodes())


def SectionID():
    """(read-only) Integer ID of the feeder section in which this bus is located."""
    return CheckForError(lib.Bus_Get_SectionID())


def SeqVoltages():
    """(read-only) Double Array of sequence voltages at this bus."""
    return get_float64_array(lib.Bus_Get_SeqVoltages)


def TotalMiles():
    """(read-only) Total length of line downline from this bus, in miles. For recloser siting algorithm."""
    return CheckForError(lib.Bus_Get_TotalMiles())


def VLL():
    """(read-only) For 2- and 3-phase buses, returns array of complex numbers represetin L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3."""
    return get_float64_array(lib.Bus_Get_VLL)


def VMagAngle():
    """(read-only) Array of doubles containing voltages in Magnitude (VLN), angle (deg)"""
    return get_float64_array(lib.Bus_Get_VMagAngle)


def Voc():
    """(read-only) Open circuit voltage; Complex array."""
    return get_float64_array(lib.Bus_Get_Voc)


def Voltages():
    """(read-only) Complex array of voltages at this bus."""
    return get_float64_array(lib.Bus_Get_Voltages)


def YscMatrix():
    """(read-only) Complex array of Ysc matrix at bus. Column by column."""
    return get_float64_array(lib.Bus_Get_YscMatrix)


def Zsc0():
    """(read-only) Complex Zero-Sequence short circuit impedance at bus."""
    return get_float64_array(lib.Bus_Get_Zsc0)


def Zsc1():
    """(read-only) Complex Positive-Sequence short circuit impedance at bus.."""
    return get_float64_array(lib.Bus_Get_Zsc1)


def ZscMatrix():
    """(read-only) Complex array of Zsc matrix at bus. Column by column."""
    return get_float64_array(lib.Bus_Get_ZscMatrix)


def kVBase():
    """(read-only) Base voltage at bus in kV"""
    return CheckForError(lib.Bus_Get_kVBase())


def puVLL():
    """(read-only) Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases."""
    return get_float64_array(lib.Bus_Get_puVLL)


def puVmagAngle():
    """(read-only) Array of doubles containig voltage magnitude, angle pairs in per unit"""
    return get_float64_array(lib.Bus_Get_puVmagAngle)


def PuVoltage():
    """(read-only) Complex Array of pu voltages at the bus."""
    return get_float64_array(lib.Bus_Get_puVoltages)


def X(*args):
    """X Coordinate for bus (double)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Bus_Get_x())

    # Setter
    Value, = args
    CheckForError(lib.Bus_Set_x(Value))


def Y(*args):
    """Y coordinate for bus(double)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Bus_Get_y())

    # Setter
    Value, = args
    CheckForError(lib.Bus_Set_y(Value))


def LoadList():
    """List of strings: Full Names of LOAD elements connected to the active bus."""
    return CheckForError(get_string_array(lib.Bus_Get_LoadList))


def LineList():
    """List of strings: Full Names of LINE elements connected to the active bus."""
    return CheckForError(get_string_array(lib.Bus_Get_LineList))


_columns = [
    "Coorddefined",
    "CplxSeqVoltages",
    "Cust_Duration",
    "Cust_Interrupts",
    "Distance",
    "Int_Duration",
    "Isc",
    "Lambda",
    "N_Customers",
    "N_interrupts",
    "Name",
    "Nodes",
    "NumNodes",
    "SectionID",
    "SeqVoltages",
    "TotalMiles",
    "VLL",
    "VMagAngle",
    "Voc",
    "Voltages",
    "YscMatrix",
    "Zsc0",
    "Zsc1",
    "ZscMatrix",
    "kVBase",
    "puVLL",
    "puVmagAngle",
    "PuVoltage",
    "X",
    "Y",
]
__all__ = [
    "GetUniqueNodeNumber",
    "ZscRefresh",
    "Coorddefined",
    "CplxSeqVoltages",
    "Cust_Duration",
    "Cust_Interrupts",
    "Distance",
    "Int_Duration",
    "Isc",
    "Lambda",
    "N_Customers",
    "N_interrupts",
    "Name",
    "Nodes",
    "NumNodes",
    "SectionID",
    "SeqVoltages",
    "TotalMiles",
    "VLL",
    "VMagAngle",
    "Voc",
    "Voltages",
    "YscMatrix",
    "Zsc0",
    "Zsc1",
    "ZscMatrix",
    "kVBase",
    "puVLL",
    "puVmagAngle",
    "PuVoltage",
    "X",
    "Y",
    "LoadList",
    "LineList",
]
