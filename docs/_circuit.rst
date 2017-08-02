
Circuit
=======


.. automodule:: opendssdirect.Circuit
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Circuit.AllBusDistances

    Returns all distances from a bus to its parent EnergyMeter element, which is generally in the substation, as a variant array of doubles. Order corresponds to that of all bus properties.

.. function:: opendssdirect.Circuit.AllBusMagPu

    Similar to AllBusVmag except that the magnitudes are reported in per unit for all buses with kVBase defined.

.. function:: opendssdirect.Circuit.AllBusNames

    The names of all buses in the system. See `:AllNodeNames`.

.. function:: opendssdirect.Circuit.AllBusVMag

    Similar to AllBusVolts except magnitude only (in actual volts). Returns the voltage (magnitude) for every node in the circuit as a complex vector.

.. function:: opendssdirect.Circuit.AllBusVolts

    Returns the voltage (complex) for every node in the circuit as a complex vector. The order of the array is the same as AllNodeNames property. The array is constructed bus-by-bus and then by node at each bus. Thus, all nodes from each bus are grouped together.

.. function:: opendssdirect.Circuit.AllElementLosses

    Returns the watt and var losses in each element of the system as a complex vector. Order is the same as AllElementNames.

.. function:: opendssdirect.Circuit.AllElementNames

    The names of all elements

.. function:: opendssdirect.Circuit.AllNodeDistances

    Returns the distance from all nodes to the parent energy meter that match the designated phase number. Returns a vector of doubles. Matches the order of AllNodeNamesByPhase, AllNodeVmagByPhase, AllNodeVmagPUByPhase.

.. function:: opendssdirect.Circuit.AllNodeNames

    Returns the names of all nodes (busname.nodenumber) in the same order as AllBusVolts, AllBusVmag, and AllBusVMagPu

.. function:: opendssdirect.Circuit.Capacity

    Executes the DSS capacity function. Start is the per unit load multiplier for the current year at which to start the search. Increment is the per unit value by which the load increments for each step of the analysis. The program sets the load at the Start value the PRESENT YEAR (including growth) and increments the load until something in thecircuit reports an overload or undervoltage violation. The function returns the total load at which the violation occurs or the peak load for the present year if no violations.

.. function:: opendssdirect.Circuit.Disable

    Disable a circuit element by name (full name).

.. function:: opendssdirect.Circuit.Enable

    Enable a circuit element by name (full name).

.. function:: opendssdirect.Circuit.EndOfTimeStepUpdate

    Calls EndOfTimeStepCleanup in SolutionAlgs

.. function:: opendssdirect.Circuit.FirstElement

    Sets First element of active class to be the Active element in the active circuit. Returns 0 if none.

.. function:: opendssdirect.Circuit.FirstPCElement

    Sets the first enabled Power Conversion (PC) element in the circuit to be active; if not successful returns a 0

.. function:: opendssdirect.Circuit.FirstPDElement

    Sets the first enabled Power Delivery (PD) element in the circuit to be active; if not successful returns a 0

.. function:: opendssdirect.Circuit.LineLosses

    Watt and var losses in all the Line elements in the circuit, complex

.. function:: opendssdirect.Circuit.Losses

    Watt and var losses in the entire circuit, complex

.. function:: opendssdirect.Circuit.Name

    Name of the active circuit

.. function:: opendssdirect.Circuit.NextElement

    Sets the next element of the active class to be the active element in the active circuit. Returns 0 if no more elements.

.. function:: opendssdirect.Circuit.NextPCElement

    Sets the next enabled Power Conversion (PC) element in the circuit to be active; if not successful returns a 0

.. function:: opendssdirect.Circuit.NextPDElement

    Sets the next enabled Power Delivery (PD) element in the circuit to be active; if not successful returns a 0

.. function:: opendssdirect.Circuit.NumBuses

    Total number of Buses in the circuit

.. function:: opendssdirect.Circuit.NumCktElements

    Number of CktElements in the circuit

.. function:: opendssdirect.Circuit.NumNodes

    Total number of Nodes in the circuit

.. function:: opendssdirect.Circuit.ParentPDElement

    Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable.

.. function:: opendssdirect.Circuit.Sample

    Force all Meters and Monitors to take a sample

.. function:: opendssdirect.Circuit.SaveSample

    Force all Meters and Monitors to save their current buffers

.. function:: opendssdirect.Circuit.SetActiveBus

    Sets the active bus by name. Returns a 0 based index of the bus to use for future direct indexing of bus values returned in arrays. Returns -1 if an error occurs.

.. function:: opendssdirect.Circuit.SetActiveBusi

    Sets the active bus by integer index. The index is 0 based. That is, the first bus has an index of 0. Returns -1 if an error occurs.

.. function:: opendssdirect.Circuit.SetActiveClass

    Sets the active class by name.  Use FirstElement, NextElement to iterate through the class. Returns ‐1 if fails.

.. function:: opendssdirect.Circuit.SetActiveElement

    Activate an element of the active circuit by name. Returns a string with the index of the active element.

.. function:: opendssdirect.Circuit.SubstationLosses

    Watt and var losses in all the Transformer elements in the circuit that are designated as substations

.. function:: opendssdirect.Circuit.TotalPower

    Returns the total power in kW and kvar supplied to the circuit by all Vsource and Isource objects. Does not include Generator objects. Complex.

.. function:: opendssdirect.Circuit.UpdateStorage

    Forces update to all storage classes. Typically done after a solution. Done automatically in intrinsic solution modes.

.. function:: opendssdirect.Circuit.YCurrents

    Vector of doubles containing complex injection currents for the present solution.

.. function:: opendssdirect.Circuit.YNodeOrder

    The names of the nodes in the same order as the Y matrix

.. function:: opendssdirect.Circuit.YNodeVArray

    Complex array of actual node voltages in same order as SystemY matrix.

