from ._utils import api_util
from .Bases import Base


class IPDElements(Base):
    """
    The PDElements interface allows accessing some common properties and 
    methods shared across power delivery elements in the DSS engine.

    Users can iterate on all PD elements directly through this interface, 
    or enable a PD element through a dedicated interface (e.g. use `Lines.Name`, `Transformers.First/Next`)
    and access the properties here.

    If you are new to OpenDSS/AltDSS and this classic interface, please read the following document
    for an overview of the "active element" paradigm used by COM and the classic APIs:
        
    https://dss-extensions.org/classic_api.html#the-active-paradigm
    """

    __slots__ = []

    __name__ = "PDElements"
    _api_prefix = "PDElements"
    _columns = [
        "Name",
        "AccumulatedL",
        "ParentPDElement",
        "FromTerminal",
        "IsShunt",
        "NumCustomers",
        "SectionID",
        "FaultRate",
        "RepairTime",
        "TotalMiles",
        "TotalCustomers",
        "PctPermanent",
        "Lambda",
    ]

    def AccumulatedL(self):
        """
        Accumulated failure rate for this branch on downline

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/AccumulatedL.html
        """
        return self._lib.PDElements_Get_AccumulatedL()

    def Count(self):
        """
        Number of PD elements (including disabled elements)

        Original COM help: https://opendss.epri.com/Count12.html
        """
        return self._lib.PDElements_Get_Count()

    def FaultRate(self, *args):
        """
        Get/Set Number of failures per year.
        For LINE elements: Number of failures per unit length per year.
        """
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_FaultRate()

        # Setter
        (Value,) = args
        self._lib.PDElements_Set_FaultRate(Value)

    def First(self):
        """
        (read-only) Set the first enabled PD element to be the active element.
        Returns 0 if none found.
        """
        return self._lib.PDElements_Get_First()

    def FromTerminal(self):
        """
        (read-only) Number of the terminal of active PD element that is on the "from"
        side. This is set after the meter zone is determined.

        *Requires an energy meter with an updated zone.*
        """
        return self._lib.PDElements_Get_FromTerminal()

    def IsShunt(self):
        """
        (read-only) Boolean indicating of PD element should be treated as a shunt
        element rather than a series element. Applies to Capacitor and Reactor
        elements in particular.
        """
        return self._lib.PDElements_Get_IsShunt()

    def Lambda(self):
        """
        Failure rate for this branch. Faults per year including length of line.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Lambda1.html
        """
        return self._lib.PDElements_Get_Lambda()

    def Name(self, *args):
        """
        Get/Set name of active PD Element. Returns null string if active element
        is not PDElement type.
        """
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_Name()

        # Setter
        (Value,) = args
        self._lib.PDElements_Set_Name(Value)

    def Next(self):
        """
        (read-only) Advance to the next PD element in the circuit. Enabled elements
        only. Returns 0 when no more elements.
        """
        return self._lib.PDElements_Get_Next()

    def NumCustomers(self):
        """
        Number of customers, this branch

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/Numcustomers.html
        """
        return self._lib.PDElements_Get_Numcustomers()

    def ParentPDElement(self):
        """
        (read-only) Sets the parent PD element to be the active circuit element.
        Returns 0 if no more elements upline.

        *Requires an energy meter with an updated zone.*
        """
        return self._lib.PDElements_Get_ParentPDElement()

    def RepairTime(self, *args):
        """
        Average repair time for this element in hours

        Original COM help: https://opendss.epri.com/RepairTime.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_RepairTime()

        # Setter
        (Value,) = args
        self._lib.PDElements_Set_RepairTime(Value)

    def SectionID(self):
        """
        Integer ID of the feeder section that this PDElement branch is part of

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/SectionID1.html
        """
        return self._lib.PDElements_Get_SectionID()

    def TotalMiles(self):
        """
        Total miles of line from this element to the end of the zone. For recloser siting algorithm.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/TotalMiles1.html
        """
        return self._lib.PDElements_Get_TotalMiles()

    def TotalCustomers(self):
        """
        Total number of customers from this branch to the end of the zone

        *Requires a circuit with an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/TotalCustomers1.html
        """
        return self._lib.PDElements_Get_Totalcustomers()

    def PctPermanent(self, *args):
        """
        Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

        Original COM help: https://opendss.epri.com/pctPermanent.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_pctPermanent()

        # Setter
        (Value,) = args
        self._lib.PDElements_Set_pctPermanent(Value)

    def AllNames(self):
        """
        Array of strings consisting of all PD element names.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllNames()

    def AllMaxCurrents(self, AllNodes=False):
        """
        Array of doubles with the maximum current across the conductors, for each PD
        element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to
        force the analysis to all terminals.

        See also:
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllMaxCurrents_GR(AllNodes)

    def AllPctNorm(self, AllNodes=False):
        """
        Array of doubles with the maximum current across the conductors as a percentage
        of the Normal Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to
        force the analysis to all terminals.

        See also:
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllPctNorm_GR(AllNodes)

    def AllPctEmerg(self, AllNodes=False):
        """
        Array of doubles with the maximum current across the conductors as a percentage
        of the Emergency Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to
        force the analysis to all terminals.

        See also:
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllPctEmerg_GR(AllNodes)

    def AllCurrents(self):
        """
        Complex array of currents for all conductors, all terminals, for each PD element.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllCurrents_GR()

    def AllCurrentsMagAng(self):
        """
        Complex array (magnitude and angle format) of currents for all conductors, all terminals, for each PD element.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllCurrentsMagAng_GR()

    def AllCplxSeqCurrents(self):
        """
        Complex double array of Sequence Currents for all conductors of all terminals, for each PD elements.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllCplxSeqCurrents_GR()

    def AllSeqCurrents(self):
        """
        Double array of the symmetrical component currents (magnitudes only) into each 3-phase terminal, for each PD element.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllSeqCurrents_GR()

    def AllPowers(self):
        """
        Complex array of powers into each conductor of each terminal, for each PD element.

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllPowers_GR()

    def AllSeqPowers(self):
        """
        Complex array of sequence powers into each 3-phase terminal, for each PD element

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllSeqPowers_GR()

    def AllNumPhases(self):
        """
        Integer array listing the number of phases of all PD elements

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllNumPhases_GR()

    def AllNumConductors(self):
        """
        Integer array listing the number of conductors of all PD elements

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllNumConductors_GR()

    def AllNumTerminals(self):
        """
        Integer array listing the number of terminals of all PD elements

        **(API Extension)**
        """
        return self._lib.PDElements_Get_AllNumTerminals_GR()


