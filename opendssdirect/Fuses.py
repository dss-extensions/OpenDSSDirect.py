from ._utils import  api_util, Iterable


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
    ]

    def Close(self):
        self.CheckForError(self._lib.Fuses_Close())

    def IsBlown(self):
        return self.CheckForError(self._lib.Fuses_IsBlown()) != 0

    def Open(self):
        self.CheckForError(self._lib.Fuses_Open())

    def Delay(self, *args):
        """
        A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        This represents a fuse clear or other delay.
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Fuses_Get_Delay())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Fuses_Set_Delay(Value))

    def MonitoredObj(self, *args):
        """Full name of the circuit element to which the fuse is connected."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Fuses_Get_MonitoredObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Fuses_Set_MonitoredObj(Value))

    def MonitoredTerm(self, *args):
        """Terminal number to which the fuse is connected."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Fuses_Get_MonitoredTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Fuses_Set_MonitoredTerm(Value))

    def NumPhases(self):
        """(read-only) Number of phases, this fuse."""
        return self.CheckForError(self._lib.Fuses_Get_NumPhases())

    def RatedCurrent(self, *args):
        """
        Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.
        Multiply current values of TCC curve by this to get actual amps.
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Fuses_Get_RatedCurrent())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Fuses_Set_RatedCurrent(Value))

    def SwitchedObj(self, *args):
        """
        Full name of the circuit element switch that the fuse controls.
        Defaults to the MonitoredObj.
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Fuses_Get_SwitchedObj())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Fuses_Set_SwitchedObj(Value))

    def SwitchedTerm(self, *args):
        """
        Number of the terminal of the controlled element containing the switch controlled by the fuse.
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Fuses_Get_SwitchedTerm())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Fuses_Set_SwitchedTerm(Value))

    def TCCCurve(self, *args):
        """Name of the TCCcurve object that determines fuse blowing."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Fuses_Get_TCCcurve()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Fuses_Set_TCCcurve(Value))


_Fuses = IFuses(api_util)

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
]
