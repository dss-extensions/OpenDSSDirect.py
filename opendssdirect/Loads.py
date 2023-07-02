from ._utils import codec, CheckForError, api_util, Iterable


class ILoads(Iterable):
    __slots__ = []
    _api_prefix = "Loads"
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Class",
        "Model",
        "NumCust",
        "IsDelta",
        "Rneut",
        "Xneut",
        "PF",
        "ZipV",
        "CVRCurve",
        "CVRvars",
        "CVRwatts",
        "CFactor",
        "Growth",
        "Daily",
        "Duty",
        "Yearly",
        "PctMean",
        "PctStdDev",
        "RelWeighting",
        "Spectrum",
        "Status",
        "VminNorm",
        "VminEmerg",
        "Vminpu",
        "Vmaxpu",
        "kV",
        "kW",
        "kVABase",
        "kvar",
        "kWh",
        "kWhDays",
        "AllocationFactor",
        "XfkVA",
        "puSeriesRL",
    ]

    def AllocationFactor(self, *args):
        """Factor for allocating loads by connected xfkva"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_AllocationFactor())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_AllocationFactor(Value))

    def CVRCurve(self, *args):
        """Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_CVRcurve()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_CVRcurve(Value))

    def CVRvars(self, *args):
        """Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_CVRvars())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_CVRvars(Value))

    def CVRwatts(self, *args):
        """Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_CVRwatts())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_CVRwatts(Value))

    def CFactor(self, *args):
        """Factor relates average to peak kw.  Used for allocation with kwh and kwhdays"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Cfactor())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Cfactor(Value))

    def Class(self, *args):
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Class_())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Class_(Value))

    def Growth(self, *args):
        """Name of the growthshape curve for yearly load growth factors."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_Growth()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_Growth(Value))

    def IsDelta(self, *args):
        """Delta loads are connected line-to-line."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_IsDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_IsDelta(Value))

    def Model(self, *args):
        """The Load Model defines variation of P and Q with voltage."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Model())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Model(Value))

    def NumCust(self, *args):
        """Number of customers in this load, defaults to one."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_NumCust())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_NumCust(Value))

    def PF(self, *args):
        """Get or set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_PF())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_PF(Value))

    def PctMean(self, *args):
        """Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_PctMean())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_PctMean(Value))

    def PctStdDev(self, *args):
        """Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_PctStdDev())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_PctStdDev(Value))

    def RelWeighting(self, *args):
        """Relative Weighting factor for the active LOAD"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_RelWeight())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_RelWeight(Value))

    def Rneut(self, *args):
        """Neutral resistance for wye-connected loads."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Rneut())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Rneut(Value))

    def Spectrum(self, *args):
        """Name of harmonic current spectrrum shape."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_Spectrum()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_Spectrum(Value))

    def Status(self, *args):
        """Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all)."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Status())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Status(Value))

    def Vmaxpu(self, *args):
        """Maximum per-unit voltage to use the load model. Above this, constant Z applies."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Vmaxpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Vmaxpu(Value))

    def VminEmerg(self, *args):
        """Minimum voltage for unserved energy (UE) evaluation."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Vminemerg())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Vminemerg(Value))

    def VminNorm(self, *args):
        """Minimum voltage for energy exceeding normal (EEN) evaluations."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Vminnorm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Vminnorm(Value))

    def Vminpu(self, *args):
        """Minimum voltage to apply the load model. Below this, constant Z is used."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Vminpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Vminpu(Value))

    def Xneut(self, *args):
        """Neutral reactance for wye-connected loads."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Xneut())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Xneut(Value))

    def Yearly(self, *args):
        """Name of yearly duration loadshape"""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_Yearly()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_Yearly(Value))

    def ZipV(self, *args):
        """Array of 7 doubles with values for ZIPV property of the load object"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Loads_Get_ZIPV)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Loads_Set_ZIPV(ValuePtr, ValueCount))

    def Daily(self, *args):
        """Name of the loadshape for a daily load profile."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_daily()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_daily(Value))

    def Duty(self, *args):
        """Name of the loadshape for a duty cycle simulation."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Loads_Get_duty()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Loads_Set_duty(Value))

    def kV(self, *args):
        """Set kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kV(Value))

    def kW(self, *args):
        """Set kW for active Load. Updates kvar based on present PF."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kW())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kW(Value))

    def kVABase(self, *args):
        """Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kva())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kva(Value))

    def kvar(self, *args):
        """Get/set kvar for active Load. If set, updates PF based on present kW."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kvar())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kvar(Value))

    def kWh(self, *args):
        """kwh billed for this period. Can be used with Cfactor for load allocation."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kwh())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kwh(Value))

    def kWhDays(self, *args):
        """Length of kwh billing period for average demand calculation. Default 30."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_kwhdays())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_kwhdays(Value))

    def puSeriesRL(self, *args):
        """Percent of Load that is modeled as series R-L for harmonics studies"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_pctSeriesRL())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_pctSeriesRL(Value))

    def XfkVA(self, *args):
        """Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_xfkVA())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_xfkVA(Value))

    def Phases(self, *args):
        """Number of phases"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Loads_Get_Phases())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Loads_Set_Phases(Value))


_Loads = ILoads(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Loads.AllNames
AllocationFactor = _Loads.AllocationFactor
CVRCurve = _Loads.CVRCurve
CVRvars = _Loads.CVRvars
CVRwatts = _Loads.CVRwatts
CFactor = _Loads.CFactor
Class = _Loads.Class
Count = _Loads.Count
First = _Loads.First
Growth = _Loads.Growth
IsDelta = _Loads.IsDelta
Model = _Loads.Model
Name = _Loads.Name
Next = _Loads.Next
NumCust = _Loads.NumCust
PF = _Loads.PF
PctMean = _Loads.PctMean
PctStdDev = _Loads.PctStdDev
RelWeighting = _Loads.RelWeighting
Rneut = _Loads.Rneut
Spectrum = _Loads.Spectrum
Status = _Loads.Status
Vmaxpu = _Loads.Vmaxpu
VminEmerg = _Loads.VminEmerg
VminNorm = _Loads.VminNorm
Vminpu = _Loads.Vminpu
Xneut = _Loads.Xneut
Yearly = _Loads.Yearly
ZipV = _Loads.ZipV
Daily = _Loads.Daily
Duty = _Loads.Duty
Idx = _Loads.Idx
kV = _Loads.kV
kW = _Loads.kW
kVABase = _Loads.kVABase
kvar = _Loads.kvar
kWh = _Loads.kWh
kWhDays = _Loads.kWhDays
puSeriesRL = _Loads.puSeriesRL
XfkVA = _Loads.XfkVA
Phases = _Loads.Phases
_columns = _Loads._columns
__all__ = [
    "AllNames",
    "AllocationFactor",
    "CVRCurve",
    "CVRvars",
    "CVRwatts",
    "CFactor",
    "Class",
    "Count",
    "First",
    "Growth",
    "IsDelta",
    "Model",
    "Name",
    "Next",
    "NumCust",
    "PF",
    "PctMean",
    "PctStdDev",
    "RelWeighting",
    "Rneut",
    "Spectrum",
    "Status",
    "Vmaxpu",
    "VminEmerg",
    "VminNorm",
    "Vminpu",
    "Xneut",
    "Yearly",
    "ZipV",
    "Daily",
    "Duty",
    "Idx",
    "kV",
    "kW",
    "kVABase",
    "kvar",
    "kWh",
    "kWhDays",
    "puSeriesRL",
    "XfkVA",
    "Phases",
]
