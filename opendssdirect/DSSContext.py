from ._utils import Base, DSSException
from .utils import run_command
from .ActiveClass import _ActiveClass, IActiveClass
from .Basic import _Basic, IBasic
from .Bus import _Bus, IBus
from .CapControls import _CapControls, ICapControls
from .Capacitors import _Capacitors, ICapacitors
from .Circuit import _Circuit, ICircuit
from .CktElement import _CktElement, ICktElement
from .CtrlQueue import _CtrlQueue, ICtrlQueue
from .DSSCore import _DSSCore
from .Element import _Element, IElement
from .Error import _Error, IError
from .Executive import _Executive, IExecutive
from .Fuses import _Fuses, IFuses
from .Generators import _Generators, IGenerators
from .GICSources import _GICSources, IGICSources
from .Isource import _Isource, IIsource
from .LineCodes import _LineCodes, ILineCodes
from .Lines import _Lines, ILines
from .LoadShape import _LoadShape, ILoadShape
from .Loads import _Loads, ILoads
from .Meters import _Meters, IMeters
from .Monitors import _Monitors, IMonitors
from .PDElements import _PDElements, IPDElements
from .PVsystems import _PVsystems, IPVsystems
from .Parallel import _Parallel, IParallel
from .Parser import _Parser, IParser
from .Progress import _Progress, IProgress
from .Properties import _Properties, IProperties
from .Reclosers import _Reclosers, IReclosers
from .RegControls import _RegControls, IRegControls
from .Relays import _Relays, IRelays
from .Sensors import _Sensors, ISensors
from .Settings import _Settings, ISettings
from .Solution import _Solution, ISolution
from .Storages import _Storages, IStorages
from .SwtControls import _SwtControls, ISwtControls
from .Text import _Text, IText
from .Topology import _Topology, ITopology
from .Transformers import _Transformers, ITransformers
from .Vsources import _Vsources, IVsources
from .XYCurves import _XYCurves, IXYCurves
from .YMatrix import _YMatrix, IYMatrix
from .CNData import _CNData, ICNData
from .LineGeometries import _LineGeometries, ILineGeometries
from .LineSpacings import _LineSpacings, ILineSpacings
from .Reactors import _Reactors, IReactors
from .ReduceCkt import _ReduceCkt, IReduceCkt
from .TSData import _TSData, ITSData
from .WireData import _WireData, IWireData
from .ZIP import _ZIP, IZIP

