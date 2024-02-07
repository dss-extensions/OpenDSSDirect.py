from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IParallel(Base):
    """
    Parallel machine interface
    
    On DSS-Extensions, prefer using DSSContexts and native threading capabilities of your programming
    language, if available.
    """

    __slots__ = []

    __name__ = "Parallel"
    _api_prefix = "Parallel"
    _columns = []

    def CreateActor(self):
        """
        Create a new actor, if there are still cores available.
        """
        self._check_for_error(self._lib.Parallel_CreateActor())

    def Wait(self):
        """
        Suspends the host's thread until all the OpenDSS running jobs finish.

        Original COM help: https://opendss.epri.com/Wait.html
        """
        self._check_for_error(self._lib.Parallel_Wait())

    def ActiveActor(self, *args):
        """
        Gets/sets the ID of the Active Actor

        Original COM help: https://opendss.epri.com/ActiveActor.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Parallel_Get_ActiveActor())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Parallel_Set_ActiveActor(Value))

    def ActiveParallel(self, *args):
        """
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active

        Original COM help: https://opendss.epri.com/ActiveParallel.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Parallel_Get_ActiveParallel())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Parallel_Set_ActiveParallel(Value))

    def ActorCPU(self, *args):
        """
        Gets/sets the CPU of the Active Actor

        Original COM help: https://opendss.epri.com/ActorCPU.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Parallel_Get_ActorCPU())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Parallel_Set_ActorCPU(Value))

    def ActorProgress(self):
        """
        Gets the progress of all existing actors in pct

        Original COM help: https://opendss.epri.com/ActorProgress.html
        """
        self._check_for_error(self._lib.Parallel_Get_ActorProgress_GR())
        return self._get_int32_gr_array()

    def ActorStatus(self):
        """
        Gets the status of each actor

        Original COM help: https://opendss.epri.com/ActorStatus.html
        """
        self._check_for_error(self._lib.Parallel_Get_ActorStatus_GR())
        return self._get_int32_gr_array()

    def ConcatenateReports(self, *args):
        """
        (read) Reads the values of the ConcatenateReports option (1=enabled, 0=disabled)
        (write) Enable/Disable (1/0) the ConcatenateReports option for extracting monitors data

        Original COM help: https://opendss.epri.com/ConcatenateReports.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Parallel_Get_ConcatenateReports())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Parallel_Set_ConcatenateReports(Value))

    def NumCPUs(self):
        """
        Delivers the number of CPUs on the current PC

        Original COM help: https://opendss.epri.com/NumCPUs.html
        """
        return self._check_for_error(self._lib.Parallel_Get_NumCPUs())

    def NumCores(self):
        """
        Delivers the number of Cores of the local PC

        Original COM help: https://opendss.epri.com/NumCores.html
        """
        return self._check_for_error(self._lib.Parallel_Get_NumCores())

    def NumOfActors(self):
        """
        Gets the number of Actors created

        Original COM help: https://opendss.epri.com/NumOfActors.html
        """
        return self._check_for_error(self._lib.Parallel_Get_NumOfActors())


_Parallel = IParallel(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
