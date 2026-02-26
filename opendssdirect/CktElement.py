from typing import Optional, List
from ._utils import api_util
from .Bases import Base
from dss import DSSException, OCPDevType as OCPDevTypeEnum

class ICktElement(Base):
    """
    The (Active)CktElement interface allows accessing some common properties and 
    methods shared across circuit elements in the DSS engine.

    Users can enable specific elements by name or use the dedicated interface 
    (e.g. use `Loads.Name`, `Transformers.First/Next`) and access the properties here.

    If you are new to OpenDSS/AltDSS and this classic interface, please read the following document
    for an overview of the "active element" paradigm used by COM and the classic APIs:
        
    https://dss-extensions.org/classic_api.html#the-active-paradigm
    """

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
        "AllLosses",
    ]

    def Close(self, Term: int, Phs: int = 0) -> None:
        """
        Close the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Close1.html
        """
        self._lib.CktElement_Close(Term, Phs)

    def Controller(self, idx: int) -> str:
        """Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range"""
        return self._lib.CktElement_Get_Controller(idx)

    def Variable(self, MyVarName: str) -> float:
        """
        If the active element is a PCElement, get the value of a variable by name.
        Otherwise, an exception is raised.

        Original COM help: https://opendss.epri.com/Variable.html
        """
        if not isinstance(MyVarName, bytes):
            MyVarName = MyVarName.encode(self._api_util.codec)
        Code = self._api_util.ffi.new("int32_t*")
        result = self._lib.CktElement_Get_Variable(MyVarName, Code)
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this name or not a PCelement.")
        
        return result

    def Variablei(self, Idx: int) -> float:
        """
        If the active element is a PCElement, get the value of a variable by its integer index.
        Otherwise, an exception is raised.

        Original COM help: https://opendss.epri.com/Variablei.html
        """
        Code = self._api_util.ffi.new("int32_t*")
        result = self._lib.CktElement_Get_Variablei(Idx, Code)
        if Code[0] != 0:
            raise DSSException(Code[0], "No variable by this index or not a PCelement.")

        return result

    def setVariableByIndex(self, Idx: int, Value: float) -> None:
        Code = self._api_util.ffi.new("int32_t*")
        self._lib.CktElement_Set_Variablei(Idx, Code, Value)
        return Code[0]

    def setVariableByName(self, Idx: int, Value: float) -> None:
        Code = self._api_util.ffi.new("int32_t*")
        self._lib.CktElement_Set_Variable(Idx, Code, Value)
        return Code[0]

    def IsOpen(self, Term: int, Phs: int = 0) -> bool:
        """
        Indicates if the specified terminal and, optionally, a specific phase conductor is open.

        Provide zero in the `Phs` argument to check if any conductor of the terminal `Term` is open.

        Provide a non-zero phase number in `Phs` to check if a specific phase conductor is open.

        Original COM help: https://opendss.epri.com/IsOpen.html
        """
        return self._lib.CktElement_IsOpen(Term, Phs)

    def Open(self, Term: int, Phs: int = 0) -> None:
        """
        Open the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Open1.html
        """
        self._lib.CktElement_Open(Term, Phs)

    def AllPropertyNames(self) -> List[str]:
        """
        Array containing all property names of the active device.

        Original COM help: https://opendss.epri.com/AllPropertyNames.html
        """
        return self._lib.CktElement_Get_AllPropertyNames()

    def AllVariableNames(self) -> List[str]:
        """
        Array of strings listing all the published state variable names.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableNames.html
        """
        return self._lib.CktElement_Get_AllVariableNames()

    def AllVariableValues(self):
        """
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableValues.html
        """
        return self._lib.CktElement_Get_AllVariableValues_GR()

    def BusNames(self, *args, removeNodes: bool = False) -> List[str]:
        """
        Bus definitions to which each terminal is connected.

        In getter mode, the keyword argument `removeNodes` is an **API Extension**.
        Use it to get only the bus names, without the connection/node specification, if present.

        Original COM help: https://opendss.epri.com/BusNames.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.CktElement_Get_BusNames(removeNodes)

        # Setter
        (Value,) = args
        self._set_string_array(self._lib.CktElement_Set_BusNames, Value)

    def CplxSeqCurrents(self):
        """
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        """
        return self._lib.CktElement_Get_CplxSeqCurrents_GR()

    def CplxSeqVoltages(self):
        """
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        """
        return self._lib.CktElement_Get_CplxSeqVoltages_GR()

    def Currents(self):
        """
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        """
        return self._lib.CktElement_Get_Currents_GR()

    def CurrentsMagAng(self):
        """
        Currents in magnitude, angle (degrees) format as an array of doubles.

        Original COM help: https://opendss.epri.com/CurrentsMagAng.html
        """
        return self._lib.CktElement_Get_CurrentsMagAng_GR()

    def DisplayName(self, *args):
        """
        Display name of the object (not necessarily unique)

        Original COM help: https://opendss.epri.com/DisplayName.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.CktElement_Get_DisplayName()

        # Setter
        (Value,) = args
        self._lib.CktElement_Set_DisplayName(Value)

    def EmergAmps(self, *args):
        """
        Emergency Ampere Rating for PD elements

        Original COM help: https://opendss.epri.com/EmergAmps.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.CktElement_Get_EmergAmps()

        # Setter
        (Value,) = args
        self._lib.CktElement_Set_EmergAmps(Value)

    def Enabled(self, *args) -> Optional[bool]:
        """
        Boolean indicating that element is currently in the circuit.

        Original COM help: https://opendss.epri.com/Enabled.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.CktElement_Get_Enabled()

        # Setter
        (Value,) = args
        self._lib.CktElement_Set_Enabled(Value)

    def EnergyMeter(self) -> str:
        """
        Name of the Energy Meter this element is assigned to.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        """
        return self._lib.CktElement_Get_EnergyMeter()

    def GUID(self) -> str:
        """
        GUID/UUID for this object.

        Original COM help: https://opendss.epri.com/GUID.html
        """
        return self._lib.CktElement_Get_GUID()

    def Handle(self) -> int:
        """
        Index of this element into the circuit's element list.

        Original COM help: https://opendss.epri.com/Handle.html
        """
        return self._lib.CktElement_Get_Handle()

    def HasOCPDevice(self) -> bool:
        """
        True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        """
        return self._lib.CktElement_Get_HasOCPDevice()

    def HasSwitchControl(self) -> bool:
        """
        True if this element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        """
        return self._lib.CktElement_Get_HasSwitchControl()

    def HasVoltControl(self) -> bool:
        """
        True if this element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        """
        return self._lib.CktElement_Get_HasVoltControl()

    def Losses(self):
        """
        Total losses in the element: two-element double array (complex), in VA (watts, vars)

        Original COM help: https://opendss.epri.com/Losses1.html
        """
        return self._lib.CktElement_Get_Losses_GR()

    def Name(self) -> str:
        """
        Full Name of Active Circuit Element

        Original COM help: https://opendss.epri.com/Name4.html
        """
        return self._lib.CktElement_Get_Name()

    def NodeOrder(self):
        """
        Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal.

        Be sure to run a solution to initialize the values after the circuit is created or modified.

        Original COM help: https://opendss.epri.com/NodeOrder.html
        """
        return self._lib.CktElement_Get_NodeOrder_GR()

    def NormalAmps(self, *args):
        """
        Normal ampere rating for PD Elements

        Original COM help: https://opendss.epri.com/NormalAmps.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.CktElement_Get_NormalAmps()

        # Setter
        (Value,) = args
        self._lib.CktElement_Set_NormalAmps(Value)

    def NumConductors(self) -> int:
        """
        Number of Conductors per Terminal

        Original COM help: https://opendss.epri.com/NumConductors.html
        """
        return self._lib.CktElement_Get_NumConductors()

    def NumControls(self) -> int:
        """
        Number of controls connected to this device.
        Use to determine valid range for index into Controller array.

        Original COM help: https://opendss.epri.com/NumControls.html
        """
        return self._lib.CktElement_Get_NumControls()

    def NumPhases(self) -> int:
        """
        Number of Phases

        Original COM help: https://opendss.epri.com/NumPhases.html
        """
        return self._lib.CktElement_Get_NumPhases()

    def NumProperties(self) -> int:
        """
        Number of Properties this Circuit Element.

        Original COM help: https://opendss.epri.com/NumProperties.html
        """
        return self._lib.CktElement_Get_NumProperties()

    def NumTerminals(self) -> int:
        """
        Number of terminals in this Circuit Element

        Original COM help: https://opendss.epri.com/NumTerminals.html
        """
        return self._lib.CktElement_Get_NumTerminals()

    def OCPDevIndex(self) -> int:
        """
        Index into Controller list of OCP Device controlling this CktElement

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        """
        return self._lib.CktElement_Get_OCPDevIndex()

    def OCPDevType(self) -> int:
        """
        0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        """
        return OCPDevTypeEnum(self._lib.CktElement_Get_OCPDevType())

    def PhaseLosses(self):
        """
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        """
        return self._lib.CktElement_Get_PhaseLosses_GR()

    def AllLosses(self):
        """
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA, for the active circuit element.

        Added in May 2025. Same as `LossesByType` introduced for Transformers in AltDSS/DSS C-API in May 2019.
        """
        return self._lib.CktElement_Get_AllLosses_GR()

    def Powers(self):
        """
        Complex array of powers (kVA) into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Powers.html
        """
        return self._lib.CktElement_Get_Powers_GR()

    def Residuals(self):
        """
        Residual currents for each terminal: (magnitude, angle in degrees)

        Original COM help: https://opendss.epri.com/Residuals.html
        """
        return self._lib.CktElement_Get_Residuals_GR()

    def SeqCurrents(self):
        """
        Double array of symmetrical component currents (magnitudes only) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        """
        return self._lib.CktElement_Get_SeqCurrents_GR()

    def SeqPowers(self):
        """
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqPowers.html
        """
        return self._lib.CktElement_Get_SeqPowers_GR()

    def SeqVoltages(self):
        """
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        """
        return self._lib.CktElement_Get_SeqVoltages_GR()

    def Voltages(self):
        """
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        """
        return self._lib.CktElement_Get_Voltages_GR()

    def VoltagesMagAng(self):
        """
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        """
        return self._lib.CktElement_Get_VoltagesMagAng_GR()

    def YPrim(self):
        """
        YPrim matrix, column order, complex numbers

        Original COM help: https://opendss.epri.com/Yprim.html
        """
        return self._lib.CktElement_Get_Yprim_GR()

    def YprimOrder(self) -> int:
        """
        Order (size) of the active circuit element's primite Y matrix (Yprim), typically `NumConductors * NumTerminals`

        **(API Extension)**
        """
        return self._lib.CktElement_Get_YprimOrder()

    def IsIsolated(self) -> bool:
        """
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.

        **(API Extension)**
        """
        return self._lib.CktElement_Get_IsIsolated()

    def TotalPowers(self):
        """
        Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.

        Original COM help: https://opendss.epri.com/TotalPowers.html
        """
        return self._lib.CktElement_Get_TotalPowers_GR()

    def NodeRef(self):
        """
        Array of integers, a copy of the internal NodeRef of the CktElement.

        Be sure to run a solution to initialize the values after the circuit is created or modified.

        **(API Extension)**
        """
        return self._lib.CktElement_Get_NodeRef_GR()


_CktElement = ICktElement(api_util)

# For backwards compatibility, bind to the default instance
AllLosses = _CktElement.AllLosses
AllPropertyNames = _CktElement.AllPropertyNames
AllVariableNames = _CktElement.AllVariableNames
AllVariableValues = _CktElement.AllVariableValues
BusNames = _CktElement.BusNames
Close = _CktElement.Close
Controller = _CktElement.Controller
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
IsIsolated = _CktElement.IsIsolated
IsOpen = _CktElement.IsOpen
Losses = _CktElement.Losses
Name = _CktElement.Name
NodeOrder = _CktElement.NodeOrder
NodeRef = _CktElement.NodeRef
NormalAmps = _CktElement.NormalAmps
NumConductors = _CktElement.NumConductors
NumControls = _CktElement.NumControls
NumPhases = _CktElement.NumPhases
NumProperties = _CktElement.NumProperties
NumTerminals = _CktElement.NumTerminals
OCPDevIndex = _CktElement.OCPDevIndex
OCPDevType = _CktElement.OCPDevType
Open = _CktElement.Open
PhaseLosses = _CktElement.PhaseLosses
Powers = _CktElement.Powers
Residuals = _CktElement.Residuals
SeqCurrents = _CktElement.SeqCurrents
SeqPowers = _CktElement.SeqPowers
SeqVoltages = _CktElement.SeqVoltages
TotalPowers = _CktElement.TotalPowers
Variable = _CktElement.Variable
Variablei = _CktElement.Variablei
Voltages = _CktElement.Voltages
VoltagesMagAng = _CktElement.VoltagesMagAng
YPrim = _CktElement.YPrim
YprimOrder = _CktElement.YprimOrder
setVariableByIndex = _CktElement.setVariableByIndex
setVariableByName = _CktElement.setVariableByName
_columns = _CktElement._columns
__all__ = [
    "AllLosses",
    "AllPropertyNames",
    "AllVariableNames",
    "AllVariableValues",
    "BusNames",
    "Close",
    "Controller",
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
    "IsIsolated",
    "IsOpen",
    "Losses",
    "Name",
    "NodeOrder",
    "NodeRef",
    "NormalAmps",
    "NumConductors",
    "NumControls",
    "NumPhases",
    "NumProperties",
    "NumTerminals",
    "OCPDevIndex",
    "OCPDevType",
    "Open",
    "PhaseLosses",
    "Powers",
    "Residuals",
    "SeqCurrents",
    "SeqPowers",
    "SeqVoltages",
    "TotalPowers",
    "Variable",
    "Variablei",
    "Voltages",
    "VoltagesMagAng",
    "YPrim",
    "YprimOrder",
    "setVariableByIndex",
    "setVariableByName",
]
