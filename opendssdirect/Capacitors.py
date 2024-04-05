from ._utils import api_util
from .Bases import Iterable


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
        return self._lib.Capacitors_AddStep()

    def Close(self):
        self._lib.Capacitors_Close()

    def Open(self):
        self._lib.Capacitors_Open()

    def SubtractStep(self):
        return self._lib.Capacitors_SubtractStep()

    def AvailableSteps(self):
        """
        Number of Steps available in cap bank to be switched ON.

        Original COM help: https://opendss.epri.com/AvailableSteps.html
        """
        return self._lib.Capacitors_Get_AvailableSteps()

    def IsDelta(self, *args):
        """
        Delta connection or wye?

        Original COM help: https://opendss.epri.com/IsDelta.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Capacitors_Get_IsDelta()

        # Setter
        (Value,) = args
        self._lib.Capacitors_Set_IsDelta(Value)

    def NumSteps(self, *args):
        """
        Number of steps (default 1) for distributing and switching the total bank kVAR.

        Original COM help: https://opendss.epri.com/NumSteps.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Capacitors_Get_NumSteps()

        # Setter
        (Value,) = args
        self._lib.Capacitors_Set_NumSteps(Value)

    def States(self, *args):
        """
        An array of integers [0..NumSteps-1] indicating state of each step. If the read value is -1 an error has occurred.

        Original COM help: https://opendss.epri.com/States.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Capacitors_Get_States_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Capacitors_Set_States(ValuePtr, ValueCount)

    def kV(self, *args):
        """
        Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.

        Original COM help: https://opendss.epri.com/kV.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Capacitors_Get_kV()

        # Setter
        (Value,) = args
        self._lib.Capacitors_Set_kV(Value)

    def kvar(self, *args):
        """Total bank KVAR, distributed equally among phases and steps."""
        # Getter
        if len(args) == 0:
            return self._lib.Capacitors_Get_kvar()

        # Setter
        (Value,) = args
        self._lib.Capacitors_Set_kvar(Value)


_Capacitors = ICapacitors(api_util)

# For backwards compatibility, bind to the default instance
AddStep = _Capacitors.AddStep
AllNames = _Capacitors.AllNames
AvailableSteps = _Capacitors.AvailableSteps
Close = _Capacitors.Close
Count = _Capacitors.Count
First = _Capacitors.First
Idx = _Capacitors.Idx
IsDelta = _Capacitors.IsDelta
Name = _Capacitors.Name
Next = _Capacitors.Next
NumSteps = _Capacitors.NumSteps
Open = _Capacitors.Open
States = _Capacitors.States
SubtractStep = _Capacitors.SubtractStep
kV = _Capacitors.kV
kvar = _Capacitors.kvar
_columns = _Capacitors._columns
__all__ = [
    "AddStep",
    "AllNames",
    "AvailableSteps",
    "Close",
    "Count",
    "First",
    "Idx",
    "IsDelta",
    "Name",
    "Next",
    "NumSteps",
    "Open",
    "States",
    "SubtractStep",
    "kV",
    "kvar",
]
