API Reference
=============

.. automodule:: opendssdirect.ActiveClass
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: ActiveClassName

    Name of the active class

.. function:: AllNames

    All element names in the active class

.. function:: Count

    Number of elements in the active class; same as NumElements

.. function:: First

    Sets the first element in the active class to be the active object; if object is a CktElement, ActiveCktElement also points to this element; returns 0 if none

.. function:: Name

    Name of the active element of the active class
    Set the name of the active element of the active class

.. function:: Next

    Sets the next element in the active class to be the active object; if object is a CktElement, ActiveCktElement also points to this element; returns 0 if no more

.. function:: NumElements

    Number of elements in the active class

.. automodule:: opendssdirect.Basic
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllowForms

    Bool flag on the status of allowing forms
    Bool flag to disable forms (once disabled, can't be enabled again)

.. function:: Classes

    List of the names of intrinsic classes

.. function:: ClearAll

    Clears all circuit definitions

.. function:: DataPath

    Default file path for reports, etc.
    Set the default file path for reports, etc.

.. function:: DefaultEditor

    The path name for the default text editor

.. function:: NewCircuit

    Make a new circuit

.. function:: NumCircuits

    Number of Circuits currently defined

.. function:: NumClasses

    Number of DSS intrinsic classes

.. function:: NumUserClasses

    Number of user-defined classes

.. function:: Reset

    Resets DSS Initialization for restarts

.. function:: ShowPanel

    Shows non-MDI child form of the Main DSS Edit Form

.. function:: Start

    Validate the user and start OpenDSS; returns true if successful

.. function:: UserClasses

    List of the names of user-defined classes

.. function:: Version

    Get version string for OpenDSS

.. automodule:: opendssdirect.Bus
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Coorddefined

    Returns true if the X-Y coordinates are defined for the active bus

.. function:: CplxSeqVoltages

    All complex sequence voltages

.. function:: Cust_Duration

    Accumulated customer outage durations, hours

.. function:: Cust_Interrupts

    Annual number of customer-interruptions from this bus

.. function:: Distance

    Distance in km that this bus isfrom the parent EnergyMeter

.. function:: GetUniqueNodeNumber

    Returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus

.. function:: Int_Duration

    Average interruption duration, hours

.. function:: Isc

    Short-circuit current vector, complex

.. function:: Lambda

    Total annual failure rate for active bus after reliability calcs

.. function:: N_Customers

    Returns the total number of customers downline from the active bus after reliability calcs

.. function:: N_interrupts

    Number of interruptions this bus per year

.. function:: Name

    Active bus name; set the active bus by name with `circuit.SetActiveBus(name)`

.. function:: Nodes

    Vector of node numbers defined at the bus in the same order as the voltages

.. function:: NumNodes

    Number of nodes

.. function:: PuVoltage

    Per-unit voltages at the bus, complex

.. function:: SectionID

    Integer ID of the feeder section in which this bus is located

.. function:: SeqVoltages

    Sequence voltages in order of 0, 1, then 2

.. function:: TotalMiles

    Total length of line downline from this bus, miles

.. function:: VLL

    Complex vector of line-to-line voltages for 2- and 3-phase buses; returns -1. for a 1-phase bus; for more than 3 phases, only returns 3 phases

.. function:: VMagAngle

    Bus voltage magnitudes with angles

.. function:: Voc

    Open-circuit voltage vector, complex

.. function:: Voltages

    Bus voltages, complex

.. function:: X

    X coordinate of the bus
    Set the X coordinate of the bus

.. function:: Y

    Y coordinate of the bus
    Set the Y coordinate of the bus

.. function:: YscMatrix

    Short-circuit admittance matrix, complex

.. function:: Zsc0

    Zero-sequence short-circuit impedance looking into the bus, complex

.. function:: Zsc1

    Positive-sequence short-circuit impedance looking into the bus, complex

.. function:: ZscMatrix

    Short-circuit impedance matrix, complex

.. function:: ZscRefresh

    Refresh Zsc and Ysc values; execute after a major change in the circuit

.. function:: kVBase

    Base voltage

.. function:: puVLL

    Complex vector of per-unit line-to-line voltages for 2- and 3-phase buses; returns -1. for a 1-phase bus; for more than 3 phases, only returns 3 phases

.. function:: puVmagAngle

    Bus voltage magnitudes (per unit) with angles

.. automodule:: opendssdirect.CapControls
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Names of all CapControls in the circuit

.. function:: CTRatio

    Transducer ratio from primary current to control current
    Set the transducer ratio from primary current to control current

.. function:: Capacitor

    Name of the Capacitor that is controlled
    Set the Capacitor (by name) that is controlled

.. function:: Count

    Number of CapControls in the active circuit

.. function:: Delay

    Time delay [s] to switch on after arming; control may reset before actuallyswitching
    Set the time delay [s] to switch on after arming; control may reset before actuallyswitching

.. function:: DelayOff

    Time delay [s] before switching off a step; control may reset before actuallyswitching
    Set the time delay [s] before switching off a step; control may reset before actually switching

.. function:: First

    Sets the first CapControl active; returns 0 if none

.. function:: Mode

    Type of automatic controller; for meaning, see CapControlModes
    Set the type of automatic controller; for choices, see CapControlModes

.. function:: MonitoredObj

    Full name of the element that PT and CT are connected to
    Set the element (by full name) that PT and CT are connected to

.. function:: MonitoredTerm

    Terminal number on the element that PT and CT are connected to
    Set the terminal number on the element that PT and CT are connected to

.. function:: Name

    The name of the active CapControl
    Set the active CapControl by name

.. function:: Next

    Sets the next CapControl active; returns 0 if no more

.. function:: OFFSetting

    Threshold to switch off a step; see the particular CapControlModes option for units
    Set the threshold to switch off a step; see the particular CapControlModes option for units

.. function:: ONSetting

    Threshold to arm or switch on a step; see Mode for units
    Set the threshold to arm or switch on a step; see Mode for units

.. function:: PTRatio

    Transducer ratio from primary voltage to control voltage
    Set the transducer ratio from primary voltage to control voltage

.. function:: UseVoltOverride

    Bool flag that enables Vmin and Vmax to override the control mode
    Set the Bool flag that enables Vmin and Vmax to override the control mode

.. function:: Vmax

    With VoltOverride, switch off whenever PT voltage exceeds this level
    Set Vmax; with VoltOverride, switch off whenever PT voltage exceeds this level

.. function:: Vmin

    With VoltOverride, switch on whenever PT voltage drops below this level
    Set Vmin; with VoltOverride, switch on whenever PT voltage drops below this level

.. automodule:: opendssdirect.Capacitors
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AddStep

    Adds one step of the capacitor if available; if successful, returns 1

.. function:: AllNames

    All capacitor names in the circuit

.. function:: AvailableSteps

    Number of steps available in the cap bank to be switched ON

.. function:: Close

    Close all steps of all phases of the capacitor

.. function:: Count

    Number of capacitor objects in the active circuit

.. function:: First

    Sets the first Capacitor active; returns 0 if none

.. function:: IsDelta

    Is the connection a delta
    Set connection type; use `arg==true` for delta and `arg==false` for wye

.. function:: Name

    The name of the active capacitor
    Sets the active capacitor by name

.. function:: Next

    Sets the next Capacitor active; returns 0 if no more

.. function:: NumSteps

    Number of steps
    Set the number of steps

.. function:: Open

    Open all steps, all phases of the capacitor

.. function:: States

    A vector of  integers [0..numsteps‐1] indicating state of each step; if value is ‐1 an error has occurred.

.. function:: SubtractStep

    Subtracts one step of the capacitor; if no more steps, returns 0

.. function:: kV

    Bank kV rating; use LL for 2 or 3 phases, or actual can rating for 1 phase
    Set the bank kV rating; use LL for 2 or 3 phases, or actual can rating for 1 phase

.. function:: kvar

    Total bank kvar, distributed equally among phases and steps
    Set the total bank kvar, distributed equally among phases and steps

.. automodule:: opendssdirect.Circuit
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllBusDistances

    Returns all distances from a bus to its parent EnergyMeter element, which is generally in the substation, as a variant array of doubles. Order corresponds to that of all bus properties.

.. function:: AllBusMagPu

    Similar to AllBusVmag except that the magnitudes are reported in per unit for all buses with kVBase defined.

.. function:: AllBusNames

    The names of all buses in the system. See `:AllNodeNames`.

.. function:: AllBusVMag

    Similar to AllBusVolts except magnitude only (in actual volts). Returns the voltage (magnitude) for every node in the circuit as a complex vector.

.. function:: AllBusVolts

    Returns the voltage (complex) for every node in the circuit as a complex vector. The order of the array is the same as AllNodeNames property. The array is constructed bus-by-bus and then by node at each bus. Thus, all nodes from each bus are grouped together.

.. function:: AllElementLosses

    Returns the watt and var losses in each element of the system as a complex vector. Order is the same as AllElementNames.

.. function:: AllElementNames

    The names of all elements

.. function:: AllNodeDistances

    Returns the distance from all nodes to the parent energy meter that match the designated phase number. Returns a vector of doubles. Matches the order of AllNodeNamesByPhase, AllNodeVmagByPhase, AllNodeVmagPUByPhase.

.. function:: AllNodeNames

    Returns the names of all nodes (busname.nodenumber) in the same order as AllBusVolts, AllBusVmag, and AllBusVMagPu

.. function:: Capacity

    Executes the DSS capacity function. Start is the per unit load multiplier for the current year at which to start the search. Increment is the per unit value by which the load increments for each step of the analysis. The program sets the load at the Start value the PRESENT YEAR (including growth) and increments the load until something in thecircuit reports an overload or undervoltage violation. The function returns the total load at which the violation occurs or the peak load for the present year if no violations.

.. function:: Disable

    Disable a circuit element by name (full name).

.. function:: Enable

    Enable a circuit element by name (full name).

.. function:: EndOfTimeStepUpdate

    Calls EndOfTimeStepCleanup in SolutionAlgs

.. function:: FirstElement

    Sets First element of active class to be the Active element in the active circuit. Returns 0 if none.

.. function:: FirstPCElement

    Sets the first enabled Power Conversion (PC) element in the circuit to be active; if not successful returns a 0

.. function:: FirstPDElement

    Sets the first enabled Power Delivery (PD) element in the circuit to be active; if not successful returns a 0

.. function:: LineLosses

    Watt and var losses in all the Line elements in the circuit, complex

.. function:: Losses

    Watt and var losses in the entire circuit, complex

.. function:: Name

    Name of the active circuit

.. function:: NextElement

    Sets the next element of the active class to be the active element in the active circuit. Returns 0 if no more elements.

.. function:: NextPCElement

    Sets the next enabled Power Conversion (PC) element in the circuit to be active; if not successful returns a 0

.. function:: NextPDElement

    Sets the next enabled Power Delivery (PD) element in the circuit to be active; if not successful returns a 0

.. function:: NumBuses

    Total number of Buses in the circuit

.. function:: NumCktElements

    Number of CktElements in the circuit

.. function:: NumNodes

    Total number of Nodes in the circuit

.. function:: ParentPDElement

    Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable.

.. function:: Sample

    Force all Meters and Monitors to take a sample

.. function:: SaveSample

    Force all Meters and Monitors to save their current buffers

.. function:: SetActiveBus

    Sets the active bus by name. Returns a 0 based index of the bus to use for future direct indexing of bus values returned in arrays. Returns -1 if an error occurs.

.. function:: SetActiveBusi

    Sets the active bus by integer index. The index is 0 based. That is, the first bus has an index of 0. Returns -1 if an error occurs.

.. function:: SetActiveClass

    Sets the active class by name.  Use FirstElement, NextElement to iterate through the class. Returns ‐1 if fails.

.. function:: SetActiveElement

    Activate an element of the active circuit by name. Returns a string with the index of the active element.

.. function:: SubstationLosses

    Watt and var losses in all the Transformer elements in the circuit that are designated as substations

.. function:: TotalPower

    Returns the total power in kW and kvar supplied to the circuit by all Vsource and Isource objects. Does not include Generator objects. Complex.

.. function:: UpdateStorage

    Forces update to all storage classes. Typically done after a solution. Done automatically in intrinsic solution modes.

.. function:: YCurrents

    Vector of doubles containing complex injection currents for the present solution.

.. function:: YNodeOrder

    The names of the nodes in the same order as the Y matrix

.. function:: YNodeVArray

    Complex array of actual node voltages in same order as SystemY matrix.

.. automodule:: opendssdirect.CktElement
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllPropertyNames

    All property names of the active device.

.. function:: AllVariableNames

    Variant array of strings listing all the published variable names, if a PCElement. Otherwise, null string.

.. function:: AllVariableValues

    Values of state variables of active element if PC element.

.. function:: BusNames

    Get  Bus definitions to which each terminal is connected. 0‐based array.

.. function:: Close

    Close the specified terminal and phase, if non‐zero.  Else all conductors at terminal.

.. function:: CplxSeqCurrents

    Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

.. function:: CplxSeqVoltages

    Complex double array of Sequence Voltage for all terminals of active circuit element.

.. function:: Currents

    Complex array of currents into each conductor of each terminal

.. function:: CurrentsMagAng

    Currents in magnitude, angle format as a variant array of doubles.

.. function:: DisplayName

    Display name of the object (not necessarily unique)
    Set the display name of the object (not necessarily unique)

.. function:: EmergAmps

    Emergency Ampere Rating for PD elements
    Set the emergency Ampere Rating for PD elements

.. function:: Enabled

    Element is enabled
    Enable the active circuit element

.. function:: EnergyMeter

    Name of the Energy Meter this element is assigned to

.. function:: GUID

    Globally unique identifier for this object

.. function:: HasSwitchControl

    Bool indicating whether this element has a SwtControl attached.

.. function:: HasVoltControl

    This element has a CapControl or RegControl attached.

.. function:: IsOpen

    Bool indicating if the specified terminal and, optionally, phase is open.

.. function:: Losses

    Total losses in the element: two‐element complex array

.. function:: Name

    Full Name of Active Circuit Element

.. function:: NodeOrder

    Node numbers (representing phases, for example)

.. function:: NormalAmps

    Normal ampere rating for PD Elements
    Set the normal ampere rating for PD Elements

.. function:: NumConductors

    Number of Conductors per Terminal

.. function:: NumControls

    Number of controls connected to this device. Use to determine valid range for index into Controller array.

.. function:: NumPhases

    Number of phases

.. function:: NumProperties

    Number of Properties this Circuit Element.

.. function:: NumTerminals

    Number of Terminals on this Circuit Element

.. function:: OCPDevIndex

    Index into Controller list of OCP Device controlling this CktElement

.. function:: OCPDevType

    0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

.. function:: Open

    Open the specified terminal and phase, if non‐zero.  Else all conductors at terminal.

.. function:: PhaseLosses

    Complex array of losses by phase

.. function:: Powers

    Complex array of powers into each conductor of each terminal

.. function:: Residuals

    Residual currents for each terminal: (mag, angle)

.. function:: SeqCurrents

    Double array of symmetrical component currents into each 3‐phase terminal

.. function:: SeqPowers

    Double array of sequence powers into each 3‐phase teminal

.. function:: SeqVoltages

    Double array of symmetrical component voltages at each 3‐phase terminal

.. function:: Variablei

    For PCElement, get the value of a variable by integer index.

.. function:: Voltages

    Complex array of voltages at terminals

.. function:: VoltagesMagAng

    Voltages at each conductor in magnitude, angle form as variant array of doubles.

.. function:: YPrim

    YPrim matrix, column order, complex numbers

.. automodule:: opendssdirect.Element
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllPropertyNames

    The names of all properties for the active DSS object.

.. function:: Name

    Full Name of Active DSS Object (general element or circuit element)

.. function:: NumProperties

    Number of Properties for the active DSS object.

.. automodule:: opendssdirect.Executive
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Command

    Get i‐th command (with i as a string)

.. function:: CommandHelp

    Get help string for i‐th command (with i as a string)

.. function:: NumCommands

    Number of DSS Executive Commands

.. function:: NumOptions

    Number of DSS Executive Options

.. function:: Option

    Get i‐th option (with i as a string)

.. function:: OptionHelp

    Get help string for i‐th option (with i as a string)

.. function:: OptionValue

    Get present value of i‐th option (with i as a string)

.. automodule:: opendssdirect.Fuses
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

     Names of all Fuses in the circuit

.. function:: Close

    Close the fuse back in and reset.

.. function:: Count

    Number of Fuse elements in the circuit

.. function:: First

    Set the first Fuse to be the active fuse. Returns 0 if none.

.. function:: Idx

    Get/set active fuse by index into the list of fuses. 1 based: 1..count
    Set Fuse active by index into the list of fuses. 1..count

.. function:: IsBlown

    Current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE.

.. function:: MonitoredObj

    Full name of the circuit element to which the fuse is connected.
    Set the full name of the circuit element to which the fuse is connected.

.. function:: MonitoredTerm

    Terminal number to which the fuse is connected.
    Set the terminal number to which the fuse is connected.

.. function:: Name

    Get the name of the active Fuse element
    Set the name of the active Fuse element

.. function:: Next

    Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses.

.. function:: NumPhases

    Number of phases, this fuse.

.. function:: Open

    Manual opening of fuse

.. function:: RatedCurrent

    Multiplier or actual amps for the TCCcurve object. Defaults to 1.0. Multipliy current values of TCC curve by this to get actual amps.
    Set the multiplier or actual amps for the TCCcurve object. Defaults to 1.0. Multipliy current values of TCC curve by this to get actual amps.

.. function:: SwitchedObj

    Full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.
    Set the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.

.. function:: TCCCurve

    Name of the TCCcurve object that determines fuse blowing.
    Set the name of the TCCcurve object that determines fuse blowing.

.. automodule:: opendssdirect.Generators
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    All generator names

.. function:: Count

    Number of Generator Objects in Active Circuit

.. function:: First

    Sets first Generator to be active.  Returns 0 if none.

.. function:: ForcedON

    Indicates whether the generator is forced ON regardles of other dispatch criteria.
    Sets indication whether the generator is forced ON regardles of other dispatch criteria.

.. function:: Idx

    Get/Set active Generator by index into generators list.  1..Count
    Set active Generator by index into generators list.  1..Count

.. function:: Model

    Generator model
    Set the Generator model

.. function:: Name

    Active generator name.
    Sets a generator active by name.

.. function:: Next

    Sets next Generator to be active.  Returns 0 if no more.

.. function:: PF

    Power factor (pos. = producing vars)
    Set the power factor (pos. = producing vars)

.. function:: Phases

    Number of phases
    Set the number of phases

.. function:: RegisterNames

    Array of Names of all generator energy meter registers

.. function:: RegisterValues

    Array of valus in generator energy meter registers.

.. function:: Vmaxpu

    Get the Vmaxpu for Generator Model.
    Set the Vmaxpu for Generator Model.

.. function:: Vminpu

    Get the Vminpu for Generator Model.
    Set the Vminpu for Generator Model.

.. function:: kV

    Voltage base for the active generator, kV
    Set the voltage base for the active generator, kV

.. function:: kVARated

    Get the KVA rating of the generator.
    Set the KVA rating of the generator.

.. function:: kW

    kW output for the active generator. kvar is updated for current power factor.
    Set the kW output for the active generator. kvar is updated for current power factor.

.. function:: kvar

    kvar output for the active generator. Updates power factor based on present kW value.
    Set the kvar output for the active generator. Updates power factor based on present kW value.

.. automodule:: opendssdirect.Isource
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Names of all Isources in the circuit.

.. function:: Amps

    Get the magnitude of the Isource in Amps.
    Set the magnitude of the Isource in Amps.

.. function:: AngleDeg

    Get the phase angle of the Isource in degrees.
    Set the phase angle of the Isource in degrees.

.. function:: Count

    Returns the number of Isource objects currently defined in the active circuit.

.. function:: First

    Set the first ISource to be active; returns 0 if none.

.. function:: Frequency

    Get the frequency of the Isource in Hz.
    Set the frequency of the Isource in Hz.

.. function:: Name

    Get the name of the active Isource object.
    Set the name of the active Isource object.

.. function:: Next

    Set the next ISource to be active; returns 0 if none.

.. automodule:: opendssdirect.Lines
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get the name of all Line Objects.

.. function:: Bus1

    Get the name of bus for terminal 1.
    Set the name of bus for terminal 1.

.. function:: Bus2

    Get the name of bus for terminal 2.
    Set the name of bus for terminal 2.

.. function:: C0

    Get the zero sequence capacitance, nanofarads per unit length.
    Set the zero sequence capacitance, nanofarads per unit length.

.. function:: C1

    Get the positive sequence capacitance, nanofarads per unit length.
    Set the positive sequence capacitance, nanofarads per unit length.

.. function:: CMatrix

    Get the capacitance matrix (full), nanofarads per unit length. Variant array of doubles.

.. function:: Count

    Get the number of Line Objects in Active Circuit.

.. function:: EmergAmps

    Get the emergency (maximum) ampere rating of Line.
    Set the emergency (maximum) ampere rating of Line.

.. function:: First

    Set the first element active. Returns 0 if no Lines. Otherwise, index of the line element.

.. function:: Geometry

    Get the name of the Line geometry code.
    Set the name of the Line geometry code.

.. function:: Length

    Get the length of line section in units compatible with the LineCode definition.
    Set the length of line section in units compatible with the LineCode definition.

.. function:: LineCode

    Get the name of LineCode object that defines the impedances.
    Set the name of LineCode object that defines the impedances.

.. function:: Name

    Get the name of the active Line element.
    Set the name of the Line element to set it active.

.. function:: Next

    Set the next element active. Returns 0 if no Lines. Otherwise, index of the line element.

.. function:: NormAmps

    Get the normal ampere rating of Line.
    Set the normal ampere rating of Line.

.. function:: NumCust

    Get the number of customers on this line section.

.. function:: Parent

    Get the parents of the active Line to be the active Line. Return 0 if no parent or action fails.

.. function:: Phases

    Get the number of phases of the active line object.
    Set the number of phases of the active line object.

.. function:: R0

    Get the zero sequence resistance, ohm per unit length.
    Set the zero sequence resistance, ohm per unit length.

.. function:: R1

    Get the positive sequence resistance, ohm per unit length.
    Set the positive sequence resistance, ohm per unit length.

.. function:: RMatrix

    Get the resistance matrix (full), ohms per unit length. Variant array of doubles.

.. function:: Rg

    Get the earth return value used to compute line impedances at power frequency.
    Set the earth return value used to compute line impedances at power frequency.

.. function:: Rho

    Get the earth resistivity, m-ohms.
    Set the earth resistivity, m-ohms.

.. function:: Spacing

    Get the name of the Line spacing code.
    Set the name of the Line spacing code.

.. function:: Units

    Get the units of the line (distance, check manual for details).
    Set the units of the line (distance, check manual for details).

.. function:: X0

    Get the zero sequence reactance, ohm per unit length.
    Set the zero sequence reactance, ohm per unit length.

.. function:: X1

    Get the positive sequence reactance, ohm per unit length.
    Set the positive sequence reactance, ohm per unit length.

.. function:: XMatrix

    Get the reactance matrix (full), ohms per unit length. Variant array of doubles.

.. function:: Xg

    Get the earth return reactance value used to compute line impedances at power frequency.
    Set the earth return reactance value used to compute line impedances at power frequency.

.. function:: Yprim

    Get the YPrimitive of the active Line.

.. automodule:: opendssdirect.LoadShape
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Names of all of the load shapes

.. function:: Count

    The number of LoadShape objects currently defined in LoadShape collection.

.. function:: First

    Set the first LoadShape active and return integer index of the LoadShape. Returns 0 if no more.

.. function:: HrInterval

    Get the fixed interval time value, hours.
    Set the fixed interval time value, hours.

.. function:: MinInterval

    Get the fixed interval time value, in minutes.
    Set the fixed interval time value, in minutes.

.. function:: Name

    Get the name of the active LoadShape object.
    Set the name of the active LoadShape object.

.. function:: Next

    Set the next LoadShape active and return integer index of the LoadShape. Returns 0 if no more.

.. function:: Normalize

    normalizes the P and Q curves based on either Pbase, Qbase or simply the peak value of the curve.

.. function:: Npts

    Get the number of points in active LoadShape.
    Set the number of points in active LoadShape.

.. function:: PBase

    Get the base for normalizing P curve. If left at zero, the peak value is used.
    Set the base for normalizing P curve. If left at zero, the peak value is used.

.. function:: PMult

    Get a variant array of doubles for the P multiplier in the LoadShape.

.. function:: QBase

    Get the base for normalizing Q curve. If left at zero, the peak value is used.
    Set the base for normalizing Q curve. If left at zero, the peak value is used.

.. function:: QMult

    Get a variant array of doubles for the Q multiplier in the LoadShape.

.. function:: SInterval

    Get the fixed interval data time interval, seconds.
    Set the fixed interval data time interval, seconds.

.. function:: TimeArray

    Get a time array in hours corresponding to P and Q multipliers when the Interval = 0.

.. function:: UseActual

    Get a TRUE/FALSE (1/0) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.
    Set a TRUE/FALSE (1/0 - Argument) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

.. automodule:: opendssdirect.Loads
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    The names of all the loads present in the active circuit. The result is delivered as variant, however, the content of this variant is an array of strings.

.. function:: AllocationFactor

    The AllocationFactor property of the active load. The parameter argument can be filled with a 0.
    Set the AllocationFactor property of the active load. The parameter argument must contain the new value in AllocationFactor for the desired active load. The return value will be equal to 0.

.. function:: CFactor

    The CFactor property of the active load. The parameter argument can be filled with a 0.
    Set the CFactor property of the active load. The parameter argument must contain the new value in CFactor for the desired active load. The return value will be equal to 0.

.. function:: CVRCurve

    The CVRCUrve property of the active load. The parameter argument can be filled with an empty string.
    Set the CVRCurve property for the active load. The parameter argument must contain the Name of the new CVRCurve to be linked to the active load. The return value will be equal to empty.

.. function:: CVRvars

    The CVRvars property of the active load. The parameter argument can be filled with a 0.
    Set the CVRvars property of the active load. The parameter argument must contain the new value in CVRvars for the desired active load. The return value will be equal to 0.

.. function:: CVRwatts

    The CVRWatts property of the active load. The parameter argument can be filled with a 0.
    Set the CVRWatts property of the active load. The parameter argument must contain the new value in CVRWatts for the desired active load. The return value will be equal to 0.

.. function:: Class

    The code number used to separate Loads by class or group. The parameter argument can be filled with a 0.
    The code number used to separate loads by class or group. The parameter argument can be filled with a 0.

.. function:: Count

    Returns the number of load elements within the active circuit. The parameter argument can be filled with a 0.

.. function:: Daily

    The daily property of the active load. The parameter argument can be filled with an empty string.
    Set the daily property for the active load. The parameter argument must contain the Name of the new daily to be linked to the active load. The return value will be equal to empty.

.. function:: Duty

    The duty property of the active load. The parameter argument can be filled with an empty string.
    Set the duty property for the active load. The parameter argument must contain the Name of the new duty to be linked to the active load. The return value will be equal to empty.

.. function:: First

    Allows to set the active load into the first load registered in the active circuit. As a result, this property will return the number 1. The parameter argument can be filled with a 0.

.. function:: Growth

    The Growth property of the active load. The parameter argument can be filled with an empty string.
    Set the Growth property for the active load. The parameter argument must contain the Name of the new Growth to be linked to the active load. The return value will be equal to empty.

.. function:: Idx

    The index of the active load. The parameter argument can be filled with a 0.
    Set the index of the active load. The parameter argument must contain the index of the desired active load. The return value will be equal to 0.

.. function:: IsDelta

    If true, loads are line to line.
    Set whether loads are delta (line to line).

.. function:: Model

    The model of the active load. The parameter argument can be filled with a 0.
    Set the model of the active load using the parameter argument. return a 0.

.. function:: Name

    The Name property of the active load. The parameter argument can be filled with an empty string.
    Set the active load by specifying the Name load. The parameter argument must contain the Name of the load to activate. The return value will be equal to empty.

.. function:: Next

    Set the active load into the next load registered in the active circuit. As a result, this property will set the index of the active load. The parameter argument can be filled with a 0.

.. function:: NumCust

    The number of customer of the active load. The parameter argument can be filled with a 0.
    Set the number of customers of the active load using the parameter argument. return a 0.

.. function:: PF

    The pf property of the active load. The parameter argument can be filled with a 0.
    Set the pf property of the active load. The parameter argument must contain the new value in pf for the desired active load. The return value will be equal to 0.

.. function:: PctMean

    The PctMean property of the active load. The parameter argument can be filled with a 0.
    Set the PctMean property of the active load. The parameter argument must contain the new value in PctMean for the desired active load. The return value will be equal to 0.

.. function:: PctStdDev

    The PctStdDev property of the active load. The parameter argument can be filled with a 0.
    Set the PctStdDev property of the active load. The parameter argument must contain the new value in PctStdDev for the desired active load. The return value will be equal to 0.

.. function:: RelWeighting

    The RelWeight (relative weighting factor) property of the active load. The parameter argument can be filled with a 0.
    Set the RelWeight (relative weighting factor) property of the active load. The parameter argument must contain the new value in RelWeight for the desired active load. The return value will be equal to 0.

.. function:: Rneut

    The RNeut (neutral resistance for wye connected loads) property of the active load. The parameter argument can be filled with a 0.
    Set the RNeut (neutral resistance for wye connected loads) property of the active load. The parameter argument must contain the new value in RNeut for the desired active load. The return value will be equal to 0.

.. function:: Spectrum

    The Spectrum property of the active load. The parameter argument can be filled with an empty string.
    Set the Spectrum property for the active load. The parameter argument must contain the Name of the new Spectrum to be linked to the active load. The return value will be equal to empty.

.. function:: Status




.. function:: Vmaxpu

    The VMaxpu property of the active load. The parameter argument can be filled with a 0.
    Set the VMaxpu property of the active load. The parameter argument must contain the new value in VMaxpu for the desired active load. The return value will be equal to 0.

.. function:: VminEmerg

    The VMinemerg property of the active load. The parameter argument can be filled with a 0.
    Set the VMinemerg property of the active load. The parameter argument must contain the new value in VMinemerg for the desired active load. The return value will be equal to 0.

.. function:: VminNorm

    The VMinnorm property of the active load. The parameter argument can be filled with a 0.
    Set the VMinnorm property of the active load. The parameter argument must contain the new value in VMinnorm for the desired active load. The return value will be equal to 0.

.. function:: Vminpu

    The VMinpu property of the active load. The parameter argument can be filled with a 0.
    Set the VMinpu property of the active load. The parameter argument must contain the new value in VMinpu for the desired active load. The return value will be equal to 0.

.. function:: XfkVA

    The xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor. Affects kW, kvar and pf.) property of the active load. The parameter argument can be filled with a 0.
    Set the xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor. Affects kW, kvar and pf.) property of the active load. The parameter argument must contain the new value in xfKVA for the desired active load. The return value will be equal to 0.

