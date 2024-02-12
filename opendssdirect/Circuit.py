import json
from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base

class ICircuit(Base):
    __slots__ = []

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
        """
        Compute the maximum load the active circuit can serve in the PRESENT YEAR.

        This method uses the EnergyMeter objects with the registers set with the
        `SET UEREGS= (...)` command for the AutoAdd functions.

        Returns the metered kW (load + losses - generation) and per unit load multiplier
        for the loading level at which something in the system reports an overload or
        undervoltage. If no violations, then it returns the metered kW for peak load
        for the year (1.0 multiplier).

        Aborts and returns 0 if no EnergyMeters.

        Original COM help: https://opendss.epri.com/Capacity1.html
        """
        return self._check_for_error(self._lib.Circuit_Capacity(Start, Increment))

    def Disable(self, Name):
        """
        Disable a circuit element by name (removes from circuit but leave in database).

        Original COM help: https://opendss.epri.com/Disable.html
        """
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)
        self._check_for_error(self._lib.Circuit_Disable(Name))

    def Enable(self, Name):
        """
        Enable a circuit element by name

        Original COM help: https://opendss.epri.com/Enable.html
        """
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)
        self._check_for_error(self._lib.Circuit_Enable(Name))

    def EndOfTimeStepUpdate(self):
        """
        Call `EndOfTimeStepCleanup` in SolutionAlgs (Do cleanup, sample monitors, and increment time).

        Original COM help: https://opendss.epri.com/EndOfTimeStepUpdate.html
        """
        self._check_for_error(self._lib.Circuit_EndOfTimeStepUpdate())

    def FirstElement(self):
        """
        Set the first element of active class to be the Active element in the active circuit.

        Returns 0 if none.

        Original COM help: https://opendss.epri.com/FirstElement.html
        """
        return self._check_for_error(self._lib.Circuit_FirstElement())

    def FirstPCElement(self):
        """
        Set the first Power Conversion (PC) element to be the active element.

        Returns 0 if none.

        Original COM help: https://opendss.epri.com/FirstPCElement.html
        """
        return self._check_for_error(self._lib.Circuit_FirstPCElement())

    def FirstPDElement(self):
        """
        Set the first Power Delivery (PD) element to be the active element.

        Returns 0 if none.

        Original COM help: https://opendss.epri.com/FirstPDElement.html
        """
        return self._check_for_error(self._lib.Circuit_FirstPDElement())

    def AllNodeDistancesByPhase(self, Phase):
        """Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties."""
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistancesByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def AllNodeNamesByPhase(self, Phase):
        """Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties."""
        return self._check_for_error(
            self._get_string_array(self._lib.Circuit_Get_AllNodeNamesByPhase, Phase)
        )

    def AllNodeVmagByPhase(self, Phase):
        """Returns Array of doubles represent voltage magnitudes for nodes on the specified phase."""
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def AllNodeVmagPUByPhase(self, Phase):
        """Returns array of per unit voltage magnitudes for each node by phase"""
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagPUByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NextElement(self):
        """
        Set the next element of the active class to be the active element in the active circuit.
        Returns 0 if no more elements..

        Original COM help: https://opendss.epri.com/NextElement.html
        """
        return self._check_for_error(self._lib.Circuit_NextElement())

    def NextPCElement(self):
        """
        Get the next Power Conversion (PC) element to be the active element.

        Original COM help: https://opendss.epri.com/NextPCElement.html
        """
        return self._check_for_error(self._lib.Circuit_NextPCElement())

    def NextPDElement(self):
        """
        Get the next Power Delivery (PD) element to be the active element.

        Original COM help: https://opendss.epri.com/NextPDElement.html
        """
        return self._check_for_error(self._lib.Circuit_NextPDElement())

    def Sample(self):
        """
        Force all Meters and Monitors to take a sample.

        Original COM help: https://opendss.epri.com/Sample.html
        """
        self._check_for_error(self._lib.Circuit_Sample())

    def SaveSample(self):
        """
        Force all meters and monitors to save their current buffers.

        Original COM help: https://opendss.epri.com/SaveSample.html
        """
        self._check_for_error(self._lib.Circuit_SaveSample())

    def SetActiveBus(self, BusName):
        """
        Sets Active bus by name.

        Ignores node list. Returns bus index (zero based) compatible with `AllBusNames` and Buses collection.

        Original COM help: https://opendss.epri.com/SetActiveBus.html
        """
        if not isinstance(BusName, bytes):
            BusName = BusName.encode(self._api_util.codec)
        return self._check_for_error(self._lib.Circuit_SetActiveBus(BusName))

    def SetActiveBusi(self, BusIndex):
        """
        Set ActiveBus by an integer value.

        0-based index compatible with SetActiveBus return value and AllBusNames indexing.
        Returns 0 if OK.

        Original COM help: https://opendss.epri.com/SetActiveBusi.html
        """
        return self._check_for_error(self._lib.Circuit_SetActiveBusi(BusIndex))

    def SetActiveClass(self, ClassName):
        """
        Set the active class by name.

        Use FirstElement, NextElement to iterate through the class. Returns -1 if fails.

        Original COM help: https://opendss.epri.com/SetActiveClass.html
        """
        if not isinstance(ClassName, bytes):
            ClassName = ClassName.encode(self._api_util.codec)
        return self._check_for_error(self._lib.Circuit_SetActiveClass(ClassName))

    def SetActiveElement(self, FullName):
        """
        Set the Active Circuit Element using the full object name (e.g. "generator.g1").

        Returns -1 if not found. Else index to be used in CktElements collection or `AllElementNames`.

        Original COM help: https://opendss.epri.com/SetActiveElement.html
        """
        if not isinstance(FullName, bytes):
            FullName = FullName.encode(self._api_util.codec)
        return self._check_for_error(self._lib.Circuit_SetActiveElement(FullName))

    def UpdateStorage(self):
        """
        Force an update to all storage classes.

        Typically done after a solution. Done automatically in intrinsic solution modes.

        Original COM help: https://opendss.epri.com/UpdateStorage.html
        """
        self._check_for_error(self._lib.Circuit_UpdateStorage())

    def AllBusDistances(self):
        """
        Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames.

        Original COM help: https://opendss.epri.com/AllBusDistances.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllBusDistances_GR())
        return self._get_float64_gr_array()

    def AllBusNames(self):
        """
        Array of strings containing names of all buses in circuit (see AllNodeNames).

        Original COM help: https://opendss.epri.com/AllBusNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Circuit_Get_AllBusNames)
        )

    def AllBusVMag(self):
        """
        Array of magnitudes (doubles) of voltages at all buses

        Original COM help: https://opendss.epri.com/AllBusVmag.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllBusVmag_GR())
        return self._get_float64_gr_array()

    def AllBusMagPu(self):
        """
        Double Array of all bus voltages (each node) magnitudes in Per unit

        Original COM help: https://opendss.epri.com/AllBusVmagPu.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllBusVmagPu_GR())
        return self._get_float64_gr_array()

    def AllBusVolts(self):
        """
        Complex array of all bus, node voltages from most recent solution

        Original COM help: https://opendss.epri.com/AllBusVolts.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllBusVolts_GR())
        return self._get_complex128_gr_array()

    def AllElementLosses(self):
        """
        Array of total losses (complex) in each circuit element

        Original COM help: https://opendss.epri.com/AllElementLosses.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllElementLosses_GR())
        return self._get_complex128_gr_array()

    def AllElementNames(self):
        """
        Array of strings containing Full Name of all elements.

        Original COM help: https://opendss.epri.com/AllElementNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Circuit_Get_AllElementNames)
        )

    def AllNodeDistances(self):
        """
        Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence.

        Original COM help: https://opendss.epri.com/AllNodeDistances.html
        """
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistances_GR())
        return self._get_float64_gr_array()

    def AllNodeNames(self):
        """
        Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.

        Original COM help: https://opendss.epri.com/AllNodeNames.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Circuit_Get_AllNodeNames)
        )

    def LineLosses(self):
        """
        Complex total line losses in the circuit

        Original COM help: https://opendss.epri.com/LineLosses.html
        """
        self._check_for_error(self._lib.Circuit_Get_LineLosses_GR())
        return self._get_complex128_gr_simple()

    def Losses(self):
        """
        Total losses in active circuit, complex number (two-element array of double).

        Original COM help: https://opendss.epri.com/Losses.html
        """
        self._check_for_error(self._lib.Circuit_Get_Losses_GR())
        return self._get_complex128_gr_simple()

    def Name(self):
        """Name of the active circuit."""
        return self._get_string(self._check_for_error(self._lib.Circuit_Get_Name()))

    def NumBuses(self):
        """
        Total number of Buses in the circuit.

        Original COM help: https://opendss.epri.com/NumBuses.html
        """
        return self._check_for_error(self._lib.Circuit_Get_NumBuses())

    def NumCktElements(self):
        """
        Number of CktElements in the circuit.

        Original COM help: https://opendss.epri.com/NumCktElements.html
        """
        return self._check_for_error(self._lib.Circuit_Get_NumCktElements())

    def NumNodes(self):
        """
        Total number of nodes in the circuit.

        Original COM help: https://opendss.epri.com/NumNodes1.html
        """
        return self._check_for_error(self._lib.Circuit_Get_NumNodes())

    def ParentPDElement(self):
        """
        Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable.

        Original COM help: https://opendss.epri.com/ParentPDElement.html
        """
        return self._check_for_error(self._lib.Circuit_Get_ParentPDElement())

    def SubstationLosses(self):
        """
        Complex losses in all transformers designated to substations.

        Original COM help: https://opendss.epri.com/SubstationLosses.html
        """
        self._check_for_error(self._lib.Circuit_Get_SubstationLosses_GR())
        return self._get_complex128_gr_simple()

    def SystemY(self):
        """
        (read-only) System Y matrix (after a solution has been performed).
        This is deprecated as it returns a dense matrix. Only use it for small systems.
        For large-scale systems, prefer YMatrix.GetCompressedYMatrix.

        Original COM help: https://opendss.epri.com/SystemY.html
        """
        self._check_for_error(self._lib.Circuit_Get_SystemY_GR())
        return self._get_complex128_gr_array()

    def TotalPower(self):
        """
        Total power (complex), kVA delivered to the circuit

        Original COM help: https://opendss.epri.com/TotalPower.html
        """
        self._check_for_error(self._lib.Circuit_Get_TotalPower_GR())
        return self._get_complex128_gr_simple()

    def YCurrents(self):
        """
        Array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV

        Original COM help: https://opendss.epri.com/YCurrents.html
        """
        self._check_for_error(self._lib.Circuit_Get_YCurrents_GR())
        return self._get_complex128_gr_array()

    def YNodeOrder(self):
        """
        Array of strings containing the names of the nodes in the same order as the Y matrix

        Original COM help: https://opendss.epri.com/YNodeOrder.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Circuit_Get_YNodeOrder)
        )

    def YNodeVArray(self):
        """
        Complex array of actual node voltages in same order as SystemY matrix.

        Original COM help: https://opendss.epri.com/YNodeVarray.html
        """
        self._check_for_error(self._lib.Circuit_Get_YNodeVarray_GR())
        return self._get_complex128_gr_array()

    def ElementLosses(self, Value):
        """
        Array of total losses (complex) in a selection of elements.
        Use the element indices (starting at 1) as parameter.

        **(API Extension)**
        """
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Circuit_Get_ElementLosses_GR(ValuePtr, ValueCount))
        return self._get_complex128_gr_array()

    def ToJSON(self, options=0):
        """
        Returns data for all objects and basic circuit properties as a JSON-encoded string.

        The JSON data is organized using the JSON schema proposed at
        https://github.com/dss-extensions/AltDSS-Schema

        The `options` parameter contains bit-flags to toggle specific features.
        See the enum `DSSJSONFlags` or `Obj_ToJSON` (C-API) for more.

        **(API Extension)**
        """
        return self._get_string(self._check_for_error(self._lib.Circuit_ToJSON(options)))

    def FromJSON(self, data, options=0):
        """
        Replaces the circuit, if any, with the one provided from a JSON-encoded string.
        If a Python dict is provided, `json.dumps(data)` is applied first.

        The expected layout is defined from the JSON schema proposed at
        https://github.com/dss-extensions/AltDSS-Schema

        The `options` parameter contains bit-flags to toggle specific features.
        See the enum `DSSJSONFlags`.

        **(API Extension)**
        """
        if isinstance(data, dict):
            data = json.dumps(data).encode()
        elif not isinstance(data, bytes):
            data = data.encode()
        self._lib.Circuit_FromJSON(data, options)
        self._check_for_error()

    def Save(self, dirOrFilePath, options):
        """
        Equivalent of the "save circuit" DSS command, but allows customization
        through the `saveFlags` argument, which is a set of bit flags.
        See the "DSSSaveFlags" enumeration for available flags:

        - `CalcVoltageBases`: Include the command CalcVoltageBases.
        - `SetVoltageBases`: Include commands to set the voltage bases individually.
        - `IncludeOptions`: Include most of the options (from the Set/Get DSS commands).
        - `IncludeDisabled`: Include disabled circuit elements (and LoadShapes).
        - `ExcludeDefault`: Exclude default DSS items if they are not modified by the user.
        - `SingleFile`: Use a single file instead of a folder for output.
        - `KeepOrder`: Save the circuit elements in the order they were loaded in the active circuit. Guarantees better reproducibility, especially when the system is ill-conditioned. Requires "SingleFile" flag.
        - `ExcludeMeterZones`: Do not export meter zones (as "feeders") separately. Has no effect when using a single file.
        - `IsOpen`: Export commands to open terminals of elements.
        - `ToString`: to the result string. Requires "SingleFile" flag.

        If `SingleFile` is enabled, the first argument (`dirOrFilePath`) is the file path,
        otherwise it is the folder path. For string output, the argument is not used.

        **(API Extension)**
        """
        if not isinstance(dirOrFilePath, bytes):
            dirOrFilePath = dirOrFilePath.encode()
        return self._check_for_error(
            self._get_string(self._lib.Circuit_Save(dirOrFilePath, options))
        )


_Circuit = ICircuit(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
ToJSON = _Circuit.ToJSON
FromJSON = _Circuit.FromJSON
Save = _Circuit.Save
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
    "ToJSON",
    "FromJSON",
    "Save",
]
