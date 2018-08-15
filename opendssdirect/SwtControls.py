# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


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


def AllNames():
    """(read-only) Array of strings with all SwtControl names in the active circuit."""
    return get_string_array(lib.SwtControls_Get_AllNames)


def Count():
    return lib.SwtControls_Get_Count()


def Delay(*args):
    """Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_Delay()

    # Setter
    Value, = args
    lib.SwtControls_Set_Delay(Value)


def First():
    """(read-only) Sets the first SwtControl active. Returns 0 if no more."""
    return lib.SwtControls_Get_First()


def IsLocked(*args):
    """The lock prevents both manual and automatic switch operation."""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_IsLocked() != 0

    # Setter
    Value, = args
    lib.SwtControls_Set_IsLocked(Value)


def Name(*args):
    """Sets a SwtControl active by Name."""
    # Getter
    if len(args) == 0:
        return get_string(lib.SwtControls_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.SwtControls_Set_Name(Value)


def Next():
    """(read-only) Sets the next SwtControl active. Returns 0 if no more."""
    return lib.SwtControls_Get_Next()


def NormalState(*args):
    """
    (read) Get Normal state of switch
    (write) set Normal state of switch  (see actioncodes) dssActionOpen or dssActionClose
    """
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_NormalState()

    # Setter
    Value, = args
    lib.SwtControls_Set_NormalState(Value)


def State(*args):
    """
    (read) Force switch to specified state
    (write) Get Present state of switch
    """
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_State()

    # Setter
    Value, = args
    lib.SwtControls_Set_State(Value)


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


def SwitchedTerm(*args):
    """Terminal number where the switch is located on the SwitchedObj"""
    # Getter
    if len(args) == 0:
        return lib.SwtControls_Get_SwitchedTerm()

    # Setter
    Value, = args
    lib.SwtControls_Set_SwitchedTerm(Value)


_columns = [
    "Action",
    "Delay",
    "IsLocked",
    "Name",
    "NormalState",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
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
]
