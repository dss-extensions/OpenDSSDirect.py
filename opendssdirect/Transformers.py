from ._utils import codec, CheckForError, api_util, Iterable


class ITransformers(Iterable):
    __slots__ = []
    _api_prefix = "Transformers"
    _columns = [
        "Name",
        "Idx",
        "XfmrCode",
        "IsDelta",
        "CoreType",
        "NumWindings",
        "Wdg",
        "NumTaps",
        "MinTap",
        "MaxTap",
        "Tap",
        "kV",
        "kVA",
        "R",
        "Xhl",
        "Xht",
        "Xlt",
        "Rneut",
        "Xneut",
        "RdcOhms",
        "WdgCurrents",
        "WdgVoltages",
        "LossesByType",
    ]

    def IsDelta(self, *args):
        """Active Winding delta or wye connection?"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_IsDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_IsDelta(Value))

    def MaxTap(self, *args):
        """Active Winding maximum tap in per-unit."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_MaxTap())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_MaxTap(Value))

    def MinTap(self, *args):
        """Active Winding minimum tap in per-unit."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_MinTap())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_MinTap(Value))

    def NumTaps(self, *args):
        """Active Winding number of tap steps betwein MinTap and MaxTap."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_NumTaps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_NumTaps(Value))

    def NumWindings(self, *args):
        """Number of windings on this transformer. Allocates memory; set or change this property first."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_NumWindings())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_NumWindings(Value))

    def R(self, *args):
        """Active Winding resistance in %"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_R())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_R(Value))

    def Rneut(self, *args):
        """Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Rneut())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Rneut(Value))

    def Tap(self, *args):
        """Active Winding tap in per-unit."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Tap())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Tap(Value))

    def Wdg(self, *args):
        """Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Wdg())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Wdg(Value))

    def XfmrCode(self, *args):
        """Name of an XfrmCode that supplies electircal parameters for this Transformer."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Transformers_Get_XfmrCode())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Transformers_Set_XfmrCode(Value))

    def Xhl(self, *args):
        """Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Xhl())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Xhl(Value))

    def Xht(self, *args):
        """Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Xht())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Xht(Value))

    def Xlt(self, *args):
        """Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Xlt())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Xlt(Value))

    def Xneut(self, *args):
        """Active Winding neutral reactance [ohms] for wye connections."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_Xneut())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_Xneut(Value))

    def kV(self, *args):
        """Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_kV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_kV(Value))

    def kVA(self, *args):
        """Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_kVA())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_kVA(Value))

    def WdgVoltages(self):
        """
        (read-only) Complex array of voltages for active winding

        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        """
        return self._get_float64_array(self._lib.Transformers_Get_WdgVoltages)

    def WdgCurrents(self):
        """
        (read-only) All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)

        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        """
        return self._get_float64_array(self._lib.Transformers_Get_WdgCurrents)

    def strWdgCurrents(self):
        """
        (read-only) All winding currents in CSV string form like the WdgCurrents property

        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        """
        return self._get_string(
            self.CheckForError(self._lib.Transformers_Get_strWdgCurrents())
        )

    def CoreType(self, *args):
        """Transformer Core Type: 0=shell;1 = 1-phase; 3= 3-leg; 5= 5-leg"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_CoreType())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_CoreType(Value))

    def RdcOhms(self, *args):
        """dc Resistance of active winding in ohms for GIC analysis"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Transformers_Get_RdcOhms())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Transformers_Set_RdcOhms(Value))

    def LossesByType(self):
        """Complex array with the losses by type (total losses, load losses, no-load losses), in VA"""
        return self._get_float64_array(self._lib.Transformers_Get_LossesByType)

    def AllLossesByType(self):
        """Complex array with the losses by type (total losses, load losses, no-load losses), in VA, concatenated for ALL transformers"""
        return self._get_float64_array(self._lib.Transformers_Get_AllLossesByType)


_Transformers = ITransformers(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Transformers.AllNames
Count = _Transformers.Count
First = _Transformers.First
IsDelta = _Transformers.IsDelta
MaxTap = _Transformers.MaxTap
MinTap = _Transformers.MinTap
Name = _Transformers.Name
Next = _Transformers.Next
NumTaps = _Transformers.NumTaps
NumWindings = _Transformers.NumWindings
R = _Transformers.R
Rneut = _Transformers.Rneut
Tap = _Transformers.Tap
Wdg = _Transformers.Wdg
XfmrCode = _Transformers.XfmrCode
Xhl = _Transformers.Xhl
Xht = _Transformers.Xht
Xlt = _Transformers.Xlt
Xneut = _Transformers.Xneut
kV = _Transformers.kV
kVA = _Transformers.kVA
WdgVoltages = _Transformers.WdgVoltages
WdgCurrents = _Transformers.WdgCurrents
strWdgCurrents = _Transformers.strWdgCurrents
CoreType = _Transformers.CoreType
RdcOhms = _Transformers.RdcOhms
LossesByType = _Transformers.LossesByType
AllLossesByType = _Transformers.AllLossesByType
Idx = _Transformers.Idx
_columns = _Transformers._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "IsDelta",
    "MaxTap",
    "MinTap",
    "Name",
    "Next",
    "NumTaps",
    "NumWindings",
    "R",
    "Rneut",
    "Tap",
    "Wdg",
    "XfmrCode",
    "Xhl",
    "Xht",
    "Xlt",
    "Xneut",
    "kV",
    "kVA",
    "WdgVoltages",
    "WdgCurrents",
    "strWdgCurrents",
    "CoreType",
    "RdcOhms",
    "LossesByType",
    "AllLossesByType",
    "Idx",
]
