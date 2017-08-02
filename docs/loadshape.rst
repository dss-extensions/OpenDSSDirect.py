
LoadShape
=========


.. automodule:: opendssdirect.LoadShape
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.LoadShape.AllNames

    Names of all of the load shapes

.. function:: opendssdirect.LoadShape.Count

    The number of LoadShape objects currently defined in LoadShape collection.

.. function:: opendssdirect.LoadShape.First

    Set the first LoadShape active and return integer index of the LoadShape. Returns 0 if no more.

.. function:: opendssdirect.LoadShape.HrInterval

    Get the fixed interval time value, hours.Set the fixed interval time value, hours.

.. function:: opendssdirect.LoadShape.MinInterval

    Get the fixed interval time value, in minutes.Set the fixed interval time value, in minutes.

.. function:: opendssdirect.LoadShape.Name

    Get the name of the active LoadShape object.Set the name of the active LoadShape object.

.. function:: opendssdirect.LoadShape.Next

    Set the next LoadShape active and return integer index of the LoadShape. Returns 0 if no more.

.. function:: opendssdirect.LoadShape.Normalize

    normalizes the P and Q curves based on either Pbase, Qbase or simply the peak value of the curve.

.. function:: opendssdirect.LoadShape.Npts

    Get the number of points in active LoadShape.Set the number of points in active LoadShape.

.. function:: opendssdirect.LoadShape.PBase

    Get the base for normalizing P curve. If left at zero, the peak value is used.Set the base for normalizing P curve. If left at zero, the peak value is used.

.. function:: opendssdirect.LoadShape.PMult

    Get a variant array of doubles for the P multiplier in the LoadShape.

.. function:: opendssdirect.LoadShape.QBase

    Get the base for normalizing Q curve. If left at zero, the peak value is used.Set the base for normalizing Q curve. If left at zero, the peak value is used.

.. function:: opendssdirect.LoadShape.QMult

    Get a variant array of doubles for the Q multiplier in the LoadShape.

.. function:: opendssdirect.LoadShape.SInterval

    Get the fixed interval data time interval, seconds.Set the fixed interval data time interval, seconds.

.. function:: opendssdirect.LoadShape.TimeArray

    Get a time array in hours corresponding to P and Q multipliers when the Interval = 0.

.. function:: opendssdirect.LoadShape.UseActual

    Get a TRUE/FALSE (1/0) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.Set a TRUE/FALSE (1/0 - Argument) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

