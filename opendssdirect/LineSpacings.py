from ._utils import api_util
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
            return self._lib.LineSpacings_Get_Phases()

        # Setter
        (Value,) = args
        self._lib.LineSpacings_Set_Phases(Value)

    def Nconds(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.LineSpacings_Get_Nconds()

        # Setter
        (Value,) = args
        self._lib.LineSpacings_Set_Nconds(Value)

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.LineSpacings_Get_Units())

        # Setter
        (Value,) = args
        self._lib.LineSpacings_Set_Units(Value)

    def Xcoords(self, *args):
        """Get/Set the X (horizontal) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            return self._lib.LineSpacings_Get_Xcoords_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount)

    def Ycoords(self, *args):
        """Get/Set the Y (vertical/height) coordinates of the conductors"""
        # Getter
        if len(args) == 0:
            return self._lib.LineSpacings_Get_Ycoords_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount)


_LineSpacings = ILineSpacings(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _LineSpacings.AllNames
Count = _LineSpacings.Count
First = _LineSpacings.First
Idx = _LineSpacings.Idx
Name = _LineSpacings.Name
Nconds = _LineSpacings.Nconds
Next = _LineSpacings.Next
Phases = _LineSpacings.Phases
Units = _LineSpacings.Units
Xcoords = _LineSpacings.Xcoords
Ycoords = _LineSpacings.Ycoords
_columns = _LineSpacings._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "Idx",
    "Name",
    "Nconds",
    "Next",
    "Phases",
    "Units",
    "Xcoords",
    "Ycoords",
]