.. function:: Xneut

    The Xneut property of the active load. The parameter argument can be filled with a 0.
    Set the Xneut property of the active load. The parameter argument must contain the new value in Xneut for the desired active load. The return value will be equal to 0.

.. function:: Yearly

    The Yearly property of the active load. The parameter argument can be filled with an empty string.
    Set the Yearly property for the active load. The parameter argument must contain the Name of the new Yearly to be linked to the active load. The return value will be equal to empty.

.. function:: ZipV

    The array of 7 elements (doubles) for ZIP property of the active Load object.

.. function:: kV

    The kV property of the active load. The parameter argument can be filled with a 0.
    Set the kV property of the active load. The parameter argument must contain the new value in kV for the desired active load. The return value will be equal to 0.

.. function:: kVABase

    The kva property of the active load. The parameter argument can be filled with a 0.
    Set the kva property of the active load. The parameter argument must contain the new value in kva for the desired active load. The return value will be equal to 0.

.. function:: kW

    The kW property of the active load. The parameter argument can be filled with a 0.
    Set the kW property of the active load. The parameter argument must contain the new value in kW for the desired active load. The return value will be equal to 0.

.. function:: kWh

    The kWh property of the active load. The parameter argument can be filled with a 0.
    Set the kWh property of the active load. The parameter argument must contain the new value in kWh for the desired active load. The return value will be equal to 0.

