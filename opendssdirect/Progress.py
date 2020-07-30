# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, codec, CheckForError


def Close():
    CheckForError(lib.DSSProgress_Close())


def Show():
    CheckForError(lib.DSSProgress_Show())


def Caption(Value):
    """(write-only) Caption to appear on the bottom of the DSS Progress form."""
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.DSSProgress_Set_Caption(Value))


def PctProgress(Value):
    """(write-only) Percent progress to indicate [0..100]"""
    CheckForError(lib.DSSProgress_Set_PctProgress(Value))


_columns = []
__all__ = ["Close", "Show", "Caption", "PctProgress"]
