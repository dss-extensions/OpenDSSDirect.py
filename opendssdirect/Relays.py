from ._utils import api_util
from .Bases import Iterable


class IRelays(Iterable):
    __slots__ = []

    __name__ = "Relays"
    _api_prefix = "Relays"
    _columns = [
        "Name",
        "Idx",
        "MonitoredObj",
        "MonitoredTerm",
        "SwitchedObj",
        "SwitchedTerm",
        "State",
        "NormalState",
    ]

    def MonitoredObj(self, *args):
        """
        Full name of object this Relay is monitoring.

        Original COM help: https://opendss.epri.com/MonitoredObj3.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_MonitoredObj()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_MonitoredObj(Value)

    def MonitoredTerm(self, *args):
        """
        Number of terminal of monitored element that this Relay is monitoring.

        Original COM help: https://opendss.epri.com/MonitoredTerm3.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_MonitoredTerm()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_MonitoredTerm(Value)

    def SwitchedObj(self, *args):
        """
        Full name of element that will be switched when relay trips.

        Original COM help: https://opendss.epri.com/SwitchedObj2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_SwitchedObj()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_SwitchedObj(Value)

    def SwitchedTerm(self, *args):
        """
        Terminal number of the switched object that will be opened when the relay trips.

        Original COM help: https://opendss.epri.com/SwitchedTerm2.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_SwitchedTerm()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_SwitchedTerm(Value)

    def Open(self):
        """
        Open relay's controlled element and lock out the relay.

        Original COM help: https://opendss.epri.com/Open4.html
        """
        self._lib.Relays_Open()

    def Close(self):
        """
        Close the switched object controlled by the relay. Resets relay to first operation.

        Original COM help: https://opendss.epri.com/Close5.html
        """
        self._lib.Relays_Close()

    def Reset(self):
        """
        Reset relay to normal state.
        If open, lock out the relay.
        If closed, resets relay to first operation.
        """
        self._lib.Relays_Reset()

    def State(self, *args):
        """
        Present state of relay.
        If set to open, open relay's controlled element and lock out the relay.
        If set to close, close relay's controlled element and resets relay to first operation.
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_State()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_State(Value)

    def NormalState(self, *args):
        """
        Normal state of relay.

        Original COM help: https://opendss.epri.com/NormalState3.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_NormalState()

        # Setter
        (Value,) = args
        self._lib.Relays_Set_NormalState(Value)


_Relays = IRelays(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Relays.AllNames
Close = _Relays.Close
Count = _Relays.Count
First = _Relays.First
Idx = _Relays.Idx
MonitoredObj = _Relays.MonitoredObj
MonitoredTerm = _Relays.MonitoredTerm
Name = _Relays.Name
Next = _Relays.Next
NormalState = _Relays.NormalState
Open = _Relays.Open
Reset = _Relays.Reset
State = _Relays.State
SwitchedObj = _Relays.SwitchedObj
SwitchedTerm = _Relays.SwitchedTerm
_columns = _Relays._columns
__all__ = [
    "AllNames",
    "Close",
    "Count",
    "First",
    "Idx",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NormalState",
    "Open",
    "Reset",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
]
