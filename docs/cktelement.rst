
CktElement
==========


.. automodule:: opendssdirect.CktElement
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.CktElement.AllPropertyNames

    All property names of the active device.

.. function:: opendssdirect.CktElement.AllVariableNames

    Variant array of strings listing all the published variable names, if a PCElement. Otherwise, null string.

.. function:: opendssdirect.CktElement.AllVariableValues

    Values of state variables of active element if PC element.

.. function:: opendssdirect.CktElement.BusNames

    Get  Bus definitions to which each terminal is connected. 0‐based array.

.. function:: opendssdirect.CktElement.Close

    Close the specified terminal and phase, if non‐zero.  Else all conductors at terminal.

.. function:: opendssdirect.CktElement.CplxSeqCurrents

    Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

.. function:: opendssdirect.CktElement.CplxSeqVoltages

    Complex double array of Sequence Voltage for all terminals of active circuit element.

.. function:: opendssdirect.CktElement.Currents

    Complex array of currents into each conductor of each terminal

.. function:: opendssdirect.CktElement.CurrentsMagAng

    Currents in magnitude, angle format as a variant array of doubles.

.. function:: opendssdirect.CktElement.DisplayName

    Display name of the object (not necessarily unique)Set the display name of the object (not necessarily unique)

.. function:: opendssdirect.CktElement.EmergAmps

    Emergency Ampere Rating for PD elementsSet the emergency Ampere Rating for PD elements

.. function:: opendssdirect.CktElement.Enabled

    Element is enabledEnable the active circuit element

.. function:: opendssdirect.CktElement.EnergyMeter

    Name of the Energy Meter this element is assigned to

.. function:: opendssdirect.CktElement.GUID

    Globally unique identifier for this object

.. function:: opendssdirect.CktElement.HasSwitchControl

    Bool indicating whether this element has a SwtControl attached.

.. function:: opendssdirect.CktElement.HasVoltControl

    This element has a CapControl or RegControl attached.

.. function:: opendssdirect.CktElement.IsOpen

    Bool indicating if the specified terminal and, optionally, phase is open.

.. function:: opendssdirect.CktElement.Losses

    Total losses in the element: two‐element complex array

.. function:: opendssdirect.CktElement.Name

    Full Name of Active Circuit Element

.. function:: opendssdirect.CktElement.NodeOrder

    Node numbers (representing phases, for example)

.. function:: opendssdirect.CktElement.NormalAmps

    Normal ampere rating for PD ElementsSet the normal ampere rating for PD Elements

.. function:: opendssdirect.CktElement.NumConductors

    Number of Conductors per Terminal

.. function:: opendssdirect.CktElement.NumControls

    Number of controls connected to this device. Use to determine valid range for index into Controller array.

.. function:: opendssdirect.CktElement.NumPhases

    Number of phases

.. function:: opendssdirect.CktElement.NumProperties

    Number of Properties this Circuit Element.

.. function:: opendssdirect.CktElement.NumTerminals

    Number of Terminals on this Circuit Element

.. function:: opendssdirect.CktElement.OCPDevIndex

    Index into Controller list of OCP Device controlling this CktElement

.. function:: opendssdirect.CktElement.OCPDevType

    0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

.. function:: opendssdirect.CktElement.Open

    Open the specified terminal and phase, if non‐zero.  Else all conductors at terminal.

.. function:: opendssdirect.CktElement.PhaseLosses

    Complex array of losses by phase

.. function:: opendssdirect.CktElement.Powers

    Complex array of powers into each conductor of each terminal

.. function:: opendssdirect.CktElement.Residuals

    Residual currents for each terminal: (mag, angle)

.. function:: opendssdirect.CktElement.SeqCurrents

    Double array of symmetrical component currents into each 3‐phase terminal

.. function:: opendssdirect.CktElement.SeqPowers

    Double array of sequence powers into each 3‐phase teminal

.. function:: opendssdirect.CktElement.SeqVoltages

    Double array of symmetrical component voltages at each 3‐phase terminal

.. function:: opendssdirect.CktElement.Variablei

    For PCElement, get the value of a variable by integer index.

.. function:: opendssdirect.CktElement.Voltages

    Complex array of voltages at terminals

.. function:: opendssdirect.CktElement.VoltagesMagAng

    Voltages at each conductor in magnitude, angle form as variant array of doubles.

.. function:: opendssdirect.CktElement.YPrim

    YPrim matrix, column order, complex numbers

