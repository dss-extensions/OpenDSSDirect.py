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
    """(read-only) List of strings with all Generator names"""
    return CheckForError(get_string_array(lib.Generators_Get_AllNames))


def Count():
    """(read-only) Number of Generators"""
    return CheckForError(lib.Generators_Get_Count())


def First():
    """Set first Generator active; returns 0 if none."""
    return CheckForError(lib.Generators_Get_First())


def ForcedON(*args):
    """Indicates whether the generator is forced ON regardles of other dispatch criteria."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_ForcedON()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_ForcedON(Value))


def Model(*args):
    """Generator Model"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_Model())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_Model(Value))


def Name(*args):
    """
    Get/set the name of the active Generator
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Generators_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Generators_Set_Name(Value))


def Next():
    """Sets next Generator active; returns 0 if no more."""
    return CheckForError(lib.Generators_Get_Next())


def PF(*args):
    """Power factor (pos. = producing vars). Updates kvar based on present kW value."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_PF())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_PF(Value))


def Phases(*args):
    """Number of phases"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_Phases())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_Phases(Value))


def RegisterNames():
    """(read-only) Array of Names of all generator energy meter registers"""
    return CheckForError(get_string_array(lib.Generators_Get_RegisterNames))


def RegisterValues():
    """(read-only) Array of valus in generator energy meter registers."""
    return get_float64_array(lib.Generators_Get_RegisterValues)


def Vmaxpu(*args):
    """Vmaxpu for generator model"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_Vmaxpu())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_Vmaxpu(Value))


def Vminpu(*args):
    """Vminpu for Generator model"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_Vminpu())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_Vminpu(Value))


def Idx(*args):
    """
    Get/set active Generator by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_idx(Value))


def kV(*args):
    """Voltage base for the active generator, kV"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_kV())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_kV(Value))


def kVARated(*args):
    """kVA rating of the generator"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_kVArated())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_kVArated(Value))


def kW(*args):
    """kW output for the active generator. kvar is updated for current power factor."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_kW())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_kW(Value))


def kvar(*args):
    """kvar output for the active generator. Updates power factor based on present kW value."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Generators_Get_kvar())

    # Setter
    Value, = args
    CheckForError(lib.Generators_Set_kvar(Value))


_columns = [
    "ForcedON",
    "Model",
    "Name",
    "PF",
    "Phases",
    "RegisterNames",
    "RegisterValues",
    "Vmaxpu",
    "Vminpu",
    "Idx",
    "kV",
    "kVARated",
    "kW",
    "kvar",
]
__all__ = [
    "AllNames",
    "Count",
    "First",
    "ForcedON",
    "Model",
    "Name",
    "Next",
    "PF",
    "Phases",
    "RegisterNames",
    "RegisterValues",
    "Vmaxpu",
    "Vminpu",
    "Idx",
    "kV",
    "kVARated",
    "kW",
    "kvar",
]
