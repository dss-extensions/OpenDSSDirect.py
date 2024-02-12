from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss import LineUnits


class ILineCodes(Iterable):
    __slots__ = []

    __name__ = "LineCodes"
    _api_prefix = "LineCodes"
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Units",
        "IsZ1Z0",
        "R0",
        "R1",
        "X0",
        "X1",
        "C0",
        "C1",
        "Rmatrix",
        "Xmatrix",
        "Cmatrix",
        "EmergAmps",
        "NormAmps",
    ]

    def C0(self, *args):
        """
        Zero-sequence capacitance, nF per unit length

        Original COM help: https://opendss.epri.com/C2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_C0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_C0(Value))

    def C1(self, *args):
        """
        Positive-sequence capacitance, nF per unit length

        Original COM help: https://opendss.epri.com/C3.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_C1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_C1(Value))

    def Cmatrix(self, *args):
        """
        Capacitance matrix, nF per unit length

        Original COM help: https://opendss.epri.com/Cmatrix1.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineCodes_Get_Cmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount))

    def EmergAmps(self, *args):
        """
        Emergency ampere rating

        Original COM help: https://opendss.epri.com/EmergAmps2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_EmergAmps(Value))

    def IsZ1Z0(self):
        """
        Flag denoting whether impedance data were entered in symmetrical components

        Original COM help: https://opendss.epri.com/IsZ1Z0.html
        """
        return self._check_for_error(self._lib.LineCodes_Get_IsZ1Z0()) != 0

    def NormAmps(self, *args):
        """
        Normal Ampere rating

        Original COM help: https://opendss.epri.com/NormAmps1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_NormAmps(Value))

    def Phases(self, *args):
        """
        Number of Phases

        Original COM help: https://opendss.epri.com/Phases2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_Phases(Value))

    def R0(self, *args):
        """
        Zero-Sequence Resistance, ohms per unit length

        Original COM help: https://opendss.epri.com/R2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_R0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_R0(Value))

    def R1(self, *args):
        """
        Positive-sequence resistance ohms per unit length

        Original COM help: https://opendss.epri.com/R3.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_R1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_R1(Value))

    def Rmatrix(self, *args):
        """
        Resistance matrix, ohms per unit length

        Original COM help: https://opendss.epri.com/Rmatrix1.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineCodes_Get_Rmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount))

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.LineCodes_Get_Units()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_Units(Value))

    def X0(self, *args):
        """
        Zero Sequence Reactance, Ohms per unit length

        Original COM help: https://opendss.epri.com/X2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_X0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_X0(Value))

    def X1(self, *args):
        """
        Positive-sequence reactance, ohms per unit length

        Original COM help: https://opendss.epri.com/X3.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineCodes_Get_X1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineCodes_Set_X1(Value))

    def Xmatrix(self, *args):
        """
        Reactance matrix, ohms per unit length

        Original COM help: https://opendss.epri.com/Xmatrix1.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineCodes_Get_Xmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount))


_LineCodes = ILineCodes(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
AllNames = _LineCodes.AllNames
C0 = _LineCodes.C0
C1 = _LineCodes.C1
Cmatrix = _LineCodes.Cmatrix
Count = _LineCodes.Count
EmergAmps = _LineCodes.EmergAmps
First = _LineCodes.First
IsZ1Z0 = _LineCodes.IsZ1Z0
Name = _LineCodes.Name
Next = _LineCodes.Next
NormAmps = _LineCodes.NormAmps
Phases = _LineCodes.Phases
R0 = _LineCodes.R0
R1 = _LineCodes.R1
Rmatrix = _LineCodes.Rmatrix
Units = _LineCodes.Units
X0 = _LineCodes.X0
X1 = _LineCodes.X1
Xmatrix = _LineCodes.Xmatrix
Idx = _LineCodes.Idx
_columns = _LineCodes._columns
__all__ = [
    "AllNames",
    "C0",
    "C1",
    "Cmatrix",
    "Count",
    "EmergAmps",
    "First",
    "IsZ1Z0",
    "Name",
    "Next",
    "NormAmps",
    "Phases",
    "R0",
    "R1",
    "Rmatrix",
    "Units",
    "X0",
    "X1",
    "Xmatrix",
    "Idx",
]
