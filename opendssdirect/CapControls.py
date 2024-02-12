from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss_python_backend.enums import CapControlModes

class ICapControls(Iterable):
    __slots__ = []

    __name__ = "CapControls"
    _api_prefix = "CapControls"
    _columns = [
        "Name",
        "Idx",
        "Capacitor",
        "CTRatio",
        "PTRatio",
        "DeadTime",
        "Delay",
        "DelayOff",
        "Vmin",
        "Vmax",
        "UseVoltOverride",
        "Mode",
        "MonitoredObj",
        "MonitoredTerm",
        "OFFSetting",
        "ONSetting",
    ]

    def Reset(self):
        """
        Force a reset of this CapControl.

        Original COM help: https://opendss.epri.com/Reset.html
        """
        self._check_for_error(self._lib.CapControls_Reset())

    def CTRatio(self, *args):
        """
        Transducer ratio from primary current to control current.

        Original COM help: https://opendss.epri.com/CTratio.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_CTratio())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_CTratio(Value))

    def Capacitor(self, *args):
        """
        Name of the Capacitor that is controlled.

        Original COM help: https://opendss.epri.com/Capacitor.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.CapControls_Get_Capacitor())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.CapControls_Set_Capacitor(Value))

    def DeadTime(self, *args):
        """
        Dead time after capacitor is turned OFF before it can be turned back ON for the active CapControl.

        Default is 300 sec.

        Original COM help: https://opendss.epri.com/DeadTime.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_DeadTime())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_DeadTime(Value))

    def Delay(self, *args):
        """
        Time delay [s] to switch on after arming.  Control may reset before actually switching.

        Original COM help: https://opendss.epri.com/Delay.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_Delay())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_Delay(Value))

    def DelayOff(self, *args):
        """
        Time delay [s] before switching off a step. Control may reset before actually switching.

        Original COM help: https://opendss.epri.com/DelayOff.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_DelayOff())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_DelayOff(Value))

    def Mode(self, *args):
        """
        Type of automatic controller.

        Original COM help: https://opendss.epri.com/Mode.html
        """
        # Getter
        if len(args) == 0:
            return CapControlModes(self._check_for_error(self._lib.CapControls_Get_Mode()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_Mode(Value))

    def MonitoredObj(self, *args):
        """
        Full name of the element that PT and CT are connected to.

        Original COM help: https://opendss.epri.com/MonitoredObj.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.CapControls_Get_MonitoredObj())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.CapControls_Set_MonitoredObj(Value))

    def MonitoredTerm(self, *args):
        """
        Terminal number on the element that PT and CT are connected to.

        Original COM help: https://opendss.epri.com/MonitoredTerm.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_MonitoredTerm())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_MonitoredTerm(Value))

    def OFFSetting(self, *args):
        """
        Threshold to switch off a step. See Mode for units.

        Original COM help: https://opendss.epri.com/OFFSetting.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_OFFSetting())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_OFFSetting(Value))

    def ONSetting(self, *args):
        """
        Threshold to arm or switch on a step.  See Mode for units.

        Original COM help: https://opendss.epri.com/ONSetting.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_ONSetting())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_ONSetting(Value))

    def PTRatio(self, *args):
        """
        Transducer ratio from primary feeder to control voltage.

        Original COM help: https://opendss.epri.com/PTratio.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_PTratio())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_PTratio(Value))

    def UseVoltOverride(self, *args):
        """
        Enables Vmin and Vmax to override the control Mode

        Original COM help: https://opendss.epri.com/UseVoltOverride.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_UseVoltOverride()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_UseVoltOverride(Value))

    def Vmax(self, *args):
        """
        With VoltOverride, swtich off whenever PT voltage exceeds this level.

        Original COM help: https://opendss.epri.com/Vmax.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_Vmax())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_Vmax(Value))

    def Vmin(self, *args):
        """
        With VoltOverride, switch ON whenever PT voltage drops below this level.

        Original COM help: https://opendss.epri.com/Vmin.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CapControls_Get_Vmin())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CapControls_Set_Vmin(Value))


_CapControls = ICapControls(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Reset = _CapControls.Reset
AllNames = _CapControls.AllNames
CTRatio = _CapControls.CTRatio
Capacitor = _CapControls.Capacitor
Count = _CapControls.Count
DeadTime = _CapControls.DeadTime
Delay = _CapControls.Delay
DelayOff = _CapControls.DelayOff
First = _CapControls.First
Mode = _CapControls.Mode
MonitoredObj = _CapControls.MonitoredObj
MonitoredTerm = _CapControls.MonitoredTerm
Name = _CapControls.Name
Next = _CapControls.Next
OFFSetting = _CapControls.OFFSetting
ONSetting = _CapControls.ONSetting
PTRatio = _CapControls.PTRatio
UseVoltOverride = _CapControls.UseVoltOverride
Vmax = _CapControls.Vmax
Vmin = _CapControls.Vmin
Idx = _CapControls.Idx
_columns = _CapControls._columns
__all__ = [
    "Reset",
    "AllNames",
    "CTRatio",
    "Capacitor",
    "Count",
    "DeadTime",
    "Delay",
    "DelayOff",
    "First",
    "Mode",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "OFFSetting",
    "ONSetting",
    "PTRatio",
    "UseVoltOverride",
    "Vmax",
    "Vmin",
    "Idx",
]
