from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss import LineUnits


class IWireData(Iterable):
    """
    WireData objects

    (API Extension)
    """

    __name__ = "WireData"
    _api_prefix = "WireData"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "NormAmps",
        "EmergAmps",
        "Rdc",
        "Rac",
        "ResistanceUnits",
        "GMRac",
        "GMRUnits",
        "Radius",
        "Diameter",
        "RadiusUnits",
        "CapRadius",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_EmergAmps(Value))

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_NormAmps(Value))

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_Rdc())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_Rdc(Value))

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_Rac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_Rac(Value))

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_GMRac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_GMRac(Value))

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.WireData_Get_GMRUnits()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_GMRUnits(Value))

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_Radius())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_Radius(Value))

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_RadiusUnits())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_RadiusUnits(Value))

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(
                self._check_for_error(self._lib.WireData_Get_ResistanceUnits())
            )

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_ResistanceUnits(Value))

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_Diameter())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_Diameter(Value))

    def CapRadius(self, *args):
        """Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius."""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.WireData_Get_CapRadius())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.WireData_Set_CapRadius(Value))


_WireData = IWireData(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
EmergAmps = _WireData.EmergAmps
NormAmps = _WireData.NormAmps
Rdc = _WireData.Rdc
Rac = _WireData.Rac
GMRac = _WireData.GMRac
GMRUnits = _WireData.GMRUnits
Radius = _WireData.Radius
RadiusUnits = _WireData.RadiusUnits
ResistanceUnits = _WireData.ResistanceUnits
Diameter = _WireData.Diameter
Idx = _WireData.Idx
First = _WireData.First
Next = _WireData.Next
AllNames = _WireData.AllNames
Count = _WireData.Count
Name = _WireData.Name
CapRadius = _WireData.CapRadius
_columns = _WireData._columns
__all__ = [
    "EmergAmps",
    "NormAmps",
    "Rdc",
    "Rac",
    "GMRac",
    "GMRUnits",
    "Radius",
    "RadiusUnits",
    "ResistanceUnits",
    "Diameter",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
    "CapRadius",
]
