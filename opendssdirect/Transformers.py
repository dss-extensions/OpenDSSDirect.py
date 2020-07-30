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


def AllNames():
    """(read-only) List of strings with all Transformer names"""
    return CheckForError(get_string_array(lib.Transformers_Get_AllNames))


def Count():
    """(read-only) Number of Transformers"""
    return CheckForError(lib.Transformers_Get_Count())


def First():
    """Set first Transformer active; returns 0 if none."""
    return CheckForError(lib.Transformers_Get_First())


def IsDelta(*args):
    """Active Winding delta or wye connection?"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_IsDelta()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_IsDelta(Value))


def MaxTap(*args):
    """Active Winding maximum tap in per-unit."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_MaxTap())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_MaxTap(Value))


def MinTap(*args):
    """Active Winding minimum tap in per-unit."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_MinTap())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_MinTap(Value))


def Name(*args):
    """
    Get/set the name of the active Transformer
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Transformers_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Transformers_Set_Name(Value))


def Next():
    """Sets next Transformer active; returns 0 if no more."""
    return CheckForError(lib.Transformers_Get_Next())


def NumTaps(*args):
    """Active Winding number of tap steps betwein MinTap and MaxTap."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_NumTaps())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_NumTaps(Value))


def NumWindings(*args):
    """Number of windings on this transformer. Allocates memory; set or change this property first."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_NumWindings())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_NumWindings(Value))


def R(*args):
    """Active Winding resistance in %"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_R())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_R(Value))


def Rneut(*args):
    """Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Rneut())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Rneut(Value))


def Tap(*args):
    """Active Winding tap in per-unit."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Tap())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Tap(Value))


def Wdg(*args):
    """Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Wdg())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Wdg(Value))


def XfmrCode(*args):
    """Name of an XfrmCode that supplies electircal parameters for this Transformer."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Transformers_Get_XfmrCode()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Transformers_Set_XfmrCode(Value))


def Xhl(*args):
    """Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Xhl())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Xhl(Value))


def Xht(*args):
    """Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Xht())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Xht(Value))


def Xlt(*args):
    """Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Xlt())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Xlt(Value))


def Xneut(*args):
    """Active Winding neutral reactance [ohms] for wye connections."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_Xneut())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_Xneut(Value))


def kV(*args):
    """Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_kV())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_kV(Value))


def kVA(*args):
    """Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_kVA())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_kVA(Value))


def Idx(*args):
    """
    Get/set active Transformer by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_idx(Value))


def WdgVoltages():
    """(read-only) Complex array of voltages for active winding"""
    return get_float64_array(lib.Transformers_Get_WdgVoltages)


def WdgCurrents():
    """(read-only) All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)"""
    return get_float64_array(lib.Transformers_Get_WdgCurrents)


def strWdgCurrents():
    """(read-only) All winding currents in CSV string form like the WdgCurrents property"""
    return get_string(CheckForError(lib.Transformers_Get_strWdgCurrents()))


def CoreType(*args):
    """Transformer Core Type: 0=shell;1 = 1-phase; 3= 3-leg; 5= 5-leg"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_CoreType())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_CoreType(Value))


def RdcOhms(*args):
    """dc Resistance of active winding in ohms for GIC analysis"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Transformers_Get_RdcOhms())

    # Setter
    Value, = args
    CheckForError(lib.Transformers_Set_RdcOhms(Value))


def LossesByType():
    """Complex array with the losses by type (total losses, load losses, no-load losses), in VA"""
    return get_float64_array(lib.Transformers_Get_LossesByType)


def AllLossesByType():
    """Complex array with the losses by type (total losses, load losses, no-load losses), in VA, concatenated for ALL transformers"""
    return get_float64_array(lib.Transformers_Get_AllLossesByType)


_columns = [
    "IsDelta",
    "MaxTap",
    "MinTap",
    "Name",
    "NumTaps",
    "NumWindings",
    "R",
    "Rneut",
    "Tap",
    "Wdg",
    "XfmrCode",
    "Xhl",
    "Xht",
    "Xlt",
    "Xneut",
    "kV",
    "kVA",
    "Idx",
    "CoreType",
    "RdcOhms",
    "WdgCurrents",
    "WdgVoltages",
    "LossesByType",
]
__all__ = [
    "AllNames",
    "Count",
    "First",
    "IsDelta",
    "MaxTap",
    "MinTap",
    "Name",
    "Next",
    "NumTaps",
    "NumWindings",
    "R",
    "Rneut",
    "Tap",
    "Wdg",
    "XfmrCode",
    "Xhl",
    "Xht",
    "Xlt",
    "Xneut",
    "kV",
    "kVA",
    "WdgVoltages",
    "WdgCurrents",
    "strWdgCurrents",
    "CoreType",
    "RdcOhms",
    "LossesByType",
    "AllLossesByType",
    "Idx",
]
