# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string


def Description():
    """(read-only) Description of error for last operation"""
    return get_string(lib.Error_Get_Description())


def Number():
    """(read-only) Error Number (returns current value and then resets to zero)"""
    return lib.Error_Get_Number()


def EarlyAbort(*args):
    """
    EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.
    """
    # Getter
    if len(args) == 0:
        return lib.Error_Get_EarlyAbort() != 0

    # Setter
    Value, = args
    lib.Error_Set_EarlyAbort(Value)


_columns = ["Description", "Number", "EarlyAbort"]
__all__ = ["Description", "Number", "EarlyAbort"]
