from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss import LineUnits


class ILineSpacings(Iterable):
    """
    LineSpacing objects

    (API Extension)
    """

    __name__ = "LineSpacings"
    _api_prefix = "LineSpacings"
    __slots__ = []
    _columns = ["Name", "Idx", "Nconds", "Phases", "Units", "Xcoords", "Ycoords"]

    def Phases(self, *args):
        """Number of Phases"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineSpacings_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineSpacings_Set_Phases(Value))

    def Nconds(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LineSpacings_Get_Nconds())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineSpacings_Set_Nconds(Value))

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.LineSpacings_Get_Units()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LineSpacings_Set_Units(Value))

    def Xcoords(self, *args):
        """Get/Set the X (horizontal) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineSpacings_Get_Xcoords_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount))

    def Ycoords(self, *args):
        """Get/Set the Y (vertical/height) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LineSpacings_Get_Ycoords_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount))


_LineSpacings = ILineSpacings(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Phases = _LineSpacings.Phases
Nconds = _LineSpacings.Nconds
Units = _LineSpacings.Units
Xcoords = _LineSpacings.Xcoords
Ycoords = _LineSpacings.Ycoords
Idx = _LineSpacings.Idx
First = _LineSpacings.First
Next = _LineSpacings.Next
AllNames = _LineSpacings.AllNames
Count = _LineSpacings.Count
Name = _LineSpacings.Name
_columns = _LineSpacings._columns
__all__ = [
    "Phases",
    "Nconds",
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
