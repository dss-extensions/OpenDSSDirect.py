# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_string_array


def ActiveBranch():
    """(read-only) Returns index of the active branch"""
    return CheckForError(lib.Topology_Get_ActiveBranch())


def ActiveLevel():
    """(read-only) Topological depth of the active branch"""
    return CheckForError(lib.Topology_Get_ActiveLevel())


def AllIsolatedBranches():
    """(read-only) Array of all isolated branch names."""
    return CheckForError(get_string_array(lib.Topology_Get_AllIsolatedBranches))


def AllIsolatedLoads():
    """(read-only) Array of all isolated load names."""
    return CheckForError(get_string_array(lib.Topology_Get_AllIsolatedLoads))


def AllLoopedPairs():
    """(read-only) Array of all looped element names, by pairs."""
    return CheckForError(get_string_array(lib.Topology_Get_AllLoopedPairs))


def BackwardBranch():
    """(read-only) MOve back toward the source, return index of new active branch, or 0 if no more."""
    return CheckForError(lib.Topology_Get_BackwardBranch())


def BranchName(*args):
    """Name of the active branch."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Topology_Get_BranchName()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Topology_Set_BranchName(Value))


def BusName(*args):
    """Set the active branch to one containing this bus, return index or 0 if not found"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Topology_Get_BusName()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Topology_Set_BusName(Value))


def First():
    """(read-only) Sets the first branch active, returns 0 if none."""
    return CheckForError(lib.Topology_Get_First())


def FirstLoad():
    """(read-only) First load at the active branch, return index or 0 if none."""
    return CheckForError(lib.Topology_Get_FirstLoad())


def ForwardBranch():
    """(read-only) Move forward in the tree, return index of new active branch or 0 if no more"""
    return CheckForError(lib.Topology_Get_ForwardBranch())


def LoopedBranch():
    """(read-only) Move to looped branch, return index or 0 if none."""
    return CheckForError(lib.Topology_Get_LoopedBranch())


def Next():
    """(read-only) Sets the next branch active, returns 0 if no more."""
    return CheckForError(lib.Topology_Get_Next())


def NextLoad():
    """(read-only) Next load at the active branch, return index or 0 if no more."""
    return CheckForError(lib.Topology_Get_NextLoad())


def NumIsolatedBranches():
    """(read-only) Number of isolated branches (PD elements and capacitors)."""
    return CheckForError(lib.Topology_Get_NumIsolatedBranches())


def NumIsolatedLoads():
    """(read-only) Number of isolated loads"""
    return CheckForError(lib.Topology_Get_NumIsolatedLoads())


def NumLoops():
    """(read-only) Number of loops"""
    return CheckForError(lib.Topology_Get_NumLoops())


def ParallelBranch():
    """(read-only) Move to directly parallel branch, return index or 0 if none."""
    return CheckForError(lib.Topology_Get_ParallelBranch())


_columns = [
    "ActiveBranch",
    "ActiveLevel",
    "BranchName",
    "NumIsolatedBranches",
    "NumIsolatedLoads",
    "NumLoops",
    "AllIsolatedBranches",
    "AllIsolatedLoads",
    "AllLoopedPairs",
]
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
