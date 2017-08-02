
PDElements
==========


.. automodule:: opendssdirect.PDElements
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.PDElements.AccumulatedL

    Get the accumulated failure rate for this branch on down line.

.. function:: opendssdirect.PDElements.Count

    Get number of PDElements in active circuit.

.. function:: opendssdirect.PDElements.FaultRate

    Get the number of failures per year. For LINE elements: Number of failures per unit length per year.Set the number of failures per year. For LINE elements: Number of failures per unit length per year.

.. function:: opendssdirect.PDElements.First

    Set the first enabled PD element to be the active element. Returns 0 if none found.

.. function:: opendssdirect.PDElements.FromTerminal

    Get the number of the terminal of active PD element that is on the 'from' side. This is set after the meter zone is determined.

.. function:: opendssdirect.PDElements.IsShunt

    returns 1 if the PD element should be treated as a shunt element rather than a series element. Applies to capacitor and reactor elements in particular.

.. function:: opendssdirect.PDElements.Lambda

    Get the failure rate for this branch. Faults per year including length of line.

.. function:: opendssdirect.PDElements.Name

    Get the name of the active PDElement, returns null string if active element id not PDElement.Set the name of the active PDElement, returns null string if active element id not PDElement.

.. function:: opendssdirect.PDElements.Next

    Set the next enabled PD element to be the active element. Returns 0 if none found.

.. function:: opendssdirect.PDElements.NumCustomers

    Get the number of customers in this branch.

.. function:: opendssdirect.PDElements.ParentPDElement

    Set the parent PD element to be the active circuit element. Returns 0 if no more elements upline.

.. function:: opendssdirect.PDElements.PctPermanent

    Get the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.Set the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

.. function:: opendssdirect.PDElements.RepairTime

    Get the average time to repair a permanent fault on this branch, hours.

.. function:: opendssdirect.PDElements.SectionID

    Get the integer ID of the feeder section that this PDElement branch is part of.

.. function:: opendssdirect.PDElements.TotalCustomers

    Get the total number of customers from this branch to the end of the zone.

.. function:: opendssdirect.PDElements.TotalMiles

    Get the total miles of line from this element to the end of the zone. For recloser siting algorithm.

