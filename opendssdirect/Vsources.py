from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


class IVsources(Iterable):
    __slots__ = []

    __name__ = "Vsources"
    _api_prefix = "Vsources"
    _columns = ["Name", "Idx", "Phases", "BasekV", "AngleDeg", "Frequency", "PU"]

    def AngleDeg(self, *args):
        """
        Phase angle of first phase in degrees

        Original COM help: https://opendss.epri.com/AngleDeg1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Vsources_Get_AngleDeg())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Vsources_Set_AngleDeg(Value))

    def BasekV(self, *args):
        """
        Source voltage in kV

        Original COM help: https://opendss.epri.com/BasekV.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Vsources_Get_BasekV())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Vsources_Set_BasekV(Value))

    def Frequency(self, *args):
        """
        Source frequency in Hz

        Original COM help: https://opendss.epri.com/Frequency2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Vsources_Get_Frequency())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Vsources_Set_Frequency(Value))

    def Phases(self, *args):
        """
        Number of phases

        Original COM help: https://opendss.epri.com/Phases3.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Vsources_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Vsources_Set_Phases(Value))

    def PU(self, *args):
        """
        Per-unit value of source voltage

        Original COM help: https://opendss.epri.com/pu.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Vsources_Get_pu())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Vsources_Set_pu(Value))


_Vsources = IVsources(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