.. function:: kWhDays

    The kWhdays property of the active load. The parameter argument can be filled with a 0.
    Set the kWhdays property of the active load. The parameter argument must contain the new value in kWhdays for the desired active load. The return value will be equal to 0.

.. function:: kvar

    The kvar property of the active load. The parameter argument can be filled with a 0.
    Set the kvar property of the active load. The parameter argument must contain the new value in kvar for the desired active load. The return value will be equal to 0.

.. function:: puSeriesRL

    The PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies) property of the active load. The parameter argument can be filled with a 0.
    Set the PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies) property of the active load. The parameter argument must contain the new value in PctSeriesRL for the desired active load. The return value will be equal to 0.

.. automodule:: opendssdirect.Meters
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllBranchesInZone

    A wide string list of all branches in zone of the active Energy Meter object.

.. function:: AllEndElements

    A vector of names of all zone end elements.

.. function:: AllNames

    All Energy Meter names.

.. function:: AllocFactors

    An array of doubles: allocation factors for the active Meter.

.. function:: AvgRepairTime

    The average Repair Time in this Section of the meter zone.

.. function:: CalcCurrent

    The magnitude of the real part of the Calculated Current (normally determined by solution) for the meter to force some behavior on Load Allocation.

.. function:: CloseAllDIFiles

    Close all Demand Interval (DI) files. Necessary at the end of a run.

