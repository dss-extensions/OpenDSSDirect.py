# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_int32_array,
    prepare_float64_array,
    prepare_int32_array,
)


def AllowDuplicates(*args):
    """{True | False*} Designates whether to allow duplicate names of objects"""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_AllowDuplicates() != 0

    # Setter
    Value, = args
    lib.Settings_Set_AllowDuplicates(Value)
    CheckForError()


def AutoBusList(*args):
    """List of Buses or (File=xxxx) syntax for the AutoAdd solution mode."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Settings_Get_AutoBusList())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.Settings_Set_AutoBusList(Value)
    CheckForError()


def CktModel(*args):
    """{dssMultiphase * | dssPositiveSeq} IIndicate if the circuit model is positive sequence."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_CktModel()

    # Setter
    Value, = args
    lib.Settings_Set_CktModel(Value)
    CheckForError()


def ControlTrace(*args):
    """{True | False*} Denotes whether to trace the control actions to a file."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_ControlTrace() != 0

    # Setter
    Value, = args
    lib.Settings_Set_ControlTrace(Value)
    CheckForError()


def EmergVmaxpu(*args):
    """Per Unit maximum voltage for Emergency conditions."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_EmergVmaxpu()

    # Setter
    Value, = args
    lib.Settings_Set_EmergVmaxpu(Value)
    CheckForError()


def EmergVminpu(*args):
    """Per Unit minimum voltage for Emergency conditions."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_EmergVminpu()

    # Setter
    Value, = args
    lib.Settings_Set_EmergVminpu(Value)
    CheckForError()


def LossRegs(*args):
    """Integer array defining which energy meter registers to use for computing losses"""
    # Getter
    if len(args) == 0:
        return get_int32_array(lib.Settings_Get_LossRegs)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_int32_array(Value)
    lib.Settings_Set_LossRegs(ValuePtr, ValueCount)
    CheckForError()


def LossWeight(*args):
    """Weighting factor applied to Loss register values."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_LossWeight()

    # Setter
    Value, = args
    lib.Settings_Set_LossWeight(Value)
    CheckForError()


def NormVmaxpu(*args):
    """Per Unit maximum voltage for Normal conditions."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_NormVmaxpu()

    # Setter
    Value, = args
    lib.Settings_Set_NormVmaxpu(Value)
    CheckForError()


def NormVminpu(*args):
    """Per Unit minimum voltage for Normal conditions."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_NormVminpu()

    # Setter
    Value, = args
    lib.Settings_Set_NormVminpu(Value)
    CheckForError()


def PriceCurve(*args):
    """Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Settings_Get_PriceCurve())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.Settings_Set_PriceCurve(Value)
    CheckForError()


def PriceSignal(*args):
    """Price Signal for the Circuit"""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_PriceSignal()

    # Setter
    Value, = args
    lib.Settings_Set_PriceSignal(Value)
    CheckForError()


def Trapezoidal(*args):
    """{True | False *} Gets value of trapezoidal integration flag in energy meters."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_Trapezoidal() != 0

    # Setter
    Value, = args
    lib.Settings_Set_Trapezoidal(Value)
    CheckForError()


def UERegs(*args):
    """Array of Integers defining energy meter registers to use for computing UE"""
    # Getter
    if len(args) == 0:
        return get_int32_array(lib.Settings_Get_UEregs)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_int32_array(Value)
    lib.Settings_Set_UEregs(ValuePtr, ValueCount)
    CheckForError()


def UEWeight(*args):
    """Weighting factor applied to UE register values."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_UEweight()

    # Setter
    Value, = args
    lib.Settings_Set_UEweight(Value)
    CheckForError()


def VoltageBases(*args):
    """Array of doubles defining the legal voltage bases in kV L-L"""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.Settings_Get_VoltageBases)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)
    CheckForError()


def ZoneLock(*args):
    """{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs."""
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_ZoneLock() != 0

    # Setter
    Value, = args
    lib.Settings_Set_ZoneLock(Value)
    CheckForError()


def AllocationFactors(Value):
    """(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value."""
    lib.Settings_Set_AllocationFactors(Value)
    CheckForError()


def LoadsTerminalCheck(*args):
    """
    Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
    If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.
    """
    # Getter
    if len(args) == 0:
        return lib.Settings_Get_LoadsTerminalCheck() != 0

    # Setter
    Value, = args
    return lib.Settings_Set_LoadsTerminalCheck(Value)


_columns = [
    "AllowDuplicates",
    "AutoBusList",
    "CktModel",
    "ControlTrace",
    "EmergVmaxpu",
    "EmergVminpu",
    "LossRegs",
    "LossWeight",
    "NormVmaxpu",
    "NormVminpu",
    "PriceCurve",
    "PriceSignal",
    "Trapezoidal",
    "UERegs",
    "UEWeight",
    "VoltageBases",
    "ZoneLock",
]
__all__ = [
    "AllowDuplicates",
    "AutoBusList",
    "CktModel",
    "ControlTrace",
    "EmergVmaxpu",
    "EmergVminpu",
    "LossRegs",
    "LossWeight",
    "NormVmaxpu",
    "NormVminpu",
    "PriceCurve",
    "PriceSignal",
    "Trapezoidal",
    "UERegs",
    "UEWeight",
    "VoltageBases",
    "ZoneLock",
    "AllocationFactors",
    "LoadsTerminalCheck",
]
