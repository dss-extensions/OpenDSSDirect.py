from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable

class IGICSources(Iterable):
    __slots__ = []

    __name__ = "GICSources"
    _api_prefix = "GICSources"
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Bus1",
        "Bus2",
        "EN",
        "EE",
        "Lat1",
        "Lat2",
        "Lon1",
        "Lon2",
        "Volts",
    ]

    def Bus1(self):
        """First bus name of GICSource (Created name)"""
        return self._get_string(self._check_for_error(self._lib.GICSources_Get_Bus1()))

    def Bus2(self):
        """Second bus name"""
        return self._get_string(self._check_for_error(self._lib.GICSources_Get_Bus2()))

    def Phases(self, *args):
        """Number of Phases, this GICSource element."""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Phases())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Phases(Value))

    def EN(self, *args):
        """Northward E Field V/km"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_EN())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_EN(Value))

    def EE(self, *args):
        """Eastward E Field, V/km"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_EE())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_EE(Value))

    def Lat1(self, *args):
        """Latitude of Bus1 (degrees)"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Lat1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Lat1(Value))

    def Lat2(self, *args):
        """Latitude of Bus2 (degrees)"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Lat2())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Lat2(Value))

    def Lon1(self, *args):
        """Longitude of Bus1 (Degrees)"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Lon1())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Lon1(Value))

    def Lon2(self, *args):
        """Longitude of Bus2 (Degrees)"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Lon2())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Lon2(Value))

    def Volts(self, *args):
        """Specify dc voltage directly"""
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.GICSources_Get_Volts())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.GICSources_Set_Volts(Value))


_GICSources = IGICSources(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Bus1 = _GICSources.Bus1
Bus2 = _GICSources.Bus2
Phases = _GICSources.Phases
EN = _GICSources.EN
EE = _GICSources.EE
Lat1 = _GICSources.Lat1
Lat2 = _GICSources.Lat2
Lon1 = _GICSources.Lon1
Lon2 = _GICSources.Lon2
Volts = _GICSources.Volts
Idx = _GICSources.Idx
First = _GICSources.First
Next = _GICSources.Next
AllNames = _GICSources.AllNames
Count = _GICSources.Count
Name = _GICSources.Name
_columns = _GICSources._columns
__all__ = [
    "Bus1",
    "Bus2",
    "Phases",
    "EN",
    "EE",
    "Lat1",
    "Lat2",
    "Lon1",
    "Lon2",
    "Volts",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
