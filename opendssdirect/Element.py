from ._utils import lib, CheckForError, get_string, get_string_array


def AllPropertyNames():
    """(read-only) Array of strings containing the names of all properties for the active DSS object."""
    return CheckForError(get_string_array(lib.DSSElement_Get_AllPropertyNames))


def Name():
    """(read-only) Full Name of Active DSS Object (general element or circuit element)."""
    return get_string(CheckForError(lib.DSSElement_Get_Name()))


def NumProperties():
    """(read-only) Number of Properties for the active DSS object."""
    return CheckForError(lib.DSSElement_Get_NumProperties())


def ToJSON(options=0):
    """
    Returns the properties of the active DSS object as a JSON-encoded string.

    The `options` parameter contains bit-flags to toggle specific features.
    See `Obj_ToJSON` (C-API) for more.

    (API Extension)
    """
    return get_string(CheckForError(lib.DSSElement_ToJSON(options)))


_columns = ["Name", "NumProperties", "AllPropertyNames"]
__all__ = ["AllPropertyNames", "Name", "NumProperties", "ToJSON"]
