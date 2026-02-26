from ._utils import api_util
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
        return self._lib.DSSElement_Get_AllPropertyNames()

    def Name(self):
        """
        Full Name of Active DSS Object (general element or circuit element).

        Original COM help: https://opendss.epri.com/Name5.html
        """
        return self._lib.DSSElement_Get_Name()

    def NumProperties(self):
        """
        Number of Properties for the active DSS object.

        Original COM help: https://opendss.epri.com/NumProperties1.html
        """
        return self._lib.DSSElement_Get_NumProperties()

    def ToJSON(self, options=0):
        """
        Returns the properties of the active DSS object as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        **(API Extension)**
        """
        return self._lib.DSSElement_ToJSON(options)

    def to_altdss(self):
        """
        Returns a Python object for the current active DSS object in this interface.

        Requires AltDSS-Python.

        *Available only for the AltDSS engine.*

        **(API Extension)**
        """
        ptr = self._api_util._lib.DSSElement_Get_Pointer()
        return self._api_util.get_dss_obj(ptr)


_Element = IElement(api_util)

# For backwards compatibility, bind to the default instance
AllPropertyNames = _Element.AllPropertyNames
Name = _Element.Name
NumProperties = _Element.NumProperties
ToJSON = _Element.ToJSON
to_altdss = _Element.to_altdss
_columns = _Element._columns
__all__ = ["AllPropertyNames", "Name", "NumProperties", "ToJSON", "to_altdss"]
