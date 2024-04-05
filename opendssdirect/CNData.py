from ._utils import api_util
from .Bases import Iterable
from dss_python_backend.enums import LineUnits

class ICNData(Iterable):
    """
    CNData objects

    *Not available when using EPRI's OpenDSS distribution.*

    **(API Extension)**
    """

    __name__ = "CNData"
    _api_prefix = "CNData"
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
        "EpsR",
        "InsLayer",
        "DiaIns",
        "DiaCable",
        "DiaStrand",
        "RStrand",
        "k",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_EmergAmps()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_EmergAmps(Value)

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_NormAmps()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_NormAmps(Value)

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Rdc()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_Rdc(Value)

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Rac()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_Rac(Value)

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_GMRac()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_GMRac(Value)

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.CNData_Get_GMRUnits())

        # Setter
        (Value,) = args
        self._lib.CNData_Set_GMRUnits(Value)

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Radius()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_Radius(Value)

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.CNData_Get_RadiusUnits())

        # Setter
        (Value,) = args
        self._lib.CNData_Set_RadiusUnits(Value)

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._lib.CNData_Get_ResistanceUnits())

        # Setter
        (Value,) = args
        self._lib.CNData_Set_ResistanceUnits(Value)

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Diameter()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_Diameter(Value)

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_EpsR()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_EpsR(Value)

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_InsLayer()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_InsLayer(Value)

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaIns()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_DiaIns(Value)

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaCable()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_DiaCable(Value)

    def k(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_k()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_k(Value)

    def DiaStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaStrand()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_DiaStrand(Value)

    def GmrStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_GmrStrand()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_GmrStrand(Value)

    def RStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_RStrand()

        # Setter
        (Value,) = args
        self._lib.CNData_Set_RStrand(Value)


_CNData = ICNData(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _CNData.AllNames
Count = _CNData.Count
DiaCable = _CNData.DiaCable
DiaIns = _CNData.DiaIns
DiaStrand = _CNData.DiaStrand
Diameter = _CNData.Diameter
EmergAmps = _CNData.EmergAmps
EpsR = _CNData.EpsR
First = _CNData.First
GMRUnits = _CNData.GMRUnits
GMRac = _CNData.GMRac
GmrStrand = _CNData.GmrStrand
Idx = _CNData.Idx
InsLayer = _CNData.InsLayer
Name = _CNData.Name
Next = _CNData.Next
NormAmps = _CNData.NormAmps
RStrand = _CNData.RStrand
Rac = _CNData.Rac
Radius = _CNData.Radius
RadiusUnits = _CNData.RadiusUnits
Rdc = _CNData.Rdc
ResistanceUnits = _CNData.ResistanceUnits
k = _CNData.k
_columns = _CNData._columns
__all__ = [
    "AllNames",
    "Count",
    "DiaCable",
    "DiaIns",
    "DiaStrand",
    "Diameter",
    "EmergAmps",
    "EpsR",
    "First",
    "GMRUnits",
    "GMRac",
    "GmrStrand",
    "Idx",
    "InsLayer",
    "Name",
    "Next",
    "NormAmps",
    "RStrand",
    "Rac",
    "Radius",
    "RadiusUnits",
    "Rdc",
    "ResistanceUnits",
    "k",
]
