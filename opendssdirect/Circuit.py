from ._utils import api_util, Base


class ICircuit(Base):
    __slots__ = [
    ]
    __name__ = "Circuit"
    _api_prefix = "Circuit"
    _columns = [
        "Name",
        "NumBuses",
        "NumNodes",
        "NumCktElements",
        "AllBusDistances",
        "AllBusNames",
        "AllBusVMag",
        "AllBusMagPu",
        "AllBusVolts",
        "AllNodeNames",
        "AllNodeDistances",
        "AllElementNames",
        "YNodeOrder",
        "YNodeVArray",
        "YCurrents",
        "AllElementLosses",
        "LineLosses",
        "Losses",
        "SubstationLosses",
        "TotalPower",
    ]

    def Capacity(self, Start, Increment):
        return self.CheckForError(self._lib.Circuit_Capacity(Start, Increment))

    def Disable(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)
        self.CheckForError(self._lib.Circuit_Disable(Name))

    def Enable(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)
        self.CheckForError(self._lib.Circuit_Enable(Name))

    def EndOfTimeStepUpdate(self):
        self.CheckForError(self._lib.Circuit_EndOfTimeStepUpdate())

    def FirstElement(self):
        return self.CheckForError(self._lib.Circuit_FirstElement())

    def FirstPCElement(self):
        return self.CheckForError(self._lib.Circuit_FirstPCElement())

    def FirstPDElement(self):
        return self.CheckForError(self._lib.Circuit_FirstPDElement())

    def AllNodeDistancesByPhase(self, Phase):
        """(read-only) Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties."""
        self.CheckForError(self._lib.Circuit_Get_AllNodeDistancesByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def AllNodeNamesByPhase(self, Phase):
        """(read-only) Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties."""
        return self.CheckForError(
            self._get_string_array(self._lib.Circuit_Get_AllNodeNamesByPhase, Phase)
        )

    def AllNodeVmagByPhase(self, Phase):
        """(read-only) Returns Array of doubles represent voltage magnitudes for nodes on the specified phase."""
        self.CheckForError(self._lib.Circuit_Get_AllNodeVmagByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def AllNodeVmagPUByPhase(self, Phase):
        """(read-only) Returns array of per unit voltage magnitudes for each node by phase"""
        self.CheckForError(self._lib.Circuit_Get_AllNodeVmagPUByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NextElement(self):
        return self.CheckForError(self._lib.Circuit_NextElement())

    def NextPCElement(self):
        return self.CheckForError(self._lib.Circuit_NextPCElement())

    def NextPDElement(self):
        return self.CheckForError(self._lib.Circuit_NextPDElement())

    def Sample(self):
        self.CheckForError(self._lib.Circuit_Sample())

    def SaveSample(self):
        self.CheckForError(self._lib.Circuit_SaveSample())

    def SetActiveBus(self, BusName):
        if type(BusName) is not bytes:
            BusName = BusName.encode(self._api_util.codec)
        return self.CheckForError(self._lib.Circuit_SetActiveBus(BusName))

    def SetActiveBusi(self, BusIndex):
        return self.CheckForError(self._lib.Circuit_SetActiveBusi(BusIndex))

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(self._api_util.codec)
        return self.CheckForError(self._lib.Circuit_SetActiveClass(ClassName))

    def SetActiveElement(self, FullName):
        if type(FullName) is not bytes:
            FullName = FullName.encode(self._api_util.codec)
        return self.CheckForError(self._lib.Circuit_SetActiveElement(FullName))

    def UpdateStorage(self):
        self.CheckForError(self._lib.Circuit_UpdateStorage())

    def AllBusDistances(self):
        """(read-only) Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames."""
        self.CheckForError(self._lib.Circuit_Get_AllBusDistances_GR())
        return self._get_float64_gr_array()

    def AllBusNames(self):
        """(read-only) Array of strings containing names of all buses in circuit (see AllNodeNames)."""
        return self.CheckForError(
            self._get_string_array(self._lib.Circuit_Get_AllBusNames)
        )

    def AllBusVMag(self):
        """(read-only) Array of magnitudes (doubles) of voltages at all buses"""
        self.CheckForError(self._lib.Circuit_Get_AllBusVmag_GR())
        return self._get_float64_gr_array()

    def AllBusMagPu(self):
        """(read-only) Double Array of all bus voltages (each node) magnitudes in Per unit"""
        self.CheckForError(self._lib.Circuit_Get_AllBusVmagPu_GR())
        return self._get_float64_gr_array()

    def AllBusVolts(self):
        """(read-only) Complex array of all bus, node voltages from most recent solution"""
        self.CheckForError(self._lib.Circuit_Get_AllBusVolts_GR())
        return self._get_complex128_gr_array()

    def AllElementLosses(self):
        """(read-only) Array of total losses (complex) in each circuit element"""
        self.CheckForError(self._lib.Circuit_Get_AllElementLosses_GR())
        return self._get_complex128_gr_array()

    def AllElementNames(self):
        """(read-only) Array of strings containing Full Name of all elements."""
        return self.CheckForError(
            self._get_string_array(self._lib.Circuit_Get_AllElementNames)
        )

    def AllNodeDistances(self):
        """(read-only) Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence."""
        self.CheckForError(self._lib.Circuit_Get_AllNodeDistances_GR())
        return self._get_float64_gr_array()

    def AllNodeNames(self):
        """(read-only) Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc."""
        return self.CheckForError(
            self._get_string_array(self._lib.Circuit_Get_AllNodeNames)
        )

    def LineLosses(self):
        """(read-only) Complex total line losses in the circuit"""
        self.CheckForError(self._lib.Circuit_Get_LineLosses_GR())
        return self._get_complex128_gr_simple()

    def Losses(self):
        """(read-only) Total losses in active circuit, complex number (two-element array of double)."""
        self.CheckForError(self._lib.Circuit_Get_Losses_GR())
        return self._get_complex128_gr_simple()

    def Name(self):
        """(read-only) Name of the active circuit."""
        return self._get_string(self.CheckForError(self._lib.Circuit_Get_Name()))

    def NumBuses(self):
        """(read-only) Total number of Buses in the circuit."""
        return self.CheckForError(self._lib.Circuit_Get_NumBuses())

    def NumCktElements(self):
        """(read-only) Number of CktElements in the circuit."""
        return self.CheckForError(self._lib.Circuit_Get_NumCktElements())

    def NumNodes(self):
        """(read-only) Total number of nodes in the circuit."""
        return self.CheckForError(self._lib.Circuit_Get_NumNodes())

    def ParentPDElement(self):
        """(read-only) Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable."""
        return self.CheckForError(self._lib.Circuit_Get_ParentPDElement())

    def SubstationLosses(self):
        """(read-only) Complex losses in all transformers designated to substations."""
        self.CheckForError(self._lib.Circuit_Get_SubstationLosses_GR())
        return self._get_complex128_gr_simple()

    def SystemY(self):
        """
        (read-only) System Y matrix (after a solution has been performed).
        This is deprecated as it returns a dense matrix. Only use it for small systems.
        For large-scale systems, prefer YMatrix.GetCompressedYMatrix.
        """
        self.CheckForError(self._lib.Circuit_Get_SystemY_GR())
        return self._get_complex128_gr_array()

    def TotalPower(self):
        """(read-only) Total power (complex), kVA delivered to the circuit"""
        self.CheckForError(self._lib.Circuit_Get_TotalPower_GR())
        return self._get_complex128_gr_simple()

    def YCurrents(self):
        """(read-only) Array of doubles containing complex injection currents for the present solution. Is is the "I" vector of I=YV"""
        self.CheckForError(self._lib.Circuit_Get_YCurrents_GR())
        return self._get_complex128_gr_array()

    def YNodeOrder(self):
        """(read-only) Array of strings containing the names of the nodes in the same order as the Y matrix"""
        return self.CheckForError(
            self._get_string_array(self._lib.Circuit_Get_YNodeOrder)
        )

    def YNodeVArray(self):
        """(read-only) Complex array of actual node voltages in same order as SystemY matrix."""
        self.CheckForError(self._lib.Circuit_Get_YNodeVarray_GR())
        return self._get_complex128_gr_array()

    def ElementLosses(self, Value):
        """
        Array of total losses (complex) in a selection of elements.
        Use the element indices (starting at 1) as parameter.

        (API Extension)
        """
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.Circuit_Get_ElementLosses_GR(ValuePtr, ValueCount))
        return self._get_complex128_gr_array()


_Circuit = ICircuit(api_util)

# For backwards compatibility, bind to the default instance
Capacity = _Circuit.Capacity
Disable = _Circuit.Disable
Enable = _Circuit.Enable
EndOfTimeStepUpdate = _Circuit.EndOfTimeStepUpdate
FirstElement = _Circuit.FirstElement
FirstPCElement = _Circuit.FirstPCElement
FirstPDElement = _Circuit.FirstPDElement
AllNodeDistancesByPhase = _Circuit.AllNodeDistancesByPhase
AllNodeNamesByPhase = _Circuit.AllNodeNamesByPhase
AllNodeVmagByPhase = _Circuit.AllNodeVmagByPhase
AllNodeVmagPUByPhase = _Circuit.AllNodeVmagPUByPhase
NextElement = _Circuit.NextElement
NextPCElement = _Circuit.NextPCElement
NextPDElement = _Circuit.NextPDElement
Sample = _Circuit.Sample
SaveSample = _Circuit.SaveSample
SetActiveBus = _Circuit.SetActiveBus
SetActiveBusi = _Circuit.SetActiveBusi
SetActiveClass = _Circuit.SetActiveClass
SetActiveElement = _Circuit.SetActiveElement
UpdateStorage = _Circuit.UpdateStorage
AllBusDistances = _Circuit.AllBusDistances
AllBusNames = _Circuit.AllBusNames
AllBusVMag = _Circuit.AllBusVMag
AllBusMagPu = _Circuit.AllBusMagPu
AllBusVolts = _Circuit.AllBusVolts
AllElementLosses = _Circuit.AllElementLosses
AllElementNames = _Circuit.AllElementNames
AllNodeDistances = _Circuit.AllNodeDistances
AllNodeNames = _Circuit.AllNodeNames
LineLosses = _Circuit.LineLosses
Losses = _Circuit.Losses
Name = _Circuit.Name
NumBuses = _Circuit.NumBuses
NumCktElements = _Circuit.NumCktElements
NumNodes = _Circuit.NumNodes
ParentPDElement = _Circuit.ParentPDElement
SubstationLosses = _Circuit.SubstationLosses
SystemY = _Circuit.SystemY
TotalPower = _Circuit.TotalPower
YCurrents = _Circuit.YCurrents
YNodeOrder = _Circuit.YNodeOrder
YNodeVArray = _Circuit.YNodeVArray
ElementLosses = _Circuit.ElementLosses
_columns = _Circuit._columns
__all__ = [
    "Capacity",
    "Disable",
    "Enable",
    "EndOfTimeStepUpdate",
    "FirstElement",
    "FirstPCElement",
    "FirstPDElement",
    "AllNodeDistancesByPhase",
    "AllNodeNamesByPhase",
    "AllNodeVmagByPhase",
    "AllNodeVmagPUByPhase",
    "NextElement",
    "NextPCElement",
    "NextPDElement",
    "Sample",
    "SaveSample",
    "SetActiveBus",
    "SetActiveBusi",
    "SetActiveClass",
    "SetActiveElement",
    "UpdateStorage",
    "AllBusDistances",
    "AllBusNames",
    "AllBusVMag",
    "AllBusMagPu",
    "AllBusVolts",
    "AllElementLosses",
    "AllElementNames",
    "AllNodeDistances",
    "AllNodeNames",
    "LineLosses",
    "Losses",
    "Name",
    "NumBuses",
    "NumCktElements",
    "NumNodes",
    "ParentPDElement",
    "SubstationLosses",
    "SystemY",
    "TotalPower",
    "YCurrents",
    "YNodeOrder",
    "YNodeVArray",
    "ElementLosses",
]
