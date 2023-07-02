from ._utils import codec, CheckForError, api_util, Iterable


class IMeters(Iterable):
    __slots__ = []
    __name__ = "Meters"
    _api_prefix = "Meters"
    _columns = [
        "Name",
        "Totals",
        "MeteredTerminal",
        "NumSectionCustomers",
        "SectSeqidx",
        "SumBranchFltRates",
        "SeqListSize",
        "AvgRepairTime",
        "RegisterNames",
        "SectTotalCust",
        "SequenceList",
        "MeteredElement",
        "PeakCurrent",
        "AllocFactors",
        "AllEndElements",
        "OCPDeviceType",
        "SAIFIkW",
        "CountEndElements",
        "NumSections",
        "SAIDI",
        "TotalCustomers",
        "RegisterValues",
        "SAIFI",
        "CustInterrupts",
        "CountBranches",
        "CalcCurrent",
        "AllBranchesInZone",
        "FaultRateXRepairHrs",
        "NumSectionBranches",
    ]

    def CloseAllDIFiles(self):
        self.CheckForError(self._lib.Meters_CloseAllDIFiles())

    def DoReliabilityCalc(self, AssumeRestoration):
        self.CheckForError(self._lib.Meters_DoReliabilityCalc(AssumeRestoration))

    def OpenAllDIFiles(self):
        self.CheckForError(self._lib.Meters_OpenAllDIFiles())

    def Reset(self):
        self.CheckForError(self._lib.Meters_Reset())

    def ResetAll(self):
        self.CheckForError(self._lib.Meters_ResetAll())

    def Sample(self):
        self.CheckForError(self._lib.Meters_Sample())

    def SampleAll(self):
        self.CheckForError(self._lib.Meters_SampleAll())

    def Save(self):
        self.CheckForError(self._lib.Meters_Save())

    def SaveAll(self):
        self.CheckForError(self._lib.Meters_SaveAll())

    def SetActiveSection(self, SectIdx):
        self.CheckForError(self._lib.Meters_SetActiveSection(SectIdx))

    def AllBranchesInZone(self):
        """(read-only) Wide string list of all branches in zone of the active energymeter object."""
        return self.CheckForError(
            self._get_string_array(self._lib.Meters_Get_AllBranchesInZone)
        )

    def AllEndElements(self):
        """(read-only) Array of names of all zone end elements."""
        return self.CheckForError(
            self._get_string_array(self._lib.Meters_Get_AllEndElements)
        )

    def AllocFactors(self, *args):
        """Array of doubles: set the phase allocation factors for the active meter."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Meters_Get_AllocFactors)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))

    def AvgRepairTime(self):
        """(read-only) Average Repair time in this section of the meter zone"""
        return self.CheckForError(self._lib.Meters_Get_AvgRepairTime())

    def CalcCurrent(self, *args):
        """Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Meters_Get_CalcCurrent)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))

    def CountBranches(self):
        """(read-only) Number of branches in Active energymeter zone. (Same as sequencelist size)"""
        return self.CheckForError(self._lib.Meters_Get_CountBranches())

    def CountEndElements(self):
        """(read-only) Number of zone end elements in the active meter zone."""
        return self.CheckForError(self._lib.Meters_Get_CountEndElements())

    def CustInterrupts(self):
        """(read-only) Total customer interruptions for this Meter zone based on reliability calcs."""
        return self.CheckForError(self._lib.Meters_Get_CustInterrupts())

    def DIFilesAreOpen(self):
        """(read-only) Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened."""
        return self.CheckForError(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    def FaultRateXRepairHrs(self):
        """(read-only) Sum of Fault Rate time Repair Hrs in this section of the meter zone"""
        return self.CheckForError(self._lib.Meters_Get_FaultRateXRepairHrs())

    def MeteredElement(self, *args):
        """Set Name of metered element"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Meters_Get_MeteredElement())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Meters_Set_MeteredElement(Value))

    def MeteredTerminal(self, *args):
        """set Number of Metered Terminal"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Meters_Get_MeteredTerminal())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Meters_Set_MeteredTerminal(Value))

    def NumSectionBranches(self):
        """(read-only) Number of branches (lines) in this section"""
        return self.CheckForError(self._lib.Meters_Get_NumSectionBranches())

    def NumSectionCustomers(self):
        """(read-only) Number of Customers in the active section."""
        return self.CheckForError(self._lib.Meters_Get_NumSectionCustomers())

    def NumSections(self):
        """(read-only) Number of feeder sections in this meter's zone"""
        return self.CheckForError(self._lib.Meters_Get_NumSections())

    def OCPDeviceType(self):
        """(read-only) Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay"""
        return self.CheckForError(self._lib.Meters_Get_OCPDeviceType())

    def PeakCurrent(self, *args):
        """Array of doubles to set values of Peak Current property"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Meters_Get_Peakcurrent)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))

    def RegisterNames(self):
        """(read-only) Array of strings containing the names of the registers."""
        return self.CheckForError(
            self._get_string_array(self._lib.Meters_Get_RegisterNames)
        )

    def RegisterValues(self):
        """(read-only) Array of all the values contained in the Meter registers for the active Meter."""
        return self._get_float64_array(self._lib.Meters_Get_RegisterValues)

    def SAIDI(self):
        """(read-only) SAIDI for this meter's zone. Execute DoReliabilityCalc first."""
        return self.CheckForError(self._lib.Meters_Get_SAIDI())

    def SAIFI(self):
        """(read-only) Returns SAIFI for this meter's Zone. Execute Reliability Calc method first."""
        return self.CheckForError(self._lib.Meters_Get_SAIFI())

    def SAIFIkW(self):
        """(read-only) SAIFI based on kW rather than number of customers. Get after reliability calcs."""
        return self.CheckForError(self._lib.Meters_Get_SAIFIKW())

    def SectSeqidx(self):
        """(read-only) SequenceIndex of the branch at the head of this section"""
        return self.CheckForError(self._lib.Meters_Get_SectSeqIdx())

    def SectTotalCust(self):
        """(read-only) Total Customers downline from this section"""
        return self.CheckForError(self._lib.Meters_Get_SectTotalCust())

    def SeqListSize(self):
        """(read-only) Size of Sequence List"""
        return self.CheckForError(self._lib.Meters_Get_SeqListSize())

    def SequenceList(self, *args):
        """Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Meters_Get_SequenceIndex())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Meters_Set_SequenceIndex(Value))

    def SumBranchFltRates(self):
        """(read-only) Sum of the branch fault rates in this section of the meter's zone"""
        return self.CheckForError(self._lib.Meters_Get_SumBranchFltRates())

    def TotalCustomers(self):
        """(read-only) Total Number of customers in this zone (downline from the EnergyMeter)"""
        return self.CheckForError(self._lib.Meters_Get_TotalCustomers())

    def Totals(self):
        """(read-only) Totals of all registers of all meters"""
        return self._get_float64_array(self._lib.Meters_Get_Totals)

    def ZonePCE(self):
        """Returns the list of all PCE within the area covered by the energy meter"""
        result = self.CheckForError(
            self._get_string_array(self._lib.Meters_Get_ZonePCE)
        )
        return result


_Meters = IMeters(api_util)

# For backwards compatibility, bind to the default instance
CloseAllDIFiles = _Meters.CloseAllDIFiles
DoReliabilityCalc = _Meters.DoReliabilityCalc
OpenAllDIFiles = _Meters.OpenAllDIFiles
Reset = _Meters.Reset
ResetAll = _Meters.ResetAll
Sample = _Meters.Sample
SampleAll = _Meters.SampleAll
Save = _Meters.Save
SaveAll = _Meters.SaveAll
SetActiveSection = _Meters.SetActiveSection
AllBranchesInZone = _Meters.AllBranchesInZone
AllEndElements = _Meters.AllEndElements
AllNames = _Meters.AllNames
AllocFactors = _Meters.AllocFactors
AvgRepairTime = _Meters.AvgRepairTime
CalcCurrent = _Meters.CalcCurrent
Count = _Meters.Count
CountBranches = _Meters.CountBranches
CountEndElements = _Meters.CountEndElements
CustInterrupts = _Meters.CustInterrupts
DIFilesAreOpen = _Meters.DIFilesAreOpen
FaultRateXRepairHrs = _Meters.FaultRateXRepairHrs
First = _Meters.First
MeteredElement = _Meters.MeteredElement
MeteredTerminal = _Meters.MeteredTerminal
Name = _Meters.Name
Next = _Meters.Next
NumSectionBranches = _Meters.NumSectionBranches
NumSectionCustomers = _Meters.NumSectionCustomers
NumSections = _Meters.NumSections
OCPDeviceType = _Meters.OCPDeviceType
PeakCurrent = _Meters.PeakCurrent
RegisterNames = _Meters.RegisterNames
RegisterValues = _Meters.RegisterValues
SAIDI = _Meters.SAIDI
SAIFI = _Meters.SAIFI
SAIFIkW = _Meters.SAIFIkW
SectSeqidx = _Meters.SectSeqidx
SectTotalCust = _Meters.SectTotalCust
SeqListSize = _Meters.SeqListSize
SequenceList = _Meters.SequenceList
SumBranchFltRates = _Meters.SumBranchFltRates
TotalCustomers = _Meters.TotalCustomers
Totals = _Meters.Totals
ZonePCE = _Meters.ZonePCE
Idx = _Meters.Idx
_columns = _Meters._columns
__all__ = [
    "CloseAllDIFiles",
    "DoReliabilityCalc",
    "OpenAllDIFiles",
    "Reset",
    "ResetAll",
    "Sample",
    "SampleAll",
    "Save",
    "SaveAll",
    "SetActiveSection",
    "AllBranchesInZone",
    "AllEndElements",
    "AllNames",
    "AllocFactors",
    "AvgRepairTime",
    "CalcCurrent",
    "Count",
    "CountBranches",
    "CountEndElements",
    "CustInterrupts",
    "DIFilesAreOpen",
    "FaultRateXRepairHrs",
    "First",
    "MeteredElement",
    "MeteredTerminal",
    "Name",
    "Next",
    "NumSectionBranches",
    "NumSectionCustomers",
    "NumSections",
    "OCPDeviceType",
    "PeakCurrent",
    "RegisterNames",
    "RegisterValues",
    "SAIDI",
    "SAIFI",
    "SAIFIkW",
    "SectSeqidx",
    "SectTotalCust",
    "SeqListSize",
    "SequenceList",
    "SumBranchFltRates",
    "TotalCustomers",
    "Totals",
    "ZonePCE",
    "Idx",
]
