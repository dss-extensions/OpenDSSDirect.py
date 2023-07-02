from ._utils import CheckForError, api_util, Base


class IBus(Base):
    __slots__ = []
    _api_prefix = "Bus"
    _columns = [
        "Name",
        "NumNodes",
        "Nodes",
        "Coorddefined",
        "CplxSeqVoltages",
        "Cust_Duration",
        "Cust_Interrupts",
        "Cust_Interrupts",
        "Distance",
        "Int_Duration",
        "Isc",
        "Lambda",
        "N_Customers",
        "N_interrupts",
        "SectionID",
        "SeqVoltages",
        "TotalMiles",
        "VLL",
        "VMagAngle",
        "Voc",
        "Voltages",
        "YscMatrix",
        "Zsc0",
        "Zsc1",
        "ZscMatrix",
        "kVBase",
        "puVLL",
        "puVmagAngle",
        "PuVoltage",
        "X",
        "Y",
        "AllPCEatBus",
        "AllPDEatBus",
    ]

    def GetUniqueNodeNumber(self, StartNumber):
        return self.CheckForError(self._lib.Bus_GetUniqueNodeNumber(StartNumber))

    def ZscRefresh(self):
        return self.CheckForError(self._lib.Bus_ZscRefresh()) != 0

    def Coorddefined(self):
        """(read-only) False=0 else True. Indicates whether a coordinate has been defined for this bus"""
        return self.CheckForError(self._lib.Bus_Get_Coorddefined()) != 0

    def CplxSeqVoltages(self):
        """(read-only) Complex Double array of Sequence Voltages (0, 1, 2) at this Bus."""
        return self._get_float64_array(self._lib.Bus_Get_CplxSeqVoltages)

    def Cust_Duration(self):
        """(read-only) Accumulated customer outage durations"""
        return self.CheckForError(self._lib.Bus_Get_Cust_Duration())

    def Cust_Interrupts(self):
        """(read-only) Annual number of customer-interruptions from this bus"""
        return self.CheckForError(self._lib.Bus_Get_Cust_Interrupts())

    def Distance(self):
        """(read-only) Distance from energymeter (if non-zero)"""
        return self.CheckForError(self._lib.Bus_Get_Distance())

    def Int_Duration(self):
        """(read-only) Average interruption duration, hr."""
        return self.CheckForError(self._lib.Bus_Get_Int_Duration())

    def Isc(self):
        """(read-only) Short circuit currents at bus; Complex Array."""
        return self._get_float64_array(self._lib.Bus_Get_Isc)

    def Lambda(self):
        """(read-only) Accumulated failure rate downstream from this bus; faults per year"""
        return self.CheckForError(self._lib.Bus_Get_Lambda())

    def N_Customers(self):
        """(read-only) Total numbers of customers served downline from this bus"""
        return self.CheckForError(self._lib.Bus_Get_N_Customers())

    def N_interrupts(self):
        """(read-only) Number of interruptions this bus per year"""
        return self.CheckForError(self._lib.Bus_Get_N_interrupts())

    def Name(self):
        """(read-only) Name of Bus"""
        return self._get_string(self.CheckForError(self._lib.Bus_Get_Name()))

    def Nodes(self):
        """(read-only) Integer Array of Node Numbers defined at the bus in same order as the voltages."""
        return self._get_int32_array(self._lib.Bus_Get_Nodes)

    def NumNodes(self):
        """(read-only) Number of Nodes this bus."""
        return self.CheckForError(self._lib.Bus_Get_NumNodes())

    def SectionID(self):
        """(read-only) Integer ID of the feeder section in which this bus is located."""
        return self.CheckForError(self._lib.Bus_Get_SectionID())

    def SeqVoltages(self):
        """(read-only) Double Array of sequence voltages at this bus."""
        return self._get_float64_array(self._lib.Bus_Get_SeqVoltages)

    def TotalMiles(self):
        """(read-only) Total length of line downline from this bus, in miles. For recloser siting algorithm."""
        return self.CheckForError(self._lib.Bus_Get_TotalMiles())

    def VLL(self):
        """(read-only) For 2- and 3-phase buses, returns array of complex numbers represetin L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3."""
        return self._get_float64_array(self._lib.Bus_Get_VLL)

    def VMagAngle(self):
        """(read-only) Array of doubles containing voltages in Magnitude (VLN), angle (deg)"""
        return self._get_float64_array(self._lib.Bus_Get_VMagAngle)

    def Voc(self):
        """(read-only) Open circuit voltage; Complex array."""
        return self._get_float64_array(self._lib.Bus_Get_Voc)

    def Voltages(self):
        """(read-only) Complex array of voltages at this bus."""
        return self._get_float64_array(self._lib.Bus_Get_Voltages)

    def YscMatrix(self):
        """(read-only) Complex array of Ysc matrix at bus. Column by column."""
        return self._get_float64_array(self._lib.Bus_Get_YscMatrix)

    def Zsc0(self):
        """(read-only) Complex Zero-Sequence short circuit impedance at bus."""
        return self._get_float64_array(self._lib.Bus_Get_Zsc0)

    def Zsc1(self):
        """(read-only) Complex Positive-Sequence short circuit impedance at bus.."""
        return self._get_float64_array(self._lib.Bus_Get_Zsc1)

    def ZscMatrix(self):
        """(read-only) Complex array of Zsc matrix at bus. Column by column."""
        return self._get_float64_array(self._lib.Bus_Get_ZscMatrix)

    def kVBase(self):
        """(read-only) Base voltage at bus in kV"""
        return self.CheckForError(self._lib.Bus_Get_kVBase())

    def puVLL(self):
        """(read-only) Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases."""
        return self._get_float64_array(self._lib.Bus_Get_puVLL)

    def puVmagAngle(self):
        """(read-only) Array of doubles containig voltage magnitude, angle pairs in per unit"""
        return self._get_float64_array(self._lib.Bus_Get_puVmagAngle)

    def PuVoltage(self):
        """(read-only) Complex Array of pu voltages at the bus."""
        return self._get_float64_array(self._lib.Bus_Get_puVoltages)

    def X(self, *args):
        """X Coordinate for bus (double)"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Bus_Get_x())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Bus_Set_x(Value))

    def Y(self, *args):
        """Y coordinate for bus(double)"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Bus_Get_y())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Bus_Set_y(Value))

    def LoadList(self):
        """List of strings: Full Names of LOAD elements connected to the active bus."""
        return self.CheckForError(self._get_string_array(self._lib.Bus_Get_LoadList))

    def LineList(self):
        """List of strings: Full Names of LINE elements connected to the active bus."""
        return self.CheckForError(self._get_string_array(self._lib.Bus_Get_LineList))

    def AllPCEatBus(self):
        """Returns an array with the names of all PCE connected to the active bus"""
        result = self.CheckForError(
            self._get_string_array(self._lib.Bus_Get_AllPCEatBus)
        )
        return result

    def AllPDEatBus(self):
        """Returns an array with the names of all PDE connected to the active bus"""
        result = self.CheckForError(
            self._get_string_array(self._lib.Bus_Get_AllPDEatBus)
        )
        return result


