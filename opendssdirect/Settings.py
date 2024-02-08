from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base
from dss.enums import DSSPropertyNameStyle, CktModels

class ISettings(Base):
    __slots__ = []

    __name__ = "Settings"
    _api_prefix = "Settings"
    _columns = [
        "Trapezoidal",
        "LossRegs",
        "VoltageBases",
        "ZoneLock",
        "EmergVminpu",
        "PriceSignal",
        "CktModel",
        "UERegs",
        "UEWeight",
        "PriceCurve",
        "NormVminpu",
        "LossWeight",
        "EmergVmaxpu",
        "AutoBusList",
        "NormVmaxpu",
        "AllowDuplicates",
        "ControlTrace",
        "LoadsTerminalCheck",
        "IterateDisabled",
    ]

    def AllowDuplicates(self, *args):
        """
        {True | False*} Designates whether to allow duplicate names of objects

        **NOTE**: for DSS-Extensions, we are considering removing this option in a future
        release since it has performance impacts even when not used.
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_AllowDuplicates()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_AllowDuplicates(Value))

    def AutoBusList(self, *args):
        """
        List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.

        Original COM help: https://opendss.epri.com/AutoBusList.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Settings_Get_AutoBusList())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Settings_Set_AutoBusList(Value))

    def CktModel(self, *args):
        """
        Indicate if the circuit model is positive sequence.

        Original COM help: https://opendss.epri.com/CktModel.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(CktModels(self._lib.Settings_Get_CktModel()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_CktModel(Value))

    def ControlTrace(self, *args):
        """
        Denotes whether to trace the control actions to a file.

        Original COM help: https://opendss.epri.com/ControlTrace.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_ControlTrace()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_ControlTrace(Value))

    def EmergVmaxpu(self, *args):
        """
        Per Unit maximum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVmaxpu.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_EmergVmaxpu())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_EmergVmaxpu(Value))

    def EmergVminpu(self, *args):
        """
        Per Unit minimum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVminpu.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_EmergVminpu())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_EmergVminpu(Value))

    def LossRegs(self, *args):
        """
        Integer array defining which energy meter registers to use for computing losses

        Original COM help: https://opendss.epri.com/LossRegs.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Settings_Get_LossRegs_GR())
            return self._get_int32_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount))

    def LossWeight(self, *args):
        """
        Weighting factor applied to Loss register values.

        Original COM help: https://opendss.epri.com/LossWeight.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_LossWeight())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_LossWeight(Value))

    def NormVmaxpu(self, *args):
        """
        Per Unit maximum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVmaxpu.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_NormVmaxpu())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_NormVmaxpu(Value))

    def NormVminpu(self, *args):
        """
        Per Unit minimum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVminpu.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_NormVminpu())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_NormVminpu(Value))

    def PriceCurve(self, *args):
        """
        Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

        Original COM help: https://opendss.epri.com/PriceCurve.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Settings_Get_PriceCurve())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Settings_Set_PriceCurve(Value))

    def PriceSignal(self, *args):
        """
        Price Signal for the Circuit

        Original COM help: https://opendss.epri.com/PriceSignal.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_PriceSignal())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_PriceSignal(Value))

    def Trapezoidal(self, *args):
        """
        Gets value of trapezoidal integration flag in energy meters. Defaults to `False`.

        Original COM help: https://opendss.epri.com/Trapezoidal.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_Trapezoidal()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_Trapezoidal(Value))

    def UERegs(self, *args):
        """
        Array of Integers defining energy meter registers to use for computing UE

        Original COM help: https://opendss.epri.com/UEregs.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Settings_Get_UEregs_GR())
            return self._get_int32_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Settings_Set_UEregs(ValuePtr, ValueCount))

    def UEWeight(self, *args):
        """
        Weighting factor applied to UE register values.

        Original COM help: https://opendss.epri.com/UEweight.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_UEweight())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_UEweight(Value))

    def VoltageBases(self, *args):
        """
        Array of doubles defining the legal voltage bases in kV L-L

        Original COM help: https://opendss.epri.com/VoltageBases.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Settings_Get_VoltageBases_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount))

    def ZoneLock(self, *args):
        """
        Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.

        Original COM help: https://opendss.epri.com/ZoneLock.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_ZoneLock()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_ZoneLock(Value))

    def AllocationFactors(self, Value):
        """(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value."""
        self._check_for_error(self._lib.Settings_Set_AllocationFactors(Value))

    def LoadsTerminalCheck(self, *args):
        """
        Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
        If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_LoadsTerminalCheck()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_LoadsTerminalCheck(Value))

    def IterateDisabled(self, *args):
        """
        Controls whether `First`/`Next` iteration includes or skips disabled circuit elements.
        The default behavior from OpenDSS is to skip those. The user can still activate the element by name or index.

        The default value for IterateDisabled is 0, keeping the original behavior.
        Set it to 1 (or `True`) to include disabled elements.
        Other numeric values are reserved for other potential behaviors.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Settings_Get_IterateDisabled())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Settings_Set_IterateDisabled(Value))

    def SetPropertyNameStyle(self, value):
        """Switch the property names according"""
        self._check_for_error(self._lib.Settings_SetPropertyNameStyle(value))


_Settings = ISettings(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
AllowDuplicates = _Settings.AllowDuplicates
AutoBusList = _Settings.AutoBusList
CktModel = _Settings.CktModel
ControlTrace = _Settings.ControlTrace
EmergVmaxpu = _Settings.EmergVmaxpu
EmergVminpu = _Settings.EmergVminpu
LossRegs = _Settings.LossRegs
LossWeight = _Settings.LossWeight
NormVmaxpu = _Settings.NormVmaxpu
NormVminpu = _Settings.NormVminpu
PriceCurve = _Settings.PriceCurve
PriceSignal = _Settings.PriceSignal
Trapezoidal = _Settings.Trapezoidal
UERegs = _Settings.UERegs
UEWeight = _Settings.UEWeight
VoltageBases = _Settings.VoltageBases
ZoneLock = _Settings.ZoneLock
AllocationFactors = _Settings.AllocationFactors
LoadsTerminalCheck = _Settings.LoadsTerminalCheck
IterateDisabled = _Settings.IterateDisabled
SetPropertyNameStyle = _Settings.SetPropertyNameStyle
_columns = _Settings._columns
__all__ = [
    "AllowDuplicates",
    "AutoBusList",
    "CktModel",
    "ControlTrace",
    "EmergVmaxpu",
    "EmergVminpu",
    "LossRegs",
    "LossWeight",
    "NormVmaxpu",
    "NormVminpu",
    "PriceCurve",
    "PriceSignal",
    "Trapezoidal",
    "UERegs",
    "UEWeight",
    "VoltageBases",
    "ZoneLock",
    "AllocationFactors",
    "LoadsTerminalCheck",
    "IterateDisabled",
    "SetPropertyNameStyle",
]
