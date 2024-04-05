from ._utils import api_util
from .Bases import Iterable
from dss_python_backend.enums import StorageStates

class IStorages(Iterable):
    """Storage objects"""

    __name__ = "Storages"
    _api_prefix = "Storages"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "RegisterNames",
        "RegisterValues",
        "puSOC",
        "State",
        "AmpLimit",
        "AmpLimitGain",
        "ChargeTrigger",
        "ControlMode",
        "DischargeTrigger",
        "EffCharge",
        "EffDischarge",
        "Kp",
        "kV",
        "kVA",
        "kvar",
        "kVDC",
        "kW",
        "kWhRated",
        "kWRated",
        "LimitCurrent",
        "PF",
        "PITol",
        "SafeMode",
        "SafeVoltage",
        "TimeChargeTrig",
        "VarFollowInverter",
    ]

    def puSOC(self, *args):
        """Per unit state of charge"""
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_puSOC()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_puSOC(Value)

    def State(self, *args):
        """
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;
        """
        # Getter
        if len(args) == 0:
            return StorageStates(self._lib.Storages_Get_State())

        # Setter
        (Value,) = args
        self._lib.Storages_Set_State(Value)

    def RegisterNames(self):
        """
        Array of Storage energy meter register names

        See also the enum `GeneratorRegisters`.
        """
        return self._lib.Storages_Get_RegisterNames()

    def RegisterValues(self):
        """Array of values in Storage registers."""
        return self._lib.Storages_Get_RegisterValues_GR()

    def AmpLimit(self, *args):
        """
        Current limit per phase for the IBR when operating in GFM mode.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_AmpLimit()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_AmpLimit(Value)

    def AmpLimitGain(self, *args):
        """
        Use it for fine tuning the current limiter when active.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_AmpLimitGain()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_AmpLimitGain(Value)

    def ChargeTrigger(self, *args):
        """
        Dispatch trigger value for charging the Storage.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_ChargeTrigger()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_ChargeTrigger(Value)

    def ControlMode(self, *args):
        """
        Control mode for the inverter. It can be one of {GFM = 1 | GFL* = 0}.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_ControlMode()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_ControlMode(Value)

    def DischargeTrigger(self, *args):
        """
        Dispatch trigger value for discharging the Storage.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_DischargeTrigger()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_DischargeTrigger(Value)

    def EffCharge(self, *args):
        """
        Percentage efficiency for CHARGING the Storage element.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_EffCharge()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_EffCharge(Value)

    def EffDischarge(self, *args):
        """
        Percentage efficiency for DISCHARGING the Storage element.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_EffDischarge()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_EffDischarge(Value)

    def Kp(self, *args):
        """
        Proportional gain for the PI controller within the inverter.
        Use it to modify the controller response in dynamics simulation mode.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_Kp()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_Kp(Value)

    def kV(self, *args):
        """
        Nominal rated (1.0 per unit) voltage, kV, for Storage element.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kV()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kV(Value)

    def kVA(self, *args):
        """
        Inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kVA()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kVA(Value)

    def kvar(self, *args):
        """
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kvar()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kvar(Value)

    def kVDC(self, *args):
        """
        Rated voltage (kV) at the input of the inverter while the storage is discharging
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kVDC()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kVDC(Value)

    def kW(self, *args):
        """
        Get/set the requested kW value. Final kW is subjected to the inverter ratings.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kW()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kW(Value)

    def kWhRated(self, *args):
        """
        Rated Storage capacity in kWh.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kWhRated()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kWhRated(Value)

    def kWRated(self, *args):
        """
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_kWRated()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_kWRated(Value)

    def LimitCurrent(self, *args):
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7.
        For 3-phase, limits the positive-sequence current but not the negative-sequence."
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_LimitCurrent()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_LimitCurrent(Value)

    def PF(self, *args):
        """
        Get/set the requested PF value.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_PF()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_PF(Value)

    def PITol(self, *args):
        """
        Tolerance (%) for the closed loop controller of the inverter
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_PITol()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_PITol(Value)

    def SafeMode(self):
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.
        """
        return self._lib.Storages_Get_SafeMode()

    def SafeVoltage(self, *args):
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_SafeVoltage()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_SafeVoltage(Value)

    def TimeChargeTrig(self, *args):
        """
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_TimeChargeTrig()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_TimeChargeTrig(Value)

    def VarFollowInverter(self, *args):
        """
        Indicates if the reactive power generation/absorption does not respect the inverter status
        """
        # Getter
        if len(args) == 0:
            return self._lib.Storages_Get_VarFollowInverter()

        # Setter
        (Value,) = args
        self._lib.Storages_Set_VarFollowInverter(Value)


_Storages = IStorages(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Storages.AllNames
AmpLimit = _Storages.AmpLimit
AmpLimitGain = _Storages.AmpLimitGain
ChargeTrigger = _Storages.ChargeTrigger
ControlMode = _Storages.ControlMode
Count = _Storages.Count
DischargeTrigger = _Storages.DischargeTrigger
EffCharge = _Storages.EffCharge
EffDischarge = _Storages.EffDischarge
First = _Storages.First
Idx = _Storages.Idx
Kp = _Storages.Kp
LimitCurrent = _Storages.LimitCurrent
Name = _Storages.Name
Next = _Storages.Next
PF = _Storages.PF
PITol = _Storages.PITol
RegisterNames = _Storages.RegisterNames
RegisterValues = _Storages.RegisterValues
SafeMode = _Storages.SafeMode
SafeVoltage = _Storages.SafeVoltage
State = _Storages.State
TimeChargeTrig = _Storages.TimeChargeTrig
VarFollowInverter = _Storages.VarFollowInverter
kV = _Storages.kV
kVA = _Storages.kVA
kVDC = _Storages.kVDC
kW = _Storages.kW
kWRated = _Storages.kWRated
kWhRated = _Storages.kWhRated
kvar = _Storages.kvar
puSOC = _Storages.puSOC
_columns = _Storages._columns
__all__ = [
    "AllNames",
    "AmpLimit",
    "AmpLimitGain",
    "ChargeTrigger",
    "ControlMode",
    "Count",
    "DischargeTrigger",
    "EffCharge",
    "EffDischarge",
    "First",
    "Idx",
    "Kp",
    "LimitCurrent",
    "Name",
    "Next",
    "PF",
    "PITol",
    "RegisterNames",
    "RegisterValues",
    "SafeMode",
    "SafeVoltage",
    "State",
    "TimeChargeTrig",
    "VarFollowInverter",
    "kV",
    "kVA",
    "kVDC",
    "kW",
    "kWRated",
    "kWhRated",
    "kvar",
    "puSOC",
]
