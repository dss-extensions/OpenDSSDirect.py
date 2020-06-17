# -*- coding: utf-8 -*-
"""
This package tries to implement the OpenDSSDirect.py API using dss_CAPI instead
of the official OpenDSS Direct DLL.
"""
from __future__ import absolute_import
from ._version import __version__
from . import dss, utils
from .dss import (
    run_command,
    ActiveClass,
    Basic,
    Bus,
    CapControls,
    Capacitors,
    Circuit,
    CktElement,
    CmathLib,
    CtrlQueue,
    DSSCore,
    DSSEvents,
    DSSimComs,
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
    Parser,
    Progress,
    Properties,
    Reclosers,
    RegControls,
    Relays,
    Sensors,
    Settings,
    Solution,
    SwtControls,
    Text,
    Topology,
    Transformers,
    Vsources,
    XYCurves,
    YMatrix,
    dss_lib,
    DSSException,
)

dss.dss = dss
