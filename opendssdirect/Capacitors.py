from ._utils import api_util, Iterable


class ICapacitors(Iterable):
    __slots__ = []
    __name__ = "Capacitors"
    _api_prefix = "Capacitors"
    _columns = [
        "Name",
        "Idx",
        "kV",
        "NumSteps",
        "AvailableSteps",
        "IsDelta",
        "States",
        "kvar",
    ]

    def AddStep(self):
        return self.CheckForError(self._lib.Capacitors_AddStep()) != 0

    def Close(self):
        self.CheckForError(self._lib.Capacitors_Close())

    def Open(self):
        self.CheckForError(self._lib.Capacitors_Open())

    def SubtractStep(self):
        return self.CheckForError(self._lib.Capacitors_SubtractStep()) != 0

    def AvailableSteps(self):
        """(read-only) Number of Steps available in cap bank to be switched ON."""
        return self.CheckForError(self._lib.Capacitors_Get_AvailableSteps())

    def IsDelta(self, *args):
        """Delta connection or wye?"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Capacitors_Get_IsDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Capacitors_Set_IsDelta(Value))

    def NumSteps(self, *args):
        """Number of steps (default 1) for distributing and switching the total bank kVAR."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Capacitors_Get_NumSteps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Capacitors_Set_NumSteps(Value))

    def States(self, *args):
        """A array of  integer [0..numsteps-1] indicating state of each step. If the read value is -1 an error has occurred."""
        # Getter
        if len(args) == 0:
            return self._get_int32_array(self._lib.Capacitors_Get_States)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.Capacitors_Set_States(ValuePtr, ValueCount))

    def kV(self, *args):
        """Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Capacitors_Get_kV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Capacitors_Set_kV(Value))

    def kvar(self, *args):
        """Total bank KVAR, distributed equally among phases and steps."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Capacitors_Get_kvar())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Capacitors_Set_kvar(Value))


_Capacitors = ICapacitors(api_util)

# For backwards compatibility, bind to the default instance
AddStep = _Capacitors.AddStep
Close = _Capacitors.Close
Open = _Capacitors.Open
SubtractStep = _Capacitors.SubtractStep
AllNames = _Capacitors.AllNames
AvailableSteps = _Capacitors.AvailableSteps
Count = _Capacitors.Count
First = _Capacitors.First
IsDelta = _Capacitors.IsDelta
Name = _Capacitors.Name
Next = _Capacitors.Next
NumSteps = _Capacitors.NumSteps
States = _Capacitors.States
kV = _Capacitors.kV
kvar = _Capacitors.kvar
Idx = _Capacitors.Idx
_columns = _Capacitors._columns
__all__ = [
    "AddStep",
    "Close",
    "Open",
    "SubtractStep",
    "AllNames",
    "AvailableSteps",
    "Count",
    "First",
    "IsDelta",
    "Name",
    "Next",
    "NumSteps",
    "States",
    "kV",
    "kvar",
    "Idx",
]
