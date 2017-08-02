
SwtControls
===========


.. automodule:: opendssdirect.SwtControls
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.SwtControls.Action

    Get the open (1) or close (2) action of the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action.Set open (1) or close (2) the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action (see manual for details).

.. function:: opendssdirect.SwtControls.AllNames

    Get a vector of strings with all SwtControl names in the active circuit.

.. function:: opendssdirect.SwtControls.Count

    Get the total number of SwtControls in the active circuit.

.. function:: opendssdirect.SwtControls.Delay

    Get the time delay [s] between arming and opening or closing the switch. Control may reset before actually operating the switch.Set the time delay [s] between arming and opening or closing the switch. Control may reset before actually operating the switch.

.. function:: opendssdirect.SwtControls.First

    Set the first SwtControl active. Returns 0 if no more.

.. function:: opendssdirect.SwtControls.IsLocked

    Get the lock state: {1 locked | 0 not locked}.Set the lock to prevent both manual and automatic switch operation.

.. function:: opendssdirect.SwtControls.Name

    Get the name of the active SwtControl.Set a SwtControl active by name.

.. function:: opendssdirect.SwtControls.Next

    Set the next SwtControl active. Returns 0 if no more.

.. function:: opendssdirect.SwtControls.SwitchedObj

    Get the name of the switched object by the active SwtControl.Set the switched object by name.

.. function:: opendssdirect.SwtControls.SwitchedTerm

    Get the terminal number where the switch is located on the SwitchedObj.Set the terminal number where the switch is located on the SwitchedObj.

