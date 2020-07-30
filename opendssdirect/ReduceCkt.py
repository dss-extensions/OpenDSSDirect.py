# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError, get_string


def Zmag(*args):
    """Zmag (ohms) for Reduce Option for Z of short lines"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ReduceCkt_Get_Zmag())

    # Setter
    Value, = args
    CheckForError(lib.ReduceCkt_Set_Zmag(Value))


def KeepLoad(*args):
    """Keep load flag (T/F) for Reduction options that remove branches"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.ReduceCkt_Get_KeepLoad()) != 0

    # Setter
    Value, = args
    CheckForError(lib.ReduceCkt_Set_KeepLoad(bool(Value)))


def EditString(*args):
    """Edit String for RemoveBranches functions"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.ReduceCkt_Get_EditString()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.ReduceCkt_Set_EditString(Value))


def StartPDElement(*args):
    """Start element for Remove Branch function"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.ReduceCkt_Get_StartPDElement()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.ReduceCkt_Set_StartPDElement(Value))


def EnergyMeter(*args):
    """Name of Energymeter to use for reduction"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.ReduceCkt_Get_EnergyMeter()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.ReduceCkt_Set_EnergyMeter(Value))


def SaveCircuit(CktName):
    """
    Save present (reduced) circuit
    Filename is listed in the Text Result interface
    """
    if type(CktName) is not bytes:
        CktName = CktName.encode(codec)
    CheckForError(lib.ReduceCkt_SaveCircuit(CktName))


def DoDefault():
    """Do Default Reduction algorithm"""
    CheckForError(lib.ReduceCkt_DoDefault())


def DoShortLines():
    """Do ShortLines algorithm: Set Zmag first if you don't want the default"""
    CheckForError(lib.ReduceCkt_DoShortLines())


def DoDangling():
    """Reduce Dangling Algorithm; branches with nothing connected"""
    CheckForError(lib.ReduceCkt_DoDangling())


def DoLoopBreak():
    CheckForError(lib.ReduceCkt_DoLoopBreak())


def DoParallelLines():
    CheckForError(lib.ReduceCkt_DoParallelLines())


def DoSwitches():
    CheckForError(lib.ReduceCkt_DoSwitches())


def Do1phLaterals():
    CheckForError(lib.ReduceCkt_Do1phLaterals())


def DoBranchRemove():
    CheckForError(lib.ReduceCkt_DoBranchRemove())


_columns = []
__all__ = [
    "Zmag",
    "KeepLoad",
    "EditString",
    "StartPDElement",
    "EnergyMeter",
    "SaveCircuit",
    "DoDefault",
    "DoShortLines",
    "DoDangling",
    "DoLoopBreak",
    "DoParallelLines",
    "DoSwitches",
    "Do1phLaterals",
    "DoBranchRemove",
]
