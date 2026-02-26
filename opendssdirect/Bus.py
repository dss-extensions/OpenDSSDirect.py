from ._utils import api_util
from .Bases import Base


class IBus(Base):
    __slots__ = []

    __name__ = "Bus"
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
        """
        Return a unique node number at the active bus to avoid node collisions and adds
        it to the node list for the bus.

        Original COM help: https://opendss.epri.com/GetUniqueNodeNumber.html
        """
        return self._lib.Bus_GetUniqueNodeNumber(StartNumber)

    def ZscRefresh(self):
        """
        Refreshes the Zsc matrix for the active bus.

        Original COM help: https://opendss.epri.com/ZscRefresh.html
        """
        return self._lib.Bus_ZscRefresh()

    def Coorddefined(self):
        """
        Indicates whether a coordinate has been defined for this bus

        Original COM help: https://opendss.epri.com/Coorddefined.html
        """
        return self._lib.Bus_Get_Coorddefined()

    def CplxSeqVoltages(self):
        """
        Complex array of Sequence Voltages (0, 1, 2) at this Bus.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages.html
        """
        return self._lib.Bus_Get_CplxSeqVoltages_GR()

    def Cust_Duration(self):
        """
        Accumulated customer outage durations

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Cust_Duration.html
        """
        return self._lib.Bus_Get_Cust_Duration()

    def Cust_Interrupts(self):
        """
        Annual number of customer-interruptions from this bus

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Cust_Interrupts.html
        """
        return self._lib.Bus_Get_Cust_Interrupts()

    def Distance(self):
        """
        Distance from EnergyMeter (if non-zero)

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/Distance.html
        """
        return self._lib.Bus_Get_Distance()

    def Int_Duration(self):
        """
        Average interruption duration, hours.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Int_Duration.html
        """
        return self._lib.Bus_Get_Int_Duration()

    def Isc(self):
        """
        Short circuit currents at bus; Complex Array.

        *Requires a previous solution in `FaultStudy` mode.*

        Original COM help: https://opendss.epri.com/Isc.html
        """
        return self._lib.Bus_Get_Isc_GR()

    def Lambda(self):
        """
        Accumulated failure rate downstream from this bus; faults per year

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Lambda.html
        """
        return self._lib.Bus_Get_Lambda()

    def N_Customers(self):
        """
        Total numbers of customers served downline from this bus

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/N_Customers.html
        """
        return self._lib.Bus_Get_N_Customers()

    def N_interrupts(self):
        """
        Number of interruptions this bus per year

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/N_interrupts.html
        """
        return self._lib.Bus_Get_N_interrupts()

    def Name(self):
        """
        Name of the active Bus

        Original COM help: https://opendss.epri.com/Name1.html
        """
        return self._lib.Bus_Get_Name()

    def Nodes(self):
        """
        Integer Array of Node Numbers defined at the bus in same order as the voltages.

        Original COM help: https://opendss.epri.com/Nodes.html
        """
        return self._lib.Bus_Get_Nodes_GR()

    def NumNodes(self):
        """
        Number of Nodes this bus.

        Original COM help: https://opendss.epri.com/NumNodes.html
        """
        return self._lib.Bus_Get_NumNodes()

    def SectionID(self):
        """
        Integer ID of the feeder section in which this bus is located.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/SectionID.html
        """
        return self._lib.Bus_Get_SectionID()

    def SeqVoltages(self):
        """
        Double Array of sequence voltages at this bus. Magnitudes only.

        Original COM help: https://opendss.epri.com/SeqVoltages.html
        """
        return self._lib.Bus_Get_SeqVoltages_GR()

    def TotalMiles(self):
        """
        Total length of line downline from this bus, in miles. For recloser siting algorithm.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/TotalMiles.html
        """
        return self._lib.Bus_Get_TotalMiles()

    def VLL(self):
        """
        For 2- and 3-phase buses, returns array of complex numbers representing L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.

        Original COM help: https://opendss.epri.com/VLL.html
        """
        return self._lib.Bus_Get_VLL_GR()

    def VMagAngle(self):
        """
        Array of doubles containing voltages in Magnitude (VLN), angle (degrees)

        Original COM help: https://opendss.epri.com/VMagAngle.html
        """
        return self._lib.Bus_Get_VMagAngle_GR()

    def Voc(self):
        """
        Open circuit voltage; Complex array.

        *Requires a previous solution in `FaultStudy` mode.*

        Original COM help: https://opendss.epri.com/Voc.html
        """
        return self._lib.Bus_Get_Voc_GR()

    def Voltages(self):
        """
        Complex array of voltages at this bus.

        Original COM help: https://opendss.epri.com/Voltages.html
        """
        return self._lib.Bus_Get_Voltages_GR()

    def YscMatrix(self):
        """
        Complex array of Ysc matrix at bus. Column by column.

        *Requires a previous solution in `FaultStudy` mode or a call to `ZscRefresh`.*

        Original COM help: https://opendss.epri.com/YscMatrix.html
        """
        return self._lib.Bus_Get_YscMatrix_GR()

    def Zsc0(self):
        """
        Complex Zero-Sequence short circuit impedance at bus.

        *Requires a previous solution in `FaultStudy` mode or a call to `ZscRefresh`.*

        Original COM help: https://opendss.epri.com/Zsc0.html
        """
        return self._lib.Bus_Get_Zsc0_GR()

    def Zsc1(self):
        """
        Complex Positive-Sequence short circuit impedance at bus.

        *Requires a previous solution in `FaultStudy` mode or a call to `ZscRefresh`.*

        Original COM help: https://opendss.epri.com/Zsc1.html
        """
        return self._lib.Bus_Get_Zsc1_GR()

    def ZscMatrix(self):
        """
        Complex array of Zsc matrix at bus. Column by column.

        *Requires a previous solution in `FaultStudy` mode or a call to `ZscRefresh`.*

        Original COM help: https://opendss.epri.com/ZscMatrix.html
        """
        return self._lib.Bus_Get_ZscMatrix_GR()

    def kVBase(self):
        """
        Base voltage at bus in kV

        Original COM help: https://opendss.epri.com/kVBase.html
        """
        return self._lib.Bus_Get_kVBase()

    def puVLL(self):
        """
        Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.

        Original COM help: https://opendss.epri.com/puVLL.html
        """
        return self._lib.Bus_Get_puVLL_GR()

    def puVmagAngle(self):
        """
        Array of doubles containing voltage magnitude, angle (degrees) pairs in per unit

        Original COM help: https://opendss.epri.com/puVmagAngle.html
        """
        return self._lib.Bus_Get_puVmagAngle_GR()

    def PuVoltage(self):
        """
        Complex Array of pu voltages at the bus.

        Original COM help: https://opendss.epri.com/puVoltages.html
        """
        return self._lib.Bus_Get_puVoltages_GR()

    def ZSC012Matrix(self):
        """
        Complex array containing the complete 012 Zsc matrix.
        Only available after Zsc is computed, either through the "ZscRefresh" command, or running a "FaultStudy" solution.
        Only available for buses with 3 nodes.

        *Requires a previous solution in `FaultStudy` mode or a call to `ZscRefresh`.*

        Original COM help: https://opendss.epri.com/ZSC012Matrix.html
        """
        return self._lib.Bus_Get_ZSC012Matrix_GR()

    def X(self, *args):
        """
        X Coordinate for bus

        Original COM help: https://opendss.epri.com/x.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Bus_Get_x()

        # Setter
        (Value,) = args
        self._lib.Bus_Set_x(Value)

    def Y(self, *args):
        """
        Y coordinate for bus

        Original COM help: https://opendss.epri.com/y.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.Bus_Get_y()

        # Setter
        (Value,) = args
        self._lib.Bus_Set_y(Value)

    def LoadList(self):
        """
        List of strings: Full Names of LOAD elements connected to the active bus.

        Original COM help: https://opendss.epri.com/LoadList.html
        """
        return self._lib.Bus_Get_LoadList()

    def LineList(self):
        """
        List of strings: Full Names of LINE elements connected to the active bus.

        Original COM help: https://opendss.epri.com/LineList.html
        """
        return self._lib.Bus_Get_LineList()

    def AllPCEatBus(self):
        """
        Returns an array with the names of all PCE connected to the active bus

        This also includes shunt Capacitors/Reactors.

        Original COM help: https://opendss.epri.com/AllPCEatBus.html
        """
        return self._lib.Bus_Get_AllPCEatBus()

    def AllPDEatBus(self):
        """
        Returns an array with the names of all PDE connected to the active bus

        This excludes shunt Capacitors/Reactors.

        Original COM help: https://opendss.epri.com/AllPDEatBus1.html
        """
        return self._lib.Bus_Get_AllPDEatBus()

    def to_altdss(self):
        """
        Returns a Python object for the current active bus in the circuit (if any).

        Requires AltDSS-Python.

        *Available only for the AltDSS engine.*

        **(API Extension)**

        """
        idx = self._lib.Bus_Get_idx()
        if idx < 0:
            return None
        return self._api_util.get_bus_obj(self._lib.Alt_Bus_GetByIndex(idx))