_PDElements = IPDElements(api_util)

# For backwards compatibility, bind to the default instance
AccumulatedL = _PDElements.AccumulatedL
AllCplxSeqCurrents = _PDElements.AllCplxSeqCurrents
AllCurrents = _PDElements.AllCurrents
AllCurrentsMagAng = _PDElements.AllCurrentsMagAng
AllMaxCurrents = _PDElements.AllMaxCurrents
AllNames = _PDElements.AllNames
AllNumConductors = _PDElements.AllNumConductors
AllNumPhases = _PDElements.AllNumPhases
AllNumTerminals = _PDElements.AllNumTerminals
AllPctEmerg = _PDElements.AllPctEmerg
AllPctNorm = _PDElements.AllPctNorm
AllPowers = _PDElements.AllPowers
AllSeqCurrents = _PDElements.AllSeqCurrents
AllSeqPowers = _PDElements.AllSeqPowers
Count = _PDElements.Count
FaultRate = _PDElements.FaultRate
First = _PDElements.First
FromTerminal = _PDElements.FromTerminal
IsShunt = _PDElements.IsShunt
Lambda = _PDElements.Lambda
Name = _PDElements.Name
Next = _PDElements.Next
NumCustomers = _PDElements.NumCustomers
ParentPDElement = _PDElements.ParentPDElement
PctPermanent = _PDElements.PctPermanent
RepairTime = _PDElements.RepairTime
SectionID = _PDElements.SectionID
TotalCustomers = _PDElements.TotalCustomers
TotalMiles = _PDElements.TotalMiles
_columns = _PDElements._columns
__all__ = [
    "AccumulatedL",
    "AllCplxSeqCurrents",
    "AllCurrents",
    "AllCurrentsMagAng",
    "AllMaxCurrents",
    "AllNames",
    "AllNumConductors",
    "AllNumPhases",
    "AllNumTerminals",
    "AllPctEmerg",
    "AllPctNorm",
    "AllPowers",
    "AllSeqCurrents",
    "AllSeqPowers",
    "Count",
    "FaultRate",
    "First",
    "FromTerminal",
    "IsShunt",
    "Lambda",
    "Name",
    "Next",
    "NumCustomers",
    "ParentPDElement",
    "PctPermanent",
    "RepairTime",
    "SectionID",
    "TotalCustomers",
    "TotalMiles",
]
