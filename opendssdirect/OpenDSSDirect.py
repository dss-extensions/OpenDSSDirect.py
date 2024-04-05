from __future__ import annotations
import warnings
from typing import TYPE_CHECKING
from weakref import WeakKeyDictionary
from typing import AnyStr, List, Union
from ._utils import DSSException, dss_py, OPENDSSDIRECT_PY_USE_NUMPY
from ._utils import lib as dss_lib
from ._utils import ffi as dss_ffi
from .Bases import Base
from . import utils as _utils
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
from .WindGens import _WindGens, IWindGens
from .WireData import _WireData, IWireData
from .ZIP import _ZIP, IZIP

if TYPE_CHECKING:
    # DSS-Python is always required at the moment
    from dss import IDSS as DSSPython

    # AltDSS is optional
    try:
        from altdss import AltDSS
    except:
        pass


class OpenDSSDirect(Base):
    """
    This is the main OpenDSSDirect.py class that wraps all the available interfaces.
    
    Besides the traditional submodules from previous (pre-v0.9) versions, it has a
    shortcut for commands as the call operator, plus some utility methods.
        
    Note that users do not typically need to create instances of this class manually.
    For creating multiple, separate DSS engine instances, use the [`NewContext()`](OpenDSSDirect.NewContext)
    method.
    For Oddie-wrapped libraries (EPRI's OpenDSS and OpenDSS-C), prefer the dedicated constructors and classes
    (e.g. `IOddieDSS`, `EPRIOpenDSSC`, `EPRIOpenDSS`).

    This class also provides function to return DSS-Python and AltDSS representations
    of the same engine, allowing users to mix usage of the packages more easily.
    """
        
    try:
        # Version is now populated by the build script based
        # on the git tags. See pyproject.toml for more info.
        from ._version import __version__
    except:
        __version__ = "0.0dev"

    DSSException = DSSException
    """Shortcut to the `DSSException` class."""

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
        "WindGens",
        "WireData",
        "ZIP",
        "dss_lib",
        "dss_ffi",
        "dss",
        "Command",
        "Commands",
        "Version",
    ]

    utils = _utils
    """Shortcut to the [`utils`](opendssdirect.utils) module."""

    # `_ctx_to_dss` is to be used in callbacks (mapping the pointer 
    # to the equivalent Python object)
    _ctx_to_dss = WeakKeyDictionary()

    @classmethod
    def _get_instance(cls: OpenDSSDirect, api_util: dss_py.AltDSSAPIUtil = None, ctx=None) -> OpenDSSDirect:
        """
        If there is an existing OpenDSSDirect instance for a context, return it.
        Otherwise, try to wrap the context into a new OpenDSSDirect.py API instance.
        """
        if api_util is None:
            # If none exists, something is probably wrong elsewhere,
            # so let's allow the IndexError to propagate
            api_util = dss_py.AltDSSAPIUtil._ctx_to_util[ctx]

        dss = cls._ctx_to_dss.get(api_util.ctx)
        if dss is None:
            dss = cls(api_util)

        return dss

    def __init__(self, ctx_api_util=None, prefer_lists=None):
        """
        Creates a new OpenDSSDirect.py instance for the DSS context specified in `ctx_api_util`.

        Not intended for typical usage. For creating new separate DSS instances, refer
        to the [`NewContext()`](OpenDSSDirect.NewContext) method.
        """
        
        if ctx_api_util is None:
            # If ctx_api_util is None, grab the default instance, already initialized.
            ctx_api_util = _ActiveClass._api_util

        if ctx_api_util._opendssdirect is None:
            ctx_api_util._opendssdirect = self

        Base.__init__(self, ctx_api_util)
        if prefer_lists is None:
            self._lib.prefer_lists = not OPENDSSDIRECT_PY_USE_NUMPY
        else:
            if self._lib.prefer_lists != prefer_lists:
                warnings.warn('"prefer_lists" is deprecated. Use instead the method `Settings.PreferLists` to toggle the behavior on an existing OpenDSSDirect instance. Current behavior: the value passed in "prefer_lists" will update the value on the new instance and potentially affect existing instances.', DeprecationWarning, stacklevel=2)

            self._lib.prefer_lists = prefer_lists

        OpenDSSDirect._ctx_to_dss[ctx_api_util.ctx] = self
        object.__setattr__(self, '_frozen_attrs', False)
        
        self.dss_lib = ctx_api_util.lib_unpatched
        """
        `dss_lib` provides access to the low-level CFFI library; this is not recommended for most users and may 
        change across versions. The intention is to allow some (very) advanced operations directly, when the
        high-level interface either does not model some specific detail, or when users know how to manually
        address some data directly with lower overhead.

        Note that the prepared alternative, which already abstracts away some details, is available in the 
        `_lib` attribute. That one is private and could change when required to introduce new features. See
        the source code for OpenDSSDirect.py or DSS-Python for examples of how it is used.

        **WARNING**: if used incorrectly, could even crash your computer.
        """


        self.dss_ffi = ctx_api_util.ffi
        self.dss = self

        # Check if we're creating the default instance, with the same options
        grab_default = (ctx_api_util is _ActiveClass._api_util)

        if grab_default:
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
            self.WindGens = _WindGens
            self.WireData = _WireData
            self.ZIP = _ZIP

            # Shortcuts
            self.Command = self.Text.Command
            self.Commands = self.Text.Commands
            self.Version = self.Basic.Version

            object.__setattr__(self, '_frozen_attrs', True)
            return
        
        not_using_oddie = not ctx_api_util._is_oddie

        self.ActiveClass = IActiveClass(ctx_api_util)
        self.Basic = IBasic(ctx_api_util)
        self.Bus = IBus(ctx_api_util)
        self.CapControls = ICapControls(ctx_api_util)
        self.Capacitors = ICapacitors(ctx_api_util)
        self.Circuit = ICircuit(ctx_api_util)
        self.CktElement = ICktElement(ctx_api_util)
        self.CtrlQueue = ICtrlQueue(ctx_api_util)
        self.Element = IElement(ctx_api_util)
        self.Error = IError(ctx_api_util)
        self.Executive = IExecutive(ctx_api_util)
        self.Fuses = IFuses(ctx_api_util)
        self.Generators = IGenerators(ctx_api_util)
        self.GICSources = IGICSources(ctx_api_util)
        self.Isource = IIsource(ctx_api_util)
        self.LineCodes = ILineCodes(ctx_api_util)
        self.Lines = ILines(ctx_api_util)
        self.LoadShape = ILoadShape(ctx_api_util)
        self.Loads = ILoads(ctx_api_util)
        self.Meters = IMeters(ctx_api_util)
        self.Monitors = IMonitors(ctx_api_util)
        self.PDElements = IPDElements(ctx_api_util)
        self.PVsystems = IPVsystems(ctx_api_util)
        self.Parallel = IParallel(ctx_api_util)
        self.Parser = IParser(ctx_api_util)
        self.Progress = IProgress(ctx_api_util)
        self.Properties = IProperties(ctx_api_util)
        self.Reclosers = IReclosers(ctx_api_util)
        self.RegControls = IRegControls(ctx_api_util)
        self.Relays = IRelays(ctx_api_util)
        self.Sensors = ISensors(ctx_api_util)
        self.Settings = ISettings(ctx_api_util)
        self.Solution = ISolution(ctx_api_util)
        self.Storages = IStorages(ctx_api_util)
        self.SwtControls = ISwtControls(ctx_api_util)
        self.Text = IText(ctx_api_util)
        self.Topology = ITopology(ctx_api_util)
        self.Transformers = ITransformers(ctx_api_util)
        self.Vsources = IVsources(ctx_api_util)
        self.XYCurves = IXYCurves(ctx_api_util)
        self.YMatrix = IYMatrix(ctx_api_util)
        self.CNData = ICNData(ctx_api_util) if not_using_oddie else None
        self.LineGeometries = ILineGeometries(ctx_api_util) if not_using_oddie else None
        self.LineSpacings = ILineSpacings(ctx_api_util) if not_using_oddie else None
        self.Reactors = IReactors(ctx_api_util)
        self.ReduceCkt = IReduceCkt(ctx_api_util)
        self.TSData = ITSData(ctx_api_util) if not_using_oddie else None
        self.WindGens = IWindGens(ctx_api_util)
        self.WireData = IWireData(ctx_api_util) if not_using_oddie else None
        self.ZIP = IZIP(ctx_api_util)
        self.DSSCore = self.YMatrix

        # Shortcuts
        self.Command = self.Text.Command
        self.Commands = self.Text.Commands
        self.Version = self.Basic.Version

        object.__setattr__(self, '_frozen_attrs', True)


    def run_command(self, text):
        """
        Use the Text interface of OpenDSS, grabbing all output text in a string.
        
        This is **deprecated** since it doesn't handle errors as exceptions and can confuse users.

        Use instead: [`dss("commands")`](#opendssdirect.OpenDSSDirect.OpenDSSDirect.__call__), [`dss.Text.Command("command")`](#opendssdirect.Text.IText.Command), or [`dss.Text.Commands("commands")`](#opendssdirect.Text.IText.Commands).
        """
        run_command(text, self)


    def NewContext(self):
        """
        Creates a new DSS engine context, wrapped by the OpenDSSDirect.py classes.

        A DSS Context encapsulates most of the global state of the original OpenDSS engine,
        allowing the user to create multiple instances in the same process. By creating contexts
        manually, the management of threads and potential issues should be handled by the user.

        **(API Extension)**
        """
        from .OpenDSSDirect import OpenDSSDirect
        ffi = self._api_util.ffi
        lib = self._api_util.lib_unpatched
        new_ctx = ffi.gc(lib.ctx_New(), lib.ctx_Dispose)
        new_api_util = dss_py.AltDSSAPIUtil(ffi, lib, new_ctx, parent=self._api_util)
        return OpenDSSDirect(new_api_util, prefer_lists=self._lib.prefer_lists)

    def to_dss_python(self) -> DSSPython:
        """
        Returns an instance of DSS-Python for the active DSS Context.
        """
        from dss import IDSS as DSSPython
        return DSSPython._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)

    def to_altdss(self) -> AltDSS:
        """
        Returns an instance of AltDSS for the active DSS Context.

        A compatible AltDSS (`pip install altdss`) is required.
        """
        from altdss import AltDSS
        return AltDSS._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)

    def is_oddie(self) -> bool:
        """
        Returns True if this instance is based on the Oddie compatibility layer for
        the official OpenDSS Direct API (a.k.a. DCSL).
        
        Note that the default engine in OpenDSSDirect.py has been based on AltDSS since
        2018, even though it was not called AltDSS then.
        """
        return self._api_util._is_oddie

    def __call__(self, cmds: Union[AnyStr, List[AnyStr]] = None):
        '''
        Shortcut to pass text commands. Allow single and multiple commands in a string, or a list of commands.

        For multiple commands, a big string tends to be the faster.

        Equivalent to `OpenDSSDirect.Text.Commands`

        Examples:

        ```python

            # single command
            dss("new Circuit.test") 

            # list of commands (either will work)
            dss(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            dss("""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)
        ```

        **(API Extension)**
        '''
        # self.Commands(cmds) -- inlined
        if isinstance(cmds, (str, bytes)):
            self._lib.Text_CommandBlock(cmds)
        else:
            self._lib.Text_CommandArray(cmds)



