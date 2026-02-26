from ._utils import api_util
from .Bases import Iterable


class IReactors(Iterable):
    """
    Reactor objects
    
    API Status: **(API Extension)** before 2024-10-04. Since then, functions partially marked as extensions (see each property/function documentation).
    """

    __name__ = "Reactors"
    _api_prefix = "Reactors"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Bus1",
        "Bus2",
        "SpecType",
        "kV",
        "kvar",
        "IsDelta",
        "Parallel",
        "LCurve",
        "RCurve",
        "R",
        "Rp",
        "X",
        "Z0",
        "Z1",
        "Z2",
        "Z",
        "Rmatrix",
        "Xmatrix",
    ]

    def SpecType(self):
        """
        How the reactor data was provided: 1=kvar, 2=R+jX, 3=R and X matrices, 4=sym components.
        Depending on this value, only some properties are filled or make sense in the context.

        Typically not used by end users.

        **(API Extension)**
        """
        return self._lib.Reactors_Get_SpecType()

    def IsDelta(self, *args):
        """
        Delta connection or wye?

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_IsDelta()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_IsDelta(Value)

    def Parallel(self, *args):
        """Indicates whether Rmatrix and Xmatrix are to be considered in parallel."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Parallel()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_Parallel(Value)

    def LmH(self, *args):
        """Inductance, mH. Alternate way to define the reactance, X, property."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_LmH()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_LmH(Value)

    def kV(self, *args):
        """For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_kV()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_kV(Value)

    def kvar(self, *args):
        """Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately"""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_kvar()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_kvar(Value)

    def Phases(self, *args):
        """
        Number of phases.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Phases()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_Phases(Value)

    def Bus1(self, *args):
        """
        Name of first bus.
        Bus2 property will default to this bus, node 0, unless previously specified.
        Only Bus1 need be specified for a Yg shunt reactor.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Bus1()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_Bus1(Value)

    def Bus2(self, *args):
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.
        Not necessary to specify for delta (LL) connection.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Bus2()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_Bus2(Value)

    def LCurve(self, *args):
        """Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property. L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_LCurve()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_LCurve(Value)

    def RCurve(self, *args):
        """Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_RCurve()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_RCurve(Value)

    def R(self, *args):
        """Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_R()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_R(Value)

    def X(self, *args):
        """Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_X()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_X(Value)

    def Rp(self, *args):
        """Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Rp()

        # Setter
        (Value,) = args
        self._lib.Reactors_Set_Rp(Value)

    def Rmatrix(self, *args):
        """Resistance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Rmatrix_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Rmatrix(ValuePtr, ValueCount)

    def Xmatrix(self, *args):
        """Reactance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Xmatrix_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Xmatrix(ValuePtr, ValueCount)

    def Z(self, *args):
        """Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms."""
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Z_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._lib.Reactors_Set_Z(ValuePtr, ValueCount)

    def Z1(self, *args):
        """
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number.

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR.

        Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Z1_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._lib.Reactors_Set_Z1(ValuePtr, ValueCount)

    def Z2(self, *args):
        """
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Z2_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._lib.Reactors_Set_Z2(ValuePtr, ValueCount)

    def Z0(self, *args):
        """
        Zero-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z0 defaults to Z1 if it is not specifically defined.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reactors_Get_Z0_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._lib.Reactors_Set_Z0(ValuePtr, ValueCount)


_Reactors = IReactors(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Reactors.AllNames
Bus1 = _Reactors.Bus1
Bus2 = _Reactors.Bus2
Count = _Reactors.Count
First = _Reactors.First
Idx = _Reactors.Idx
IsDelta = _Reactors.IsDelta
LCurve = _Reactors.LCurve
LmH = _Reactors.LmH
Name = _Reactors.Name
Next = _Reactors.Next
Parallel = _Reactors.Parallel
Phases = _Reactors.Phases
R = _Reactors.R
RCurve = _Reactors.RCurve
Rmatrix = _Reactors.Rmatrix
Rp = _Reactors.Rp
SpecType = _Reactors.SpecType
X = _Reactors.X
Xmatrix = _Reactors.Xmatrix
Z = _Reactors.Z
Z0 = _Reactors.Z0
Z1 = _Reactors.Z1
Z2 = _Reactors.Z2
kV = _Reactors.kV
kvar = _Reactors.kvar
_columns = _Reactors._columns
__all__ = [
    "AllNames",
    "Bus1",
    "Bus2",
    "Count",
    "First",
    "Idx",
    "IsDelta",
    "LCurve",
    "LmH",
    "Name",
    "Next",
    "Parallel",
    "Phases",
    "R",
    "RCurve",
    "Rmatrix",
    "Rp",
    "SpecType",
    "X",
    "Xmatrix",
    "Z",
    "Z0",
    "Z1",
    "Z2",
    "kV",
    "kvar",
]
