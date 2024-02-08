from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


class IPVsystems(Iterable):
    __slots__ = []

    __name__ = "PVsystems"
    _api_prefix = "PVSystems"
    _columns = [
        "Name",
        "Idx",
        "pf",
        "Irradiance",
        "IrradianceNow",
        "Pmpp",
        "RegisterNames",
        "RegisterValues",
        "kVARated",
        "kW",
        "kvar",
        "daily",
        "duty",
        "yearly",
        "Tdaily",
        "Tduty",
        "Tyearly",
        "Sensor",
    ]

    def Irradiance(self, *args):
        """
        Get/set the present value of the Irradiance property in kW/m²

        Original COM help: https://opendss.epri.com/Irradiance.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.PVSystems_Get_Irradiance())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.PVSystems_Set_Irradiance(Value))

    def pf(self, *args):
        """
        Get/set the power factor for the active PVSystem

        Original COM help: https://opendss.epri.com/PF2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.PVSystems_Get_PF())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.PVSystems_Set_PF(Value))

    def RegisterNames(self):
        """
        Array of PVSystem energy meter register names

        See also the enum `GeneratorRegisters`.

        Original COM help: https://opendss.epri.com/RegisterNames2.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.PVSystems_Get_RegisterNames)
        )

    def RegisterValues(self):
        """
        Array of doubles containing values in PVSystem registers.

        Original COM help: https://opendss.epri.com/RegisterValues2.html
        """
        self._check_for_error(self._lib.PVSystems_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    def kVARated(self, *args):
        """
        Get/set Rated kVA of the PVSystem

        Original COM help: https://opendss.epri.com/kVArated1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.PVSystems_Get_kVArated())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.PVSystems_Set_kVArated(Value))

    def kW(self):
        """
        Get kW output

        Original COM help: https://opendss.epri.com/kW2.html
        """
        return self._check_for_error(self._lib.PVSystems_Get_kW())

    def kvar(self, *args):
        """
        Get/set kvar output value

        Original COM help: https://opendss.epri.com/kvar2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.PVSystems_Get_kvar())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.PVSystems_Set_kvar(Value))

    def daily(self, *args):
        """
        Name of the dispatch shape to use for daily simulations. Must be previously
        defined as a Loadshape object of 24 hrs, typically. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.PVSystems_Get_daily()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_daily(Value))

    def duty(self, *args):
        """
        Name of the load shape to use for duty cycle dispatch simulations such as
        for solar ramp rate studies. Must be previously defined as a Loadshape
        object. Typically would have time intervals of 1-5 seconds.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.PVSystems_Get_duty()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_duty(Value))

    def yearly(self, *args):
        """
        Dispatch shape to use for yearly simulations. Must be previously defined
        as a Loadshape object. If this is not specified, the Daily dispatch shape,
        if any, is repeated during Yearly solution modes. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.PVSystems_Get_yearly())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_yearly(Value))

    def Tdaily(self, *args):
        """
        Temperature shape to use for daily simulations. Must be previously defined
        as a TShape object of 24 hrs, typically. The PVSystem element uses this
        TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
        with the Pmpp vs T curve.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.PVSystems_Get_Tdaily())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_Tdaily(Value))

    def Tduty(self, *args):
        """
        Temperature shape to use for duty cycle dispatch simulations such as for
        solar ramp rate studies. Must be previously defined as a TShape object.
        Typically would have time intervals of 1-5 seconds. Designate the number
        of points to solve using the Set Number=xxxx command. If there are fewer
        points in the actual shape, the shape is assumed to repeat. The PVSystem
        model uses this TShape to determine the Pmpp from the Pmpp vs T curve.
        Units must agree with the Pmpp vs T curve.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Tduty()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_Tduty(Value))

    def Tyearly(self, *args):
        """
        Temperature shape to use for yearly simulations. Must be previously defined
        as a TShape object. If this is not specified, the Daily dispatch shape, if
        any, is repeated during Yearly solution modes. The PVSystem element uses
        this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
        agree with the Pmpp vs T curve.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.PVSystems_Get_Tyearly())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.PVSystems_Set_Tyearly(Value))

    def IrradianceNow(self):
        """
        Returns the current irradiance value for the active PVSystem. Use it to
        know what's the current irradiance value for the PV during a simulation.

        Original COM help: https://opendss.epri.com/IrradianceNow.html
        """
        return self._check_for_error(self._lib.PVSystems_Get_IrradianceNow())

    def Pmpp(self, *args):
        """
        Gets/sets the rated max power of the PV array for 1.0 kW/m² irradiance
        and a user-selected array temperature of the active PVSystem.

        Original COM help: https://opendss.epri.com/Pmpp.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.PVSystems_Get_Pmpp())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.PVSystems_Set_Pmpp(Value))

    def Sensor(self):
        """
        Name of the sensor monitoring this element.

        Original COM help: https://opendss.epri.com/Sensor1.html
        """
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Sensor()))


_PVsystems = IPVsystems(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
AllNames = _PVsystems.AllNames
Count = _PVsystems.Count
First = _PVsystems.First
Irradiance = _PVsystems.Irradiance
Name = _PVsystems.Name
Next = _PVsystems.Next
pf = _PVsystems.pf
RegisterNames = _PVsystems.RegisterNames
RegisterValues = _PVsystems.RegisterValues
Idx = _PVsystems.Idx
kVARated = _PVsystems.kVARated
kW = _PVsystems.kW
kvar = _PVsystems.kvar
daily = _PVsystems.daily
duty = _PVsystems.duty
yearly = _PVsystems.yearly
Tdaily = _PVsystems.Tdaily
Tduty = _PVsystems.Tduty
Tyearly = _PVsystems.Tyearly
IrradianceNow = _PVsystems.IrradianceNow
Pmpp = _PVsystems.Pmpp
Sensor = _PVsystems.Sensor
_columns = _PVsystems._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "Irradiance",
    "Name",
    "Next",
    "pf",
    "RegisterNames",
    "RegisterValues",
    "Idx",
    "kVARated",
    "kW",
    "kvar",
    "daily",
    "duty",
    "yearly",
    "Tdaily",
    "Tduty",
    "Tyearly",
    "IrradianceNow",
    "Pmpp",
    "Sensor",
]
