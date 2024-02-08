from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IActiveClass(Base):
    __slots__ = []
    __name__ = "ActiveClass"
    _api_prefix = "ActiveClass"
    _columns = ["ActiveClassName", "ActiveClassParent", "Name", "NumElements"]

    def ActiveClassName(self):
        """
        Returns name of active class.

        Original COM help: https://opendss.epri.com/ActiveClassName.html
        """
        return self._get_string(
            self._check_for_error(self._lib.ActiveClass_Get_ActiveClassName())
        )

    def AllNames(self):
        """
        Array of strings consisting of all element names in the active class.

        Original COM help: https://opendss.epri.com/AllNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.ActiveClass_Get_AllNames)
        )

    def Count(self):
        """
        Number of elements in Active Class. Same as NumElements Property.

        Original COM help: https://opendss.epri.com/Count.html
        """
        return self._check_for_error(self._lib.ActiveClass_Get_Count())

    def First(self):
        """
        Sets first element in the active class to be the active DSS object.
        If the object is a CktElement, ActiveCktELement also points to this element.

        Returns 0 if none.

        Original COM help: https://opendss.epri.com/First.html
        """
        return self._check_for_error(self._lib.ActiveClass_Get_First())

    def Name(self, *args):
        """
        Name of the Active Element of the Active Class

        Original COM help: https://opendss.epri.com/Name.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.ActiveClass_Get_Name())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.ActiveClass_Set_Name(Value))

    def Next(self):
        """
        Sets next element in active class to be the active DSS object.
        If the object is a CktElement, ActiveCktElement also points to this element.

        Returns 0 if no more.

        Original COM help: https://opendss.epri.com/Next.html
        """
        return self._check_for_error(self._lib.ActiveClass_Get_Next())

    def NumElements(self):
        """
        Number of elements in this class. Same as Count property.

        Original COM help: https://opendss.epri.com/NumElements.html
        """
        return self._check_for_error(self._lib.ActiveClass_Get_NumElements())

    def ActiveClassParent(self):
        """
        Get the name of the parent class of the active class

        Original COM help: https://opendss.epri.com/ActiveClassParent.html
        """
        return self._get_string(
            self._check_for_error(self._lib.ActiveClass_Get_ActiveClassParent())
        )

    def ToJSON(self, options=0):
        """
        Returns the data (as a list) of all elements from the active class as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.

        **(API Extension)**
        """
        return self._get_string(
            self._check_for_error(self._lib.ActiveClass_ToJSON(options))
        )


_ActiveClass = IActiveClass(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
ActiveClassName = _ActiveClass.ActiveClassName
AllNames = _ActiveClass.AllNames
Count = _ActiveClass.Count
First = _ActiveClass.First
Name = _ActiveClass.Name
Next = _ActiveClass.Next
NumElements = _ActiveClass.NumElements
ActiveClassParent = _ActiveClass.ActiveClassParent
ToJSON = _ActiveClass.ToJSON
_columns = _ActiveClass._columns
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
