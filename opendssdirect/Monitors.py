# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    get_string,
    get_string_array,
    get_float64_array,
    get_int8_array,
    codec,
)

def Channel(Index):
    """(read-only) Array of doubles for the specified channel  (usage: MyArray = DSSMonitor.Channel(i)) A Save or SaveAll  should be executed first. Done automatically by most standard solution modes."""
    return get_float64_array(lib.Monitors_Get_Channel, Index)


def Process():
    lib.Monitors_Process()


def ProcessAll():
    lib.Monitors_ProcessAll()


def Reset():
    lib.Monitors_Reset()


def ResetAll():
    lib.Monitors_ResetAll()


def Sample():
    lib.Monitors_Sample()


def SampleAll():
    lib.Monitors_SampleAll()


def Save():
    lib.Monitors_Save()


def SaveAll():
    lib.Monitors_SaveAll()


def Show():
    lib.Monitors_Show()


def AllNames():
    """(read-only) Array of all Monitor Names"""
    return get_string_array(lib.Monitors_Get_AllNames)


def ByteStream():
    """(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)"""
    result = get_int8_array(lib.Monitors_Get_ByteStream)
    if result == [0]:
        return []

    return result


def Count():
    """(read-only) Number of Monitors"""
    return lib.Monitors_Get_Count()


def Element(*args):
    """Full object name of element being monitored."""
    # Getter
    if len(args) == 0:
        result = get_string(lib.Monitors_Get_Element())
        if result == "":
            return "0"

        return result

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Monitors_Set_Element(Value)


def FileName():
    """(read-only) Name of CSV file associated with active Monitor."""
    return get_string(lib.Monitors_Get_FileName())


def FileVersion():
    """(read-only) Monitor File Version (integer)"""
    return lib.Monitors_Get_FileVersion()


def First():
    """(read-only) Sets the first Monitor active.  Returns 0 if no monitors."""
    return lib.Monitors_Get_First()


def Header():
    """(read-only) Header string;  Array of strings containing Channel names"""
    return get_string_array(lib.Monitors_Get_Header)


def Mode(*args):
    """Set Monitor mode (bitmask integer - see DSS Help)"""
    # Getter
    if len(args) == 0:
        return lib.Monitors_Get_Mode()

    # Setter
    Value, = args
    lib.Monitors_Set_Mode(Value)


def Name(*args):
    """Sets the active Monitor object by name"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Monitors_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.Monitors_Set_Name(Value)


def Next():
    """(read-only) Sets next monitor active.  Returns 0 if no more."""
    return lib.Monitors_Get_Next()


def NumChannels():
    """(read-only) Number of Channels in the active Monitor"""
    return lib.Monitors_Get_NumChannels()


def RecordSize():
    """(read-only) Size of each record in ByteStream (Integer). Same as NumChannels."""
    return lib.Monitors_Get_RecordSize()


def SampleCount():
    """(read-only) Number of Samples in Monitor at Present"""
    return lib.Monitors_Get_SampleCount()


def Terminal(*args):
    """Terminal number of element being monitored."""
    # Getter
    if len(args) == 0:
        return lib.Monitors_Get_Terminal()

    # Setter
    Value, = args
    lib.Monitors_Set_Terminal(Value)


def dblFreq():
    """(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)"""
    return get_float64_array(lib.Monitors_Get_dblFreq)


def dblHour():
    """(read-only) Array of doubles containgin time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution  (see dblFreq)"""
    return get_float64_array(lib.Monitors_Get_dblHour)


_columns = [
    "Element",
    "FileName",
    "FileVersion",
    "Header",
    "Mode",
    "Name",
    "NumChannels",
    "RecordSize",
    "SampleCount",
    "Terminal",
    "dblFreq",
    "dblHour",
]
__all__ = [
    "Channel",
    "Process",
    "ProcessAll",
    "Reset",
    "ResetAll",
    "Sample",
    "SampleAll",
    "Save",
    "SaveAll",
    "Show",
    "AllNames",
    "ByteStream",
    "Count",
    "Element",
    "FileName",
    "FileVersion",
    "First",
    "Header",
    "Mode",
    "Name",
    "Next",
    "NumChannels",
    "RecordSize",
    "SampleCount",
    "Terminal",
    "dblFreq",
    "dblHour",
]
