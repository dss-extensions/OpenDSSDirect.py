from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class ITopology(Base):
    __slots__ = []

    __name__ = "Topology"
    _api_prefix = "Topology"
    _columns = [
        "NumIsolatedLoads",
        "AllIsolatedBranches",
        "NumIsolatedBranches",
        "AllIsolatedLoads",
        "ActiveLevel",
        "BranchName",
        "AllLoopedPairs",
        "NumLoops",
        "ActiveBranch",
    ]

    def ActiveBranch(self):
        """
        Returns index of the active branch

        Original COM help: https://opendss.epri.com/ActiveBranch.html
        """
        return self._check_for_error(self._lib.Topology_Get_ActiveBranch())

    def ActiveLevel(self):
        """
        Topological depth of the active branch

        Original COM help: https://opendss.epri.com/ActiveLevel.html
        """
        return self._check_for_error(self._lib.Topology_Get_ActiveLevel())

    def AllIsolatedBranches(self):
        """
        Array of all isolated branch names.

        Original COM help: https://opendss.epri.com/AllIsolatedBranches.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Topology_Get_AllIsolatedBranches)
        )

    def AllIsolatedLoads(self):
        """
        Array of all isolated load names.

        Original COM help: https://opendss.epri.com/AllIsolatedLoads.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Topology_Get_AllIsolatedLoads)
        )

    def AllLoopedPairs(self):
        """
        Array of all looped element names, by pairs.

        Original COM help: https://opendss.epri.com/AllLoopedPairs.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Topology_Get_AllLoopedPairs)
        )

    def BackwardBranch(self):
        """
        Move back toward the source, return index of new active branch, or 0 if no more.

        Original COM help: https://opendss.epri.com/BackwardBranch.html
        """
        return self._check_for_error(self._lib.Topology_Get_BackwardBranch())

    def BranchName(self, *args):
        """
        Name of the active branch.

        Original COM help: https://opendss.epri.com/BranchName.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Topology_Get_BranchName())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Topology_Set_BranchName(Value))

    def BusName(self, *args):
        """
        Set the active branch to one containing this bus, return index or 0 if not found

        Original COM help: https://opendss.epri.com/BusName.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Topology_Get_BusName())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Topology_Set_BusName(Value))

    def First(self):
        """
        Sets the first branch active, returns 0 if none.

        Original COM help: https://opendss.epri.com/First19.html
        """
        return self._check_for_error(self._lib.Topology_Get_First())

    def FirstLoad(self):
        """
        First load at the active branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/FirstLoad.html
        """
        return self._check_for_error(self._lib.Topology_Get_FirstLoad())

    def ForwardBranch(self):
        """
        Move forward in the tree, return index of new active branch or 0 if no more

        Original COM help: https://opendss.epri.com/ForwardBranch.html
        """
        return self._check_for_error(self._lib.Topology_Get_ForwardBranch())

    def LoopedBranch(self):
        """
        Move to looped branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/LoopedBranch.html
        """
        return self._check_for_error(self._lib.Topology_Get_LoopedBranch())

    def Next(self):
        """
        Sets the next branch active, returns 0 if no more.

        Original COM help: https://opendss.epri.com/Next18.html
        """
        return self._check_for_error(self._lib.Topology_Get_Next())

    def NextLoad(self):
        """
        Next load at the active branch, return index or 0 if no more.

        Original COM help: https://opendss.epri.com/NextLoad.html
        """
        return self._check_for_error(self._lib.Topology_Get_NextLoad())

    def NumIsolatedBranches(self):
        """
        Number of isolated branches (PD elements and capacitors).

        Original COM help: https://opendss.epri.com/NumIsolatedBranches.html
        """
        return self._check_for_error(self._lib.Topology_Get_NumIsolatedBranches())

    def NumIsolatedLoads(self):
        """
        Number of isolated loads

        Original COM help: https://opendss.epri.com/NumIsolatedLoads.html
        """
        return self._check_for_error(self._lib.Topology_Get_NumIsolatedLoads())

    def NumLoops(self):
        """
        Number of loops

        Original COM help: https://opendss.epri.com/NumLoops.html
        """
        return self._check_for_error(self._lib.Topology_Get_NumLoops())

    def ParallelBranch(self):
        """
        Move to directly parallel branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/ParallelBranch.html
        """
        return self._check_for_error(self._lib.Topology_Get_ParallelBranch())


_Topology = ITopology(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
ActiveBranch = _Topology.ActiveBranch
ActiveLevel = _Topology.ActiveLevel
AllIsolatedBranches = _Topology.AllIsolatedBranches
AllIsolatedLoads = _Topology.AllIsolatedLoads
AllLoopedPairs = _Topology.AllLoopedPairs
BackwardBranch = _Topology.BackwardBranch
BranchName = _Topology.BranchName
BusName = _Topology.BusName
First = _Topology.First
FirstLoad = _Topology.FirstLoad
ForwardBranch = _Topology.ForwardBranch
LoopedBranch = _Topology.LoopedBranch
Next = _Topology.Next
NextLoad = _Topology.NextLoad
NumIsolatedBranches = _Topology.NumIsolatedBranches
NumIsolatedLoads = _Topology.NumIsolatedLoads
NumLoops = _Topology.NumLoops
ParallelBranch = _Topology.ParallelBranch
_columns = _Topology._columns
__all__ = [
    "ActiveBranch",
    "ActiveLevel",
    "AllIsolatedBranches",
    "AllIsolatedLoads",
    "AllLoopedPairs",
    "BackwardBranch",
    "BranchName",
    "BusName",
    "First",
    "FirstLoad",
    "ForwardBranch",
    "LoopedBranch",
    "Next",
    "NextLoad",
    "NumIsolatedBranches",
    "NumIsolatedLoads",
    "NumLoops",
    "ParallelBranch",
]
