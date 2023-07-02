from ._utils import codec, CheckForError, api_util, Iterable


class IReclosers(Iterable):
    __slots__ = []
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
    ]

    def Close(self):
        self.CheckForError(self._lib.Reclosers_Close())

    def Open(self):
        self.CheckForError(self._lib.Reclosers_Open())

    def GroundInst(self, *args):
        """Ground (3I0) instantaneous trip setting - curve multipler or actual amps."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_GroundInst())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_GroundInst(Value))

    def GroundTrip(self, *args):
        """Ground (3I0) trip multiplier or actual amps"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_GroundTrip())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_GroundTrip(Value))

    def MonitoredObj(self, *args):
        """Full name of object this Recloser to be monitored."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Reclosers_Get_MonitoredObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Reclosers_Set_MonitoredObj(Value))

    def MonitoredTerm(self, *args):
        """Terminal number of Monitored object for the Recloser"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_MonitoredTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_MonitoredTerm(Value))

    def NumFast(self, *args):
        """Number of fast shots"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_NumFast())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_NumFast(Value))

    def PhaseInst(self, *args):
        """Phase instantaneous curve multipler or actual amps"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_PhaseInst())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_PhaseInst(Value))

    def PhaseTrip(self, *args):
        """Phase trip curve multiplier or actual amps"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_PhaseTrip())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_PhaseTrip(Value))

    def RecloseIntervals(self):
        """(read-only) Array of Doubles: reclose intervals, s, between shots."""
        return self._get_float64_array(self._lib.Reclosers_Get_RecloseIntervals)

    def Shots(self, *args):
        """Number of shots to lockout (fast + delayed)"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_Shots())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_Shots(Value))

    def SwitchedObj(self, *args):
        """Full name of the circuit element that is being switched by the Recloser."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Reclosers_Get_SwitchedObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Reclosers_Set_SwitchedObj(Value))

    def SwitchedTerm(self, *args):
        """Terminal number of the controlled device being switched by the Recloser"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Reclosers_Get_SwitchedTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Reclosers_Set_SwitchedTerm(Value))


_Reclosers = IReclosers(api_util)

# For backwards compatibility, bind to the default instance
Close = _Reclosers.Close
Open = _Reclosers.Open
AllNames = _Reclosers.AllNames
Count = _Reclosers.Count
First = _Reclosers.First
GroundInst = _Reclosers.GroundInst
GroundTrip = _Reclosers.GroundTrip
MonitoredObj = _Reclosers.MonitoredObj
MonitoredTerm = _Reclosers.MonitoredTerm
Name = _Reclosers.Name
Next = _Reclosers.Next
NumFast = _Reclosers.NumFast
PhaseInst = _Reclosers.PhaseInst
PhaseTrip = _Reclosers.PhaseTrip
RecloseIntervals = _Reclosers.RecloseIntervals
Shots = _Reclosers.Shots
SwitchedObj = _Reclosers.SwitchedObj
SwitchedTerm = _Reclosers.SwitchedTerm
Idx = _Reclosers.Idx
_columns = _Reclosers._columns
__all__ = [
    "Close",
    "Open",
    "AllNames",
    "Count",
    "First",
    "GroundInst",
    "GroundTrip",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "NumFast",
    "PhaseInst",
    "PhaseTrip",
    "RecloseIntervals",
    "Shots",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
