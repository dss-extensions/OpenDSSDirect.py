# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, CheckForError, get_float64_array


def BusVoltage(Index):
    return CheckForError(get_float64_array(lib.DSSimComs_BusVoltage, Index))


def BusVoltagepu(Index):
    return CheckForError(get_float64_array(lib.DSSimComs_BusVoltagepu, Index))


_columns = []
__all__ = ["BusVoltage", "BusVoltagepu"]
