from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss import LineUnits


class ILineGeometries(Iterable):
    """
    LineGeometry objects

    (API Extension)
    """

    __name__ = "LineGeometries"
    _api_prefix = "LineGeometries"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "Nconds",
        "Phases",
        "RhoEarth",
        "Reduce",
        "Units",
        "Conductors",
        "Xcoords",
        "Ycoords",
        # "Rmatrix",
        # "Xmatrix",
        # "Zmatrix",
        "NormAmps",
        "EmergAmps",
    ]

    def Conductors(self):
        """Array of strings with names of all conductors in the active LineGeometry object"""
        return self._check_for_error(
            self._get_string_array(self._lib.LineGeometries_Get_Conductors)
        )

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_EmergAmps(Value))

    def NormAmps(self, *args):
        """Normal ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_NormAmps(Value))

    def RhoEarth(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_RhoEarth())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_RhoEarth(Value))

    def Reduce(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_Reduce()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_Reduce(Value))

    def Phases(self, *args):
        """Number of Phases"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_Phases(Value))

    def Rmatrix(self, Frequency, Length, Units):
        """Resistance matrix, ohms"""
        self._check_for_error(
            self._lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units)
        )
        return self._get_float64_gr_array()

    def Xmatrix(self, Frequency, Length, Units):
        """Reactance matrix, ohms"""
        self._check_for_error(
            self._lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units)
        )
        return self._get_float64_gr_array()

    def Zmatrix(self, Frequency, Length, Units):
        """Complex impedance matrix, ohms"""
        self._check_for_error(
            self._lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units)
        )
        return self._get_complex128_gr_array()

    def Cmatrix(self, Frequency, Length, Units):
        """Capacitance matrix, nF"""
        self._check_for_error(
            self._lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units)
        )
        return self._get_float64_gr_array()

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineGeometries_Get_Units_GR())
            return [LineUnits(unit) for unit in self._get_int32_gr_array()]

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount))

    def Xcoords(self, *args):
        """Get/Set the X (horizontal) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineGeometries_Get_Xcoords_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount))

    def Ycoords(self, *args):
        """Get/Set the Y (vertical/height) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineGeometries_Get_Ycoords_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount))

    def Nconds(self, *args):
        """Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineGeometries_Get_Nconds())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineGeometries_Set_Nconds(Value))


_LineGeometries = ILineGeometries(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Conductors = _LineGeometries.Conductors
EmergAmps = _LineGeometries.EmergAmps
NormAmps = _LineGeometries.NormAmps
RhoEarth = _LineGeometries.RhoEarth
Reduce = _LineGeometries.Reduce
Phases = _LineGeometries.Phases
Rmatrix = _LineGeometries.Rmatrix
Xmatrix = _LineGeometries.Xmatrix
Zmatrix = _LineGeometries.Zmatrix
Cmatrix = _LineGeometries.Cmatrix
Units = _LineGeometries.Units
Xcoords = _LineGeometries.Xcoords
Ycoords = _LineGeometries.Ycoords
Idx = _LineGeometries.Idx
First = _LineGeometries.First
Next = _LineGeometries.Next
AllNames = _LineGeometries.AllNames
Count = _LineGeometries.Count
Name = _LineGeometries.Name
Nconds = _LineGeometries.Nconds
_columns = _LineGeometries._columns
__all__ = [
    "Conductors",
    "EmergAmps",
    "NormAmps",
    "RhoEarth",
    "Reduce",
    "Phases",
    "Rmatrix",
    "Xmatrix",
    "Zmatrix",
    "Cmatrix",
    "Units",
    "Xcoords",
    "Ycoords",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
    "Nconds",
]
