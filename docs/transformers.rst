
Transformers
============


.. automodule:: opendssdirect.Transformers
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Transformers.AllNames

    Get a vector of strings with all Transformer names in the active circuit.

.. function:: opendssdirect.Transformers.Count

    Get the number of Transformers within the active circuit.

.. function:: opendssdirect.Transformers.First

    Set the first Transformer active. Return 0 if no more.

.. function:: opendssdirect.Transformers.IsDelta

    Get the information about if the active winding is delta (1) or wye (0) connection.Set the information about if the active winding is delta (1) or wye (0) connection.

.. function:: opendssdirect.Transformers.MaxTap

    Get the active winding maximum tap in per-unit.Set the active winding maximum tap in per-unit.

.. function:: opendssdirect.Transformers.MinTap

    Get the active winding minimum tap in per-unit.Set the active winding minimum tap in per-unit.

.. function:: opendssdirect.Transformers.Name

    Get the active transformer name and 3, on winding_1_kVA base. Use for 3 winding transformer only.Set the active transformer name and 3, on winding_1_kVA base. Use for 3 winding transformer only.

.. function:: opendssdirect.Transformers.Next

    Set the next Transformer active. Return 0 if no more.

.. function:: opendssdirect.Transformers.NumTaps

    Get the active winding number of tap steps between MinTap and MaxTap.Set the active winding number of tap steps between MinTap and MaxTap

.. function:: opendssdirect.Transformers.NumWindings

    Get the number of windings on this transformer. Allocates memory; set or change this property first.Set the number of windings on this transformer. Allocates memory; set or change this property first.

.. function:: opendssdirect.Transformers.R

    Get the active winding resistance in %.Set the active winding resistance in %.

.. function:: opendssdirect.Transformers.Rneut

    Get the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye.Set the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye.

.. function:: opendssdirect.Transformers.Tap

    Get the active winding tap in per-unit.Set the active winding tap in per-unit.

.. function:: opendssdirect.Transformers.Wdg

    Get the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).Set the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).

.. function:: opendssdirect.Transformers.XfmrCode

    Get the name of an XfrmCode that supplies electrical paraMeters for this transformer.Set the name of an XfrmCode that supplies electrical paraMeters for this transformer.

.. function:: opendssdirect.Transformers.Xhl

    Get the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding Transformers.Set the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding Transformers.

.. function:: opendssdirect.Transformers.Xht

    Get the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.Set the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.

.. function:: opendssdirect.Transformers.Xlt

    Get the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.Set the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.

.. function:: opendssdirect.Transformers.Xneut

    Get the active winding neutral reactance [ohms] for wye connections.Set the active winding neutral reactance [ohms] for wye connections.

.. function:: opendssdirect.Transformers.kV

    Get the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.Set the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.

.. function:: opendssdirect.Transformers.kVA

    Get the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.Set the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.

