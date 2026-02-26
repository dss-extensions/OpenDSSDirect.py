from ._utils import api_util
from .Bases import Iterable


class IWindGens(Iterable):
    """WindGen objects"""

    __slots__ = []
    __name__ = "WindGens"
    _api_prefix = "WindGens"
    _columns = [
        "Name",
        "Idx",
        "RegisterNames",
        "RegisterValues",
        "Ag",
        "Bus1",
        "Class",
        "Cp",
        "daily",
        "duty",
        "IsDelta",
        "kV",
        "kVA",
        "kvar",
        "kW",
        "Lamda",
        "N_WTG",
        "NPoles",
        "pd",
        "PF",
        "Phases",
        "PSS",
        "QFlag",
        "QMode",
        "QSS",
        "Rad",
        "RThev",
        "VCutIn",
        "VCutOut",
        "Vss",
        "WindSpeed",
        "XThev",
        "Yearly",
    ]

    def RegisterNames(self):
        """
        Array of WindGen energy meter register names

        See also the enum `GeneratorRegisters`.
        """
        return self._lib.WindGens_Get_RegisterNames()

    def RegisterValues(self):
        """Array of values in WindGen registers."""
        return self._lib.WindGens_Get_RegisterValues_GR()

    def kV(self, *args):
        """
        Nominal rated (1.0 per unit) voltage for the active WindGen, in kV.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_kV()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_kV(Value)

    def kvar(self, *args):
        """
        Base kvar for the active WindGen.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_kvar()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_kvar(Value)

    def kW(self, *args):
        """
        Total base kW for the active WindGen.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_kW()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_kW(Value)

    def PF(self, *args):
        """
        WindGen power factor. Power factor (pos. = producing vars).
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_PF()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_PF(Value)

    def kVA(self, *args):
        """
        KVA rating of the electrical machine in the WindGen.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_kVA()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_kVA(Value)

    def Ag(self, *args):
        """
        Gearbox ratio
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Ag()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Ag(Value)

    def Cp(self, *args):
        """
        Turbine performance coefficient.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Cp()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Cp(Value)

    def Lamda(self, *args):
        """
        Tip speed ratio
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Lamda()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Lamda(Value)

    def N_WTG(self, *args):
        """
        Number of WTG in aggregation
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_N_WTG()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_N_WTG(Value)

    def NPoles(self, *args):
        """
        Number of pole pairs of the induction generator
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_NPoles()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_NPoles(Value)

    def pd(self, *args):
        """
        Air density in kg/m3
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_pd()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_pd(Value)

    def PSS(self, *args):
        """
        Steady state output real power.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_PSS()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_PSS(Value)

    def QFlag(self, *args):
        """
        Non-zero values enable reactive power and voltage control in the dynamic model.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_QFlag()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_QFlag(Value)

    def QMode(self, *args):
        """
        Q control mode (0:Q, 1:PF, 2:VV).
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_QMode()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_QMode(Value)

    def QSS(self, *args):
        """
        Steady state output reactive power.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_QSS()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_QSS(Value)

    def Rad(self, *args):
        """
        Rotor radius in meters
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Rad()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Rad(Value)

    def RThev(self, *args):
        """
        Per unit Thevenin equivalent resistance (R).
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_RThev()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_RThev(Value)

    def VCutIn(self, *args):
        """
        Cut-in speed for the wind generator
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_VCutIn()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_VCutIn(Value)

    def VCutOut(self, *args):
        """
        Cut-out speed for the wind generator
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_VCutOut()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_VCutOut(Value)

    def Vss(self, *args):
        """
        Steady state voltage magnitude.
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Vss()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Vss(Value)

    def WindSpeed(self, *args):
        """
        Wind speed in m/s
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_WindSpeed()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_WindSpeed(Value)

    def XThev(self, *args):
        """
        Per unit Thevenin equivalent reactance (X).
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_XThev()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_XThev(Value)

    def Phases(self, *args):
        """
        Number of phases

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Phases()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Phases(Value)

    def daily(self, *args):
        """
        Name of the loadshape for daily wind speed

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_daily()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_daily(Value)

    def duty(self, *args):
        """
        Name of the loadshape for a duty cycle simulation.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_duty()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_duty(Value)

    def Yearly(self, *args):
        """
        Name of yearly loadshape

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Yearly()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Yearly(Value)

    def IsDelta(self, *args):
        """
        WindGen connection. True/1 if delta connection, False/0 if wye.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_IsDelta()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_IsDelta(Value)

    def Class(self, *args):
        """
        An arbitrary integer number representing the class of WindGen so that WindGen values may be segregated by class.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Class_()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Class_(Value)

    def Bus1(self, *args):
        """
        Bus to which the WindGen is connected. May include specific node specification.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._lib.WindGens_Get_Bus1()

        # Setter
        (Value,) = args
        self._lib.WindGens_Set_Bus1(Value)


_WindGens = IWindGens(api_util)

# For backwards compatibility, bind to the default instance
Ag = _WindGens.Ag
AllNames = _WindGens.AllNames
Bus1 = _WindGens.Bus1
Class = _WindGens.Class
Count = _WindGens.Count
Cp = _WindGens.Cp
First = _WindGens.First
Idx = _WindGens.Idx
IsDelta = _WindGens.IsDelta
Lamda = _WindGens.Lamda
NPoles = _WindGens.NPoles
N_WTG = _WindGens.N_WTG
Name = _WindGens.Name
Next = _WindGens.Next
PF = _WindGens.PF
PSS = _WindGens.PSS
Phases = _WindGens.Phases
QFlag = _WindGens.QFlag
QMode = _WindGens.QMode
QSS = _WindGens.QSS
RThev = _WindGens.RThev
Rad = _WindGens.Rad
RegisterNames = _WindGens.RegisterNames
RegisterValues = _WindGens.RegisterValues
VCutIn = _WindGens.VCutIn
VCutOut = _WindGens.VCutOut
Vss = _WindGens.Vss
WindSpeed = _WindGens.WindSpeed
XThev = _WindGens.XThev
Yearly = _WindGens.Yearly
daily = _WindGens.daily
duty = _WindGens.duty
kV = _WindGens.kV
kVA = _WindGens.kVA
kW = _WindGens.kW
kvar = _WindGens.kvar
pd = _WindGens.pd
_columns = _WindGens._columns
__all__ = [
    "Ag",
    "AllNames",
    "Bus1",
    "Class",
    "Count",
    "Cp",
    "First",
    "Idx",
    "IsDelta",
    "Lamda",
    "NPoles",
    "N_WTG",
    "Name",
    "Next",
    "PF",
    "PSS",
    "Phases",
    "QFlag",
    "QMode",
    "QSS",
    "RThev",
    "Rad",
    "RegisterNames",
    "RegisterValues",
    "VCutIn",
    "VCutOut",
    "Vss",
    "WindSpeed",
    "XThev",
    "Yearly",
    "daily",
    "duty",
    "kV",
    "kVA",
    "kW",
    "kvar",
    "pd",
]
