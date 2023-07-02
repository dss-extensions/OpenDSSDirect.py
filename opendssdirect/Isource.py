from ._utils import CheckForError, api_util, Iterable


class IIsource(Iterable):
    __slots__ = []
    _api_prefix = "ISources"
    _columns = ["Name", "Idx", "Amps", "AngleDeg", "Frequency"]

    def Amps(self, *args):
        """Magnitude of the ISource in amps"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.ISources_Get_Amps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.ISources_Set_Amps(Value))

    def AngleDeg(self, *args):
        """Phase angle for ISource, degrees"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.ISources_Get_AngleDeg())

        # Setter
        Value, = args
        self.CheckForError(self._lib.ISources_Set_AngleDeg(Value))

    def Frequency(self, *args):
        """The present frequency of the ISource, Hz"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.ISources_Get_Frequency())

        # Setter
        Value, = args
        self.CheckForError(self._lib.ISources_Set_Frequency(Value))


_Isource = IIsource(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Isource.AllNames
Amps = _Isource.Amps
AngleDeg = _Isource.AngleDeg
Count = _Isource.Count
First = _Isource.First
Frequency = _Isource.Frequency
Name = _Isource.Name
Next = _Isource.Next
Idx = _Isource.Idx
_columns = _Isource._columns
__all__ = [
    "AllNames",
    "Amps",
    "AngleDeg",
    "Count",
    "First",
    "Frequency",
    "Name",
    "Next",
    "Idx",
]
