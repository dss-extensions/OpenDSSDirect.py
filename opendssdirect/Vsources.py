from ._utils import CheckForError, api_util, Iterable


class IVsources(Iterable):
    __slots__ = []
    __name__ = "Vsources"
    _api_prefix = "Vsources"
    _columns = ["Name", "Idx", "Phases", "BasekV", "AngleDeg", "Frequency", "PU"]

    def AngleDeg(self, *args):
        """Phase angle of first phase in degrees"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Vsources_Get_AngleDeg())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Vsources_Set_AngleDeg(Value))

    def BasekV(self, *args):
        """Source voltage in kV"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Vsources_Get_BasekV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Vsources_Set_BasekV(Value))

    def Frequency(self, *args):
        """Source frequency in Hz"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Vsources_Get_Frequency())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Vsources_Set_Frequency(Value))

    def Phases(self, *args):
        """Number of phases"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Vsources_Get_Phases())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Vsources_Set_Phases(Value))

    def PU(self, *args):
        """Per-unit value of source voltage"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Vsources_Get_pu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Vsources_Set_pu(Value))


_Vsources = IVsources(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Vsources.AllNames
AngleDeg = _Vsources.AngleDeg
BasekV = _Vsources.BasekV
Count = _Vsources.Count
First = _Vsources.First
Frequency = _Vsources.Frequency
Name = _Vsources.Name
Next = _Vsources.Next
Phases = _Vsources.Phases
PU = _Vsources.PU
Idx = _Vsources.Idx
_columns = _Vsources._columns
__all__ = [
    "AllNames",
    "AngleDeg",
    "BasekV",
    "Count",
    "First",
    "Frequency",
    "Name",
    "Next",
    "Phases",
    "PU",
    "Idx",
]
