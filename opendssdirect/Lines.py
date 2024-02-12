from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss import LineUnits


class ILines(Iterable):
    __slots__ = []

    __name__ = "Lines"
    _api_prefix = "Lines"
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Bus1",
        "Bus2",
        "LineCode",
        "Geometry",
        "Length",
        "IsSwitch",
        "Spacing",
        "EmergAmps",
        "NormAmps",
        "SeasonRating",
        "Yprim",
        "NumCust",
        "TotalCust",
        "Rho",
        "R0",
        "R1",
        "X0",
        "X1",
        "Rg",
        "Xg",
        "C0",
        "C1",
        "RMatrix",
        "XMatrix",
        "CMatrix",
        "Units",
    ]

    def New(self, Name):
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)
        return self._check_for_error(self._lib.Lines_New(Name))

    def Bus1(self, *args):
        """
        Name of bus for terminal 1.

        Original COM help: https://opendss.epri.com/Bus1.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Lines_Get_Bus1()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Lines_Set_Bus1(Value))

    def Bus2(self, *args):
        """
        Name of bus for terminal 2.

        Original COM help: https://opendss.epri.com/Bus2.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Lines_Get_Bus2()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Lines_Set_Bus2(Value))

    def C0(self, *args):
        """
        Zero Sequence capacitance, nanofarads per unit length.

        Original COM help: https://opendss.epri.com/C0.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_C0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_C0(Value))

    def C1(self, *args):
        """
        Positive Sequence capacitance, nanofarads per unit length.

        Original COM help: https://opendss.epri.com/C1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_C1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_C1(Value))

    def CMatrix(self, *args):
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Lines_Get_Cmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Cmatrix(ValuePtr, ValueCount))

    def EmergAmps(self, *args):
        """
        Emergency (maximum) ampere rating of Line.

        Original COM help: https://opendss.epri.com/EmergAmps1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_EmergAmps(Value))

    def Geometry(self, *args):
        """
        Line geometry code

        Original COM help: https://opendss.epri.com/Geometry.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Lines_Get_Geometry()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Lines_Set_Geometry(Value))

    def Length(self, *args):
        """
        Length of line section in units compatible with the LineCode definition.

        Original COM help: https://opendss.epri.com/Length.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_Length())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Length(Value))

    def LineCode(self, *args):
        """
        Name of LineCode object that defines the impedances.

        Original COM help: https://opendss.epri.com/LineCode.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Lines_Get_LineCode()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Lines_Set_LineCode(Value))

    def NormAmps(self, *args):
        """
        Normal ampere rating of Line.

        Original COM help: https://opendss.epri.com/NormAmps.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_NormAmps(Value))

    def NumCust(self):
        """
        Number of customers on this line section.

        Original COM help: https://opendss.epri.com/NumCust.html
        """
        return self._check_for_error(self._lib.Lines_Get_NumCust())

    def Parent(self):
        """
        Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails.

        Original COM help: https://opendss.epri.com/Parent.html
        """
        return self._check_for_error(self._lib.Lines_Get_Parent())

    def Phases(self, *args):
        """
        Number of Phases, this Line element.

        Original COM help: https://opendss.epri.com/Phases1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Phases(Value))

    def R0(self, *args):
        """
        Zero Sequence resistance, ohms per unit length.

        Original COM help: https://opendss.epri.com/R0.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_R0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_R0(Value))

    def R1(self, *args):
        """
        Positive Sequence resistance, ohms per unit length.

        Original COM help: https://opendss.epri.com/R1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_R1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_R1(Value))

    def Rg(self, *args):
        """
        Earth return resistance value used to compute line impedances at power frequency

        Original COM help: https://opendss.epri.com/Rg.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_Rg())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Rg(Value))

    def Rho(self, *args):
        """
        Earth Resistivity, m-ohms

        Original COM help: https://opendss.epri.com/Rho.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_Rho())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Rho(Value))

    def RMatrix(self, *args):
        """
        Resistance matrix (full), ohms per unit length. Array of doubles.

        Original COM help: https://opendss.epri.com/Rmatrix.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Lines_Get_Rmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Rmatrix(ValuePtr, ValueCount))

    def Spacing(self, *args):
        """
        Line spacing code

        Original COM help: https://opendss.epri.com/Spacing.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Lines_Get_Spacing()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Lines_Set_Spacing(Value))

    def TotalCust(self):
        """
        Total Number of customers served from this line section.

        Original COM help: https://opendss.epri.com/TotalCust.html
        """
        return self._check_for_error(self._lib.Lines_Get_TotalCust())

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.Lines_Get_Units()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Units(Value))

    def X0(self, *args):
        """
        Zero Sequence reactance ohms per unit length.

        Original COM help: https://opendss.epri.com/X0.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_X0())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_X0(Value))

    def X1(self, *args):
        """
        Positive Sequence reactance, ohms per unit length.

        Original COM help: https://opendss.epri.com/X1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_X1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_X1(Value))

    def Xg(self, *args):
        """
        Earth return reactance value used to compute line impedances at power frequency

        Original COM help: https://opendss.epri.com/Xg.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_Xg())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_Xg(Value))

    def XMatrix(self, *args):
        """
        Reactance matrix (full), ohms per unit length. Array of doubles.

        Original COM help: https://opendss.epri.com/Xmatrix.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Lines_Get_Xmatrix_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Xmatrix(ValuePtr, ValueCount))

    def Yprim(self, *args):
        """
        Yprimitive for the active line object (complex array).

        Original COM help: https://opendss.epri.com/Yprim1.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Lines_Get_Yprim_GR())
            return self._get_complex128_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Yprim(ValuePtr, ValueCount))

    def SeasonRating(self):
        """
        Delivers the rating for the current season (in Amps)  if the "SeasonalRatings" option is active

        Original COM help: https://opendss.epri.com/SeasonRating.html
        """
        return self._check_for_error(self._lib.Lines_Get_SeasonRating())

    def IsSwitch(self, *args):
        """
        Sets/gets the Line element switch status. Setting it has side-effects to the line parameters.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Lines_Get_IsSwitch()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Lines_Set_IsSwitch(Value))


