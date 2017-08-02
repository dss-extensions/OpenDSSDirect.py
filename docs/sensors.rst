
Sensors
=======


.. automodule:: opendssdirect.Sensors
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Sensors.AllNames

    Returns a vector of sensor names.

.. function:: opendssdirect.Sensors.Count

    Get number of Sensors in active circuit.

.. function:: opendssdirect.Sensors.Currents

    Get an array of doubles for the line current measurements; don't use with KWS and KVARS.

.. function:: opendssdirect.Sensors.First

    Set the first sensor active. Returns 0 if none.

.. function:: opendssdirect.Sensors.IsDelta

    Returns 1 if the sensor is connected in delta; otherwise, returns 0.Allows to set 1 if the sensor is connected in delta; otherwise, set 0 (argument).

.. function:: opendssdirect.Sensors.MeteredElement

    Get the full name of the measured element.Set the full name of the measured element.

.. function:: opendssdirect.Sensors.MeteredTerminal

    Get the number of the measured terminal in the measured element.Set the number of the measured terminal in the measured element.

.. function:: opendssdirect.Sensors.Name

    Get the name of the active sensor object.Set the name of the active sensor object.

.. function:: opendssdirect.Sensors.Next

    Set the next sensor active. Returns 0 if none

.. function:: opendssdirect.Sensors.PctError

    Get the assumed percent error in the Sensor measurement. Default is 1.Set the assumed percent error in the Sensor measurement. Default is 1.

.. function:: opendssdirect.Sensors.Reset

    Clears the active sensor.

.. function:: opendssdirect.Sensors.ResetAll

    Clears all Sensors in the active circuit.

.. function:: opendssdirect.Sensors.ReverseDelta

    Returns 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.Allows to set 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.

.. function:: opendssdirect.Sensors.Weight

    Get the weighting factor for this sensor measurement with respect to the other Sensors. Default is 1.Set the weighting factor for this sensor measurement with respect to the other Sensors. Default is 1.

.. function:: opendssdirect.Sensors.kVBase

    Get the voltage base for the sensor measurements. LL for 2 and 3 - phase Sensors, LN for 1-phase Sensors.Set the voltage base for the sensor measurements. LL for 2 and 3 - phase Sensors, LN for 1-phase Sensors.

.. function:: opendssdirect.Sensors.kW

    Get an array of doubles for P measurements; overwrites currents with a new estimate using KVARS.

.. function:: opendssdirect.Sensors.kvar

    Get an array of doubles for Q measurements; overwrites currents with a new estimate using KWS.

