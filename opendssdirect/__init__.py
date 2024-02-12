"""
This package implements the OpenDSSDirect.py API using DSS C-API instead
of the official OpenDSS Direct DLL, sharing the CFFI backend and some other
features (plotting) with DSS-Python and AltDSS.
"""
try:
    # Version is now populated by the build script based
    # on the git tags. See pyproject.toml for more info.
    from ._version import __version__
except:
    __version__ = "0.0dev"

from . import utils
from . import enums
from .OpenDSSDirect import (
    dss,
    run_command,
    ActiveClass,
    Basic,
    Bus,
    CapControls,
    Capacitors,
    Circuit,
    CktElement,
    CtrlQueue,
    DSSCore,
    Element,
    Error,
    Executive,
    Fuses,
    Generators,
    Isource,
    LineCodes,
    Lines,
    LoadShape,
    Loads,
    Meters,
    Monitors,
    PDElements,
    PVsystems,
    Parallel,
    Parser,
    Progress,
    Properties,
    Reclosers,
    RegControls,
    Relays,
    Sensors,
    Settings,
    Solution,
    Storages,
    SwtControls,
    Text,
    Topology,
    Transformers,
    Vsources,
    XYCurves,
    YMatrix,
    ZIP,
    to_dss_python,
    to_altdss,
    NewContext,
    dss_lib,
    DSSException,
)
# Since run_command is deprecated, use these instead
Command = dss.Command
Commands = dss.Commands
