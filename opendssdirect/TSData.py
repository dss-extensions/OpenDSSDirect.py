from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


class ITSData(Iterable):
    """
    TSData objects

    (API Extension)
    """

    __name__ = "TSData"
    _api_prefix = "TSData"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "NormAmps",
        "EmergAmps",
        "Rdc",
        "Rac",
        "GMRac",
        "GMRUnits",
        "Radius",
        "RadiusUnits",
        "ResistanceUnits",
        "Diameter",
        "TapeLayer",
        "TapeLap",
        "DiaShield",
        "DiaCable",
        "DiaIns",
        "InsLayer",
        "EpsR",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_EmergAmps(Value))

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_NormAmps(Value))

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_Rdc())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_Rdc(Value))

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_Rac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_Rac(Value))

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_GMRac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_GMRac(Value))

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_GMRUnits())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_GMRUnits(Value))

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_Radius())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_Radius(Value))

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_RadiusUnits())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_RadiusUnits(Value))

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_ResistanceUnits())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_ResistanceUnits(Value))

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_Diameter())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_Diameter(Value))

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_EpsR())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_EpsR(Value))

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_InsLayer())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_InsLayer(Value))

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_DiaIns())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_DiaIns(Value))

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_DiaCable())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_DiaCable(Value))

    def DiaShield(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_DiaShield())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_DiaShield(Value))

    def TapeLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_TapeLayer())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_TapeLayer(Value))

    def TapeLap(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.TSData_Get_TapeLap())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.TSData_Set_TapeLap(Value))


_TSData = ITSData(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
EmergAmps = _TSData.EmergAmps
NormAmps = _TSData.NormAmps
Rdc = _TSData.Rdc
Rac = _TSData.Rac
GMRac = _TSData.GMRac
GMRUnits = _TSData.GMRUnits
Radius = _TSData.Radius
RadiusUnits = _TSData.RadiusUnits
ResistanceUnits = _TSData.ResistanceUnits
Diameter = _TSData.Diameter
EpsR = _TSData.EpsR
InsLayer = _TSData.InsLayer
DiaIns = _TSData.DiaIns
DiaCable = _TSData.DiaCable
DiaShield = _TSData.DiaShield
TapeLayer = _TSData.TapeLayer
TapeLap = _TSData.TapeLap
Idx = _TSData.Idx
First = _TSData.First
Next = _TSData.Next
AllNames = _TSData.AllNames
Count = _TSData.Count
Name = _TSData.Name
_columns = _TSData._columns
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
    "EpsR",
    "InsLayer",
    "DiaIns",
    "DiaCable",
    "DiaShield",
    "TapeLayer",
    "TapeLap",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