dss = OpenDSSDirect(None)
ActiveClass = _ActiveClass
Basic = _Basic
Bus = _Bus
CapControls = _CapControls
Capacitors = _Capacitors
Circuit = _Circuit
CktElement = _CktElement
CtrlQueue = _CtrlQueue
DSSCore = _DSSCore
Element = _Element
Error = _Error
Executive = _Executive
Fuses = _Fuses
Generators = _Generators
GICSources = _GICSources
Isource = _Isource
LineCodes = _LineCodes
Lines = _Lines
LoadShape = _LoadShape
Loads = _Loads
Meters = _Meters
Monitors = _Monitors
PDElements = _PDElements
PVsystems = _PVsystems
Parallel = _Parallel
Parser = _Parser
Progress = _Progress
Properties = _Properties
Reclosers = _Reclosers
RegControls = _RegControls
Relays = _Relays
Sensors = _Sensors
Settings = _Settings
Solution = _Solution
Storages = _Storages
SwtControls = _SwtControls
Text = _Text
Topology = _Topology
Transformers = _Transformers
Vsources = _Vsources
XYCurves = _XYCurves
YMatrix = _YMatrix
CNData = _CNData
LineGeometries = _LineGeometries
LineSpacings = _LineSpacings
Reactors = _Reactors
ReduceCkt = _ReduceCkt
TSData = _TSData
WindGens = _WindGens
WireData = _WireData
ZIP = _ZIP
to_dss_python = dss.to_dss_python
to_altdss = dss.to_altdss
NewContext = dss.NewContext
is_oddie = dss.is_oddie

__all__ = ["OpenDSSDirect", "dss", "OPENDSSDIRECT_PY_USE_NUMPY"]
