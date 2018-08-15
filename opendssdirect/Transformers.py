# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def AllNames():
    """(read-only) Array of strings with all Transformer names in the active circuit."""
    return get_string_array(lib.Transformers_Get_AllNames)


def Count():
    return lib.Transformers_Get_Count()


def First():
    """(read-only) Sets the first Transformer active. Returns 0 if no more."""
    return lib.Transformers_Get_First()


def IsDelta(*args):
    """Active Winding delta or wye connection?"""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_IsDelta() != 0

    # Setter
    Value, = args
    lib.Transformers_Set_IsDelta(Value)


def MaxTap(*args):
    """Active Winding maximum tap in per-unit."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_MaxTap()

    # Setter
    Value, = args
    lib.Transformers_Set_MaxTap(Value)


def MinTap(*args):
    """Active Winding minimum tap in per-unit."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_MinTap()

    # Setter
    Value, = args
    lib.Transformers_Set_MinTap(Value)


def Name(*args):
    """Sets a Transformer active by Name."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Transformers_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Transformers_Set_Name(Value)


def Next():
    """(read-only) Sets the next Transformer active. Returns 0 if no more."""
    return lib.Transformers_Get_Next()


def NumTaps(*args):
    """Active Winding number of tap steps betwein MinTap and MaxTap."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_NumTaps()

    # Setter
    Value, = args
    lib.Transformers_Set_NumTaps(Value)


def NumWindings(*args):
    """Number of windings on this transformer. Allocates memory; set or change this property first."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_NumWindings()

    # Setter
    Value, = args
    lib.Transformers_Set_NumWindings(Value)


def R(*args):
    """Active Winding resistance in %"""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_R()

    # Setter
    Value, = args
    lib.Transformers_Set_R(Value)


def Rneut(*args):
    """Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Rneut()

    # Setter
    Value, = args
    lib.Transformers_Set_Rneut(Value)


def Tap(*args):
    """Active Winding tap in per-unit."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Tap()

    # Setter
    Value, = args
    lib.Transformers_Set_Tap(Value)


def Wdg(*args):
    """Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)"""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Wdg()

    # Setter
    Value, = args
    lib.Transformers_Set_Wdg(Value)


def XfmrCode(*args):
    """Name of an XfrmCode that supplies electircal parameters for this Transformer."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Transformers_Get_XfmrCode())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Transformers_Set_XfmrCode(Value)


def Xhl(*args):
    """Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Xhl()

    # Setter
    Value, = args
    lib.Transformers_Set_Xhl(Value)


def Xht(*args):
    """Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Xht()

    # Setter
    Value, = args
    lib.Transformers_Set_Xht(Value)


def Xlt(*args):
    """Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Xlt()

    # Setter
    Value, = args
    lib.Transformers_Set_Xlt(Value)


def Xneut(*args):
    """Active Winding neutral reactance [ohms] for wye connections."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_Xneut()

    # Setter
    Value, = args
    lib.Transformers_Set_Xneut(Value)


def kV(*args):
    """Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_kV()

    # Setter
    Value, = args
    lib.Transformers_Set_kV(Value)


def kVA(*args):
    """Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings."""
    # Getter
    if len(args) == 0:
        return lib.Transformers_Get_kVA()

    # Setter
    Value, = args
    lib.Transformers_Set_kVA(Value)


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
]
