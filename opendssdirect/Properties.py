# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string


def Description():
    """(read-only) Description of the property."""
    return get_string(lib.DSSProperty_Get_Description())


def Name():
    """(read-only) Name of Property"""
    return get_string(lib.DSSProperty_Get_Name())


def _setCurrentProperty(argIndex_or_Name):
    """
    Sets the current DSS property based on a 1-based integer (or integer as
    a string) as an property index, or a string as a property name.
    """
    try:
        if not isinstance(argIndex_or_Name, int):
            argIndex_or_Name = int(argIndex_or_Name)

        # use 1-based index here for compatibility
        lib.DSSProperty_Set_Index(argIndex_or_Name - 1)

    except ValueError:
        # if we cannot convert to integer, use string as name instead
        if type(argIndex_or_Name) is not bytes:
            argIndex_or_Name = argIndex_or_Name.encode(codec)

        lib.DSSProperty_Set_Name(argIndex_or_Name)


def Value(*args):
    if len(args) == 0:
        # General getter
        return get_string(lib.DSSProperty_Get_Val())
    elif len(args) == 1:
        # Getter by index as str or integer
        argIndex_or_Name, = args

        _setCurrentProperty(argIndex_or_Name)
        return get_string(lib.DSSProperty_Get_Val())

    # Setter by index as strs
    argIndex_or_Name, Value = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    _setCurrentProperty(argIndex_or_Name)
    lib.DSSProperty_Set_Val(Value)
    CheckForError()


_columns = ["Description", "Name", "Value"]
__all__ = ["Description", "Name", "Value"]
