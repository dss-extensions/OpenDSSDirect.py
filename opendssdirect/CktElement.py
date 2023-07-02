from ._utils import DSSException, api_util, Base


class ICktElement(Base):
    __slots__ = ["Properties"]
    __name__ = "CktElement"
    _api_prefix = "CktElement"
    _columns = [
        "Name",
        "DisplayName",
        "Handle",
        "GUID",
        "Enabled",
        "NumTerminals",
        "NumPhases",
        "NumConductors",
        "NumControls",
        "NumProperties",
        "AllPropertyNames",
        "AllVariableValues",
        "AllVariableNames",
        "BusNames",
        "NormalAmps",
        "EmergAmps",
        "HasVoltControl",
        "HasSwitchControl",
        "HasOCPDevice",
        "OCPDevType",
        "OCPDevIndex",
        "IsIsolated",
        "EnergyMeter",
        "TotalPowers",
        "YPrim",
        "NodeOrder",
        "Voltages",
        "VoltagesMagAng",
        "SeqVoltages",
        "CplxSeqVoltages",
        "Powers",
        "SeqPowers",
        "Currents",
        "CurrentsMagAng",
        "SeqCurrents",
        "CplxSeqCurrents",
        "Residuals",
        "Losses",
        "PhaseLosses",
    ]

    def Close(self, Term, Phs):
        self.CheckForError(self._lib.CktElement_Close(Term, Phs))

    def Controller(self, idx):
        """(read-only) Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range"""
        return self._get_string(
            self.CheckForError(self._lib.CktElement_Get_Controller(idx))
        )

    def Variable(self, MyVarName):
        """
        If the active element is a PCElement, get the value of a variable by name.
        Otherwise, an exception is raised.
        """
        if type(MyVarName) is not bytes:
            MyVarName = MyVarName.encode(self._api_util.codec)
        Code = self._api_util.ffi.new("int32_t*")
        result = self.CheckForError(self._lib.CktElement_Get_Variable(MyVarName, Code))
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this name or not a PCelement.")
        
        return result

    def Variablei(self, Idx):
        """
        If the active element is a PCElement, get the value of a variable by its integer index.
        Otherwise, an exception is raised.
        """
        Code = self._api_util.ffi.new("int32_t*")
        result = self.CheckForError(self._lib.CktElement_Get_Variablei(Idx, Code))
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this index or not a PCelement.")

        return result

    def setVariableByIndex(self, Idx, Value):
        Code = self._api_util.ffi.new("int32_t*")
        self.CheckForError(self._lib.CktElement_Set_Variablei(Idx, Code, Value))
        return Code[0]

    def setVariableByName(self, Idx, Value):
        Code = self._api_util.ffi.new("int32_t*")
        self.CheckForError(self._lib.CktElement_Set_Variable(Idx, Code, Value))
        return Code[0]

    def IsOpen(self, Term, Phs):
        return self.CheckForError(self._lib.CktElement_IsOpen(Term, Phs)) != 0

    def Open(self, Term, Phs):
        self.CheckForError(self._lib.CktElement_Open(Term, Phs))

    def AllPropertyNames(self):
        """(read-only) Array containing all property names of the active device."""
        return self.CheckForError(
            self._get_string_array(self._lib.CktElement_Get_AllPropertyNames)
        )

    def AllVariableNames(self):
        """
        Array of strings listing all the published state variable names.
        Valid only for PCElements.
        """
        return self.CheckForError(
            self._get_string_array(self._lib.CktElement_Get_AllVariableNames)
        )

    def AllVariableValues(self):
        """
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.
        """
        return self._get_float64_array(self._lib.CktElement_Get_AllVariableValues)

    def BusNames(self, *args):
        """
        Array of strings. Get  Bus definitions to which each terminal is connected. 0-based array.
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(
                self._get_string_array(self._lib.CktElement_Get_BusNames)
            )

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_string_array(Value)
        self.CheckForError(self._lib.CktElement_Set_BusNames(ValuePtr, ValueCount))

    def CplxSeqCurrents(self):
        """(read-only) Complex double array of Sequence Currents for all conductors of all terminals of active circuit element."""
        return self._get_float64_array(self._lib.CktElement_Get_CplxSeqCurrents)

    def CplxSeqVoltages(self):
        """(read-only) Complex double array of Sequence Voltage for all terminals of active circuit element."""
        return self._get_float64_array(self._lib.CktElement_Get_CplxSeqVoltages)

    def Currents(self):
        """(read-only) Complex array of currents into each conductor of each terminal"""
        return self._get_float64_array(self._lib.CktElement_Get_Currents)

    def CurrentsMagAng(self):
        """(read-only) Currents in magnitude, angle format as a array of doubles."""
        return self._get_float64_array(self._lib.CktElement_Get_CurrentsMagAng)

    def DisplayName(self, *args):
        """Display name of the object (not necessarily unique)"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.CktElement_Get_DisplayName())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.CktElement_Set_DisplayName(Value))

    def EmergAmps(self, *args):
        """Emergency Ampere Rating for PD elements"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.CktElement_Get_EmergAmps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.CktElement_Set_EmergAmps(Value))

    def Enabled(self, *args):
        """Boolean indicating that element is currently in the circuit."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.CktElement_Get_Enabled()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.CktElement_Set_Enabled(Value))

    def EnergyMeter(self):
        """(read-only) Name of the Energy Meter this element is assigned to."""
        return self._get_string(
            self.CheckForError(self._lib.CktElement_Get_EnergyMeter())
        )

    def GUID(self):
        """(read-only) globally unique identifier for this object"""
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_GUID()))

    def Handle(self):
        """(read-only) Pointer to this object"""
        return self.CheckForError(self._lib.CktElement_Get_Handle())

    def HasOCPDevice(self):
        """(read-only) True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection"""
        return self.CheckForError(self._lib.CktElement_Get_HasOCPDevice()) != 0

    def HasSwitchControl(self):
        """(read-only) This element has a SwtControl attached."""
        return self.CheckForError(self._lib.CktElement_Get_HasSwitchControl()) != 0

    def HasVoltControl(self):
        """(read-only) This element has a CapControl or RegControl attached."""
        return self.CheckForError(self._lib.CktElement_Get_HasVoltControl()) != 0

    def Losses(self):
        """(read-only) Total losses in the element: two-element complex array"""
        return self._get_float64_array(self._lib.CktElement_Get_Losses)

    def Name(self):
        """(read-only) Full Name of Active Circuit Element"""
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_Name()))

    def NodeOrder(self):
        """(read-only) Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal."""
        return self._get_int32_array(self._lib.CktElement_Get_NodeOrder)

    def NormalAmps(self, *args):
        """Normal ampere rating for PD Elements"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.CktElement_Get_NormalAmps())

        # Setter
        Value, = args
        self.CheckForError(self._lib.CktElement_Set_NormalAmps(Value))

    def NumConductors(self):
        """(read-only) Number of Conductors per Terminal"""
        return self.CheckForError(self._lib.CktElement_Get_NumConductors())

    def NumControls(self):
        """
        (read-only) Number of controls connected to this device.
        Use to determine valid range for index into Controller array.
        """
        return self.CheckForError(self._lib.CktElement_Get_NumControls())

    def NumPhases(self):
        """(read-only) Number of Phases"""
        return self.CheckForError(self._lib.CktElement_Get_NumPhases())

    def NumProperties(self):
        """(read-only) Number of Properties this Circuit Element."""
        return self.CheckForError(self._lib.CktElement_Get_NumProperties())

    def NumTerminals(self):
        """(read-only) Number of Terminals this Circuit Element"""
        return self.CheckForError(self._lib.CktElement_Get_NumTerminals())

    def OCPDevIndex(self):
        """(read-only) Index into Controller list of OCP Device controlling this CktElement"""
        return self.CheckForError(self._lib.CktElement_Get_OCPDevIndex())

    def OCPDevType(self):
        """(read-only) 0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device"""
        return self.CheckForError(self._lib.CktElement_Get_OCPDevType())

    def PhaseLosses(self):
        """(read-only) Complex array of losses by phase"""
        return self._get_float64_array(self._lib.CktElement_Get_PhaseLosses)

    def Powers(self):
        """(read-only) Complex array of powers into each conductor of each terminal"""
        return self._get_float64_array(self._lib.CktElement_Get_Powers)

    def Residuals(self):
        """(read-only) Residual currents for each terminal: (mag, angle)"""
        return self._get_float64_array(self._lib.CktElement_Get_Residuals)

    def SeqCurrents(self):
        """(read-only) Double array of symmetrical component currents into each 3-phase terminal"""
        return self._get_float64_array(self._lib.CktElement_Get_SeqCurrents)

    def SeqPowers(self):
        """(read-only) Double array of sequence powers into each 3-phase teminal"""
        return self._get_float64_array(self._lib.CktElement_Get_SeqPowers)

    def SeqVoltages(self):
        """(read-only) Double array of symmetrical component voltages at each 3-phase terminal"""
        return self._get_float64_array(self._lib.CktElement_Get_SeqVoltages)

    def Voltages(self):
        """(read-only) Complex array of voltages at terminals"""
        return self._get_float64_array(self._lib.CktElement_Get_Voltages)

    def VoltagesMagAng(self):
        """(read-only) Voltages at each conductor in magnitude, angle form as array of doubles."""
        return self._get_float64_array(self._lib.CktElement_Get_VoltagesMagAng)

    def YPrim(self):
        """(read-only) YPrim matrix, column order, complex numbers (paired)"""
        return self._get_float64_array(self._lib.CktElement_Get_Yprim)

    def IsIsolated(self):
        """
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.
        """
        return self.CheckForError(self._lib.CktElement_Get_IsIsolated()) != 0

    def TotalPowers(self):
        """Returns the total powers (complex) at ALL terminals of the active circuit element."""
        return self._get_float64_array(self._lib.CktElement_Get_TotalPowers)

    def NodeRef(self):
        """Array of integers, a copy of the internal NodeRef of the CktElement."""
        return self._get_int32_array(self._lib.CktElement_Get_NodeRef)


_CktElement = ICktElement(api_util)

# For backwards compatibility, bind to the default instance
Close = _CktElement.Close
Controller = _CktElement.Controller
Variable = _CktElement.Variable
Variablei = _CktElement.Variablei
IsOpen = _CktElement.IsOpen
Open = _CktElement.Open
AllPropertyNames = _CktElement.AllPropertyNames
AllVariableNames = _CktElement.AllVariableNames
AllVariableValues = _CktElement.AllVariableValues
BusNames = _CktElement.BusNames
CplxSeqCurrents = _CktElement.CplxSeqCurrents
CplxSeqVoltages = _CktElement.CplxSeqVoltages
Currents = _CktElement.Currents
CurrentsMagAng = _CktElement.CurrentsMagAng
DisplayName = _CktElement.DisplayName
EmergAmps = _CktElement.EmergAmps
Enabled = _CktElement.Enabled
EnergyMeter = _CktElement.EnergyMeter
GUID = _CktElement.GUID
Handle = _CktElement.Handle
HasOCPDevice = _CktElement.HasOCPDevice
HasSwitchControl = _CktElement.HasSwitchControl
HasVoltControl = _CktElement.HasVoltControl
Losses = _CktElement.Losses
Name = _CktElement.Name
NodeOrder = _CktElement.NodeOrder
NormalAmps = _CktElement.NormalAmps
NumConductors = _CktElement.NumConductors
NumControls = _CktElement.NumControls
NumPhases = _CktElement.NumPhases
NumProperties = _CktElement.NumProperties
NumTerminals = _CktElement.NumTerminals
OCPDevIndex = _CktElement.OCPDevIndex
OCPDevType = _CktElement.OCPDevType
PhaseLosses = _CktElement.PhaseLosses
Powers = _CktElement.Powers
Residuals = _CktElement.Residuals
SeqCurrents = _CktElement.SeqCurrents
SeqPowers = _CktElement.SeqPowers
SeqVoltages = _CktElement.SeqVoltages
TotalPowers = _CktElement.TotalPowers
Voltages = _CktElement.Voltages
VoltagesMagAng = _CktElement.VoltagesMagAng
YPrim = _CktElement.YPrim
IsIsolated = _CktElement.IsIsolated
setVariableByIndex = _CktElement.setVariableByIndex
setVariableByName = _CktElement.setVariableByName
NodeRef = _CktElement.NodeRef
_columns = _CktElement._columns
__all__ = [
    "Close",
    "Controller",
    "Variable",
    "Variablei",
    "IsOpen",
    "Open",
    "AllPropertyNames",
    "AllVariableNames",
    "AllVariableValues",
    "BusNames",
    "CplxSeqCurrents",
    "CplxSeqVoltages",
    "Currents",
    "CurrentsMagAng",
    "DisplayName",
    "EmergAmps",
    "Enabled",
    "EnergyMeter",
    "GUID",
    "Handle",
    "HasOCPDevice",
    "HasSwitchControl",
    "HasVoltControl",
    "Losses",
    "Name",
    "NodeOrder",
    "NormalAmps",
    "NumConductors",
    "NumControls",
    "NumPhases",
    "NumProperties",
    "NumTerminals",
    "OCPDevIndex",
    "OCPDevType",
    "PhaseLosses",
    "Powers",
    "Residuals",
    "SeqCurrents",
    "SeqPowers",
    "SeqVoltages",
    "TotalPowers",
    "Voltages",
    "VoltagesMagAng",
    "YPrim",
    "IsIsolated",
    "setVariableByIndex",
    "setVariableByName",
    "NodeRef",
]
