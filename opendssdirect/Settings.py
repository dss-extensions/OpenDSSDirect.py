from ._utils import codec, CheckForError, api_util, Base


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
        """{True | False*} Designates whether to allow duplicate names of objects"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_AllowDuplicates()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_AllowDuplicates(Value))

    def AutoBusList(self, *args):
        """List of Buses or (File=xxxx) syntax for the AutoAdd solution mode."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Settings_Get_AutoBusList())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Settings_Set_AutoBusList(Value))

    def CktModel(self, *args):
        """{dssMultiphase (0) * | dssPositiveSeq (1) } IIndicate if the circuit model is positive sequence."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_CktModel())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_CktModel(Value))

    def ControlTrace(self, *args):
        """{True | False*} Denotes whether to trace the control actions to a file."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_ControlTrace()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_ControlTrace(Value))

    def EmergVmaxpu(self, *args):
        """Per Unit maximum voltage for Emergency conditions."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_EmergVmaxpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_EmergVmaxpu(Value))

    def EmergVminpu(self, *args):
        """Per Unit minimum voltage for Emergency conditions."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_EmergVminpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_EmergVminpu(Value))

    def LossRegs(self, *args):
        """Integer array defining which energy meter registers to use for computing losses"""
        # Getter
        if len(args) == 0:
            return self._get_int32_array(self._lib.Settings_Get_LossRegs)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount))

    def LossWeight(self, *args):
        """Weighting factor applied to Loss register values."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_LossWeight())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_LossWeight(Value))

    def NormVmaxpu(self, *args):
        """Per Unit maximum voltage for Normal conditions."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_NormVmaxpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_NormVmaxpu(Value))

    def NormVminpu(self, *args):
        """Per Unit minimum voltage for Normal conditions."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_NormVminpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_NormVminpu(Value))

    def PriceCurve(self, *args):
        """Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Settings_Get_PriceCurve())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Settings_Set_PriceCurve(Value))

    def PriceSignal(self, *args):
        """Price Signal for the Circuit"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_PriceSignal())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_PriceSignal(Value))

    def Trapezoidal(self, *args):
        """{True | False *} Gets value of trapezoidal integration flag in energy meters."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_Trapezoidal()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_Trapezoidal(Value))

    def UERegs(self, *args):
        """Array of Integers defining energy meter registers to use for computing UE"""
        # Getter
        if len(args) == 0:
            return self._get_int32_array(self._lib.Settings_Get_UEregs)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.Settings_Set_UEregs(ValuePtr, ValueCount))

    def UEWeight(self, *args):
        """Weighting factor applied to UE register values."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_UEweight())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_UEweight(Value))

    def VoltageBases(self, *args):
        """Array of doubles defining the legal voltage bases in kV L-L"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Settings_Get_VoltageBases)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount))

    def ZoneLock(self, *args):
        """{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_ZoneLock()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_ZoneLock(Value))

    def AllocationFactors(self, Value):
        """(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value."""
        self.CheckForError(self._lib.Settings_Set_AllocationFactors(Value))

    def LoadsTerminalCheck(self, *args):
        """
        Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
        If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_LoadsTerminalCheck()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_LoadsTerminalCheck(Value))

    def IterateDisabled(self, *args):
        """
        Controls whether `First`/`Next` iteration includes or skips disabled circuit elements.
        The default behavior from OpenDSS is to skip those. The user can still activate the element by name or index.

        The default value for IterateDisabled is 0, keeping the original behavior.
        Set it to 1 (or `True`) to include disabled elements.
        Other numeric values are reserved for other potential behaviors.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Settings_Get_IterateDisabled())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Settings_Set_IterateDisabled(int(Value)))


_Settings = ISettings(api_util)

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
]
