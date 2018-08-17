# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, CheckForError
from ._utils import codec


def Command(*args):
    """Input command string for the DSS."""
    # Getter
    if len(args) == 0:
        return get_string(lib.Text_Get_Command())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Text_Set_Command(Value)
    CheckForError()


def Result():
    """(read-only) Result string for the last command."""
    return get_string(lib.Text_Get_Result())


_columns = ["Command", "Result"]
__all__ = ["Command", "Result"]