.. function:: Count

    The number of Energy Meters in the Active Circuit.

.. function:: CountBranches

    The number of branches in active Energy Meter zone (same as sequencelist size).

.. function:: CountEndElements

    The number of zone end elements in the active meter zone.

.. function:: CustInterrupts

    The total customer interruptions for this meter zone based on reliability calcs.

.. function:: DIFilesAreOpen

    Returns a global flag (1=true, 0=false) to indicate if Demand Interval (DI) files have been properly opened.

.. function:: DoReliabilityCalc

    calculates SAIFI, etc. if the Argument is equal to 1 assume restoration, otherwise it will not.

.. function:: FaultRateXRepairHrs

    The sum of Fault Rate time Repair Hours in this section of the meter zone.

.. function:: First

    Set the first Energy Meter active. Returns 0 if no Monitors.

.. function:: MeteredElement

    The name of the metered element (considering the active Energy Meter).
    Set the name of the metered element (considering the active Energy Meter).

.. function:: MeteredTerminal

    The number of metered terminal by the active Energy Meter.
    Set the number of metered terminal by the active Energy Meter.

.. function:: Name

    The active Energy Meter's name.
    Set the active Energy Meter's name.

.. function:: Next

    Set the next energy Meter Active. Returns 0 if no more.

.. function:: NumSectionBranches

    The number of branches (Lines) in the active section.

.. function:: NumSectionCustomers

    The number of customers in the active section.

.. function:: NumSections

    The number of feeder sections in this meter's zone.

.. function:: OCPDeviceType

    The type of OCP device: {1=fuse | 2+ recloser | 3= relay}.

.. function:: OpenAllDIFiles

    Opens Demand Interval (DI) files. Returns 0.

.. function:: PeakCurrent

    Returns an array of doubles with the Peak Current Property.

.. function:: RegisterNames

    Strings containing the names of the registers.

.. function:: RegisterValues

    Values contained in the Meter registers for the active Meter.

.. function:: Reset

    Resets the active Meter object.

.. function:: ResetAll

    Resets all Meter object.

.. function:: SAIDI

    The SAIDI for this meter zone. Execute DoreliabilityCalc first.

.. function:: SAIFI

    SAIFI for this meter's zone. Execute reliability calc method first.

.. function:: SAIFIkW

    The SAIFI based on kW rather than number of customers. Get after reliability calcs.

.. function:: Sample

    Causes active meter to take a sample.

