from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss_python_backend.enums import LineUnits

class ICNData(Iterable):
    """
    CNData objects

    (API Extension)
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
            return self._check_for_error(self._lib.CNData_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_EmergAmps(Value))

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_NormAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_NormAmps(Value))

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_Rdc())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_Rdc(Value))

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_Rac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_Rac(Value))

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_GMRac())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_GMRac(Value))

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.CNData_Get_GMRUnits()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_GMRUnits(Value))

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_Radius())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_Radius(Value))

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.CNData_Get_RadiusUnits()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_RadiusUnits(Value))

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return LineUnits(self._check_for_error(self._lib.CNData_Get_ResistanceUnits()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_ResistanceUnits(Value))

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_Diameter())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_Diameter(Value))

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_EpsR())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_EpsR(Value))

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_InsLayer())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_InsLayer(Value))

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_DiaIns())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_DiaIns(Value))

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_DiaCable())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_DiaCable(Value))

    def k(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_k())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_k(Value))

    def DiaStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_DiaStrand())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_DiaStrand(Value))

    def GmrStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_GmrStrand())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_GmrStrand(Value))

    def RStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CNData_Get_RStrand())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CNData_Set_RStrand(Value))


_CNData = ICNData(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
EmergAmps = _CNData.EmergAmps
NormAmps = _CNData.NormAmps
Rdc = _CNData.Rdc
Rac = _CNData.Rac
GMRac = _CNData.GMRac
GMRUnits = _CNData.GMRUnits
Radius = _CNData.Radius
RadiusUnits = _CNData.RadiusUnits
ResistanceUnits = _CNData.ResistanceUnits
Diameter = _CNData.Diameter
EpsR = _CNData.EpsR
InsLayer = _CNData.InsLayer
DiaIns = _CNData.DiaIns
DiaCable = _CNData.DiaCable
k = _CNData.k
DiaStrand = _CNData.DiaStrand
GmrStrand = _CNData.GmrStrand
RStrand = _CNData.RStrand
Idx = _CNData.Idx
First = _CNData.First
Next = _CNData.Next
AllNames = _CNData.AllNames
Count = _CNData.Count
Name = _CNData.Name
_columns = _CNData._columns
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
    "k",
    "DiaStrand",
    "GmrStrand",
    "RStrand",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
