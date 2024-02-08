from typing import Any
from dss._cffi_api_util import Base as DSSPyBase

class Base(DSSPyBase):
    def __init__(self, api_util, prefer_lists=None):
        DSSPyBase.__init__(self, api_util, prefer_lists=prefer_lists)
        # Keep this since there are some differences when the array is empty.
        self._get_string_array = api_util.get_string_array2
        self._frozen_attrs = True

    def __setattr__(self, __name: str, __value: Any) -> None:
        if self._frozen_attrs:
            raise AttributeError("Misuse of OpenDSSDirect.py: use function calls instead of assignments to interact with the DSS engine. For properties and COM-API compatibility, use DSS-Python.\nSee also https://dss-extensions.org/python_apis.html")
        
        object.__setattr__(self, __name, __value)


class Iterable(Base):
    """
    Provides iteration methods

    Based on DSS-Python's Iterable class.
    """ 

    __slots__ = [
        "_Get_First",
        "_Get_Next",
        "_Get_Count",
        "_Get_AllNames",
        "_Get_Name",
        "_Set_Name",
        "_Get_idx",
        "_Set_idx",
    ]
    
    def __init__(self, api_util, prefer_lists=None):
        Base.__init__(self, api_util, prefer_lists=prefer_lists)
        
        prefix = self._api_prefix
        object.__setattr__(self, '_frozen_attrs', False)
        self._Get_First = getattr(self._lib, "{}_Get_First".format(prefix))
        self._Get_Next = getattr(self._lib, "{}_Get_Next".format(prefix))
        self._Get_Count = getattr(self._lib, "{}_Get_Count".format(prefix))
        self._Get_AllNames = getattr(self._lib, "{}_Get_AllNames".format(prefix))
        self._Get_Name = getattr(self._lib, "{}_Get_Name".format(prefix))
        self._Set_Name = getattr(self._lib, "{}_Set_Name".format(prefix))
        self._Get_idx = getattr(self._lib, "{}_Get_idx".format(prefix))
        self._Set_idx = getattr(self._lib, "{}_Set_idx".format(prefix))
        object.__setattr__(self, '_frozen_attrs', True)

    def First(self):
        """Sets the first object of this type active. Returns 0 if none."""
        return self._Get_First()

    def Next(self):
        """Sets next object of this type active. Returns 0 if no more."""
        return self._Get_Next()

    def Count(self):
        """Number of objects of this type"""
        return self._Get_Count()

    def __len__(self):
        """
        Number of objects of this type
        
        **(API Extension)**
        """
        return self._Get_Count()

    def __iter__(self):
        """
        Get an iterator of the object collection.
        
        Note that OpenDSS, via the classic APIs, only allow a single object of a specific type
        to be activated. That is, you cannot use references of distinct objects and interact
        with both at the same time, or keep a reference to use later. You need to reactivate
        the target object or ensure it is the active one.

        For an alternative, consider using our AltDSS-Python package.

        **(API Extension)**
        """
        idx = self._Get_First()
        while idx != 0:
            yield self
            idx = self._Get_Next()

    def AllNames(self):
        """Array of all names of this object type"""
        return self._get_string_array(self._Get_AllNames)

    def Name(self, *args):
        """Gets the current name or sets the active object of this type by name"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._Get_Name())
        
        # Setter
        Value, = args        
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._Set_Name(Value))
        
    def Idx(self, *args):
        """Gets the current index or sets the active object of this type by index"""
        # Getter
        if len(args) == 0:
            return self._Get_idx()

        # Setter
        Value, = args        
        if not isinstance(Value, bytes):
            self._check_for_error(self._Set_idx(Value))

__all__ = ["Iterable", "Base",]