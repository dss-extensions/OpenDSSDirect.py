
Meters
======


.. automodule:: opendssdirect.Meters
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Meters.AllBranchesInZone

    A wide string list of all branches in zone of the active Energy Meter object.

.. function:: opendssdirect.Meters.AllEndElements

    A vector of names of all zone end elements.

.. function:: opendssdirect.Meters.AllNames

    All Energy Meter names.

.. function:: opendssdirect.Meters.AllocFactors

    An array of doubles: allocation factors for the active Meter.

.. function:: opendssdirect.Meters.AvgRepairTime

    The average Repair Time in this Section of the meter zone.

.. function:: opendssdirect.Meters.CalcCurrent

    The magnitude of the real part of the Calculated Current (normally determined by solution) for the meter to force some behavior on Load Allocation.

.. function:: opendssdirect.Meters.CloseAllDIFiles

    Close all Demand Interval (DI) files. Necessary at the end of a run.

.. function:: opendssdirect.Meters.Count

    The number of Energy Meters in the Active Circuit.

.. function:: opendssdirect.Meters.CountBranches

    The number of branches in active Energy Meter zone (same as sequencelist size).

.. function:: opendssdirect.Meters.CountEndElements

    The number of zone end elements in the active meter zone.

.. function:: opendssdirect.Meters.CustInterrupts

    The total customer interruptions for this meter zone based on reliability calcs.

.. function:: opendssdirect.Meters.DIFilesAreOpen

    Returns a global flag (1=true, 0=false) to indicate if Demand Interval (DI) files have been properly opened.

.. function:: opendssdirect.Meters.DoReliabilityCalc

    calculates SAIFI, etc. if the Argument is equal to 1 assume restoration, otherwise it will not.

.. function:: opendssdirect.Meters.FaultRateXRepairHrs

    The sum of Fault Rate time Repair Hours in this section of the meter zone.

.. function:: opendssdirect.Meters.First

    Set the first Energy Meter active. Returns 0 if no Monitors.

.. function:: opendssdirect.Meters.MeteredElement

    The name of the metered element (considering the active Energy Meter).Set the name of the metered element (considering the active Energy Meter).

.. function:: opendssdirect.Meters.MeteredTerminal

    The number of metered terminal by the active Energy Meter.Set the number of metered terminal by the active Energy Meter.

.. function:: opendssdirect.Meters.Name

    The active Energy Meter's name.Set the active Energy Meter's name.

.. function:: opendssdirect.Meters.Next

    Set the next energy Meter Active. Returns 0 if no more.

.. function:: opendssdirect.Meters.NumSectionBranches

    The number of branches (Lines) in the active section.

.. function:: opendssdirect.Meters.NumSectionCustomers

    The number of customers in the active section.

.. function:: opendssdirect.Meters.NumSections

    The number of feeder sections in this meter's zone.

.. function:: opendssdirect.Meters.OCPDeviceType

    The type of OCP device: {1=fuse | 2+ recloser | 3= relay}.

.. function:: opendssdirect.Meters.OpenAllDIFiles

    Opens Demand Interval (DI) files. Returns 0.

.. function:: opendssdirect.Meters.PeakCurrent

    Returns an array of doubles with the Peak Current Property.

.. function:: opendssdirect.Meters.RegisterNames

    Strings containing the names of the registers.

.. function:: opendssdirect.Meters.RegisterValues

    Values contained in the Meter registers for the active Meter.

.. function:: opendssdirect.Meters.Reset

    Resets the active Meter object.

.. function:: opendssdirect.Meters.ResetAll

    Resets all Meter object.

.. function:: opendssdirect.Meters.SAIDI

    The SAIDI for this meter zone. Execute DoreliabilityCalc first.

.. function:: opendssdirect.Meters.SAIFI

    SAIFI for this meter's zone. Execute reliability calc method first.

.. function:: opendssdirect.Meters.SAIFIkW

    The SAIFI based on kW rather than number of customers. Get after reliability calcs.

.. function:: opendssdirect.Meters.Sample

    Causes active meter to take a sample.

.. function:: opendssdirect.Meters.SampleAll

    Causes all Energy Meters to take a sample of the present state. Returns 0.

.. function:: opendssdirect.Meters.Save

    Causes active meter to save its current sample buffer to its meter stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

.. function:: opendssdirect.Meters.SaveAll

    save all Energy Meter buffers to their respective file streams. Returns 0.

.. function:: opendssdirect.Meters.SectSeqidx

    The Sequence Index of the branch at the head of this section.

.. function:: opendssdirect.Meters.SectTotalCust

    The total customers down line from this section.

.. function:: opendssdirect.Meters.SeqListSize

    The size of Sequence List.

.. function:: opendssdirect.Meters.SequenceList

    The index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.Set the index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.

.. function:: opendssdirect.Meters.SetActiveSection

    Set the designated section (argument) if the index is valid.

.. function:: opendssdirect.Meters.SumBranchFltRates

    The sum of the branch fault rates in this section of the meter's zone.

.. function:: opendssdirect.Meters.TotalCustomers

    The total number of customers in this zone (down line from the Energy Meter).

.. function:: opendssdirect.Meters.Totals

    The totals for all registers of all Meters.

