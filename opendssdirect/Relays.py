from ._utils import api_util, Iterable, OPENDSSDIRECT_PY_USE_NUMPY


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
        """Full name of object this Relay is monitoring."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Relays_Get_MonitoredObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Relays_Set_MonitoredObj(Value))

    def MonitoredTerm(self, *args):
        """Number of terminal of monitored element that this Relay is monitoring."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Relays_Get_MonitoredTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Relays_Set_MonitoredTerm(Value))

    def SwitchedObj(self, *args):
        """Full name of element that will be switched when relay trips."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Relays_Get_SwitchedObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Relays_Set_SwitchedObj(Value))

    def SwitchedTerm(self, *args):
        """Terminal number of the switched object that will be opened when the relay trips."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Relays_Get_SwitchedTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Relays_Set_SwitchedTerm(Value))

    def Open(self):
        """Open relay's controlled element and lock out the relay."""
        self.CheckForError(self._lib.Relays_Open())

    def Close(self):
        """Close the switched object controlled by the relay. Resets relay to first operation."""
        self.CheckForError(self._lib.Relays_Close())

    def Reset(self):
        """
        Reset relay to normal state.
        If open, lock out the relay.
        If closed, resets relay to first operation.
        """
        self.CheckForError(self._lib.Relays_Reset())

    def State(self, *args):
        """
        Get/Set present state of relay.
        If set to open, open relay's controlled element and lock out the relay.
        If set to close, close relay's controlled element and resets relay to first operation.
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Relays_Get_State())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Relays_Set_State(Value))

    def NormalState(self, *args):
        """Normal state of relay."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Relays_Get_NormalState())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Relays_Set_NormalState(Value))


_Relays = IRelays(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
AllNames = _Relays.AllNames
Count = _Relays.Count
First = _Relays.First
MonitoredObj = _Relays.MonitoredObj
MonitoredTerm = _Relays.MonitoredTerm
Name = _Relays.Name
Next = _Relays.Next
SwitchedObj = _Relays.SwitchedObj
SwitchedTerm = _Relays.SwitchedTerm
Idx = _Relays.Idx
Open = _Relays.Open
Close = _Relays.Close
Reset = _Relays.Reset
State = _Relays.State
NormalState = _Relays.NormalState
_columns = _Relays._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
    "Open",
    "Close",
    "Reset",
    "State",
    "NormalState",
]