.. function:: SampleAll

    Causes all Energy Meters to take a sample of the present state. Returns 0.

.. function:: Save

    Causes active meter to save its current sample buffer to its meter stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

.. function:: SaveAll

    save all Energy Meter buffers to their respective file streams. Returns 0.

.. function:: SectSeqidx

    The Sequence Index of the branch at the head of this section.

.. function:: SectTotalCust

    The total customers down line from this section.

.. function:: SeqListSize

    The size of Sequence List.

.. function:: SequenceList

    The index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.
    Set the index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.

.. function:: SetActiveSection

    Set the designated section (argument) if the index is valid.

.. function:: SumBranchFltRates

    The sum of the branch fault rates in this section of the meter's zone.

.. function:: TotalCustomers

    The total number of customers in this zone (down line from the Energy Meter).

.. function:: Totals

    The totals for all registers of all Meters.

.. automodule:: opendssdirect.Monitors
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    An array of all Monitor names (array of strings).

.. function:: ByteStream

    A byte array containing monitor stream values. Make sure a 'save' is done first (standard solution modes do this automatically).

.. function:: Count

    The number of Monitors.

.. function:: Element

    The full name of element being monitored by the active Monitor.
    Set the full name of element being monitored by the active Monitor.

.. function:: FileName

    The name of the CSV file associated with active monitor.

.. function:: FileVersion

    The Monitor File version (integer).

.. function:: First

    Set the first monitor active. Returns 0 if no Monitors.

.. function:: Mode

    The monitor mode (bitmask integer - see DSS Help).
    Set the monitor mode (bitmask integer - see DSS Help).

.. function:: Name

    The active Monitor object by name.
    Set the active Monitor object by name.

.. function:: Next

    Set the next monitor active. Returns 0 if no more.

.. function:: Process

    Post-process monitor samples taken so far, e.g., Pst for mode = 4.

.. function:: ProcessAll

    Makes that all Monitors post-process the data taken so far.

.. function:: Reset

    Resets the active Monitor object.

.. function:: ResetAll

    Resets all Monitor object.

.. function:: Sample

    Causes active monitor to take a sample.

.. function:: SampleAll

    Causes all Monitors to take a sample of the present state. Returns 0.

.. function:: Save

    Causes active monitor to save its current sample buffer to its monitor stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

.. function:: SaveAll

    Save all Monitor buffers to their respective file streams. Returns 0.

.. function:: Show

    Converts monitor file into text and displays with text editor.

.. function:: Terminal

    The terminal number of element being monitored.
    Set the terminal number of element being monitored.

.. automodule:: opendssdirect.PDElements
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AccumulatedL

    Get the accumulated failure rate for this branch on down line.

.. function:: Count

    Get number of PDElements in active circuit.

.. function:: FaultRate

    Get the number of failures per year. For LINE elements: Number of failures per unit length per year.
    Set the number of failures per year. For LINE elements: Number of failures per unit length per year.

.. function:: First

    Set the first enabled PD element to be the active element. Returns 0 if none found.

.. function:: FromTerminal

    Get the number of the terminal of active PD element that is on the 'from' side. This is set after the meter zone is determined.

.. function:: IsShunt

    returns 1 if the PD element should be treated as a shunt element rather than a series element. Applies to capacitor and reactor elements in particular.

.. function:: Lambda

    Get the failure rate for this branch. Faults per year including length of line.

.. function:: Name

    Get the name of the active PDElement, returns null string if active element id not PDElement.
    Set the name of the active PDElement, returns null string if active element id not PDElement.

.. function:: Next

    Set the next enabled PD element to be the active element. Returns 0 if none found.

.. function:: NumCustomers

    Get the number of customers in this branch.

.. function:: ParentPDElement

    Set the parent PD element to be the active circuit element. Returns 0 if no more elements upline.

.. function:: PctPermanent

    Get the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.
    Set the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

.. function:: RepairTime

    Get the average time to repair a permanent fault on this branch, hours.

.. function:: SectionID

    Get the integer ID of the feeder section that this PDElement branch is part of.

.. function:: TotalCustomers

    Get the total number of customers from this branch to the end of the zone.

.. function:: TotalMiles

    Get the total miles of line from this element to the end of the zone. For recloser siting algorithm.

.. automodule:: opendssdirect.PVsystems
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get a vector of strings with names of all PVSystems in active circuit.

.. function:: Count

    The number of PVSystem objects currently defined in the active circuit.

.. function:: First

    Set the first PVSystem to be active; returns 0 if none.

.. function:: Idx

    Get the active PVSystem by index; 1..Count.
    Set the active PVSystem by index; 1..Count.

.. function:: Irradiance

    Get the present value of the Irradiance property in W/sq-m.
    Set the present value of the Irradiance property in W/sq-m.

.. function:: Name

    Get the name of the active PVSystem Object.
    Set the name of the active PVSystem Object.

.. function:: Next

    Set the next PVSystem to be active; returns 0 if none.

.. function:: kVARated

    Get the rated kVA.
    Set the rated kVA.

.. function:: kW

    Get the kW output.

.. function:: kvar

    Get the kvar value.
    Set the kvar value.

.. function:: pf

    Get the power factor value.
    Set the power factor value.

.. automodule:: opendssdirect.Parser
        :members:
        :undoc-members:
        :show-inheritance:

.. automodule:: opendssdirect.Properties
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Description

    The description of the active property.

.. function:: Name

    The name of the active property.

.. function:: Value

    Read value of a property or Write value of a property

.. automodule:: opendssdirect.Reclosers
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get a vector of strings with names of all Reclosers in active circuit.

.. function:: Close

    Close the switched object controlled by the recloser. Resets recloser to first operation.

.. function:: Count

    Get number of Reclosers in active circuit.

.. function:: First

    Set first recloser to be active Circuit Element. Returns 0 if none.

.. function:: GroundInst

    Get the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.
    Set the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.

.. function:: GroundTrip

    Get the ground (3I0) trip multiplier or actual amps.
    Set the ground (3I0) trip multiplier or actual amps.

.. function:: Idx

    Get the active recloser by index into the recloser list. 1..Count.
    Set the active recloser by index into the recloser list. 1..Count.

.. function:: MonitoredObj

    Get the full name of object this Recloser is monitoring.
    Set the full name of object this Recloser is monitoring.

.. function:: MonitoredTerm

    Get the terminal number of Monitored Object for the Recloser.
    Set the terminal number of Monitored Object for the Recloser.

.. function:: Name

    Get the name of the active Recloser Object.
    Set the name of the active Recloser Object.

.. function:: Next

    Set next recloser to be active Circuit Element. Returns 0 if none.

.. function:: NumFast

    Get the number of fast shots.
    Set the number of fast shots.

.. function:: Open

    Open recloser's controlled element and lock out the recloser.

.. function:: PhaseInst

    Get the phase instantaneous curve multiplier or actual amps.
    Set the phase instantaneous curve multiplier or actual amps.

.. function:: PhaseTrip

    Get the phase trip curve multiplier or actual amps.
    Set the phase trip curve multiplier or actual amps.

.. function:: RecloseIntervals

    Get a vector of doubles: reclose intervals (s) between shots.

.. function:: Shots

    Get the number of shots to lockout (fast + delayed).
    Set the number of shots to lockout (fast + delayed).

.. function:: SwitchedObj

    Get the full name of the circuit element that is being switched by this Recloser.
    Set the full name of the circuit element that is being switched by this Recloser.

.. function:: SwitchedTerm

    Get the terminal of the controlled device being switched by the Recloser.
    Set the terminal of the controlled device being switched by the Recloser.

.. automodule:: opendssdirect.RegControls
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get a vector of strings containing all RegControl names.

.. function:: CTPrimary

    Get the CT primary ampere rating (secondary is 0.2 amperes).
    Set the CT primary ampere rating (secondary is 0.2 amperes).

.. function:: Count

    Get the number of RegControl objects in Active Circuit.

.. function:: Delay

    Get the time delay [s] after arming before the first tap change. Control may reset before actually changing taps.
    Set the time delay [s] after arming before the first tap change. Control may reset before actually changing taps.

.. function:: First

    Set the first RegControl active. Returns 0 if no more.

.. function:: ForwardBand

    Get the regulation bandwidth in forward direction, centered on Vreg.
    Set the regulation bandwidth in forward direction, centered on Vreg.

.. function:: ForwardR

    Get the LDC R settings in Volts.
    Set the LDC R settings in Volts.

.. function:: ForwardVreg

    Get the target voltage in the forward direction, on PT secondary base.
    Set the target voltage in the forward direction, on PT secondary base.

.. function:: ForwardX

    Get the LDC X settings in Volts.
    Set the LDC X settings in Volts.

.. function:: IsInverseTime

    Get the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.
    Set the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.

.. function:: IsReversible

    Get the setting in the reverse direction, usually not applicable to substation Transformers.
    Set the different settings for the reverse direction (see Manual for details), usually not applicable to substation Transformers.

.. function:: MaxTapChange

    Get the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.
    Set the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.

.. function:: MonitoredBus

    Get the name of the remote regulated bus, in lieu of LDC settings.
    Set the name of the remote regulated bus, in lieu of LDC settings.

