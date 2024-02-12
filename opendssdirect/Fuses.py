from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


class IFuses(Iterable):
    __slots__ = []

    __name__ = "Fuses"
    _api_prefix = "Fuses"
    _columns = [
        "Name",
        "Idx",
        "NumPhases",
        "MonitoredObj",
        "MonitoredTerm",
        "Delay",
        "IsBlown",
        "TCCCurve",
        "RatedCurrent",
        "SwitchedObj",
        "SwitchedTerm",
        "State",
        "NormalState",
    ]

    def Close(self):
        """
        Close all phases of the fuse.

        Original COM help: https://opendss.epri.com/Close3.html
        """
        self._check_for_error(self._lib.Fuses_Close())

    def IsBlown(self):
        """
        Current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE.

        Original COM help: https://opendss.epri.com/IsBlown.html
        """
        return self._check_for_error(self._lib.Fuses_IsBlown()) != 0

    def Open(self):
        """
        Manual opening of all phases of the fuse.

        Original COM help: https://opendss.epri.com/Open2.html
        """
        self._check_for_error(self._lib.Fuses_Open())

    def Reset(self):
        """
        Reset fuse to normal state.

        Original COM help: https://opendss.epri.com/Reset7.html
        """
        self._check_for_error(self._lib.Fuses_Reset())

    def Delay(self, *args):
        """
        A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        This represents a fuse clear or other delay.

        Original COM help: https://opendss.epri.com/Delay1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Fuses_Get_Delay())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Fuses_Set_Delay(Value))

    def MonitoredObj(self, *args):
        """
        Full name of the circuit element to which the fuse is connected.

        Original COM help: https://opendss.epri.com/MonitoredObj1.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Fuses_Get_MonitoredObj())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Fuses_Set_MonitoredObj(Value))

    def MonitoredTerm(self, *args):
        """
        Terminal number to which the fuse is connected.

        Original COM help: https://opendss.epri.com/MonitoredTerm1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Fuses_Get_MonitoredTerm())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Fuses_Set_MonitoredTerm(Value))

    def NumPhases(self):
        """
        Number of phases, this fuse.

        Original COM help: https://opendss.epri.com/NumPhases1.html
        """
        return self._check_for_error(self._lib.Fuses_Get_NumPhases())

    def RatedCurrent(self, *args):
        """
        Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.

        Multiply current values of TCC curve by this to get actual amps.

        Original COM help: https://opendss.epri.com/RatedCurrent.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Fuses_Get_RatedCurrent())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Fuses_Set_RatedCurrent(Value))

    def SwitchedObj(self, *args):
        """
        Full name of the circuit element switch that the fuse controls.
        Defaults to the MonitoredObj.

        Original COM help: https://opendss.epri.com/SwitchedObj.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Fuses_Get_SwitchedObj())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Fuses_Set_SwitchedObj(Value))

    def SwitchedTerm(self, *args):
        """
        Number of the terminal of the controlled element containing the switch controlled by the fuse.

        Original COM help: https://opendss.epri.com/SwitchedTerm.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Fuses_Get_SwitchedTerm())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Fuses_Set_SwitchedTerm(Value))

    def TCCCurve(self, *args):
        """
        Name of the TCCcurve object that determines fuse blowing.

        Original COM help: https://opendss.epri.com/TCCcurve.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Fuses_Get_TCCcurve()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Fuses_Set_TCCcurve(Value))

    def State(self, *args):
        """
        Array of strings indicating the state of each phase of the fuse.

        Original COM help: https://opendss.epri.com/State2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._get_string_array(self._lib.Fuses_Get_State))

        # Setter
        (Value,) = args
        self._check_for_error(self._set_string_array(self._lib.Fuses_Set_State, Value))

    def NormalState(self, *args):
        """
        Array of strings indicating the normal state of each phase of the fuse.

        Original COM help: https://opendss.epri.com/NormalState2.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(
                self._get_string_array(self._lib.Fuses_Get_NormalState)
            )

        # Setter
        (Value,) = args
        self._check_for_error(
            self._set_string_array(self._lib.Fuses_Set_NormalState, Value)
        )


_Fuses = IFuses(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Close = _Fuses.Close
IsBlown = _Fuses.IsBlown
Open = _Fuses.Open
AllNames = _Fuses.AllNames
Count = _Fuses.Count
Delay = _Fuses.Delay
First = _Fuses.First
MonitoredObj = _Fuses.MonitoredObj
MonitoredTerm = _Fuses.MonitoredTerm
Name = _Fuses.Name
Next = _Fuses.Next
NumPhases = _Fuses.NumPhases
RatedCurrent = _Fuses.RatedCurrent
SwitchedObj = _Fuses.SwitchedObj
SwitchedTerm = _Fuses.SwitchedTerm
TCCCurve = _Fuses.TCCCurve
Idx = _Fuses.Idx
Reset = _Fuses.Reset
State = _Fuses.State
NormalState = _Fuses.NormalState
_columns = _Fuses._columns
__all__ = [
    "Close",
    "IsBlown",
    "Open",
    "AllNames",
    "Count",
    "Delay",
    "First",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NumPhases",
    "RatedCurrent",
    "SwitchedObj",
    "SwitchedTerm",
    "TCCCurve",
    "Idx",
    "Reset",
    "State",
    "NormalState",
]
