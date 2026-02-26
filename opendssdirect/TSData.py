from ._utils import api_util
from .Bases import Iterable


class ITSData(Iterable):
    """
    TSData objects

    *Not available when using EPRI's OpenDSS distribution.*

    **(API Extension)**
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
            return self._lib.TSData_Get_EmergAmps()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_EmergAmps(Value)

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_NormAmps()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_NormAmps(Value)

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Rdc()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_Rdc(Value)

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Rac()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_Rac(Value)

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_GMRac()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_GMRac(Value)

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_GMRUnits()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_GMRUnits(Value)

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Radius()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_Radius(Value)

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_RadiusUnits()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_RadiusUnits(Value)

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_ResistanceUnits()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_ResistanceUnits(Value)

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Diameter()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_Diameter(Value)

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_EpsR()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_EpsR(Value)

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_InsLayer()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_InsLayer(Value)

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaIns()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_DiaIns(Value)

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaCable()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_DiaCable(Value)

    def DiaShield(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaShield()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_DiaShield(Value)

    def TapeLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_TapeLayer()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_TapeLayer(Value)

    def TapeLap(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_TapeLap()

        # Setter
        (Value,) = args
        self._lib.TSData_Set_TapeLap(Value)


_TSData = ITSData(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _TSData.AllNames
Count = _TSData.Count
DiaCable = _TSData.DiaCable
DiaIns = _TSData.DiaIns
DiaShield = _TSData.DiaShield
Diameter = _TSData.Diameter
EmergAmps = _TSData.EmergAmps
EpsR = _TSData.EpsR
First = _TSData.First
GMRUnits = _TSData.GMRUnits
GMRac = _TSData.GMRac
Idx = _TSData.Idx
InsLayer = _TSData.InsLayer
Name = _TSData.Name
Next = _TSData.Next
NormAmps = _TSData.NormAmps
Rac = _TSData.Rac
Radius = _TSData.Radius
RadiusUnits = _TSData.RadiusUnits
Rdc = _TSData.Rdc
ResistanceUnits = _TSData.ResistanceUnits
TapeLap = _TSData.TapeLap
TapeLayer = _TSData.TapeLayer
_columns = _TSData._columns
__all__ = [
    "AllNames",
    "Count",
    "DiaCable",
    "DiaIns",
    "DiaShield",
    "Diameter",
    "EmergAmps",
    "EpsR",
    "First",
    "GMRUnits",
    "GMRac",
    "Idx",
    "InsLayer",
    "Name",
    "Next",
    "NormAmps",
    "Rac",
    "Radius",
    "RadiusUnits",
    "Rdc",
    "ResistanceUnits",
    "TapeLap",
    "TapeLayer",
]
