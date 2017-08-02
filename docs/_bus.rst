
Bus
===


.. automodule:: opendssdirect.Bus
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Bus.Coorddefined

    Returns true if the X-Y coordinates are defined for the active bus

.. function:: opendssdirect.Bus.CplxSeqVoltages

    All complex sequence voltages

.. function:: opendssdirect.Bus.Cust_Duration

    Accumulated customer outage durations, hours

.. function:: opendssdirect.Bus.Cust_Interrupts

    Annual number of customer-interruptions from this bus

.. function:: opendssdirect.Bus.Distance

    Distance in km that this bus isfrom the parent EnergyMeter

.. function:: opendssdirect.Bus.GetUniqueNodeNumber

    Returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus

.. function:: opendssdirect.Bus.Int_Duration

    Average interruption duration, hours

.. function:: opendssdirect.Bus.Isc

    Short-circuit current vector, complex

.. function:: opendssdirect.Bus.Lambda

    Total annual failure rate for active bus after reliability calcs

.. function:: opendssdirect.Bus.N_Customers

    Returns the total number of customers downline from the active bus after reliability calcs

.. function:: opendssdirect.Bus.N_interrupts

    Number of interruptions this bus per year

.. function:: opendssdirect.Bus.Name

    Active bus name; set the active bus by name with `circuit.SetActiveBus(name)`

.. function:: opendssdirect.Bus.Nodes

    Vector of node numbers defined at the bus in the same order as the voltages

.. function:: opendssdirect.Bus.NumNodes

    Number of nodes

.. function:: opendssdirect.Bus.PuVoltage

    Per-unit voltages at the bus, complex

.. function:: opendssdirect.Bus.SectionID

    Integer ID of the feeder section in which this bus is located

.. function:: opendssdirect.Bus.SeqVoltages

    Sequence voltages in order of 0, 1, then 2

.. function:: opendssdirect.Bus.TotalMiles

    Total length of line downline from this bus, miles

.. function:: opendssdirect.Bus.VLL

    Complex vector of line-to-line voltages for 2- and 3-phase buses; returns -1. for a 1-phase bus; for more than 3 phases, only returns 3 phases

.. function:: opendssdirect.Bus.VMagAngle

    Bus voltage magnitudes with angles

.. function:: opendssdirect.Bus.Voc

    Open-circuit voltage vector, complex

.. function:: opendssdirect.Bus.Voltages

    Bus voltages, complex

.. function:: opendssdirect.Bus.X

    X coordinate of the busSet the X coordinate of the bus

.. function:: opendssdirect.Bus.Y

    Y coordinate of the busSet the Y coordinate of the bus

.. function:: opendssdirect.Bus.YscMatrix

    Short-circuit admittance matrix, complex

.. function:: opendssdirect.Bus.Zsc0

    Zero-sequence short-circuit impedance looking into the bus, complex

.. function:: opendssdirect.Bus.Zsc1

    Positive-sequence short-circuit impedance looking into the bus, complex

.. function:: opendssdirect.Bus.ZscMatrix

    Short-circuit impedance matrix, complex

.. function:: opendssdirect.Bus.ZscRefresh

    Refresh Zsc and Ysc values; execute after a major change in the circuit

.. function:: opendssdirect.Bus.kVBase

    Base voltage

.. function:: opendssdirect.Bus.puVLL

    Complex vector of per-unit line-to-line voltages for 2- and 3-phase buses; returns -1. for a 1-phase bus; for more than 3 phases, only returns 3 phases

.. function:: opendssdirect.Bus.puVmagAngle

    Bus voltage magnitudes (per unit) with angles

