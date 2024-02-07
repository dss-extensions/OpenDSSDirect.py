from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
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
        return self._check_for_error(self._lib.Capacitors_AddStep()) != 0

    def Close(self):
        self._check_for_error(self._lib.Capacitors_Close())

    def Open(self):
        self._check_for_error(self._lib.Capacitors_Open())

    def SubtractStep(self):
        return self._check_for_error(self._lib.Capacitors_SubtractStep()) != 0

    def AvailableSteps(self):
        """
        Number of Steps available in cap bank to be switched ON.

        Original COM help: https://opendss.epri.com/AvailableSteps.html
        """
        return self._check_for_error(self._lib.Capacitors_Get_AvailableSteps())

    def IsDelta(self, *args):
        """
        Delta connection or wye?

        Original COM help: https://opendss.epri.com/IsDelta.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Capacitors_Get_IsDelta()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Capacitors_Set_IsDelta(Value))

    def NumSteps(self, *args):
        """
        Number of steps (default 1) for distributing and switching the total bank kVAR.

        Original COM help: https://opendss.epri.com/NumSteps.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Capacitors_Get_NumSteps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Capacitors_Set_NumSteps(Value))

    def States(self, *args):
        """
        An array of integers [0..NumSteps-1] indicating state of each step. If the read value is -1 an error has occurred.

        Original COM help: https://opendss.epri.com/States.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Capacitors_Get_States_GR())
            return self._get_int32_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Capacitors_Set_States(ValuePtr, ValueCount))

    def kV(self, *args):
        """
        Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.

        Original COM help: https://opendss.epri.com/kV.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Capacitors_Get_kV())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Capacitors_Set_kV(Value))

    def kvar(self, *args):
        """Total bank KVAR, distributed equally among phases and steps."""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Capacitors_Get_kvar())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Capacitors_Set_kvar(Value))


_Capacitors = ICapacitors(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
