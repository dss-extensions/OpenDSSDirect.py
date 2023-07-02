from ._utils import codec, CheckForError, api_util, Iterable


class ISensors(Iterable):
    __slots__ = []
    _api_prefix = "Sensors"
    _columns = [
        "Name",
        "Idx",
        "MeteredElement",
        "MeteredTerminal",
        "IsDelta",
        "ReverseDelta",
        "Currents",
        "PctError",
        "Weight",
        "kVBase",
        "kvar",
        "kVS",
        "kW",
    ]

    def Reset(self):
        self.CheckForError(self._lib.Sensors_Reset())

    def ResetAll(self):
        self.CheckForError(self._lib.Sensors_ResetAll())

    def Currents(self, *args):
        """Array of doubles for the line current measurements; don't use with kWS and kVARS."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Sensors_Get_Currents)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_Currents(ValuePtr, ValueCount))

    def IsDelta(self, *args):
        """True if measured voltages are line-line. Currents are always line currents."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_IsDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_IsDelta(Value))

    def MeteredElement(self, *args):
        """Full Name of the measured element"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Sensors_Get_MeteredElement())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Sensors_Set_MeteredElement(Value))

    def MeteredTerminal(self, *args):
        """Number of the measured terminal in the measured element."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_MeteredTerminal())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_MeteredTerminal(Value))

    def PctError(self, *args):
        """Assumed percent error in the Sensor measurement. Default is 1."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_PctError())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_PctError(Value))

    def ReverseDelta(self, *args):
        """True if voltage measurements are 1-3, 3-2, 2-1."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_ReverseDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_ReverseDelta(Value))

    def Weight(self, *args):
        """Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_Weight())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_Weight(Value))

    def kvar(self, *args):
        """Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Sensors_Get_kVARS)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVARS(ValuePtr, ValueCount))

    def kVS(self, *args):
        """Array of doubles for the LL or LN (depending on Delta connection) voltage measurements."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Sensors_Get_kVS)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVS(ValuePtr, ValueCount))

    def kVBase(self, *args):
        """Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Sensors_Get_kVbase())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Sensors_Set_kVbase(Value))

    def kW(self, *args):
        """Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Sensors_Get_kWS)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kWS(ValuePtr, ValueCount))


_Sensors = ISensors(api_util)

# For backwards compatibility, bind to the default instance
Reset = _Sensors.Reset
ResetAll = _Sensors.ResetAll
AllNames = _Sensors.AllNames
Count = _Sensors.Count
Currents = _Sensors.Currents
First = _Sensors.First
IsDelta = _Sensors.IsDelta
MeteredElement = _Sensors.MeteredElement
MeteredTerminal = _Sensors.MeteredTerminal
Name = _Sensors.Name
Next = _Sensors.Next
PctError = _Sensors.PctError
ReverseDelta = _Sensors.ReverseDelta
Weight = _Sensors.Weight
kvar = _Sensors.kvar
kVS = _Sensors.kVS
kVBase = _Sensors.kVBase
kW = _Sensors.kW
Idx = _Sensors.Idx
_columns = _Sensors._columns
__all__ = [
    "Reset",
    "ResetAll",
    "AllNames",
    "Count",
    "Currents",
    "First",
    "IsDelta",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "Next",
    "PctError",
    "ReverseDelta",
    "Weight",
    "kvar",
    "kVS",
    "kVBase",
    "kW",
    "Idx",
]
