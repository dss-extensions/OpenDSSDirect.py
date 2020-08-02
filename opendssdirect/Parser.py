# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string, get_float64_array


def Matrix(ExpectedOrder):
    """(read-only) Use this property to parse a Matrix token in OpenDSS format.  Returns square matrix of order specified. Order same as default Fortran order: column by column."""
    return CheckForError(get_float64_array(lib.Parser_Get_Matrix, ExpectedOrder))


def SymMatrix(ExpectedOrder):
    """(read-only) Use this property to parse a matrix token specified in lower triangle form. Symmetry is forced."""
    return CheckForError(get_float64_array(lib.Parser_Get_SymMatrix, ExpectedOrder))


def Vector(ExpectedSize):
    """(read-only) Returns token as array of doubles. For parsing quoted array syntax."""
    return CheckForError(get_float64_array(lib.Parser_Get_Vector, ExpectedSize))


def ResetDelimiters():
    CheckForError(lib.Parser_ResetDelimiters())


def AutoIncrement(*args):
    """Default is FALSE. If TRUE parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Parser_Get_AutoIncrement()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Parser_Set_AutoIncrement(Value))


def BeginQuote(*args):
    """
    Get/Set String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Parser_Get_BeginQuote()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Parser_Set_BeginQuote(Value))


def CmdString(*args):
    """String to be parsed. Loading this string resets the Parser to the beginning of the line. Then parse off the tokens in sequence."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Parser_Get_CmdString()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Parser_Set_CmdString(Value))


def DblValue():
    """(read-only) Return next parameter as a double."""
    return CheckForError(lib.Parser_Get_DblValue())


def Delimiters(*args):
    """String defining hard delimiters used to separate token on the command string. Default is , and =. The = separates token name from token value. These override whitesspace to separate tokens."""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Parser_Get_Delimiters()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Parser_Set_Delimiters(Value))


def EndQuote(*args):
    """String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')]}"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Parser_Get_EndQuote()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Parser_Set_EndQuote(Value))


def IntValue():
    """(read-only) Return next parameter as a long integer."""
    return CheckForError(lib.Parser_Get_IntValue())


def NextParam():
    """(read-only) Get next token and return tag name (before = sign) if any. See AutoIncrement."""
    return get_string(CheckForError(lib.Parser_Get_NextParam()))


def StrValue():
    """(read-only) Return next parameter as a string"""
    return get_string(CheckForError(lib.Parser_Get_StrValue()))


def WhiteSpace(*args):
    """
    (read) Get the characters used for White space in the command string.  Default is blank and Tab.
    (write) Set the characters used for White space in the command string.  Default is blank and Tab.
    """
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Parser_Get_WhiteSpace()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Parser_Set_WhiteSpace(Value))


_columns = [
    "AutoIncrement",
    "BeginQuote",
    "CmdString",
    "Delimiters",
    "EndQuote",
    "WhiteSpace",
]
__all__ = [
    "Matrix",
    "SymMatrix",
    "Vector",
    "ResetDelimiters",
    "AutoIncrement",
    "BeginQuote",
    "CmdString",
    "DblValue",
    "Delimiters",
    "EndQuote",
    "IntValue",
    "NextParam",
    "StrValue",
    "WhiteSpace",
]
