# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, CheckForError, get_string


def Command(i):
    """(read-only) Get i-th command"""
    return get_string(CheckForError(lib.DSS_Executive_Get_Command(i)))


def CommandHelp(i):
    """(read-only) Get help string for i-th command"""
    return get_string(CheckForError(lib.DSS_Executive_Get_CommandHelp(i)))


def Option(i):
    """(read-only) Get i-th option"""
    return get_string(CheckForError(lib.DSS_Executive_Get_Option(i)))


def OptionHelp(i):
    """(read-only) Get help string for i-th option"""
    return get_string(CheckForError(lib.DSS_Executive_Get_OptionHelp(i)))


def OptionValue(i):
    """(read-only) Get present value of i-th option"""
    return get_string(CheckForError(lib.DSS_Executive_Get_OptionValue(i)))


def NumCommands():
    """(read-only) Number of DSS Executive Commands"""
    return CheckForError(lib.DSS_Executive_Get_NumCommands())


def NumOptions():
    """(read-only) Number of DSS Executive Options"""
    return CheckForError(lib.DSS_Executive_Get_NumOptions())


_columns = ["NumCommands", "NumOptions"]
__all__ = [
    "Command",
    "CommandHelp",
    "Option",
    "OptionHelp",
    "OptionValue",
    "NumCommands",
    "NumOptions",
]
