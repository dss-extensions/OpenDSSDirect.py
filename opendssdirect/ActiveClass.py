from ._utils import lib, codec, CheckForError, get_string, get_string_array


def ActiveClassName():
    """(read-only) Returns name of active class."""
    return get_string(CheckForError(lib.ActiveClass_Get_ActiveClassName()))


def AllNames():
    """(read-only) Array of strings consisting of all element names in the active class."""
    return CheckForError(get_string_array(lib.ActiveClass_Get_AllNames))


def Count():
    """(read-only) Number of elements in Active Class. Same as NumElements Property."""
    return CheckForError(lib.ActiveClass_Get_Count())


def First():
    """(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none."""
    return CheckForError(lib.ActiveClass_Get_First())


def Name(*args):
    """Name of the Active Element of the Active Class"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.ActiveClass_Get_Name()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.ActiveClass_Set_Name(Value))


def Next():
    """(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more."""
    return CheckForError(lib.ActiveClass_Get_Next())


def NumElements():
    """(read-only) Number of elements in this class. Same as Count property."""
    return CheckForError(lib.ActiveClass_Get_NumElements())


def ActiveClassParent():
    """Get the name of the parent class of the active class"""
    return get_string(CheckForError(lib.ActiveClass_Get_ActiveClassParent()))


def ToJSON(options=0):
    """
    Returns the data (as a list) of all elements from the active class as a JSON-encoded string.

    The `options` parameter contains bit-flags to toggle specific features.
    See `Obj_ToJSON` (C-API) for more.

    Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.

    (API Extension)
    """
    return get_string(CheckForError(lib.ActiveClass_ToJSON(options)))


_columns = ["ActiveClassName", "Name", "NumElements", "ActiveClassParent"]
__all__ = [
    "ActiveClassName",
    "AllNames",
    "Count",
    "First",
    "Name",
    "Next",
    "NumElements",
    "ActiveClassParent",
    "ToJSON",
]
