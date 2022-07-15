from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_float64_array,
    get_string_array,
)


def AllNames():
    """(read-only) List of strings with all Storage names"""
    return CheckForError(get_string_array(lib.Storages_Get_AllNames))


def Count():
    """(read-only) Number of Storages"""
    return CheckForError(lib.Storages_Get_Count())


def Idx(*args):
    """
    Get/set active Storage by index;  1..Count
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Storages_Get_idx())

    # Setter
    Value, = args
    CheckForError(lib.Storages_Set_idx(Value))


def First():
    """Set first Storage active; returns 0 if none."""
    return CheckForError(lib.Storages_Get_First())


def Next():
    """Sets next Storage active; returns 0 if no more."""
    return CheckForError(lib.Storages_Get_Next())


def Name(*args):
    """
    Get/set the name of the active Storage
    """
    # Getter
    if len(args) == 0:
        return CheckForError(get_string(lib.Storages_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    CheckForError(lib.Storages_Set_Name(Value))


def puSOC(*args):
    """Per unit state of charge"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Storages_Get_puSOC())

    # Setter
    Value, = args
    CheckForError(lib.Storages_Set_puSOC(Value))


def State(*args):
    """
    Get/set state: 0=Idling; 1=Discharging; -1=Charging;

    Related enumeration: StorageStates
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Storages_Get_State())

    # Setter
    Value, = args
    CheckForError(lib.Storages_Set_State(Value))


def RegisterNames():
    """Array of Names of all Storage energy meter registers"""
    return CheckForError(get_string_array(lib.Storages_Get_RegisterNames))


def RegisterValues():
    """Array of values in Storage registers."""
    return get_float64_array(lib.Storages_Get_RegisterValues)


_columns = ["Name", "Idx", "RegisterNames", "RegisterValues", "puSOC", "State"]
__all__ = [
    "puSOC",
    "State",
    "RegisterNames",
    "RegisterValues",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
