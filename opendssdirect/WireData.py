from ._utils import api_util
from .Bases import Iterable
from dss import LineUnits


class IWireData(Iterable):
    """
    WireData objects

    *Not available when using EPRI's OpenDSS distribution.*

    **(API Extension)**
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
            return self._lib.WireData_Get_EmergAmps()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_EmergAmps(Value)

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_NormAmps()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_NormAmps(Value)

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Rdc()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_Rdc(Value)

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Rac()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_Rac(Value)

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_GMRac()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_GMRac(Value)

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.WireData_Get_GMRUnits())

        # Setter
        (Value,) = args
        self._lib.WireData_Set_GMRUnits(Value)

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Radius()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_Radius(Value)

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_RadiusUnits()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_RadiusUnits(Value)

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.WireData_Get_ResistanceUnits())

        # Setter
        (Value,) = args
        self._lib.WireData_Set_ResistanceUnits(Value)

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Diameter()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_Diameter(Value)

    def CapRadius(self, *args):
        """Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius."""
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_CapRadius()

        # Setter
        (Value,) = args
        self._lib.WireData_Set_CapRadius(Value)


_WireData = IWireData(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _WireData.AllNames
CapRadius = _WireData.CapRadius
Count = _WireData.Count
Diameter = _WireData.Diameter
EmergAmps = _WireData.EmergAmps
First = _WireData.First
GMRUnits = _WireData.GMRUnits
GMRac = _WireData.GMRac
Idx = _WireData.Idx
Name = _WireData.Name
Next = _WireData.Next
NormAmps = _WireData.NormAmps
Rac = _WireData.Rac
Radius = _WireData.Radius
RadiusUnits = _WireData.RadiusUnits
Rdc = _WireData.Rdc
ResistanceUnits = _WireData.ResistanceUnits
_columns = _WireData._columns
__all__ = [
    "AllNames",
    "CapRadius",
    "Count",
    "Diameter",
    "EmergAmps",
    "First",
    "GMRUnits",
    "GMRac",
    "Idx",
    "Name",
    "Next",
    "NormAmps",
    "Rac",
    "Radius",
    "RadiusUnits",
    "Rdc",
    "ResistanceUnits",
]
