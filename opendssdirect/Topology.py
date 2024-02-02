from ._utils import api_util, Base, OPENDSSDIRECT_PY_USE_NUMPY


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
        """(read-only) Returns index of the active branch"""
        return self.CheckForError(self._lib.Topology_Get_ActiveBranch())

    def ActiveLevel(self):
        """(read-only) Topological depth of the active branch"""
        return self.CheckForError(self._lib.Topology_Get_ActiveLevel())

    def AllIsolatedBranches(self):
        """(read-only) Array of all isolated branch names."""
        return self.CheckForError(
            self._get_string_array(self._lib.Topology_Get_AllIsolatedBranches)
        )

    def AllIsolatedLoads(self):
        """(read-only) Array of all isolated load names."""
        return self.CheckForError(
            self._get_string_array(self._lib.Topology_Get_AllIsolatedLoads)
        )

    def AllLoopedPairs(self):
        """(read-only) Array of all looped element names, by pairs."""
        return self.CheckForError(
            self._get_string_array(self._lib.Topology_Get_AllLoopedPairs)
        )

    def BackwardBranch(self):
        """(read-only) MOve back toward the source, return index of new active branch, or 0 if no more."""
        return self.CheckForError(self._lib.Topology_Get_BackwardBranch())

    def BranchName(self, *args):
        """Name of the active branch."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Topology_Get_BranchName())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Topology_Set_BranchName(Value))

    def BusName(self, *args):
        """Set the active branch to one containing this bus, return index or 0 if not found"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Topology_Get_BusName())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Topology_Set_BusName(Value))

    def First(self):
        """(read-only) Sets the first branch active, returns 0 if none."""
        return self.CheckForError(self._lib.Topology_Get_First())

    def FirstLoad(self):
        """(read-only) First load at the active branch, return index or 0 if none."""
        return self.CheckForError(self._lib.Topology_Get_FirstLoad())

    def ForwardBranch(self):
        """(read-only) Move forward in the tree, return index of new active branch or 0 if no more"""
        return self.CheckForError(self._lib.Topology_Get_ForwardBranch())

    def LoopedBranch(self):
        """(read-only) Move to looped branch, return index or 0 if none."""
        return self.CheckForError(self._lib.Topology_Get_LoopedBranch())

    def Next(self):
        """(read-only) Sets the next branch active, returns 0 if no more."""
        return self.CheckForError(self._lib.Topology_Get_Next())

    def NextLoad(self):
        """(read-only) Next load at the active branch, return index or 0 if no more."""
        return self.CheckForError(self._lib.Topology_Get_NextLoad())

    def NumIsolatedBranches(self):
        """(read-only) Number of isolated branches (PD elements and capacitors)."""
        return self.CheckForError(self._lib.Topology_Get_NumIsolatedBranches())

    def NumIsolatedLoads(self):
        """(read-only) Number of isolated loads"""
        return self.CheckForError(self._lib.Topology_Get_NumIsolatedLoads())

    def NumLoops(self):
        """(read-only) Number of loops"""
        return self.CheckForError(self._lib.Topology_Get_NumLoops())

    def ParallelBranch(self):
        """(read-only) Move to directly parallel branch, return index or 0 if none."""
        return self.CheckForError(self._lib.Topology_Get_ParallelBranch())


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
