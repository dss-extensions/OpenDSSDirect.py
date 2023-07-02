from ._utils import CheckForError, api_util, Base


class IElement(Base):
    __slots__ = ["Properties"]
    _api_prefix = "DSSElement"
    _columns = ["AllPropertyNames", "Name", "NumProperties"]

    def AllPropertyNames(self):
        """(read-only) Array of strings containing the names of all properties for the active DSS object."""
        return self.CheckForError(
            self._get_string_array(self._lib.DSSElement_Get_AllPropertyNames)
        )

    def Name(self):
        """(read-only) Full Name of Active DSS Object (general element or circuit element)."""
        return self._get_string(self.CheckForError(self._lib.DSSElement_Get_Name()))

    def NumProperties(self):
        """(read-only) Number of Properties for the active DSS object."""
        return self.CheckForError(self._lib.DSSElement_Get_NumProperties())

    def ToJSON(self, options=0):
        """
        Returns the properties of the active DSS object as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        (API Extension)
        """
        return self._get_string(
            self.CheckForError(self._lib.DSSElement_ToJSON(options))
        )


_Element = IElement(api_util)

# For backwards compatibility, bind to the default instance
AllPropertyNames = _Element.AllPropertyNames
Name = _Element.Name
NumProperties = _Element.NumProperties
ToJSON = _Element.ToJSON
_columns = _Element._columns
__all__ = ["AllPropertyNames", "Name", "NumProperties", "ToJSON"]
