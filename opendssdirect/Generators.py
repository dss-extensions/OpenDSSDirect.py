from ._utils import  api_util, Iterable


class IGenerators(Iterable):
    __slots__ = []
    __name__ = "Generators"
    _api_prefix = "Generators"
    _columns = [
        "Name",
        "Idx",
        "ForcedON",
        "Model",
        "Phases",
        "PF",
        "kVARated",
        "kV",
        "kW",
        "kvar",
        "Vminpu",
        "Vmaxpu",
        "RegisterNames",
        "RegisterValues",
        "Bus1",
        "Class",
        "kva",
        "IsDelta",
        "Status",
        "daily",
        "duty",
        "Yearly",
    ]

    def ForcedON(self, *args):
        """Indicates whether the generator is forced ON regardles of other dispatch criteria."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_ForcedON()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_ForcedON(Value))

    def Model(self, *args):
        """Generator Model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Model())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Model(Value))

    def PF(self, *args):
        """Power factor (pos. = producing vars). Updates kvar based on present kW value."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_PF())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_PF(Value))

    def Phases(self, *args):
        """Number of phases"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Phases())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Phases(Value))

    def RegisterNames(self):
        """(read-only) Array of Names of all generator energy meter registers"""
        return self.CheckForError(
            self._get_string_array(self._lib.Generators_Get_RegisterNames)
        )

    def RegisterValues(self):
        """(read-only) Array of valus in generator energy meter registers."""
        return self._get_float64_array(self._lib.Generators_Get_RegisterValues)

    def Vmaxpu(self, *args):
        """Vmaxpu for generator model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Vmaxpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Vmaxpu(Value))

    def Vminpu(self, *args):
        """Vminpu for Generator model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Vminpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Vminpu(Value))

    def kV(self, *args):
        """Voltage base for the active generator, kV"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kV(Value))

    def kVARated(self, *args):
        """kVA rating of the generator"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kVArated())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kVArated(Value))

    def kW(self, *args):
        """kW output for the active generator. kvar is updated for current power factor."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kW())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kW(Value))

    def kvar(self, *args):
        """kvar output for the active generator. Updates power factor based on present kW value."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kvar())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kvar(Value))

    def daily(self, *args):
        """
        Name of the loadshape for a daily generation profile.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Generators_Get_daily())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Generators_Set_daily(Value))

    def duty(self, *args):
        """
        Name of the loadshape for a duty cycle simulation.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Generators_Get_duty()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Generators_Set_duty(Value))

    def Yearly(self, *args):
        """
        Name of yearly loadshape

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Generators_Get_Yearly())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Generators_Set_Yearly(Value))

    def Status(self, *args):
        """
        Response to dispatch multipliers: Fixed=1 (dispatch multipliers do not apply), Variable=0 (follows curves).

        Related enumeration: GeneratorStatus

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Status())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Status(Value))

    def IsDelta(self, *args):
        """
        Generator connection. True/1 if delta connection, False/0 if wye.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_IsDelta()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_IsDelta(Value))

    def kva(self, *args):
        """
        kVA rating of electrical machine. Applied to machine or inverter definition for Dynamics mode solutions.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kva())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kva(Value))

    def Class(self, *args):
        """
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Class_())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Class_(Value))

    def Bus1(self, *args):
        """
        Bus to which the Generator is connected. May include specific node specification.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Generators_Get_Bus1()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Generators_Set_Bus1(Value))


_Generators = IGenerators(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Generators.AllNames
Count = _Generators.Count
First = _Generators.First
ForcedON = _Generators.ForcedON
Model = _Generators.Model
Name = _Generators.Name
Next = _Generators.Next
PF = _Generators.PF
Phases = _Generators.Phases
RegisterNames = _Generators.RegisterNames
RegisterValues = _Generators.RegisterValues
Vmaxpu = _Generators.Vmaxpu
Vminpu = _Generators.Vminpu
Idx = _Generators.Idx
kV = _Generators.kV
kVARated = _Generators.kVARated
kW = _Generators.kW
kvar = _Generators.kvar
daily = _Generators.daily
duty = _Generators.duty
Yearly = _Generators.Yearly
Status = _Generators.Status
IsDelta = _Generators.IsDelta
kva = _Generators.kva
Class = _Generators.Class
Bus1 = _Generators.Bus1
_columns = _Generators._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "ForcedON",
    "Model",
    "Name",
    "Next",
    "PF",
    "Phases",
    "RegisterNames",
    "RegisterValues",
    "Vmaxpu",
    "Vminpu",
    "Idx",
    "kV",
    "kVARated",
    "kW",
    "kvar",
    "daily",
    "duty",
    "Yearly",
    "Status",
    "IsDelta",
    "kva",
    "Class",
    "Bus1",
]