.. function:: Name

    Get the active RegControl name.
    Set the active RegControl name.

.. function:: Next

    Set the next RegControl active. Returns 0 if no more

.. function:: PTRatio

    Get the PT ratio for voltage control settings.
    Set the PT ratio for voltage control settings.

.. function:: ReverseBand

    Get the bandwidth in reverse direction, centered on reverse Vreg.
    Set the bandwidth in reverse direction, centered on reverse Vreg.

.. function:: ReverseR

    Get the reverse LDC R settings in Volts.
    Set the reverse LDC R settings in Volts.

.. function:: ReverseVreg

    Get the target voltage in the reverse direction, on PT secondary base.
    Set the target voltage in the reverse direction, on PT secondary base.

.. function:: ReverseX

    Get the reverse LDC X settings in Volts.
    Set the reverse LDC X settings in Volts.

.. function:: TapDelay

    Get the time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.
    Set the time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.

.. function:: TapNumber

    Get the tap number.
    Set the tap number.

.. function:: TapWinding

    Get the tapped winding number.
    Set the tapped winding number.

.. function:: Transformer

    Get the name of the transformer this regulator controls.
    Set the name of the transformer this regulator controls.

.. function:: VoltageLimit

    Get the first house voltage limit on PT secondary base. Setting to 0 disables this function.
    Set the first house voltage limit on PT secondary base. Setting to 0 disables this function.

.. function:: Winding

    Get the winding number for PT and CT connections.
    Set the winding number for PT and CT connections.

.. automodule:: opendssdirect.Relays
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get a vector of strings containing names of all relay elements.

.. function:: Count

    Get number of Relays in active circuit.

.. function:: First

    Set first relay active. If none, returns 0.

.. function:: Idx

    Get the active relay by index into the Relay list. 1..Count.
    Set the active relay by index into the Relay list. 1..Count.

.. function:: MonitoredObj

    Get the full name of the object this relay is monitoring.
    Set the full name of the object this relay is monitoring.

.. function:: MonitoredTerm

    Get the number of terminal of monitored element that this relay is monitoring.
    Set the number of terminal of monitored element that this relay is monitoring.

.. function:: Name

    Get the name of the active Relay.
    Set the name of the active Relay.

.. function:: Next

    Set next relay active. If none, returns 0.

.. function:: SwitchedObj

    Get the full name of element that will switched when relay trips.
    Set the full name of element that will switched when relay trips.

.. function:: SwitchedTerm

    Get the number of terminal of the switched object that will be opened when the relay trips.
    Set the number of terminal of the switched object that will be opened when the relay trips.

.. automodule:: opendssdirect.Sensors
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Returns a vector of sensor names.

.. function:: Count

    Get number of Sensors in active circuit.

.. function:: Currents

    Get an array of doubles for the line current measurements; don't use with KWS and KVARS.

.. function:: First

    Set the first sensor active. Returns 0 if none.

.. function:: IsDelta

    Returns 1 if the sensor is connected in delta; otherwise, returns 0.
    Allows to set 1 if the sensor is connected in delta; otherwise, set 0 (argument).

.. function:: MeteredElement

    Get the full name of the measured element.
    Set the full name of the measured element.

.. function:: MeteredTerminal

    Get the number of the measured terminal in the measured element.
    Set the number of the measured terminal in the measured element.

.. function:: Name

    Get the name of the active sensor object.
    Set the name of the active sensor object.

.. function:: Next

    Set the next sensor active. Returns 0 if none

.. function:: PctError

    Get the assumed percent error in the Sensor measurement. Default is 1.
    Set the assumed percent error in the Sensor measurement. Default is 1.

.. function:: Reset

    Clears the active sensor.

.. function:: ResetAll

    Clears all Sensors in the active circuit.

.. function:: ReverseDelta

    Returns 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.
    Allows to set 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.

.. function:: Weight

    Get the weighting factor for this sensor measurement with respect to the other Sensors. Default is 1.
    Set the weighting factor for this sensor measurement with respect to the other Sensors. Default is 1.

.. function:: kVBase

    Get the voltage base for the sensor measurements. LL for 2 and 3 - phase Sensors, LN for 1-phase Sensors.
    Set the voltage base for the sensor measurements. LL for 2 and 3 - phase Sensors, LN for 1-phase Sensors.

.. function:: kW

    Get an array of doubles for P measurements; overwrites currents with a new estimate using KVARS.

.. function:: kvar

    Get an array of doubles for Q measurements; overwrites currents with a new estimate using KWS.

.. automodule:: opendssdirect.Settings
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllocationFactors

    Set all load allocation factors for all loads defined by XFKVA property to this value.

.. function:: AllowDuplicates

    Get if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}.
    Set if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}.

.. function:: AutoBusList

    Get the list of Buses or (File=xxxxx) syntax for the AutoAdd solution mode.
    Set the list of Buses or (File=xxxxx) syntax for the AutoAdd solution mode.

.. function:: CktModel

    Get {dssMultiphase* | dssPositiveSeq} Indicate if the circuit model is positive sequence.
    Set {dssMultiphase* | dssPositiveSeq} Indicate if the circuit model is positive sequence.

.. function:: EmergVmaxpu

    Get the per unit maximum voltage for Emergency conditions.
    Set the per unit maximum voltage for Emergency conditions.

.. function:: EmergVminpu

    Get the per unit minimum voltage for Emergency conditions.
    Set the per unit minimum voltage for Emergency conditions.

.. function:: LossRegs

    Get the array of Integers defining Energy Meter registers to use for computing Losses.

.. function:: LossWeight

    Get the weighting factor applied to Loss register values.
    Set the weighting factor applied to Loss register values.

.. function:: NormVmaxpu

    Get the per unit maximum voltage for Normal conditions.
    Set the per unit maximum voltage for Normal conditions.

.. function:: NormVminpu

    Get the per unit minimum voltage for Normal conditions.
    Set the per unit minimum voltage for Normal conditions.

.. function:: PriceCurve

    Get the name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.
    Set the name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

.. function:: PriceSignal

    Get the price signal for the circuit.
    Set the price signal for the circuit.

.. function:: Trapezoidal

    Get {True (1) | False (0)} value of trapezoidal integration flag in Energy Meters.
    Set {True (1) | False (0)} value of trapezoidal integration flag in Energy Meters.

.. function:: UERegs

    Get the array of Integers defining Energy Meter registers to use for computing UE.

.. function:: UEWeight

    Get the weighting factor applied to UE register values.
    Set the weighting factor applied to UE register values.

.. function:: VoltageBases

    Get the array of doubles defining the legal voltage bases in kV L-L.

.. function:: ZoneLock

    Get the status of Lock zones on energy Meters to prevent rebuilding if a circuit change occurs: {1= true, 0= False}.
    Set the status of Lock zones on energy Meters to prevent rebuilding if a circuit change occurs: {1= true, 0= False}.

.. automodule:: opendssdirect.Solution
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AddType

    The type of device to add in AutoAdd Mode: {dssGen (default)|dssCap}.
    Modifies the type of device to add in AutoAdd Mode: {dssGen (default)|dssCap}.

.. function:: Algorithm

    The base solution algorithm: {dssNormalSolve | dssNewtonSolve}.
    Modifies the base solution algorithm: {dssNormalSolve | dssNewtonSolve}.

.. function:: BuildYMatrix

    Forces building of the System Y matrix according to the argument: {1= series elements only | 2= Whole Y matrix}.

.. function:: Capkvar

    The capacitor kvar for adding in AutoAdd mode.
    Set the capacitor kvar for adding in AutoAdd mode.

.. function:: CheckControls

    Performs the normal process for sampling and executing Control Actions and Fault Status and rebuilds Y if necessary.

.. function:: CheckFaultStatus

    Executes status check on all fault objects defined in the circuit. Returns 0.

.. function:: Cleanup

    Update storage, invcontrol, etc., at end of time step.

.. function:: ControlActionsDone

    Indicates that the control actions are done: {1 done, 0 not done}.
    Modifies the flag to indicate that the control actions are done: {1 done, 0 not done}.

.. function:: ControlIterations

    The current value of the control iteration counter.
    Modifies the current value of the control iteration counter.

.. function:: ControlMode

    The mode for control devices: {dssStatic (default) | dssEvent | dssTime}.
    Modifies the mode for control devices: {dssStatic (default) | dssEvent | dssTime}.

.. function:: Converged

    Indicates whether the circuit solution converged (1 converged | 0 not converged).
    Modifies the converged flag (1 converged | 0 not converged).

.. function:: Convergence

    The solution convergence tolerance.
    Set the solution convergence tolerance.

.. function:: DblHour

    The hour as a double, including fractional part.
    Set the hour as a double, including fractional part.

.. function:: DefaultDaily

    The default daily load shape (defaults to 'Default').
    Set the default daily load shape (defaults to 'Default').

.. function:: DefaultYearly

    The default yearly load shape (defaults to 'Default').
    Set the default yearly load shape (defaults to 'Default').

.. function:: DoControlActions

    Pops control actions off the control queue and dispatches to the proper control element.

.. function:: EventLog

    Returns an array of strings containing the Event Log.

.. function:: FinishTimeStep

    Call cleanup, sample Monitors, and increment time at end of time step.

