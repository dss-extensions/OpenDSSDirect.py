
CapControls
===========


.. automodule:: opendssdirect.CapControls
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.CapControls.AllNames

    Names of all CapControls in the circuit

.. function:: opendssdirect.CapControls.CTRatio

    Transducer ratio from primary current to control currentSet the transducer ratio from primary current to control current

.. function:: opendssdirect.CapControls.Capacitor

    Name of the Capacitor that is controlledSet the Capacitor (by name) that is controlled

.. function:: opendssdirect.CapControls.Count

    Number of CapControls in the active circuit

.. function:: opendssdirect.CapControls.Delay

    Time delay [s] to switch on after arming; control may reset before actuallyswitchingSet the time delay [s] to switch on after arming; control may reset before actuallyswitching

.. function:: opendssdirect.CapControls.DelayOff

    Time delay [s] before switching off a step; control may reset before actuallyswitchingSet the time delay [s] before switching off a step; control may reset before actually switching

.. function:: opendssdirect.CapControls.First

    Sets the first CapControl active; returns 0 if none

.. function:: opendssdirect.CapControls.Mode

    Type of automatic controller; for meaning, see CapControlModesSet the type of automatic controller; for choices, see CapControlModes

.. function:: opendssdirect.CapControls.MonitoredObj

    Full name of the element that PT and CT are connected toSet the element (by full name) that PT and CT are connected to

.. function:: opendssdirect.CapControls.MonitoredTerm

    Terminal number on the element that PT and CT are connected toSet the terminal number on the element that PT and CT are connected to

.. function:: opendssdirect.CapControls.Name

    The name of the active CapControlSet the active CapControl by name

.. function:: opendssdirect.CapControls.Next

    Sets the next CapControl active; returns 0 if no more

.. function:: opendssdirect.CapControls.OFFSetting

    Threshold to switch off a step; see the particular CapControlModes option for unitsSet the threshold to switch off a step; see the particular CapControlModes option for units

.. function:: opendssdirect.CapControls.ONSetting

    Threshold to arm or switch on a step; see Mode for unitsSet the threshold to arm or switch on a step; see Mode for units

.. function:: opendssdirect.CapControls.PTRatio

    Transducer ratio from primary voltage to control voltageSet the transducer ratio from primary voltage to control voltage

.. function:: opendssdirect.CapControls.UseVoltOverride

    Bool flag that enables Vmin and Vmax to override the control modeSet the Bool flag that enables Vmin and Vmax to override the control mode

.. function:: opendssdirect.CapControls.Vmax

    With VoltOverride, switch off whenever PT voltage exceeds this levelSet Vmax; with VoltOverride, switch off whenever PT voltage exceeds this level

.. function:: opendssdirect.CapControls.Vmin

    With VoltOverride, switch on whenever PT voltage drops below this levelSet Vmin; with VoltOverride, switch on whenever PT voltage drops below this level

