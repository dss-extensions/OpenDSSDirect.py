from ._utils import CheckForError, api_util, Iterable


class ILineGeometries(Iterable):
    """Experimental API extension exposing part of the LineGeometry objects"""

    _api_prefix = "LineGeometries"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "RhoEarth",
        "Reduce",
        "Units",
        "Conductors",
        "Xcoords",
        "Ycoords",
        "Rmatrix",
        "Xmatrix",
        "Zmatrix",
        "NormAmps",
        "EmergAmps",
    ]

    def Conductors(self):
        """(read-only) Array of strings with names of all conductors in the active LineGeometry object"""
        return self.CheckForError(
            self._get_string_array(self._lib.LineGeometries_Get_Conductors)
        )

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LineGeometries_Get_EmergAmps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LineGeometries_Set_EmergAmps(Value))

    def NormAmps(self, *args):
        """Normal ampere rating"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LineGeometries_Get_NormAmps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LineGeometries_Set_NormAmps(Value))

    def RhoEarth(self, *args):
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LineGeometries_Get_RhoEarth())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LineGeometries_Set_RhoEarth(Value))

    def Reduce(self, *args):
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LineGeometries_Get_Reduce()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.LineGeometries_Set_Reduce(Value))

    def Phases(self, *args):
        """Number of Phases"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LineGeometries_Get_Phases())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LineGeometries_Set_Phases(Value))

    def Rmatrix(self, Frequency, Length, Units):
        """(read-only) Resistance matrix, ohms"""
        return self.CheckForError(
            self._get_float64_array(
                self._lib.LineGeometries_Get_Rmatrix, Frequency, Length, Units
            )
        )

    def Xmatrix(self, Frequency, Length, Units):
        """(read-only) Reactance matrix, ohms"""
        return self.CheckForError(
            self._get_float64_array(
                self._lib.LineGeometries_Get_Xmatrix, Frequency, Length, Units
            )
        )

    def Zmatrix(self, Frequency, Length, Units):
        """(read-only) Complex impedance matrix, ohms"""
        return self.CheckForError(
            self._get_float64_array(
                self._lib.LineGeometries_Get_Zmatrix, Frequency, Length, Units
            )
        )

    def Cmatrix(self, Frequency, Length, Units):
        """(read-only) Capacitance matrix, nF"""
        return self.CheckForError(
            self._get_float64_array(
                self._lib.LineGeometries_Get_Cmatrix, Frequency, Length, Units
            )
        )

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return self._get_int32_array(self._lib.LineGeometries_Get_Units)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount))

    def Xcoords(self, *args):
        """Get/Set the X (horizontal) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.LineGeometries_Get_Xcoords)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount))

    def Ycoords(self, *args):
        """Get/Set the Y (vertical/height) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.LineGeometries_Get_Ycoords)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount))


_LineGeometries = ILineGeometries(api_util)

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
]
