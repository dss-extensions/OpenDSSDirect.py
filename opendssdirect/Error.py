# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string


def Description():
    """(read-only) Description of error for last operation"""
    return get_string(lib.Error_Get_Description())


def Number():
    """(read-only) Error Number"""
    return lib.Error_Get_Number()


_columns = ["Description", "Number"]
__all__ = ["Description", "Number"]