_Bus = IBus(api_util)

# For backwards compatibility, bind to the default instance
AllPCEatBus = _Bus.AllPCEatBus
AllPDEatBus = _Bus.AllPDEatBus
GetUniqueNodeNumber = _Bus.GetUniqueNodeNumber
ZscRefresh = _Bus.ZscRefresh
Coorddefined = _Bus.Coorddefined
CplxSeqVoltages = _Bus.CplxSeqVoltages
Cust_Duration = _Bus.Cust_Duration
Cust_Interrupts = _Bus.Cust_Interrupts
Distance = _Bus.Distance
Int_Duration = _Bus.Int_Duration
Isc = _Bus.Isc
Lambda = _Bus.Lambda
N_Customers = _Bus.N_Customers
N_interrupts = _Bus.N_interrupts
Name = _Bus.Name
Nodes = _Bus.Nodes
NumNodes = _Bus.NumNodes
SectionID = _Bus.SectionID
SeqVoltages = _Bus.SeqVoltages
TotalMiles = _Bus.TotalMiles
VLL = _Bus.VLL
VMagAngle = _Bus.VMagAngle
Voc = _Bus.Voc
Voltages = _Bus.Voltages
YscMatrix = _Bus.YscMatrix
Zsc0 = _Bus.Zsc0
Zsc1 = _Bus.Zsc1
ZscMatrix = _Bus.ZscMatrix
kVBase = _Bus.kVBase
puVLL = _Bus.puVLL
puVmagAngle = _Bus.puVmagAngle
PuVoltage = _Bus.PuVoltage
X = _Bus.X
Y = _Bus.Y
LoadList = _Bus.LoadList
LineList = _Bus.LineList
_columns = _Bus._columns
__all__ = [
    "AllPCEatBus",
    "AllPDEatBus",
    "GetUniqueNodeNumber",
    "ZscRefresh",
    "Coorddefined",
    "CplxSeqVoltages",
    "Cust_Duration",
    "Cust_Interrupts",
    "Distance",
    "Int_Duration",
    "Isc",
    "Lambda",
    "N_Customers",
    "N_interrupts",
    "Name",
    "Nodes",
    "NumNodes",
    "SectionID",
    "SeqVoltages",
    "TotalMiles",
    "VLL",
    "VMagAngle",
    "Voc",
    "Voltages",
    "YscMatrix",
    "Zsc0",
    "Zsc1",
    "ZscMatrix",
    "kVBase",
    "puVLL",
    "puVmagAngle",
    "PuVoltage",
    "X",
    "Y",
    "LoadList",
    "LineList",
]
