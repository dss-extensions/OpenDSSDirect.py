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
    """(read-only) List of strings with all Load names"""
    return CheckForError(get_string_array(lib.Loads_Get_AllNames))


def AllocationFactor(*args):
    """Factor for allocating loads by connected xfkva"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_AllocationFactor())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_AllocationFactor(Value))


def CVRCurve(*args):
    """Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_CVRcurve()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_CVRcurve(Value))


def CVRvars(*args):
    """Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_CVRvars())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_CVRvars(Value))


def CVRwatts(*args):
    """Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_CVRwatts())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_CVRwatts(Value))


def CFactor(*args):
    """Factor relates average to peak kw.  Used for allocation with kwh and kwhdays"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Cfactor())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Cfactor(Value))


def Class(*args):
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Class_())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Class_(Value))


def Count():
    """(read-only) Number of Loads"""
    return CheckForError(lib.Loads_Get_Count())


def First():
    """Set first Load active; returns 0 if none."""
    return CheckForError(lib.Loads_Get_First())


def Growth(*args):
    """Name of the growthshape curve for yearly load growth factors."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_Growth()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_Growth(Value))


def IsDelta(*args):
    """Delta loads are connected line-to-line."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_IsDelta()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_IsDelta(Value))


def Model(*args):
    """The Load Model defines variation of P and Q with voltage."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Model())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Model(Value))


def Name(*args):
    """
    Get/set the name of the active Load
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Loads_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_Name(Value))


def Next():
    """Sets next Load active; returns 0 if no more."""
    return CheckForError(lib.Loads_Get_Next())


def NumCust(*args):
    """Number of customers in this load, defaults to one."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_NumCust())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_NumCust(Value))


def PF(*args):
    """Get or set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_PF())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_PF(Value))


def PctMean(*args):
    """Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_PctMean())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_PctMean(Value))


def PctStdDev(*args):
    """Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_PctStdDev())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_PctStdDev(Value))


def RelWeighting(*args):
    """Relative Weighting factor for the active LOAD"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_RelWeight())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_RelWeight(Value))


def Rneut(*args):
    """Neutral resistance for wye-connected loads."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Rneut())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Rneut(Value))


def Spectrum(*args):
    """Name of harmonic current spectrrum shape."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_Spectrum()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_Spectrum(Value))


def Status(*args):
    """Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all)."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Status())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Status(Value))


def Vmaxpu(*args):
    """Maximum per-unit voltage to use the load model. Above this, constant Z applies."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Vmaxpu())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Vmaxpu(Value))


def VminEmerg(*args):
    """Minimum voltage for unserved energy (UE) evaluation."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Vminemerg())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Vminemerg(Value))


def VminNorm(*args):
    """Minimum voltage for energy exceeding normal (EEN) evaluations."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Vminnorm())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Vminnorm(Value))


def Vminpu(*args):
    """Minimum voltage to apply the load model. Below this, constant Z is used."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Vminpu())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Vminpu(Value))


def Xneut(*args):
    """Neutral reactance for wye-connected loads."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Xneut())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Xneut(Value))


def Yearly(*args):
    """Name of yearly duration loadshape"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_Yearly()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_Yearly(Value))


def ZipV(*args):
    """Array of 7 doubles with values for ZIPV property of the load object"""
    # Getter
    if len(args) == 0:
        result = get_float64_array(lib.Loads_Get_ZIPV)
        if result == [0]:
            return []

        return result

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Loads_Set_ZIPV(ValuePtr, ValueCount)
    CheckForError()


def Daily(*args):
    """Name of the loadshape for a daily load profile."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_daily()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_daily(Value))


def Duty(*args):
    """Name of the loadshape for a duty cycle simulation."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Loads_Get_duty()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Loads_Set_duty(Value))


def Idx(*args):
    """
    Get/set active Load by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_idx(Value))


def kV(*args):
    """Set kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kV())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kV(Value))


def kW(*args):
    """Set kW for active Load. Updates kvar based on present PF."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kW())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kW(Value))


def kVABase(*args):
    """Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kva())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kva(Value))


def kvar(*args):
    """Get/set kvar for active Load. If set, updates PF based on present kW."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kvar())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kvar(Value))


def kWh(*args):
    """kwh billed for this period. Can be used with Cfactor for load allocation."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kwh())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kwh(Value))


def kWhDays(*args):
    """Length of kwh billing period for average demand calculation. Default 30."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_kwhdays())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_kwhdays(Value))


def puSeriesRL(*args):
    """Percent of Load that is modeled as series R-L for harmonics studies"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_pctSeriesRL())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_pctSeriesRL(Value))


def XfkVA(*args):
    """Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_xfkVA())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_xfkVA(Value))


def Phases(*args):
    """Number of phases"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Loads_Get_Phases())

    # Setter
    Value, = args
    CheckForError(lib.Loads_Set_Phases(Value))


_columns = [
    "CVRCurve",
    "CVRvars",
    "CVRwatts",
    "CFactor",
    "Class",
    "Growth",
    "IsDelta",
    "Model",
    "Name",
    "NumCust",
    "PF",
    "PctMean",
    "PctStdDev",
    "RelWeighting",
    "Rneut",
    "Spectrum",
    "Status",
    "Vmaxpu",
    "VminEmerg",
    "VminNorm",
    "Vminpu",
    "Xneut",
    "Yearly",
    "ZipV",
    "Daily",
    "Duty",
    "Idx",
    "kV",
    "kW",
    "kVABase",
    "kvar",
    "kWh",
    "kWhDays",
    "puSeriesRL",
    "XfkVA",
    "Phases",
    "AllocationFactor",
]
__all__ = [
    "AllNames",
    "AllocationFactor",
    "CVRCurve",
    "CVRvars",
    "CVRwatts",
    "CFactor",
    "Class",
    "Count",
    "First",
    "Growth",
    "IsDelta",
    "Model",
    "Name",
    "Next",
    "NumCust",
    "PF",
    "PctMean",
    "PctStdDev",
    "RelWeighting",
    "Rneut",
    "Spectrum",
    "Status",
    "Vmaxpu",
    "VminEmerg",
    "VminNorm",
    "Vminpu",
    "Xneut",
    "Yearly",
    "ZipV",
    "Daily",
    "Duty",
    "Idx",
    "kV",
    "kW",
    "kVABase",
    "kvar",
    "kWh",
    "kWhDays",
    "puSeriesRL",
    "XfkVA",
    "Phases",
]
