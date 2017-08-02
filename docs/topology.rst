
Topology
========


.. automodule:: opendssdirect.Topology
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Topology.ActiveBranch

    The index of the active Branch.

.. function:: opendssdirect.Topology.ActiveLevel

    Get the topological depth of the active branch.

.. function:: opendssdirect.Topology.AllIsolatedBranches

    Get a vector of all isolated branch names.

.. function:: opendssdirect.Topology.AllIsolatedLoads

    Get a vector of all isolated load names.

.. function:: opendssdirect.Topology.AllLoopedPairs

    Get a vector of all looped element names, by pairs.

.. function:: opendssdirect.Topology.BranchName

    Get the name of the active branch.Set the name of the active branch.

.. function:: opendssdirect.Topology.BusName

    Get the name of the active Bus.Set the Bus active by name.

.. function:: opendssdirect.Topology.First

    Set the first branch active, returns 0 if none.

.. function:: opendssdirect.Topology.FirstLoad

    Set as active load the first load at the active branch, return index or 0 if none.

.. function:: opendssdirect.Topology.ForwardBranch

    Move forward in the tree, return index of new active branch or 0 if no more.

.. function:: opendssdirect.Topology.LoopedBranch

    Move to looped branch, return index or 0 if none.

.. function:: opendssdirect.Topology.Next

    Set the next branch active, returns 0 if none.

.. function:: opendssdirect.Topology.NextLoad

    Set as active load the next load at the active branch, return index or 0 if none.

.. function:: opendssdirect.Topology.NumIsolatedBranches

    Get the number of isolated branches (PD elements and capacitors).

.. function:: opendssdirect.Topology.NumIsolatedLoads

    Get the number of isolated loads.

.. function:: opendssdirect.Topology.NumLoops

    Get the number of loops.

.. function:: opendssdirect.Topology.ParallelBranch

    Mode to directly parallel branch, return index or 0 if none.

