# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def Reset():
    lib.SwtControls_Reset()


def Action(*args):
    """Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state)."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_Action()

    # Setter
    Value, = args
    lib.SwtControls_Set_Action(Value)
    CheckForError()


def AllNames():
    """(read-only) List of strings with all SwtControl names"""
    return get_string_array(lib.SwtControls_Get_AllNames)


def Count():
    """(read-only) Number of SwtControls"""
    return lib.SwtControls_Get_Count()


def Delay(*args):
    """Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_Delay()

    # Setter
    Value, = args
    lib.SwtControls_Set_Delay(Value)
    CheckForError()


def First():
    """Set first SwtControl active; returns 0 if none."""
    return lib.SwtControls_Get_First()


def IsLocked(*args):
    """The lock prevents both manual and automatic switch operation."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_IsLocked() != 0

    # Setter
    Value, = args
    lib.SwtControls_Set_IsLocked(Value)
    CheckForError()


def Name(*args):
    """
    Get/set the name of the active SwtControl
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.SwtControls_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.SwtControls_Set_Name(Value))


def Next():
    """Sets next SwtControl active; returns 0 if no more."""
    return lib.SwtControls_Get_Next()


def NormalState(*args):
    """
    Get/set Normal state of switch (see actioncodes) dssActionOpen or dssActionClose
    """
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_NormalState()

    # Setter
    Value, = args
    lib.SwtControls_Set_NormalState(Value)
    CheckForError()


def State(*args):
    """Set it to force the switch to a specified state, otherwise read its present state."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_State()

    # Setter
    Value, = args
    lib.SwtControls_Set_State(Value)
    CheckForError()


def SwitchedObj(*args):
    """Full name of the switched element."""
    # Getter
    if len(args) == 0:
        return get_string(lib.SwtControls_Get_SwitchedObj())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.SwtControls_Set_SwitchedObj(Value)
    CheckForError()


def SwitchedTerm(*args):
    """Terminal number where the switch is located on the SwitchedObj"""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_SwitchedTerm()

    # Setter
    Value, = args
    lib.SwtControls_Set_SwitchedTerm(Value)
    CheckForError()


def Idx(*args):
    """
    Get/set active SwtControl by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_idx()

    # Setter
    Value, = args
    CheckForError(lib.SwtControls_Set_idx(Value))


_columns = [
    "Action",
    "Delay",
    "IsLocked",
    "Name",
    "NormalState",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
__all__ = [
    "Reset",
    "Action",
    "AllNames",
    "Count",
    "Delay",
    "First",
    "IsLocked",
    "Name",
    "Next",
    "NormalState",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