_Lines = ILines(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
New = _Lines.New
AllNames = _Lines.AllNames
Bus1 = _Lines.Bus1
Bus2 = _Lines.Bus2
C0 = _Lines.C0
C1 = _Lines.C1
CMatrix = _Lines.CMatrix
Count = _Lines.Count
EmergAmps = _Lines.EmergAmps
First = _Lines.First
Geometry = _Lines.Geometry
Length = _Lines.Length
LineCode = _Lines.LineCode
Name = _Lines.Name
Next = _Lines.Next
NormAmps = _Lines.NormAmps
NumCust = _Lines.NumCust
Parent = _Lines.Parent
Phases = _Lines.Phases
R0 = _Lines.R0
R1 = _Lines.R1
Rg = _Lines.Rg
Rho = _Lines.Rho
RMatrix = _Lines.RMatrix
Spacing = _Lines.Spacing
TotalCust = _Lines.TotalCust
Units = _Lines.Units
X0 = _Lines.X0
X1 = _Lines.X1
Xg = _Lines.Xg
XMatrix = _Lines.XMatrix
Yprim = _Lines.Yprim
SeasonRating = _Lines.SeasonRating
IsSwitch = _Lines.IsSwitch
Idx = _Lines.Idx
_columns = _Lines._columns
__all__ = [
    "New",
    "AllNames",
    "Bus1",
    "Bus2",
    "C0",
    "C1",
    "CMatrix",
    "Count",
    "EmergAmps",
    "First",
    "Geometry",
    "Length",
    "LineCode",
    "Name",
    "Next",
    "NormAmps",
    "NumCust",
    "Parent",
    "Phases",
    "R0",
    "R1",
    "Rg",
    "Rho",
    "RMatrix",
    "Spacing",
    "TotalCust",
    "Units",
    "X0",
    "X1",
    "Xg",
    "XMatrix",
    "Yprim",
    "SeasonRating",
    "IsSwitch",
    "Idx",
]
