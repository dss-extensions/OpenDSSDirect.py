from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss_python_backend.enums import StorageStates

class IStorages(Iterable):
    """Storage objects"""

    __name__ = "Storages"
    _api_prefix = "Storages"
    __slots__ = []
    _columns = ["Name", "Idx", "RegisterNames", "RegisterValues", "puSOC", "State"]

    def puSOC(self, *args):
        """Per unit state of charge"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Storages_Get_puSOC())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Storages_Set_puSOC(Value))

    def State(self, *args):
        """
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;
        """
        # Getter
        if len(args) == 0:
            return StorageStates(self._check_for_error(self._lib.Storages_Get_State()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Storages_Set_State(Value))

    def RegisterNames(self):
        """
        Array of Storage energy meter register names

        See also the enum `GeneratorRegisters`.
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Storages_Get_RegisterNames)
        )

    def RegisterValues(self):
        """Array of values in Storage registers."""
        self._check_for_error(self._lib.Storages_Get_RegisterValues_GR())
        return self._get_float64_gr_array()


_Storages = IStorages(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
puSOC = _Storages.puSOC
State = _Storages.State
RegisterNames = _Storages.RegisterNames
RegisterValues = _Storages.RegisterValues
Idx = _Storages.Idx
First = _Storages.First
Next = _Storages.Next
AllNames = _Storages.AllNames
Count = _Storages.Count
Name = _Storages.Name
_columns = _Storages._columns
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
