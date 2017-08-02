
Fuses
=====


.. automodule:: opendssdirect.Fuses
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Fuses.AllNames

     Names of all Fuses in the circuit

.. function:: opendssdirect.Fuses.Close

    Close the fuse back in and reset.

.. function:: opendssdirect.Fuses.Count

    Number of Fuse elements in the circuit

.. function:: opendssdirect.Fuses.First

    Set the first Fuse to be the active fuse. Returns 0 if none.

.. function:: opendssdirect.Fuses.Idx

    Get/set active fuse by index into the list of fuses. 1 based: 1..countSet Fuse active by index into the list of fuses. 1..count

.. function:: opendssdirect.Fuses.IsBlown

    Current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE.

.. function:: opendssdirect.Fuses.MonitoredObj

    Full name of the circuit element to which the fuse is connected.Set the full name of the circuit element to which the fuse is connected.

.. function:: opendssdirect.Fuses.MonitoredTerm

    Terminal number to which the fuse is connected.Set the terminal number to which the fuse is connected.

.. function:: opendssdirect.Fuses.Name

    Get the name of the active Fuse elementSet the name of the active Fuse element

.. function:: opendssdirect.Fuses.Next

    Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses.

.. function:: opendssdirect.Fuses.NumPhases

    Number of phases, this fuse.

.. function:: opendssdirect.Fuses.Open

    Manual opening of fuse

.. function:: opendssdirect.Fuses.RatedCurrent

    Multiplier or actual amps for the TCCcurve object. Defaults to 1.0. Multipliy current values of TCC curve by this to get actual amps.Set the multiplier or actual amps for the TCCcurve object. Defaults to 1.0. Multipliy current values of TCC curve by this to get actual amps.

.. function:: opendssdirect.Fuses.SwitchedObj

    Full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.Set the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.

.. function:: opendssdirect.Fuses.TCCCurve

    Name of the TCCcurve object that determines fuse blowing.Set the name of the TCCcurve object that determines fuse blowing.

