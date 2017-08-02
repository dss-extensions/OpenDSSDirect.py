
Reclosers
=========


.. automodule:: opendssdirect.Reclosers
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Reclosers.AllNames

    Get a vector of strings with names of all Reclosers in active circuit.

.. function:: opendssdirect.Reclosers.Close

    Close the switched object controlled by the recloser. Resets recloser to first operation.

.. function:: opendssdirect.Reclosers.Count

    Get number of Reclosers in active circuit.

.. function:: opendssdirect.Reclosers.First

    Set first recloser to be active Circuit Element. Returns 0 if none.

.. function:: opendssdirect.Reclosers.GroundInst

    Get the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.Set the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.

.. function:: opendssdirect.Reclosers.GroundTrip

    Get the ground (3I0) trip multiplier or actual amps.Set the ground (3I0) trip multiplier or actual amps.

.. function:: opendssdirect.Reclosers.Idx

    Get the active recloser by index into the recloser list. 1..Count.Set the active recloser by index into the recloser list. 1..Count.

.. function:: opendssdirect.Reclosers.MonitoredObj

    Get the full name of object this Recloser is monitoring.Set the full name of object this Recloser is monitoring.

.. function:: opendssdirect.Reclosers.MonitoredTerm

    Get the terminal number of Monitored Object for the Recloser.Set the terminal number of Monitored Object for the Recloser.

.. function:: opendssdirect.Reclosers.Name

    Get the name of the active Recloser Object.Set the name of the active Recloser Object.

.. function:: opendssdirect.Reclosers.Next

    Set next recloser to be active Circuit Element. Returns 0 if none.

.. function:: opendssdirect.Reclosers.NumFast

    Get the number of fast shots.Set the number of fast shots.

.. function:: opendssdirect.Reclosers.Open

    Open recloser's controlled element and lock out the recloser.

.. function:: opendssdirect.Reclosers.PhaseInst

    Get the phase instantaneous curve multiplier or actual amps.Set the phase instantaneous curve multiplier or actual amps.

.. function:: opendssdirect.Reclosers.PhaseTrip

    Get the phase trip curve multiplier or actual amps.Set the phase trip curve multiplier or actual amps.

.. function:: opendssdirect.Reclosers.RecloseIntervals

    Get a vector of doubles: reclose intervals (s) between shots.

.. function:: opendssdirect.Reclosers.Shots

    Get the number of shots to lockout (fast + delayed).Set the number of shots to lockout (fast + delayed).

.. function:: opendssdirect.Reclosers.SwitchedObj

    Get the full name of the circuit element that is being switched by this Recloser.Set the full name of the circuit element that is being switched by this Recloser.

.. function:: opendssdirect.Reclosers.SwitchedTerm

    Get the terminal of the controlled device being switched by the Recloser.Set the terminal of the controlled device being switched by the Recloser.