.. function:: Frequency

    The frequency for the next solution.
    Set the frequency for the next solution.

.. function:: GenMult

    The default multiplier applied to generators (like LoadMult).
    Set the default multiplier applied to generators (like LoadMult).

.. function:: GenPF

    The pf for generators in AutoAdd mode.
    Set the pf for generators in AutoAdd mode.

.. function:: GenkW

    The generator kW for AutoAdd mode.
    Set the generator kW for AutoAdd mode.

.. function:: Hour

    The present hour (See DSS help).
    Modifies the present hour (See DSS help).

.. function:: InitSnap

    Initializes some variables for snap shot power flow. SolveSnap does this automatically.

.. function:: Iterations

    Return the number of iterations taken for the last solution.

.. function:: LDCurve

    The Load-Duration Curve name for LD modes.
    Set the Load-Duration Curve name for LD modes.

.. function:: LoadModel

    The Load Model: {dssPowerFlow (default)|dssAdmittance}.
    Modifies the Load Model: {dssPowerFlow (default)|dssAdmittance}.

.. function:: LoadMult

    The default load multiplier applied to all non-fixed loads.
    Set the default load multiplier applied to all non-fixed loads.

.. function:: MaxControlIterations

    The maximum allowable control iterations.
    Modifies the maximum allowable control iterations.

.. function:: MaxIterations

    The Maximum number of iterations used to solve the circuit.
    Modifies the Maximum number of iterations used to solve the circuit.

.. function:: Mode

    The present solution mode (See DSS help).
    Modifies the present solution mode (See DSS help).

.. function:: ModeID

    The ID (text) of the present solution mode.

.. function:: MostIterationsDone

    The max number of iterations required to converge at any control iteration of the most recent solution.

.. function:: Number

    The number of solutions to perform for MonteCarlo and time series simulations.
    Modifies the number of solutions to perform for MonteCarlo and time series simulations.

.. function:: PctGrowth

    The percent default annual load growth rate.
    Set the percent default annual load growth rate.

.. function:: ProcessTime

    The time required (microseconds) to perform the latest solution time step, this time does not includes the time required for sampling meters/monitors.

.. function:: Random

    The randomization mode for random variables 'Gaussian' or 'Uniform'.
    Modifies the randomization mode for random variables 'Gaussian' or 'Uniform'.

.. function:: SampleControlDevices

    Executes a sampling of all intrinsic control devices, which push control actions into the control queue.

.. function:: SampleDoControlActions

    Sample controls and then process the control queue for present control mode and dispatch control actions. Returns 0.

.. function:: Seconds

    The seconds from top of the hour.
    Set the seconds from top of the hour.

.. function:: Solve

    Executes the solution for the present solution mode. Returns 0.

.. function:: SolveDirect

    Executes a direct solution from the system Y matrix, ignoring compensation currents of loads, generators (includes Yprim only).

.. function:: SolveNoControl

    Is similar to SolveSnap except no control actions are checked or executed.

.. function:: SolvePFlow

    Solves using present power flow method. Iterative solution rather than direct solution.

.. function:: SolvePlusControl

    Executes a power flow solution (SolveNoControl) plus executes a CheckControlActions that executes any pending control actions.

.. function:: StepSize

    The step size for the next solution.
    Set the step size for the next solution.

.. function:: StepSizeHr

    Set the step size in Hours.

.. function:: StepSizeMin

    Set the step size in minutes.

.. function:: SystemYChanged

    Indicates if elements of the System Y have been changed by recent activity. If changed returns 1; otherwise 0.

.. function:: TimeTimeStep

    The time required (microseconds) to perform the latest solution time step including the time required for sampling meters/monitors

.. function:: TotalIterations

    The total iterations including control iterations for most recent solution.

.. function:: TotalTime

    Get the accumulated time required (microseconds) to perform the simulation.
    Set the accumulated time required (microseconds) to perform the simulation.

.. function:: Year

    The present Year (See DSS help).
    Modifies the present Year (See DSS help).

.. automodule:: opendssdirect.SwtControls
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Action

    Get the open (1) or close (2) action of the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action.
    Set open (1) or close (2) the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action (see manual for details).

.. function:: AllNames

    Get a vector of strings with all SwtControl names in the active circuit.

.. function:: Count

    Get the total number of SwtControls in the active circuit.

.. function:: Delay

    Get the time delay [s] between arming and opening or closing the switch. Control may reset before actually operating the switch.
    Set the time delay [s] between arming and opening or closing the switch. Control may reset before actually operating the switch.

.. function:: First

    Set the first SwtControl active. Returns 0 if no more.

.. function:: IsLocked

    Get the lock state: {1 locked | 0 not locked}.
    Set the lock to prevent both manual and automatic switch operation.

.. function:: Name

    Get the name of the active SwtControl.
    Set a SwtControl active by name.

.. function:: Next

    Set the next SwtControl active. Returns 0 if no more.

.. function:: SwitchedObj

    Get the name of the switched object by the active SwtControl.
    Set the switched object by name.

.. function:: SwitchedTerm

    Get the terminal number where the switch is located on the SwitchedObj.
    Set the terminal number where the switch is located on the SwitchedObj.

.. automodule:: opendssdirect.Topology
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: ActiveBranch

    The index of the active Branch.

.. function:: ActiveLevel

    Get the topological depth of the active branch.

.. function:: AllIsolatedBranches

    Get a vector of all isolated branch names.

.. function:: AllIsolatedLoads

    Get a vector of all isolated load names.

.. function:: AllLoopedPairs

    Get a vector of all looped element names, by pairs.

.. function:: BranchName

    Get the name of the active branch.
    Set the name of the active branch.

.. function:: BusName

    Get the name of the active Bus.
    Set the Bus active by name.

.. function:: First

    Set the first branch active, returns 0 if none.

.. function:: FirstLoad

    Set as active load the first load at the active branch, return index or 0 if none.

.. function:: ForwardBranch

    Move forward in the tree, return index of new active branch or 0 if no more.

.. function:: LoopedBranch

    Move to looped branch, return index or 0 if none.

.. function:: Next

    Set the next branch active, returns 0 if none.

.. function:: NextLoad

    Set as active load the next load at the active branch, return index or 0 if none.

.. function:: NumIsolatedBranches

    Get the number of isolated branches (PD elements and capacitors).

.. function:: NumIsolatedLoads

    Get the number of isolated loads.

.. function:: NumLoops

    Get the number of loops.

.. function:: ParallelBranch

    Mode to directly parallel branch, return index or 0 if none.

.. automodule:: opendssdirect.Transformers
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get a vector of strings with all Transformer names in the active circuit.

.. function:: Count

    Get the number of Transformers within the active circuit.

.. function:: First

    Set the first Transformer active. Return 0 if no more.

.. function:: IsDelta

    Get the information about if the active winding is delta (1) or wye (0) connection.
    Set the information about if the active winding is delta (1) or wye (0) connection.

.. function:: MaxTap

    Get the active winding maximum tap in per-unit.
    Set the active winding maximum tap in per-unit.

.. function:: MinTap

    Get the active winding minimum tap in per-unit.
    Set the active winding minimum tap in per-unit.

.. function:: Name

    Get the active transformer name and 3, on winding_1_kVA base. Use for 3 winding transformer only.
    Set the active transformer name and 3, on winding_1_kVA base. Use for 3 winding transformer only.

.. function:: Next

    Set the next Transformer active. Return 0 if no more.

.. function:: NumTaps

    Get the active winding number of tap steps between MinTap and MaxTap.
    Set the active winding number of tap steps between MinTap and MaxTap

.. function:: NumWindings

    Get the number of windings on this transformer. Allocates memory; set or change this property first.
    Set the number of windings on this transformer. Allocates memory; set or change this property first.

.. function:: R

    Get the active winding resistance in %.
    Set the active winding resistance in %.

.. function:: Rneut

    Get the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye.
    Set the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye.

.. function:: Tap

    Get the active winding tap in per-unit.
    Set the active winding tap in per-unit.

.. function:: Wdg

    Get the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).
    Set the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).

.. function:: XfmrCode

    Get the name of an XfrmCode that supplies electrical paraMeters for this transformer.
    Set the name of an XfrmCode that supplies electrical paraMeters for this transformer.

.. function:: Xhl

    Get the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding Transformers.
    Set the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding Transformers.

.. function:: Xht

    Get the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.
    Set the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.

.. function:: Xlt

    Get the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.
    Set the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding Transformers only.

.. function:: Xneut

    Get the active winding neutral reactance [ohms] for wye connections.
    Set the active winding neutral reactance [ohms] for wye connections.

.. function:: kV

    Get the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.
    Set the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.

.. function:: kVA

    Get the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.
    Set the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.

.. automodule:: opendssdirect.Vsources
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: AllNames

    Get the names of all Vsources

.. function:: AngleDeg

    Get the source phase angle of first phase in degrees.
    Set the source phase angle of first phase in degrees.

.. function:: BasekV

    Get the source voltage in kV.
    Set the source voltage in kV.

.. function:: Count

    The number of VSource objects currently defined in the active circuit.

.. function:: First

    Set the first VSource to be active; returns 0 if none.