class DSSContext(Base):
    DSSException = DSSException

    __slots__ = [
        "ActiveClass",
        "Basic",
        "Bus",
        "CapControls",
        "Capacitors",
        "Circuit",
        "CktElement",
        "CtrlQueue",
        "DSSCore",
        "Element",
        "Error",
        "Executive",
        "Fuses",
        "Generators",
        "GICSources",
        "Isource",
        "LineCodes",
        "Lines",
        "LoadShape",
        "Loads",
        "Meters",
        "Monitors",
        "PDElements",
        "PVsystems",
        "Parallel",
        "Parser",
        "Progress",
        "Properties",
        "Reclosers",
        "RegControls",
        "Relays",
        "Sensors",
        "Settings",
        "Solution",
        "Storages",
        "SwtControls",
        "Text",
        "Topology",
        "Transformers",
        "Vsources",
        "XYCurves",
        "YMatrix",
        "CNData",
        "LineGeometries",
        "LineSpacings",
        "Reactors",
        "ReduceCkt",
        "TSData",
        "WireData",
        "ZIP",
        "dss_lib",
        "dss_ffi",
        "dss",
    ]

    # `_ptr_to_ctx` is to be used in callbacks (mapping the pointer 
    # to the equivalent Python object)
    _ptr_to_ctx = {}

    def __init__(self, api_util):
        api_util_ = api_util
        if api_util is None:
            api_util = _ActiveClass._api_util
        
        Base.__init__(self, api_util)
        DSSContext._ptr_to_ctx[api_util.ctx] = self
        self.dss_lib = api_util.lib
        self.dss_ffi = api_util.ffi
        self.dss = self

        if api_util_ is None:
            # If api_util is None, grab the default instance, already initialized.
            self.ActiveClass = _ActiveClass
            self.Basic = _Basic
            self.Bus = _Bus
            self.CapControls = _CapControls
            self.Capacitors = _Capacitors
            self.Circuit = _Circuit
            self.CktElement = _CktElement
            self.CtrlQueue = _CtrlQueue
            self.DSSCore = _DSSCore
            self.Element = _Element
            self.Error = _Error
            self.Executive = _Executive
            self.Fuses = _Fuses
            self.Generators = _Generators
            self.GICSources = _GICSources
            self.Isource = _Isource
            self.LineCodes = _LineCodes
            self.Lines = _Lines
            self.LoadShape = _LoadShape
            self.Loads = _Loads
            self.Meters = _Meters
            self.Monitors = _Monitors
            self.PDElements = _PDElements
            self.PVsystems = _PVsystems
            self.Parallel = _Parallel
            self.Parser = _Parser
            self.Progress = _Progress
            self.Properties = _Properties
            self.Reclosers = _Reclosers
            self.RegControls = _RegControls
            self.Relays = _Relays
            self.Sensors = _Sensors
            self.Settings = _Settings
            self.Solution = _Solution
            self.Storages = _Storages
            self.SwtControls = _SwtControls
            self.Text = _Text
            self.Topology = _Topology
            self.Transformers = _Transformers
            self.Vsources = _Vsources
            self.XYCurves = _XYCurves
            self.YMatrix = _YMatrix
            self.CNData = _CNData
            self.LineGeometries = _LineGeometries
            self.LineSpacings = _LineSpacings
            self.Reactors = _Reactors
            self.ReduceCkt = _ReduceCkt
            self.TSData = _TSData
            self.WireData = _WireData
            self.ZIP = _ZIP
            return

        self.ActiveClass = IActiveClass(api_util)
        self.Basic = IBasic(api_util)
        self.Bus = IBus(api_util)
        self.CapControls = ICapControls(api_util)
        self.Capacitors = ICapacitors(api_util)
        self.Circuit = ICircuit(api_util)
        self.CktElement = ICktElement(api_util)
        self.CtrlQueue = ICtrlQueue(api_util)
        self.Element = IElement(api_util)
        self.Error = IError(api_util)
        self.Executive = IExecutive(api_util)
        self.Fuses = IFuses(api_util)
        self.Generators = IGenerators(api_util)
        self.GICSources = IGICSources(api_util)
        self.Isource = IIsource(api_util)
        self.LineCodes = ILineCodes(api_util)
        self.Lines = ILines(api_util)
        self.LoadShape = ILoadShape(api_util)
        self.Loads = ILoads(api_util)
        self.Meters = IMeters(api_util)
        self.Monitors = IMonitors(api_util)
        self.PDElements = IPDElements(api_util)
        self.PVsystems = IPVsystems(api_util)
        self.Parallel = IParallel(api_util)
        self.Parser = IParser(api_util)
        self.Progress = IProgress(api_util)
        self.Properties = IProperties(api_util)
        self.Reclosers = IReclosers(api_util)
        self.RegControls = IRegControls(api_util)
        self.Relays = IRelays(api_util)
        self.Sensors = ISensors(api_util)
        self.Settings = ISettings(api_util)
        self.Solution = ISolution(api_util)
        self.Storages = IStorages(api_util)
        self.SwtControls = ISwtControls(api_util)
        self.Text = IText(api_util)
        self.Topology = ITopology(api_util)
        self.Transformers = ITransformers(api_util)
        self.Vsources = IVsources(api_util)
        self.XYCurves = IXYCurves(api_util)
        self.YMatrix = IYMatrix(api_util)
        self.CNData = ICNData(api_util)
        self.LineGeometries = ILineGeometries(api_util)
        self.LineSpacings = ILineSpacings(api_util)
        self.Reactors = IReactors(api_util)
        self.ReduceCkt = IReduceCkt(api_util)
        self.TSData = ITSData(api_util)
        self.WireData = IWireData(api_util)
        self.ZIP = IZIP(api_util)
        self.DSSCore = self.YMatrix

    def run_command(self, text):
        run_command(text, self)

dss = DSSContext(None)
__all__ = ["DSSContext", "dss"]
