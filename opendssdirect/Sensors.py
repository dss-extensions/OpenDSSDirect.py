from ._utils import api_util
from .Bases import Iterable


class ISensors(Iterable):
    __slots__ = []

    __name__ = "Sensors"
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
        "AllocationFactor",
    ]

    def Reset(self):
        self._lib.Sensors_Reset()

    def ResetAll(self):
        self._lib.Sensors_ResetAll()

    def Currents(self, *args):
        """
        Array of doubles for the line current measurements; don't use with kWS and kVARS.

        Original COM help: https://opendss.epri.com/Currents2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_Currents_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Sensors_Set_Currents(ValuePtr, ValueCount)

    def IsDelta(self, *args):
        """
        True if measured voltages are line-line. Currents are always line currents.

        Original COM help: https://opendss.epri.com/IsDelta2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_IsDelta()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_IsDelta(Value)

    def MeteredElement(self, *args):
        """
        Full Name of the measured element

        Original COM help: https://opendss.epri.com/MeteredElement1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_MeteredElement()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_MeteredElement(Value)

    def MeteredTerminal(self, *args):
        """
        Number of the measured terminal in the measured element.

        Original COM help: https://opendss.epri.com/MeteredTerminal1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_MeteredTerminal()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_MeteredTerminal(Value)

    def PctError(self, *args):
        """
        Assumed percent error in the Sensor measurement. Default is 1.

        Original COM help: https://opendss.epri.com/PctError.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_PctError()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_PctError(Value)

    def ReverseDelta(self, *args):
        """
        True if voltage measurements are 1-3, 3-2, 2-1.

        Original COM help: https://opendss.epri.com/ReverseDelta.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_ReverseDelta()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_ReverseDelta(Value)

    def Weight(self, *args):
        """
        Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.

        Original COM help: https://opendss.epri.com/Weight.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_Weight()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_Weight(Value)

    def kvar(self, *args):
        """
        Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.

        Original COM help: https://opendss.epri.com/kVARS.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_kVARS_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Sensors_Set_kVARS(ValuePtr, ValueCount)

    def kVS(self, *args):
        """
        Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.

        Original COM help: https://opendss.epri.com/kVS.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_kVS_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Sensors_Set_kVS(ValuePtr, ValueCount)

    def kVBase(self, *args):
        """
        Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.

        Original COM help: https://opendss.epri.com/kVBase1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_kVbase()

        # Setter
        (Value,) = args
        self._lib.Sensors_Set_kVbase(Value)

    def kW(self, *args):
        """
        Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.

        Original COM help: https://opendss.epri.com/kWS.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Sensors_Get_kWS_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Sensors_Set_kWS(ValuePtr, ValueCount)

    def AllocationFactor(self):
        """
        Array of doubles for the allocation factors for each phase.

        Original COM help: https://opendss.epri.com/AllocationFactor1.html
        """
        return self._lib.Sensors_Get_AllocationFactor_GR()


_Sensors = ISensors(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Sensors.AllNames
AllocationFactor = _Sensors.AllocationFactor
Count = _Sensors.Count
Currents = _Sensors.Currents
First = _Sensors.First
Idx = _Sensors.Idx
IsDelta = _Sensors.IsDelta
MeteredElement = _Sensors.MeteredElement
MeteredTerminal = _Sensors.MeteredTerminal
Name = _Sensors.Name
Next = _Sensors.Next
PctError = _Sensors.PctError
Reset = _Sensors.Reset
ResetAll = _Sensors.ResetAll
ReverseDelta = _Sensors.ReverseDelta
Weight = _Sensors.Weight
kVBase = _Sensors.kVBase
kVS = _Sensors.kVS
kW = _Sensors.kW
kvar = _Sensors.kvar
_columns = _Sensors._columns
__all__ = [
    "AllNames",
    "AllocationFactor",
    "Count",
    "Currents",
    "First",
    "Idx",
    "IsDelta",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "Next",
    "PctError",
    "Reset",
    "ResetAll",
    "ReverseDelta",
    "Weight",
    "kVBase",
    "kVS",
    "kW",
    "kvar",
]
