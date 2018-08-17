# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string
from ._utils import codec


def AccumulatedL():
    """(read-only) accummulated failure rate for this branch on downline"""
    return lib.PDElements_Get_AccumulatedL()


def Count():
    """(read-only) Number of PD elements (including disabled elements)"""
    return lib.PDElements_Get_Count()


def FaultRate(*args):
    """Get/Set Number of failures per year. For LINE elements: Number of failures per unit length per year. """
    # Getter
    if len(args) == 0:
        return lib.PDElements_Get_FaultRate()

    # Setter
    Value, = args
    lib.PDElements_Set_FaultRate(Value)


def First():
    """(read-only) Set the first enabled PD element to be the active element.  Returns 0 if none found."""
    return lib.PDElements_Get_First()


def FromTerminal():
    """(read-only) Number of the terminal of active PD element that is on the "from" side. This is set after the meter zone is determined."""
    return lib.PDElements_Get_FromTerminal()


def IsShunt():
    """(read-only) Variant boolean indicating of PD element should be treated as a shunt element rather than a series element. Applies to Capacitor and Reactor elements in particular."""
    return lib.PDElements_Get_IsShunt() != 0


def Lambda():
    """(read-only) Failure rate for this branch. Faults per year including length of line."""
    return lib.PDElements_Get_Lambda()


def Name(*args):
    """Get/Set name of active PD Element. Returns null string if active element is not PDElement type."""
    # Getter
    if len(args) == 0:
        return get_string(lib.PDElements_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.PDElements_Set_Name(Value)


def Next():
    """(read-only) Advance to the next PD element in the circuit. Enabled elements only. Returns 0 when no more elements."""
    return lib.PDElements_Get_Next()


def NumCustomers():
    """(read-only) Number of customers, this branch"""
    return lib.PDElements_Get_Numcustomers()


def ParentPDElement():
    """(read-only) Sets the parent PD element to be the active circuit element.  Returns 0 if no more elements upline."""
    return lib.PDElements_Get_ParentPDElement()


def RepairTime(*args):
    """Average repair time for this element in hours"""
    # Getter
    if len(args) == 0:
        return lib.PDElements_Get_RepairTime()

    # Setter
    Value, = args
    lib.PDElements_Set_RepairTime(Value)


def SectionID():
    """(read-only) Integer ID of the feeder section that this PDElement branch is part of"""
    return lib.PDElements_Get_SectionID()


def TotalMiles():
    """(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm."""
    return lib.PDElements_Get_TotalMiles()


def TotalCustomers():
    """(read-only) Total number of customers from this branch to the end of the zone"""
    return lib.PDElements_Get_Totalcustomers()


def PctPermanent(*args):
    """Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary."""
    # Getter
    if len(args) == 0:
        return lib.PDElements_Get_pctPermanent()

    # Setter
    Value, = args
    lib.PDElements_Set_pctPermanent(Value)


_columns = [
    "AccumulatedL",
    "FaultRate",
    "FromTerminal",
    "IsShunt",
    "Lambda",
    "Name",
    "NumCustomers",
    "ParentPDElement",
    "RepairTime",
    "SectionID",
    "TotalMiles",
    "TotalCustomers",
    "PctPermanent",
]
__all__ = [
    "AccumulatedL",
    "Count",
    "FaultRate",
    "First",
    "FromTerminal",
    "IsShunt",
    "Lambda",
    "Name",
    "Next",
    "NumCustomers",
    "ParentPDElement",
    "RepairTime",
    "SectionID",
    "TotalMiles",
    "TotalCustomers",
    "PctPermanent",
]
