
RegControls
===========


.. automodule:: opendssdirect.RegControls
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.RegControls.AllNames

    Get a vector of strings containing all RegControl names.

.. function:: opendssdirect.RegControls.CTPrimary

    Get the CT primary ampere rating (secondary is 0.2 amperes).Set the CT primary ampere rating (secondary is 0.2 amperes).

.. function:: opendssdirect.RegControls.Count

    Get the number of RegControl objects in Active Circuit.

.. function:: opendssdirect.RegControls.Delay

    Get the time delay [s] after arming before the first tap change. Control may reset before actually changing taps.Set the time delay [s] after arming before the first tap change. Control may reset before actually changing taps.

.. function:: opendssdirect.RegControls.First

    Set the first RegControl active. Returns 0 if no more.

.. function:: opendssdirect.RegControls.ForwardBand

    Get the regulation bandwidth in forward direction, centered on Vreg.Set the regulation bandwidth in forward direction, centered on Vreg.

.. function:: opendssdirect.RegControls.ForwardR

    Get the LDC R settings in Volts.Set the LDC R settings in Volts.

.. function:: opendssdirect.RegControls.ForwardVreg

    Get the target voltage in the forward direction, on PT secondary base.Set the target voltage in the forward direction, on PT secondary base.

.. function:: opendssdirect.RegControls.ForwardX

    Get the LDC X settings in Volts.Set the LDC X settings in Volts.

.. function:: opendssdirect.RegControls.IsInverseTime

    Get the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.Set the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.

.. function:: opendssdirect.RegControls.IsReversible

    Get the setting in the reverse direction, usually not applicable to substation Transformers.Set the different settings for the reverse direction (see Manual for details), usually not applicable to substation Transformers.

.. function:: opendssdirect.RegControls.MaxTapChange

    Get the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.Set the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.

.. function:: opendssdirect.RegControls.MonitoredBus

    Get the name of the remote regulated bus, in lieu of LDC settings.Set the name of the remote regulated bus, in lieu of LDC settings.

.. function:: opendssdirect.RegControls.Name

    Get the active RegControl name.Set the active RegControl name.

.. function:: opendssdirect.RegControls.Next

    Set the next RegControl active. Returns 0 if no more

.. function:: opendssdirect.RegControls.PTRatio

    Get the PT ratio for voltage control settings.Set the PT ratio for voltage control settings.

.. function:: opendssdirect.RegControls.ReverseBand

    Get the bandwidth in reverse direction, centered on reverse Vreg.Set the bandwidth in reverse direction, centered on reverse Vreg.

.. function:: opendssdirect.RegControls.ReverseR

    Get the reverse LDC R settings in Volts.Set the reverse LDC R settings in Volts.

.. function:: opendssdirect.RegControls.ReverseVreg

    Get the target voltage in the reverse direction, on PT secondary base.Set the target voltage in the reverse direction, on PT secondary base.

.. function:: opendssdirect.RegControls.ReverseX

    Get the reverse LDC X settings in Volts.Set the reverse LDC X settings in Volts.

.. function:: opendssdirect.RegControls.TapDelay

    Get the time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.Set the time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.

.. function:: opendssdirect.RegControls.TapNumber

    Get the tap number.Set the tap number.

.. function:: opendssdirect.RegControls.TapWinding

    Get the tapped winding number.Set the tapped winding number.

.. function:: opendssdirect.RegControls.Transformer

    Get the name of the transformer this regulator controls.Set the name of the transformer this regulator controls.

.. function:: opendssdirect.RegControls.VoltageLimit

    Get the first house voltage limit on PT secondary base. Setting to 0 disables this function.Set the first house voltage limit on PT secondary base. Setting to 0 disables this function.

.. function:: opendssdirect.RegControls.Winding

    Get the winding number for PT and CT connections.Set the winding number for PT and CT connections.

