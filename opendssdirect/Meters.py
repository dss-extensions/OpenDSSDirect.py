from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable
from dss_python_backend.enums import OCPDevType as OCPDevTypeEnum

class IMeters(Iterable):
    __slots__ = []

    __name__ = "Meters"
    _api_prefix = "Meters"
    _columns = [
        "Name",
        "MeteredTerminal",
        "SeqListSize",
        "RegisterNames",
        "MeteredElement",
        "PeakCurrent",
        "AllocFactors",
        "AllEndElements",
        "SAIFIkW",
        "CountEndElements",
        "SAIDI",
        "TotalCustomers",
        "RegisterValues",
        "SAIFI",
        "CustInterrupts",
        "CountBranches",
        "CalcCurrent",
        "AllBranchesInZone",
        "NumSections",
        # "NumSectionCustomers",
        # "SectSeqidx",
        # "SumBranchFltRates",
        # "AvgRepairTime",
        # "SectTotalCust",
        # "OCPDeviceType",
        # "FaultRateXRepairHrs",
        # "NumSectionBranches",
    ]

    def CloseAllDIFiles(self):
        """
        Close All Demand Interval Files. Users are required to close the DI files at the end of a run.

        Original COM help: https://opendss.epri.com/CloseAllDIFiles.html
        """
        self._check_for_error(self._lib.Meters_CloseAllDIFiles())

    def DoReliabilityCalc(self, AssumeRestoration):
        """
        Calculate reliability indices

        Original COM help: https://opendss.epri.com/DoReliabilityCalc.html
        """
        self._check_for_error(self._lib.Meters_DoReliabilityCalc(AssumeRestoration))

    def OpenAllDIFiles(self):
        """
        Open Demand Interval (DI) files

        Original COM help: https://opendss.epri.com/OpenAllDIFiles.html
        """
        self._check_for_error(self._lib.Meters_OpenAllDIFiles())

    def Reset(self):
        """
        Resets registers of active meter.

        Original COM help: https://opendss.epri.com/Reset2.html
        """
        self._check_for_error(self._lib.Meters_Reset())

    def ResetAll(self):
        """
        Resets registers of all meter objects.

        Original COM help: https://opendss.epri.com/ResetAll.html
        """
        self._check_for_error(self._lib.Meters_ResetAll())

    def Sample(self):
        """
        Forces active Meter to take a sample.

        Original COM help: https://opendss.epri.com/Sample1.html
        """
        self._check_for_error(self._lib.Meters_Sample())

    def SampleAll(self):
        """
        Causes all EnergyMeter objects to take a sample at the present time.

        Original COM help: https://opendss.epri.com/SampleAll.html
        """
        self._check_for_error(self._lib.Meters_SampleAll())

    def Save(self):
        """
        Saves meter register values.

        Original COM help: https://opendss.epri.com/Save.html
        """
        self._check_for_error(self._lib.Meters_Save())

    def SaveAll(self):
        """
        Save All EnergyMeter objects

        Original COM help: https://opendss.epri.com/SaveAll.html
        """
        self._check_for_error(self._lib.Meters_SaveAll())

    def SetActiveSection(self, SectIdx):
        self._check_for_error(self._lib.Meters_SetActiveSection(SectIdx))

    def AllBranchesInZone(self):
        """
        Wide string list of all branches in zone of the active EnergyMeter object.

        Original COM help: https://opendss.epri.com/AllBranchesInZone.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Meters_Get_AllBranchesInZone)
        )

    def AllEndElements(self):
        """
        Array of names of all zone end elements.

        Original COM help: https://opendss.epri.com/AllEndElements.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Meters_Get_AllEndElements)
        )

    def AllocFactors(self, *args):
        """
        Array of doubles: set the phase allocation factors for the active meter.

        Original COM help: https://opendss.epri.com/AllocFactors.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Meters_Get_AllocFactors_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))

    def AvgRepairTime(self):
        """
        Average Repair time in this section of the meter zone

        Original COM help: https://opendss.epri.com/AvgRepairTime.html
        """
        return self._check_for_error(self._lib.Meters_Get_AvgRepairTime())

    def CalcCurrent(self, *args):
        """
        Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation

        Original COM help: https://opendss.epri.com/CalcCurrent.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Meters_Get_CalcCurrent_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))

    def CountBranches(self):
        """
        Number of branches in Active EnergyMeter zone. (Same as sequence list size)

        Original COM help: https://opendss.epri.com/CountBranches.html
        """
        return self._check_for_error(self._lib.Meters_Get_CountBranches())

    def CountEndElements(self):
        """
        Number of zone end elements in the active meter zone.

        Original COM help: https://opendss.epri.com/CountEndElements.html
        """
        return self._check_for_error(self._lib.Meters_Get_CountEndElements())

    def CustInterrupts(self):
        """
        Total customer interruptions for this Meter zone based on reliability calcs.

        Original COM help: https://opendss.epri.com/CustInterrupts.html
        """
        return self._check_for_error(self._lib.Meters_Get_CustInterrupts())

    def DIFilesAreOpen(self):
        """
        Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.

        Original COM help: https://opendss.epri.com/DIFilesAreOpen.html
        """
        return self._check_for_error(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    def FaultRateXRepairHrs(self):
        """
        Sum of Fault Rate time Repair Hrs in this section of the meter zone

        Original COM help: https://opendss.epri.com/FaultRateXRepairHrs.html
        """
        return self._check_for_error(self._lib.Meters_Get_FaultRateXRepairHrs())

    def MeteredElement(self, *args):
        """
        Name of metered element

        Original COM help: https://opendss.epri.com/MeteredElement.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Meters_Get_MeteredElement())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Meters_Set_MeteredElement(Value))

    def MeteredTerminal(self, *args):
        """
        Number of Metered Terminal

        Original COM help: https://opendss.epri.com/MeteredTerminal.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Meters_Get_MeteredTerminal())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Meters_Set_MeteredTerminal(Value))

    def NumSectionBranches(self):
        """
        Number of branches (lines) in this section

        Original COM help: https://opendss.epri.com/NumSectionBranches.html
        """
        return self._check_for_error(self._lib.Meters_Get_NumSectionBranches())

    def NumSectionCustomers(self):
        """
        Number of Customers in the active section.

        Original COM help: https://opendss.epri.com/NumSectionCustomers.html
        """
        return self._check_for_error(self._lib.Meters_Get_NumSectionCustomers())

    def NumSections(self):
        """
        Number of feeder sections in this meter's zone

        Original COM help: https://opendss.epri.com/NumSections.html
        """
        return self._check_for_error(self._lib.Meters_Get_NumSections())

    def OCPDeviceType(self):
        """
        Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay

        Original COM help: https://opendss.epri.com/OCPDeviceType.html
        """
        return OCPDevTypeEnum(self._check_for_error(self._lib.Meters_Get_OCPDeviceType()))

    def PeakCurrent(self, *args):
        """
        Array of doubles to set values of Peak Current property

        Original COM help: https://opendss.epri.com/Peakcurrent.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.Meters_Get_Peakcurrent_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))

    def RegisterNames(self):
        """
        Array of strings containing the names of the registers.

        See also the enum `EnergyMeterRegisters` for the standard register names.
        Besides those listed in the enumeration, users may need to check `RegisterNames`
        in order to find a specific register index at runtime.

        Original COM help: https://opendss.epri.com/RegisterNames1.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Meters_Get_RegisterNames)
        )

    def RegisterValues(self):
        """
        Array of all the values contained in the Meter registers for the active Meter.

        Original COM help: https://opendss.epri.com/RegisterValues1.html
        """
        self._check_for_error(self._lib.Meters_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    def SAIDI(self):
        """
        SAIDI for this meter's zone. Execute DoReliabilityCalc first.

        Original COM help: https://opendss.epri.com/SAIDI.html
        """
        return self._check_for_error(self._lib.Meters_Get_SAIDI())

    def SAIFI(self):
        """
        Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.

        Original COM help: https://opendss.epri.com/SAIFI.html
        """
        return self._check_for_error(self._lib.Meters_Get_SAIFI())

    def SAIFIkW(self):
        """
        SAIFI based on kW rather than number of customers. Get after reliability calcs.

        Original COM help: https://opendss.epri.com/SAIFIKW.html
        """
        return self._check_for_error(self._lib.Meters_Get_SAIFIKW())

    def SectSeqidx(self):
        """
        SequenceIndex of the branch at the head of this section

        Original COM help: https://opendss.epri.com/SectSeqIdx.html
        """
        return self._check_for_error(self._lib.Meters_Get_SectSeqIdx())

    def SectTotalCust(self):
        """
        Total Customers downline from this section

        Original COM help: https://opendss.epri.com/SectTotalCust.html
        """
        return self._check_for_error(self._lib.Meters_Get_SectTotalCust())

    def SeqListSize(self):
        """
        Size of the Sequence List

        Original COM help: https://opendss.epri.com/SeqListSize.html
        """
        return self._check_for_error(self._lib.Meters_Get_SeqListSize())

    def SequenceList(self, *args):
        """
        Get/set Index into Meter's SequenceList that contains branch pointers in lexical order.
        Earlier index guaranteed to be upline from later index. Sets PDelement active.

        Original COM help: https://opendss.epri.com/SequenceIndex.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Meters_Get_SequenceIndex())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Meters_Set_SequenceIndex(Value))

    def SumBranchFltRates(self):
        """
        Sum of the branch fault rates in this section of the meter's zone

        Original COM help: https://opendss.epri.com/SumBranchFltRates.html
        """
        return self._check_for_error(self._lib.Meters_Get_SumBranchFltRates())

    def TotalCustomers(self):
        """
        Total Number of customers in this zone (downline from the EnergyMeter)

        Original COM help: https://opendss.epri.com/TotalCustomers.html
        """
        return self._check_for_error(self._lib.Meters_Get_TotalCustomers())

    def Totals(self):
        """
        Totals of all registers of all meters

        Original COM help: https://opendss.epri.com/Totals.html
        """
        self._check_for_error(self._lib.Meters_Get_Totals_GR())
        return self._get_float64_gr_array()

    def ZonePCE(self):
        """
        Returns the list of all PCE within the area covered by the energy meter

        Original COM help: https://opendss.epri.com/ZonePCE.html
        """
        result = self._check_for_error(
            self._get_string_array(self._lib.Meters_Get_ZonePCE)
        )
        return result


_Meters = IMeters(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