.. function:: Frequency

    Get the source frequency in Hz.
    Set the source frequency in Hz.

.. function:: Name

    Get the name of the active VSource.
    Set the name of the active VSource.

.. function:: Next

    Set the next VSource to be active; returns 0 if none.

.. function:: PU

    Get the source voltage in pu.
    Set the source voltage in pu.

.. function:: Phases

    Get the number of phases of the active VSource.
    Set the number of phases of the active VSource.

.. automodule:: opendssdirect.XYCurves
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Count

    Get number of XYCurves in active circuit.

.. function:: First

    Set first XYCurves object active; returns 0 if none.

.. function:: Name

    Get the name of the active XYCurve Object.
    Set the name of the active XYCurve Object.

.. function:: Next

    Set next XYCurves object active; returns 0 if none.

.. function:: Npts

    Get the number of points in X-Y curve.
    Set the number of points in X-Y curve.

.. function:: X

    Get the interpolated value after setting Y.
    Set the X value.

.. function:: XArray

    Get the X values as a vector of doubles. Set Npts to max number expected if setting.

.. function:: XScale

    Get the factor to scale X values from original curve.
    Set the factor to scale X values from original curve.

.. function:: XShift

    Get the amount to shift X value from original curve.
    Set the amount to shift X value from original curve.

.. function:: Y

    Get the interpolated value after setting X.
    Set the Y value.

.. function:: YArray

    Get the Y values as a vector of doubles. Set Npts to max number expected if setting.

.. function:: YScale

    Get the factor to scale Y values from original curve.
    Set the factor to scale Y values from original curve.

.. function:: YShift

    Get the amount to shift Y value from original curve.
    Set the amount to shift Y value from original curve.

.. automodule:: opendssdirect.dss
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: ActiveClass

    None

.. function:: Basic

    None

.. function:: Bus

    None

.. function:: CapControls

    None

.. function:: Capacitors

    None

.. function:: Circuit

    None

.. function:: CktElement

    None

.. function:: Element

    None

.. function:: Executive

    None

.. function:: Fuses

    None

.. function:: Generators

    None

.. function:: Isource

    None

.. function:: Lines

    None

.. function:: LoadShape

    None

.. function:: Loads

    None

.. function:: Meters

    None

.. function:: Monitors

    None

.. function:: PDElements

    None

.. function:: PVsystems

    None

.. function:: Parser

    None

.. function:: Properties

    None

.. function:: Reclosers

    None

.. function:: RegControls

    None

.. function:: Relays

    None

.. function:: Sensors

    None

.. function:: Settings

    None

.. function:: Solution

    None

.. function:: SwtControls

    None

.. function:: Topology

    None

.. function:: Transformers

    None

.. function:: Vsources

    None

.. function:: XYCurves

    None

.. function:: dss

    None

.. function:: dss_lib

    An instance of this class represents a loaded dll/shared
    library, exporting functions using the standard C calling
    convention (named 'cdecl' on Windows).

    The exported functions can be accessed as attributes, or by
    indexing with the function name.  Examples:

    <obj>.qsort -> callable object
    <obj>['qsort'] -> callable object

    Calling the functions releases the Python GIL during the call and
    reacquires it afterwards.


.. automodule:: opendssdirect.dss_lib
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: ActiveClassI

    None

.. function:: ActiveClassS

    None

.. function:: ActiveClassV

    None

.. function:: AddInAuxCurrents

    None

.. function:: BUSF

    None

.. function:: BUSI

    None

.. function:: BUSS

    None

.. function:: BUSV

    None

.. function:: BuildYMatrixD

    None

.. function:: CapControlsF

    None

.. function:: CapControlsI

    None

.. function:: CapControlsS

    None

.. function:: CapControlsV

    None

.. function:: CapacitorsF

    None

.. function:: CapacitorsI

    None

.. function:: CapacitorsS

    None

.. function:: CapacitorsV

    None

.. function:: CircuitF

    None

.. function:: CircuitI

    None

.. function:: CircuitS

    None

.. function:: CircuitV

    None

.. function:: CktElementF

    None

.. function:: CktElementI

    None

.. function:: CktElementS

    None

.. function:: CktElementV

    None

.. function:: CmathLibF

    None

.. function:: CmathLibV

    None

.. function:: DSSElementI

    None

.. function:: DSSElementS

    None

.. function:: DSSElementV

    None

.. function:: DSSExecutiveI

    None

.. function:: DSSExecutiveS

    None

.. function:: DSSI

    None

.. function:: DSSLoads

    None

.. function:: DSSLoadsF

    None

.. function:: DSSLoadsS

    None

.. function:: DSSLoadsV

    None

.. function:: DSSProperties

    None

.. function:: DSSPut_Command

    None

.. function:: DSSS

    None

.. function:: DSSV

    None

.. function:: ErrorCode

    None

.. function:: ErrorDesc

    None

.. function:: FusesF

    None

.. function:: FusesI

    None

.. function:: FusesS

    None

.. function:: FusesV

    None

.. function:: GeneratorsF

    None

.. function:: GeneratorsI

    None

.. function:: GeneratorsS

    None

.. function:: GeneratorsV

    None

.. function:: GetCompressedYMatrix

    None

.. function:: GetPCInjCurr

    None

.. function:: GetSourceInjCurrents

    None

.. function:: InitAndGetYparams

    None

.. function:: IsourceF

    None

.. function:: IsourceI

    None

.. function:: IsourceS

    None

.. function:: IsourceV

    None

.. function:: LinesF

    None

.. function:: LinesI

    None

.. function:: LinesS

    None

.. function:: LinesV

    None

.. function:: LoadShapeF

    None

.. function:: LoadShapeI

    None

.. function:: LoadShapeS

    None

.. function:: LoadShapeV

    None

.. function:: MetersF

    None

.. function:: MetersI

    None

.. function:: MetersS

    None

.. function:: MetersV

    None

.. function:: MonitorsI

    None

.. function:: MonitorsS

    None

.. function:: MonitorsV

    None

.. function:: PDElementsF

    None

.. function:: PDElementsI

    None

.. function:: PDElementsS

    None

.. function:: PVsystemsF

    None

.. function:: PVsystemsI

    None

.. function:: PVsystemsS

    None

.. function:: PVsystemsV

    None

.. function:: ParserF

    None

.. function:: ParserI

    None

.. function:: ParserS

    None

.. function:: ParserV

    None

.. function:: ReclosersF

    None

.. function:: ReclosersI

    None

.. function:: ReclosersS

    None

.. function:: ReclosersV

    None

.. function:: RegControlsF

    None

.. function:: RegControlsI

    None

.. function:: RegControlsS

    None

.. function:: RegControlsV

    None

.. function:: RelaysI

    None

.. function:: RelaysS

    None

.. function:: RelaysV

    None

.. function:: SensorsF

    None

.. function:: SensorsI

    None

.. function:: SensorsS

    None

.. function:: SensorsV

    None

.. function:: SettingsF

    None

.. function:: SettingsI

    None

.. function:: SettingsS

    None

.. function:: SettingsV

    None

.. function:: SolutionF

    None

.. function:: SolutionI

    None

.. function:: SolutionS

    None

.. function:: SolutionV

    None

.. function:: SolveSystem

    None

.. function:: SwtControlsF

    None

.. function:: SwtControlsI

    None

.. function:: SwtControlsS

    None

.. function:: SwtControlsV

    None

.. function:: SystemYChanged

    None

.. function:: TopologyI

    None

.. function:: TopologyS

    None

.. function:: TopologyV

    None

.. function:: TransformersF

    None

.. function:: TransformersI

    None

.. function:: TransformersS

    None

.. function:: TransformersV

    None

.. function:: UseAuxCurrents

    None

.. function:: VsourcesF

    None

.. function:: VsourcesI

    None

.. function:: VsourcesS

    None

.. function:: VsourcesV

    None

.. function:: XYCurvesF

    None

.. function:: XYCurvesI

    None

.. function:: XYCurvesS

    None

.. function:: XYCurvesV

    None

.. function:: ZeroInjCurr

    None

.. function:: getIpointer

    None

.. function:: getVpointer

    None

.. automodule:: opendssdirect.utils
        :members:
        :undoc-members:
        :show-inheritance:

.. function:: Iterator

    None

.. function:: capacitors_to_dataframe

    None

.. function:: class_to_dataframe

    None

.. function:: fuses_to_dataframe

    None

.. function:: generators_to_dataframe

    None

.. function:: isource_to_dataframe

    None

.. function:: lines_to_dataframe

    None

.. function:: loads_to_dataframe

    None

.. function:: loadshape_to_dataframe

    None

.. function:: meters_to_dataframe

    None

.. function:: monitors_to_dataframe

    None

.. function:: pvsystems_to_dataframe

    None

.. function:: reclosers_to_dataframe

    None

.. function:: regcontrols_to_dataframe

    None

.. function:: relays_to_dataframe

    None

.. function:: run_command

    Use Text interface of OpenDSS

.. function:: sensors_to_dataframe

    None

.. function:: to_dataframe

    None

.. function:: transformers_to_dataframe

    None

.. function:: vsources_to_dataframe

    None

.. function:: xycurves_to_dataframe

    None
