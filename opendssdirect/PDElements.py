# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_int32_array,
    get_string_array,
)


def AccumulatedL():
    """(read-only) accummulated failure rate for this branch on downline"""
    return CheckForError(lib.PDElements_Get_AccumulatedL())


def Count():
    """(read-only) Number of PD elements (including disabled elements)"""
    return CheckForError(lib.PDElements_Get_Count())


def FaultRate(*args):
    """
    Get/Set Number of failures per year. 
    For LINE elements: Number of failures per unit length per year.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PDElements_Get_FaultRate())

    # Setter
    Value, = args
    CheckForError(lib.PDElements_Set_FaultRate(Value))


def First():
    """
    (read-only) Set the first enabled PD element to be the active element.
    Returns 0 if none found.
    """
    return CheckForError(lib.PDElements_Get_First())


def FromTerminal():
    """
    (read-only) Number of the terminal of active PD element that is on the "from" 
    side. This is set after the meter zone is determined.
    """
    return CheckForError(lib.PDElements_Get_FromTerminal())


def IsShunt():
    """
    (read-only) Boolean indicating of PD element should be treated as a shunt 
    element rather than a series element. Applies to Capacitor and Reactor 
    elements in particular.
    """
    return CheckForError(lib.PDElements_Get_IsShunt()) != 0


def Lambda():
    """(read-only) Failure rate for this branch. Faults per year including length of line."""
    return CheckForError(lib.PDElements_Get_Lambda())


def Name(*args):
    """
    Get/Set name of active PD Element. Returns null string if active element 
    is not PDElement type.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.PDElements_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.PDElements_Set_Name(Value))


def Next():
    """
    (read-only) Advance to the next PD element in the circuit. Enabled elements 
    only. Returns 0 when no more elements.
    """
    return CheckForError(lib.PDElements_Get_Next())


def NumCustomers():
    """(read-only) Number of customers, this branch"""
    return CheckForError(lib.PDElements_Get_Numcustomers())


def ParentPDElement():
    """
    (read-only) Sets the parent PD element to be the active circuit element.
    Returns 0 if no more elements upline.
    """
    return CheckForError(lib.PDElements_Get_ParentPDElement())


def RepairTime(*args):
    """Average repair time for this element in hours"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PDElements_Get_RepairTime())

    # Setter
    Value, = args
    CheckForError(lib.PDElements_Set_RepairTime(Value))


def SectionID():
    """(read-only) Integer ID of the feeder section that this PDElement branch is part of"""
    return CheckForError(lib.PDElements_Get_SectionID())


def TotalMiles():
    """(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm."""
    return CheckForError(lib.PDElements_Get_TotalMiles())


def TotalCustomers():
    """(read-only) Total number of customers from this branch to the end of the zone"""
    return CheckForError(lib.PDElements_Get_Totalcustomers())


def PctPermanent(*args):
    """Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.PDElements_Get_pctPermanent())

    # Setter
    Value, = args
    CheckForError(lib.PDElements_Set_pctPermanent(Value))


def AllNames():
    """
    Array of strings consisting of all PD element names.

    (API Extension)
    """
    return CheckForError(get_string_array(lib.PDElements_Get_AllNames))


def AllMaxCurrents(AllNodes=False):
    """
    Array of doubles with the maximum current across the conductors, for each PD 
    element.

    By default, only the *first terminal* is used for the maximum current, matching
    the behavior of the "export capacity" command. Pass `AllNodes=True` to 
    force the analysis to all terminals.

    See also: 
    https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

    (API Extension)
    """
    return CheckForError(
        get_float64_array(lib.PDElements_Get_AllMaxCurrents, AllNodes)
    )


def AllPctNorm(AllNodes=False):
    """
    Array of doubles with the maximum current across the conductors as a percentage 
    of the Normal Ampere Rating, for each PD element.

    By default, only the *first terminal* is used for the maximum current, matching
    the behavior of the "export capacity" command. Pass `AllNodes=True` to 
    force the analysis to all terminals.

    See also: 
    https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

    (API Extension)
    """
    return CheckForError(get_float64_array(lib.PDElements_Get_AllPctNorm, AllNodes))


def AllPctEmerg(AllNodes=False):
    """
    Array of doubles with the maximum current across the conductors as a percentage
    of the Emergency Ampere Rating, for each PD element.

    By default, only the *first terminal* is used for the maximum current, matching
    the behavior of the "export capacity" command. Pass `AllNodes=True` to 
    force the analysis to all terminals.

    See also: 
    https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

    (API Extension)
    """
    return CheckForError(
        get_float64_array(lib.PDElements_Get_AllPctEmerg, AllNodes)
    )


def AllCurrents():
    """
    Complex array of currents for all conductors, all terminals, for each PD element.

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllCurrents)


def AllCurrentsMagAng():
    """
    Complex array (magnitude and angle format) of currents for all conductors, all terminals, for each PD element.

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllCurrentsMagAng)


def AllCplxSeqCurrents():
    """
    Complex double array of Sequence Currents for all conductors of all terminals, for each PD elements.

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllCplxSeqCurrents)


def AllSeqCurrents():
    """
    Double array of the symmetrical component currents into each 3-phase terminal, for each PD element.

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllSeqCurrents)


def AllPowers():
    """
    Complex array of powers into each conductor of each terminal, for each PD element.

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllPowers)


def AllSeqPowers():
    """
    Double array of sequence powers into each 3-phase teminal, for each PD element

    (API Extension)
    """
    return get_float64_array(lib.PDElements_Get_AllSeqPowers)


def AllNumPhases():
    """
    Integer array listing the number of phases of all PD elements

    (API Extension)
    """
    return get_int32_array(lib.PDElements_Get_AllNumPhases)


def AllNumConductors():
    """
    Integer array listing the number of conductors of all PD elements

    (API Extension)
    """
    return get_int32_array(lib.PDElements_Get_AllNumConductors)


def AllNumTerminals():
    """
    Integer array listing the number of terminals of all PD elements

    (API Extension)
    """
    return get_int32_array(lib.PDElements_Get_AllNumTerminals)


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
    "AllNames",
    "AllMaxCurrents",
    "AllPctNorm",
    "AllPctEmerg",
    "AllCurrents",
    "AllCurrentsMagAng",
    "AllCplxSeqCurrents",
    "AllSeqCurrents",
    "AllPowers",
    "AllSeqPowers",
    "AllNumPhases",
    "AllNumConductors",
    "AllNumTerminals",
]
