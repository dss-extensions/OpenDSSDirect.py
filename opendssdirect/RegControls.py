from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


class IRegControls(Iterable):
    __slots__ = []

    __name__ = "RegControls"
    _api_prefix = "RegControls"
    _columns = [
        "Name",
        "Idx",
        "Transformer",
        "Winding",
        "MonitoredBus",
        "CTPrimary",
        "PTRatio",
        "Delay",
        "IsInverseTime",
        "IsReversible",
        "MaxTapChange",
        "TapDelay",
        "TapNumber",
        "TapWinding",
        "VoltageLimit",
        "ForwardBand",
        "ForwardR",
        "ForwardX",
        "ForwardVreg",
        "ReverseBand",
        "ReverseR",
        "ReverseX",
        "ReverseVreg",
    ]

    def Reset(self):
        self._check_for_error(self._lib.RegControls_Reset())

    def CTPrimary(self, *args):
        """
        CT primary ampere rating (secondary is 0.2 amperes)

        Original COM help: https://opendss.epri.com/CTPrimary.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_CTPrimary())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_CTPrimary(Value))

    def Delay(self, *args):
        """
        Time delay [s] after arming before the first tap change. Control may reset before actually changing taps.

        Original COM help: https://opendss.epri.com/Delay2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_Delay())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_Delay(Value))

    def ForwardBand(self, *args):
        """
        Regulation bandwidth in forward direction, centered on Vreg

        Original COM help: https://opendss.epri.com/ForwardBand.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ForwardBand())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ForwardBand(Value))

    def ForwardR(self, *args):
        """
        LDC R setting in Volts

        Original COM help: https://opendss.epri.com/ForwardR.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ForwardR())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ForwardR(Value))

    def ForwardVreg(self, *args):
        """
        Target voltage in the forward direction, on PT secondary base.

        Original COM help: https://opendss.epri.com/ForwardVreg.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ForwardVreg())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ForwardVreg(Value))

    def ForwardX(self, *args):
        """
        LDC X setting in Volts

        Original COM help: https://opendss.epri.com/ForwardX.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ForwardX())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ForwardX(Value))

    def IsInverseTime(self, *args):
        """
        Time delay is inversely adjusted, proportional to the amount of voltage outside the regulating band.

        Original COM help: https://opendss.epri.com/IsInverseTime.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_IsInverseTime()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_IsInverseTime(Value))

    def IsReversible(self, *args):
        """
        Regulator can use different settings in the reverse direction.  Usually not applicable to substation transformers.

        Original COM help: https://opendss.epri.com/IsReversible.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_IsReversible()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_IsReversible(Value))

    def MaxTapChange(self, *args):
        """
        Maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for a faster solution.

        Original COM help: https://opendss.epri.com/MaxTapChange.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_MaxTapChange())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_MaxTapChange(Value))

    def MonitoredBus(self, *args):
        """
        Name of a remote regulated bus, in lieu of LDC settings

        Original COM help: https://opendss.epri.com/MonitoredBus.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.RegControls_Get_MonitoredBus())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.RegControls_Set_MonitoredBus(Value))

    def PTRatio(self, *args):
        """
        PT ratio for voltage control settings

        Original COM help: https://opendss.epri.com/PTratio1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_PTratio())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_PTratio(Value))

    def ReverseBand(self, *args):
        """
        Bandwidth in reverse direction, centered on reverse Vreg.

        Original COM help: https://opendss.epri.com/ReverseBand.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ReverseBand())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ReverseBand(Value))

    def ReverseR(self, *args):
        """
        Reverse LDC R setting in Volts.

        Original COM help: https://opendss.epri.com/ReverseR.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ReverseR())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ReverseR(Value))

    def ReverseVreg(self, *args):
        """
        Target voltage in the revese direction, on PT secondary base.

        Original COM help: https://opendss.epri.com/ReverseVreg.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ReverseVreg())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ReverseVreg(Value))

    def ReverseX(self, *args):
        """
        Reverse LDC X setting in volts.

        Original COM help: https://opendss.epri.com/ReverseX.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_ReverseX())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_ReverseX(Value))

    def TapDelay(self, *args):
        """
        Time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.

        Original COM help: https://opendss.epri.com/TapDelay.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_TapDelay())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_TapDelay(Value))

    def TapNumber(self, *args):
        """
        Integer number of the tap that the controlled transformer winding is currently on.

        Original COM help: https://opendss.epri.com/TapNumber.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_TapNumber())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_TapNumber(Value))

    def TapWinding(self, *args):
        """
        Tapped winding number

        Original COM help: https://opendss.epri.com/TapWinding.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_TapWinding())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_TapWinding(Value))

    def Transformer(self, *args):
        """
        Name of the transformer this regulator controls

        Original COM help: https://opendss.epri.com/Transformer.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.RegControls_Get_Transformer())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.RegControls_Set_Transformer(Value))

    def VoltageLimit(self, *args):
        """
        First house voltage limit on PT secondary base.  Setting to 0 disables this function.

        Original COM help: https://opendss.epri.com/VoltageLimit.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_VoltageLimit())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_VoltageLimit(Value))

    def Winding(self, *args):
        """
        Winding number for PT and CT connections

        Original COM help: https://opendss.epri.com/Winding.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.RegControls_Get_Winding())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.RegControls_Set_Winding(Value))


_RegControls = IRegControls(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Reset = _RegControls.Reset
AllNames = _RegControls.AllNames
CTPrimary = _RegControls.CTPrimary
Count = _RegControls.Count
Delay = _RegControls.Delay
First = _RegControls.First
ForwardBand = _RegControls.ForwardBand
ForwardR = _RegControls.ForwardR
ForwardVreg = _RegControls.ForwardVreg
ForwardX = _RegControls.ForwardX
IsInverseTime = _RegControls.IsInverseTime
IsReversible = _RegControls.IsReversible
MaxTapChange = _RegControls.MaxTapChange
MonitoredBus = _RegControls.MonitoredBus
Name = _RegControls.Name
Next = _RegControls.Next
PTRatio = _RegControls.PTRatio
ReverseBand = _RegControls.ReverseBand
ReverseR = _RegControls.ReverseR
ReverseVreg = _RegControls.ReverseVreg
ReverseX = _RegControls.ReverseX
TapDelay = _RegControls.TapDelay
TapNumber = _RegControls.TapNumber
TapWinding = _RegControls.TapWinding
Transformer = _RegControls.Transformer
VoltageLimit = _RegControls.VoltageLimit
Winding = _RegControls.Winding
Idx = _RegControls.Idx
_columns = _RegControls._columns
__all__ = [
    "Reset",
    "AllNames",
    "CTPrimary",
    "Count",
    "Delay",
    "First",
    "ForwardBand",
    "ForwardR",
    "ForwardVreg",
    "ForwardX",
    "IsInverseTime",
    "IsReversible",
    "MaxTapChange",
    "MonitoredBus",
    "Name",
    "Next",
    "PTRatio",
    "ReverseBand",
    "ReverseR",
    "ReverseVreg",
    "ReverseX",
    "TapDelay",
    "TapNumber",
    "TapWinding",
    "Transformer",
    "VoltageLimit",
    "Winding",
    "Idx",
]
