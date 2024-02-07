from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IElement(Base):
    __slots__ = []

    __name__ = "Element"
    _api_prefix = "DSSElement"
    _columns = ["AllPropertyNames", "Name", "NumProperties"]

    def AllPropertyNames(self):
        """
        Array of strings containing the names of all properties for the active DSS object.

        Original COM help: https://opendss.epri.com/AllPropertyNames1.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.DSSElement_Get_AllPropertyNames)
        )

    def Name(self):
        """
        Full Name of Active DSS Object (general element or circuit element).

        Original COM help: https://opendss.epri.com/Name5.html
        """
        return self._get_string(self._check_for_error(self._lib.DSSElement_Get_Name()))

    def NumProperties(self):
        """
        Number of Properties for the active DSS object.

        Original COM help: https://opendss.epri.com/NumProperties1.html
        """
        return self._check_for_error(self._lib.DSSElement_Get_NumProperties())

    def ToJSON(self, options=0):
        """
        Returns the properties of the active DSS object as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        **(API Extension)**
        """
        return self._get_string(
            self._check_for_error(self._lib.DSSElement_ToJSON(options))
        )


_Element = IElement(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
AllPropertyNames = _Element.AllPropertyNames
Name = _Element.Name
NumProperties = _Element.NumProperties
ToJSON = _Element.ToJSON
_columns = _Element._columns
__all__ = ["AllPropertyNames", "Name", "NumProperties", "ToJSON"]
