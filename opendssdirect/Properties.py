from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IProperties(Base):
    __slots__ = []
    __name__ = "Properties"
    _api_prefix = "DSSProperty"
    _columns = ["Description", "Name", "Value"]

    def Description(self):
        """(read-only) Description of the property."""
        return self._get_string(
            self._check_for_error(self._lib.DSSProperty_Get_Description())
        )

    def Name(self):
        """(read-only) Name of Property"""
        return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Name()))

    def _setCurrentProperty(self, argIndex_or_Name):
        """
        Sets the current DSS property based on a 1-based integer (or integer as
        a string) as an property index, or a string as a property name.
        """
        try:
            if not isinstance(argIndex_or_Name, int):
                argIndex_or_Name = int(argIndex_or_Name)

            # use 1-based index here for compatibility
            self._lib.DSSProperty_Set_Index(argIndex_or_Name - 1)

        except ValueError:
            # if we cannot convert to integer, use string as name instead
            if not isinstance(argIndex_or_Name, bytes):
                argIndex_or_Name = argIndex_or_Name.encode(self._api_util.codec)

            self._lib.DSSProperty_Set_Name(argIndex_or_Name)
        

    def Value(self, *args):
        # Getter
        if len(args) == 0:
            # General getter
            return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Val()))
        elif len(args) == 1:
            # Getter by index as str or integer
            argIndex_or_Name, = args

            self._setCurrentProperty(argIndex_or_Name)
            return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Val()))

        # Setter by index as strs
        argIndex_or_Name, Value = args
        if not isinstance(Value, bytes):
            Value = str(Value).encode(self._api_util.codec)

        self._setCurrentProperty(argIndex_or_Name)
        self._lib.DSSProperty_Set_Val(Value)
        self._check_for_error()


_Properties = IProperties(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Description = _Properties.Description
Name = _Properties.Name
Value = _Properties.Value
_columns = _Properties._columns
__all__ = ["Description", "Name", "Value"]
