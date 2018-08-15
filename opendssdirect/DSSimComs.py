# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_float64_array


def BusVoltage(Index):
    return get_float64_array(lib.DSSimComs_BusVoltage, Index)


def BusVoltagepu(Index):
    return get_float64_array(lib.DSSimComs_BusVoltagepu, Index)


_columns = []
__all__ = ["BusVoltage", "BusVoltagepu"]
