
Capacitors
==========


.. automodule:: opendssdirect.Capacitors
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Capacitors.AddStep

    Adds one step of the capacitor if available; if successful, returns 1

.. function:: opendssdirect.Capacitors.AllNames

    All capacitor names in the circuit

.. function:: opendssdirect.Capacitors.AvailableSteps

    Number of steps available in the cap bank to be switched ON

.. function:: opendssdirect.Capacitors.Close

    Close all steps of all phases of the capacitor

.. function:: opendssdirect.Capacitors.Count

    Number of capacitor objects in the active circuit

.. function:: opendssdirect.Capacitors.First

    Sets the first Capacitor active; returns 0 if none

.. function:: opendssdirect.Capacitors.IsDelta

    Is the connection a deltaSet connection type; use `arg==true` for delta and `arg==false` for wye

.. function:: opendssdirect.Capacitors.Name

    The name of the active capacitorSets the active capacitor by name

.. function:: opendssdirect.Capacitors.Next

    Sets the next Capacitor active; returns 0 if no more

.. function:: opendssdirect.Capacitors.NumSteps

    Number of stepsSet the number of steps

.. function:: opendssdirect.Capacitors.Open

    Open all steps, all phases of the capacitor

.. function:: opendssdirect.Capacitors.States

    A vector of  integers [0..numsteps‐1] indicating state of each step; if value is ‐1 an error has occurred.

.. function:: opendssdirect.Capacitors.SubtractStep

    Subtracts one step of the capacitor; if no more steps, returns 0

.. function:: opendssdirect.Capacitors.kV

    Bank kV rating; use LL for 2 or 3 phases, or actual can rating for 1 phaseSet the bank kV rating; use LL for 2 or 3 phases, or actual can rating for 1 phase

.. function:: opendssdirect.Capacitors.kvar

    Total bank kvar, distributed equally among phases and stepsSet the total bank kvar, distributed equally among phases and steps

