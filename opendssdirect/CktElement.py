from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base
from dss import DSSException, OCPDevType as OCPDevTypeEnum


class ICktElement(Base):
    __slots__ = []

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
        """
        Close the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Close1.html
        """
        self._check_for_error(self._lib.CktElement_Close(Term, Phs))

    def Controller(self, idx):
        """Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range"""
        return self._get_string(
            self._check_for_error(self._lib.CktElement_Get_Controller(idx))
        )

    def Variable(self, MyVarName):
        """
        If the active element is a PCElement, get the value of a variable by name.
        Otherwise, an exception is raised.
        """
        if not isinstance(MyVarName, bytes):
            MyVarName = MyVarName.encode(self._api_util.codec)
        Code = self._api_util.ffi.new("int32_t*")
        result = self._check_for_error(self._lib.CktElement_Get_Variable(MyVarName, Code))
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this name or not a PCelement.")
        
        return result

    def Variablei(self, Idx):
        """
        If the active element is a PCElement, get the value of a variable by its integer index.
        Otherwise, an exception is raised.
        """
        Code = self._api_util.ffi.new("int32_t*")
        result = self._check_for_error(self._lib.CktElement_Get_Variablei(Idx, Code))
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this index or not a PCelement.")

        return result

    def setVariableByIndex(self, Idx, Value):
        Code = self._api_util.ffi.new("int32_t*")
        self._check_for_error(self._lib.CktElement_Set_Variablei(Idx, Code, Value))
        return Code[0]

    def setVariableByName(self, Idx, Value):
        Code = self._api_util.ffi.new("int32_t*")
        self._check_for_error(self._lib.CktElement_Set_Variable(Idx, Code, Value))
        return Code[0]

    def IsOpen(self, Term, Phs):
        return self._check_for_error(self._lib.CktElement_IsOpen(Term, Phs)) != 0

    def Open(self, Term, Phs):
        """
        Open the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Open1.html
        """
        self._check_for_error(self._lib.CktElement_Open(Term, Phs))

    def AllPropertyNames(self):
        """
        Array containing all property names of the active device.

        Original COM help: https://opendss.epri.com/AllPropertyNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.CktElement_Get_AllPropertyNames)
        )

    def AllVariableNames(self):
        """
        Array of strings listing all the published state variable names.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.CktElement_Get_AllVariableNames)
        )

    def AllVariableValues(self):
        """
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableValues.html
        """
        self._check_for_error(self._lib.CktElement_Get_AllVariableValues_GR())
        return self._get_float64_gr_array()

    def BusNames(self, *args):
        """
        Bus definitions to which each terminal is connected.

        Original COM help: https://opendss.epri.com/BusNames.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(
                self._get_string_array(self._lib.CktElement_Get_BusNames)
            )

        # Setter
        (Value,) = args
        self._check_for_error(
            self._set_string_array(self._lib.CktElement_Set_BusNames, Value)
        )

    def CplxSeqCurrents(self):
        """
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        """
        self._check_for_error(self._lib.CktElement_Get_CplxSeqCurrents_GR())
        return self._get_complex128_gr_array()

    def CplxSeqVoltages(self):
        """
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        """
        self._check_for_error(self._lib.CktElement_Get_CplxSeqVoltages_GR())
        return self._get_complex128_gr_array()

    def Currents(self):
        """
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        """
        self._check_for_error(self._lib.CktElement_Get_Currents_GR())
        return self._get_complex128_gr_array()

    def CurrentsMagAng(self):
        """
        Currents in magnitude, angle (degrees) format as a array of doubles.

        Original COM help: https://opendss.epri.com/CurrentsMagAng.html
        """
        self._check_for_error(self._lib.CktElement_Get_CurrentsMagAng_GR())
        return self._get_float64_gr_array()

    def DisplayName(self, *args):
        """
        Display name of the object (not necessarily unique)

        Original COM help: https://opendss.epri.com/DisplayName.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.CktElement_Get_DisplayName())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.CktElement_Set_DisplayName(Value))

    def EmergAmps(self, *args):
        """
        Emergency Ampere Rating for PD elements

        Original COM help: https://opendss.epri.com/EmergAmps.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CktElement_Get_EmergAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CktElement_Set_EmergAmps(Value))

    def Enabled(self, *args):
        """
        Boolean indicating that element is currently in the circuit.

        Original COM help: https://opendss.epri.com/Enabled.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CktElement_Get_Enabled()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CktElement_Set_Enabled(Value))

    def EnergyMeter(self):
        """
        Name of the Energy Meter this element is assigned to.

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        """
        return self._get_string(
            self._check_for_error(self._lib.CktElement_Get_EnergyMeter())
        )

    def GUID(self):
        """
        globally unique identifier for this object

        Original COM help: https://opendss.epri.com/GUID.html
        """
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_GUID()))

    def Handle(self):
        """
        Pointer to this object

        Original COM help: https://opendss.epri.com/Handle.html
        """
        return self._check_for_error(self._lib.CktElement_Get_Handle())

    def HasOCPDevice(self):
        """
        True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        """
        return self._check_for_error(self._lib.CktElement_Get_HasOCPDevice()) != 0

    def HasSwitchControl(self):
        """
        This element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        """
        return self._check_for_error(self._lib.CktElement_Get_HasSwitchControl()) != 0

    def HasVoltControl(self):
        """
        This element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        """
        return self._check_for_error(self._lib.CktElement_Get_HasVoltControl()) != 0

    def Losses(self):
        """
        Total losses in the element: two-element double array (complex), in VA (watts, vars)

        Original COM help: https://opendss.epri.com/Losses1.html
        """
        self._check_for_error(self._lib.CktElement_Get_Losses_GR())
        return self._get_complex128_gr_simple()

    def Name(self):
        """
        Full Name of Active Circuit Element

        Original COM help: https://opendss.epri.com/Name4.html
        """
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_Name()))

    def NodeOrder(self):
        """
        Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal.

        Original COM help: https://opendss.epri.com/NodeOrder.html
        """
        self._check_for_error(self._lib.CktElement_Get_NodeOrder_GR())
        return self._get_int32_gr_array()

    def NormalAmps(self, *args):
        """
        Normal ampere rating for PD Elements

        Original COM help: https://opendss.epri.com/NormalAmps.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.CktElement_Get_NormalAmps())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.CktElement_Set_NormalAmps(Value))

    def NumConductors(self):
        """
        Number of Conductors per Terminal

        Original COM help: https://opendss.epri.com/NumConductors.html
        """
        return self._check_for_error(self._lib.CktElement_Get_NumConductors())

    def NumControls(self):
        """
        Number of controls connected to this device.
        Use to determine valid range for index into Controller array.

        Original COM help: https://opendss.epri.com/NumControls.html
        """
        return self._check_for_error(self._lib.CktElement_Get_NumControls())

    def NumPhases(self):
        """
        Number of Phases

        Original COM help: https://opendss.epri.com/NumPhases.html
        """
        return self._check_for_error(self._lib.CktElement_Get_NumPhases())

    def NumProperties(self):
        """
        Number of Properties this Circuit Element.

        Original COM help: https://opendss.epri.com/NumProperties.html
        """
        return self._check_for_error(self._lib.CktElement_Get_NumProperties())

    def NumTerminals(self):
        """
        Number of Terminals this Circuit Element

        Original COM help: https://opendss.epri.com/NumTerminals.html
        """
        return self._check_for_error(self._lib.CktElement_Get_NumTerminals())

    def OCPDevIndex(self):
        """
        Index into Controller list of OCP Device controlling this CktElement

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        """
        return self._check_for_error(self._lib.CktElement_Get_OCPDevIndex())

    def OCPDevType(self):
        """
        0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        """
        return OCPDevTypeEnum(self._check_for_error(self._lib.CktElement_Get_OCPDevType()))

    def PhaseLosses(self):
        """
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        """
        self._check_for_error(self._lib.CktElement_Get_PhaseLosses_GR())
        return self._get_complex128_gr_array()

    def Powers(self):
        """
        Complex array of powers (kVA) into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Powers.html
        """
        self._check_for_error(self._lib.CktElement_Get_Powers_GR())
        return self._get_complex128_gr_array()

    def Residuals(self):
        """
        Residual currents for each terminal: (magnitude, angle in degrees)

        Original COM help: https://opendss.epri.com/Residuals.html
        """
        self._check_for_error(self._lib.CktElement_Get_Residuals_GR())
        return self._get_float64_gr_array()

    def SeqCurrents(self):
        """
        Double array of symmetrical component currents (magnitudes only) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        """
        self._check_for_error(self._lib.CktElement_Get_SeqCurrents_GR())
        return self._get_float64_gr_array()

    def SeqPowers(self):
        """
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqPowers.html
        """
        self._check_for_error(self._lib.CktElement_Get_SeqPowers_GR())
        return self._get_complex128_gr_array()

    def SeqVoltages(self):
        """
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        """
        self._check_for_error(self._lib.CktElement_Get_SeqVoltages_GR())
        return self._get_float64_gr_array()

    def Voltages(self):
        """
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        """
        self._check_for_error(self._lib.CktElement_Get_Voltages_GR())
        return self._get_complex128_gr_array()

    def VoltagesMagAng(self):
        """
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        """
        self._check_for_error(self._lib.CktElement_Get_VoltagesMagAng_GR())
        return self._get_float64_gr_array()

    def YPrim(self):
        """
        YPrim matrix, column order, complex numbers

        Original COM help: https://opendss.epri.com/Yprim.html
        """
        self._check_for_error(self._lib.CktElement_Get_Yprim_GR())
        return self._get_complex128_gr_array()

    def IsIsolated(self):
        """
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.

        **(API Extension)**
        """
        return self._check_for_error(self._lib.CktElement_Get_IsIsolated()) != 0

    def TotalPowers(self):
        """
        Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.

        Original COM help: https://opendss.epri.com/TotalPowers.html
        """
        self._check_for_error(self._lib.CktElement_Get_TotalPowers_GR())
        return self._get_complex128_gr_array()

    def NodeRef(self):
        """
        Array of integers, a copy of the internal NodeRef of the CktElement.

        **(API Extension)**
        """
        self._lib.CktElement_Get_NodeRef_GR()
        return self._get_int32_gr_array()


_CktElement = ICktElement(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
