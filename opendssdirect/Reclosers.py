from ._utils import api_util
from .Bases import Iterable
from dss import ActionCodes


class IReclosers(Iterable):
    __slots__ = []

    __name__ = "Reclosers"
    _api_prefix = "Reclosers"
    _columns = [
        "Name",
        "Idx",
        "GroundInst",
        "GroundTrip",
        "MonitoredObj",
        "MonitoredTerm",
        "SwitchedObj",
        "SwitchedTerm",
        "NumFast",
        "PhaseInst",
        "PhaseTrip",
        "RecloseIntervals",
        "Shots",
        "State",
        "NormalState",
    ]

    def Close(self):
        self._lib.Reclosers_Close()

    def Open(self):
        self._lib.Reclosers_Open()

    def GroundInst(self, *args):
        """
        Ground (3I0) instantaneous trip setting - curve multiplier or actual amps.

        Original COM help: https://opendss.epri.com/GroundInst.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_GroundInst()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_GroundInst(Value)

    def GroundTrip(self, *args):
        """
        Ground (3I0) trip multiplier or actual amps

        Original COM help: https://opendss.epri.com/GroundTrip.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_GroundTrip()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_GroundTrip(Value)

    def MonitoredObj(self, *args):
        """
        Full name of object this Recloser to be monitored.

        Original COM help: https://opendss.epri.com/MonitoredObj2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_MonitoredObj()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_MonitoredObj(Value)

    def MonitoredTerm(self, *args):
        """
        Terminal number of Monitored object for the Recloser

        Original COM help: https://opendss.epri.com/MonitoredTerm2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_MonitoredTerm()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_MonitoredTerm(Value)

    def NumFast(self, *args):
        """
        Number of fast shots

        Original COM help: https://opendss.epri.com/NumFast.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_NumFast()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_NumFast(Value)

    def PhaseInst(self, *args):
        """
        Phase instantaneous curve multiplier or actual amps

        Original COM help: https://opendss.epri.com/PhaseInst.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_PhaseInst()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_PhaseInst(Value)

    def PhaseTrip(self, *args):
        """
        Phase trip curve multiplier or actual amps

        Original COM help: https://opendss.epri.com/PhaseTrip.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_PhaseTrip()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_PhaseTrip(Value)

    def RecloseIntervals(self):
        """
        Array of Doubles: reclose intervals, s, between shots.

        Original COM help: https://opendss.epri.com/RecloseIntervals.html
        """
        return self._lib.Reclosers_Get_RecloseIntervals_GR()

    def Shots(self, *args):
        """
        Number of shots to lockout (fast + delayed)

        Original COM help: https://opendss.epri.com/Shots.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_Shots()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_Shots(Value)

    def SwitchedObj(self, *args):
        """
        Full name of the circuit element that is being switched by the Recloser.

        Original COM help: https://opendss.epri.com/SwitchedObj1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_SwitchedObj()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_SwitchedObj(Value)

    def SwitchedTerm(self, *args):
        """
        Terminal number of the controlled device being switched by the Recloser

        Original COM help: https://opendss.epri.com/SwitchedTerm1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_SwitchedTerm()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_SwitchedTerm(Value)

    def Reset(self):
        """
        Reset recloser to normal state.
        If open, lock out the recloser.
        If closed, resets recloser to first operation.
        """
        self._lib.Reclosers_Reset()

    def State(self, *args):
        """
        Present state of recloser.
        If set to open (ActionCodes.Open=1), open recloser's controlled element and lock out the recloser.
        If set to close (ActionCodes.Close=2), close recloser's controlled element and resets recloser to first operation.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_State()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_State(Value)

    def NormalState(self, *args):
        """
        Normal state (ActionCodes.Open=1, ActionCodes.Close=2) of the recloser.

        Original COM help: https://opendss.epri.com/NormalState1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Reclosers_Get_NormalState()

        # Setter
        (Value,) = args
        self._lib.Reclosers_Set_NormalState(Value)


_Reclosers = IReclosers(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Reclosers.AllNames
Close = _Reclosers.Close
Count = _Reclosers.Count
First = _Reclosers.First
GroundInst = _Reclosers.GroundInst
GroundTrip = _Reclosers.GroundTrip
Idx = _Reclosers.Idx
MonitoredObj = _Reclosers.MonitoredObj
MonitoredTerm = _Reclosers.MonitoredTerm
Name = _Reclosers.Name
Next = _Reclosers.Next
NormalState = _Reclosers.NormalState
NumFast = _Reclosers.NumFast
Open = _Reclosers.Open
PhaseInst = _Reclosers.PhaseInst
PhaseTrip = _Reclosers.PhaseTrip
RecloseIntervals = _Reclosers.RecloseIntervals
Reset = _Reclosers.Reset
Shots = _Reclosers.Shots
State = _Reclosers.State
SwitchedObj = _Reclosers.SwitchedObj
SwitchedTerm = _Reclosers.SwitchedTerm
_columns = _Reclosers._columns
__all__ = [
    "AllNames",
    "Close",
    "Count",
    "First",
    "GroundInst",
    "GroundTrip",
    "Idx",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NormalState",
    "NumFast",
    "Open",
    "PhaseInst",
    "PhaseTrip",
    "RecloseIntervals",
    "Reset",
    "Shots",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
]