_Bus = IBus(api_util)

# For backwards compatibility, bind to the default instance
AllPCEatBus = _Bus.AllPCEatBus
AllPDEatBus = _Bus.AllPDEatBus
Coorddefined = _Bus.Coorddefined
CplxSeqVoltages = _Bus.CplxSeqVoltages
Cust_Duration = _Bus.Cust_Duration
Cust_Interrupts = _Bus.Cust_Interrupts
Distance = _Bus.Distance
GetUniqueNodeNumber = _Bus.GetUniqueNodeNumber
Int_Duration = _Bus.Int_Duration
Isc = _Bus.Isc
Lambda = _Bus.Lambda
LineList = _Bus.LineList
LoadList = _Bus.LoadList
N_Customers = _Bus.N_Customers
N_interrupts = _Bus.N_interrupts
Name = _Bus.Name
Nodes = _Bus.Nodes
NumNodes = _Bus.NumNodes
PuVoltage = _Bus.PuVoltage
SectionID = _Bus.SectionID
SeqVoltages = _Bus.SeqVoltages
TotalMiles = _Bus.TotalMiles
VLL = _Bus.VLL
VMagAngle = _Bus.VMagAngle
Voc = _Bus.Voc
Voltages = _Bus.Voltages
X = _Bus.X
Y = _Bus.Y
YscMatrix = _Bus.YscMatrix
ZSC012Matrix = _Bus.ZSC012Matrix
Zsc0 = _Bus.Zsc0
Zsc1 = _Bus.Zsc1
ZscMatrix = _Bus.ZscMatrix
ZscRefresh = _Bus.ZscRefresh
kVBase = _Bus.kVBase
puVLL = _Bus.puVLL
puVmagAngle = _Bus.puVmagAngle
to_altdss = _Bus.to_altdss
_columns = _Bus._columns
__all__ = [
    "AllPCEatBus",
    "AllPDEatBus",
    "Coorddefined",
    "CplxSeqVoltages",
    "Cust_Duration",
    "Cust_Interrupts",
    "Distance",
    "GetUniqueNodeNumber",
    "Int_Duration",
    "Isc",
    "Lambda",
    "LineList",
    "LoadList",
    "N_Customers",
    "N_interrupts",
    "Name",
    "Nodes",
    "NumNodes",
    "PuVoltage",
    "SectionID",
    "SeqVoltages",
    "TotalMiles",
    "VLL",
    "VMagAngle",
    "Voc",
    "Voltages",
    "X",
    "Y",
    "YscMatrix",
    "ZSC012Matrix",
    "Zsc0",
    "Zsc1",
    "ZscMatrix",
    "ZscRefresh",
    "kVBase",
    "puVLL",
    "puVmagAngle",
    "to_altdss",
]
