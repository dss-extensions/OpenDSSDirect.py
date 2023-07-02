from ._utils import CheckForError, api_util, Iterable


class IStorages(Iterable):
    """Storage objects"""

    _api_prefix = "Storages"
    __slots__ = []
    _columns = ["Name", "Idx", "RegisterNames", "RegisterValues", "puSOC", "State"]

    def puSOC(self, *args):
        """Per unit state of charge"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Storages_Get_puSOC())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Storages_Set_puSOC(Value))

    def State(self, *args):
        """
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;

        Related enumeration: StorageStates
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Storages_Get_State())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Storages_Set_State(Value))

    def RegisterNames(self):
        """Array of Names of all Storage energy meter registers"""
        return self.CheckForError(
            self._get_string_array(self._lib.Storages_Get_RegisterNames)
        )

    def RegisterValues(self):
        """Array of values in Storage registers."""
        return self._get_float64_array(self._lib.Storages_Get_RegisterValues)


_Storages = IStorages(api_util)

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
