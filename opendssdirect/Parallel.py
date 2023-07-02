from ._utils import api_util, Base


class IParallel(Base):
    """Parallel machine interface"""

    __name__ = "Parallel"
    _api_prefix = "Parallel"
    _columns = []

    __slots__ = []

    def CreateActor(self):
        self.CheckForError(self._lib.Parallel_CreateActor())

    def Wait(self):
        self.CheckForError(self._lib.Parallel_Wait())

    def ActiveActor(self, *args):
        """Gets/sets the ID of the Active Actor"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Parallel_Get_ActiveActor())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Parallel_Set_ActiveActor(Value))

    def ActiveParallel(self, *args):
        """
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Parallel_Get_ActiveParallel())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Parallel_Set_ActiveParallel(Value))

    def ActorCPU(self, *args):
        """Gets/sets the CPU of the Active Actor"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Parallel_Get_ActorCPU())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Parallel_Set_ActorCPU(Value))

    def ActorProgress(self):
        """(read-only) Gets the progress of all existing actors in pct"""
        self.CheckForError(self._lib.Parallel_Get_ActorProgress_GR())
        return self._get_int32_gr_array()

    def ActorStatus(self):
        """(read-only) Gets the status of each actor"""
        self.CheckForError(self._lib.Parallel_Get_ActorStatus_GR())
        return self._get_int32_gr_array()

    def ConcatenateReports(self, *args):
        """
        Controls the ConcatenateReports option (1=enabled, 0=disabled)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Parallel_Get_ConcatenateReports())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Parallel_Set_ConcatenateReports(Value))

    def NumCPUs(self):
        """(read-only) Delivers the number of CPUs on the current PC"""
        return self.CheckForError(self._lib.Parallel_Get_NumCPUs())

    def NumCores(self):
        """(read-only) Delivers the number of Cores of the local PC"""
        return self.CheckForError(self._lib.Parallel_Get_NumCores())

    def NumOfActors(self):
        """(read-only) Gets the number of Actors created"""
        return self.CheckForError(self._lib.Parallel_Get_NumOfActors())


_Parallel = IParallel(api_util)

# For backwards compatibility, bind to the default instance
CreateActor = _Parallel.CreateActor
Wait = _Parallel.Wait
ActiveActor = _Parallel.ActiveActor
ActiveParallel = _Parallel.ActiveParallel
ActorCPU = _Parallel.ActorCPU
ActorProgress = _Parallel.ActorProgress
ActorStatus = _Parallel.ActorStatus
ConcatenateReports = _Parallel.ConcatenateReports
NumCPUs = _Parallel.NumCPUs
NumCores = _Parallel.NumCores
NumOfActors = _Parallel.NumOfActors
_columns = _Parallel._columns
__all__ = [
    "CreateActor",
    "Wait",
    "ActiveActor",
    "ActiveParallel",
    "ActorCPU",
    "ActorProgress",
    "ActorStatus",
    "ConcatenateReports",
    "NumCPUs",
    "NumCores",
    "NumOfActors",
]
