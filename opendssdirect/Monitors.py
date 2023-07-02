import numpy as np
from ._utils import api_util, Iterable

class IMonitors(Iterable):
    __slots__ = []
    __name__ = "Monitors"
    _api_prefix = "Monitors"
    _columns = [
        "Name",
        "FileVersion",
        "NumChannels",
        "RecordSize",
        "dblFreq",
        "Mode",
        "FileName",
        "Element",
        "Header",
        "Terminal",
        "dblHour",
        "SampleCount",
    ]

    def Channel(self, Index):
        """
        (read-only) Array of float32 for the specified channel (usage: MyArray = DSSMonitor.Channel(i)).
        A Save or SaveAll should be executed first. Done automatically by most standard solution modes.
        Channels start at index 1.
        """
        return self.CheckForError(
            self._get_float64_array(self._lib.Monitors_Get_Channel, Index)
        )

    def AsMatrix(self):
        """
        Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1).
        If you need multiple channels, prefer using this function as it processes the monitor byte-stream once.
        """
        buffer = np.asarray(self._get_int8_array(self._lib.Monitors_Get_ByteStream), dtype=np.int8)
        self.CheckForError()
        if len(buffer) <= 1:
            return None
        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def Process(self):
        self._lib.Monitors_Process()

    def ProcessAll(self):
        self._lib.Monitors_ProcessAll()

    def Reset(self):
        self._lib.Monitors_Reset()

    def ResetAll(self):
        self._lib.Monitors_ResetAll()

    def Sample(self):
        self._lib.Monitors_Sample()

    def SampleAll(self):
        self._lib.Monitors_SampleAll()

    def Save(self):
        self._lib.Monitors_Save()

    def SaveAll(self):
        self._lib.Monitors_SaveAll()

    def Show(self):
        self._lib.Monitors_Show()

    def ByteStream(self):
        """(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)"""
        return self._get_int8_array(self._lib.Monitors_Get_ByteStream)

    def Element(self, *args):
        """Full object name of element being monitored."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Monitors_Get_Element())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Monitors_Set_Element(Value)
        self.CheckForError()

    def FileName(self):
        """(read-only) Name of CSV file associated with active Monitor."""
        return self._get_string(self._lib.Monitors_Get_FileName())

    def FileVersion(self):
        """(read-only) Monitor File Version (integer)"""
        return self._lib.Monitors_Get_FileVersion()

    def Header(self):
        """(read-only) Header string;  Array of strings containing Channel names"""
        return self._get_string_array(self._lib.Monitors_Get_Header)

    def Mode(self, *args):
        """Set Monitor mode (bitmask integer - see DSS Help)"""
        # Getter
        if len(args) == 0:
            return self._lib.Monitors_Get_Mode()

        # Setter
        Value, = args
        self._lib.Monitors_Set_Mode(Value)
        self.CheckForError()

    def NumChannels(self):
        """(read-only) Number of Channels in the active Monitor"""
        return self._lib.Monitors_Get_NumChannels()

    def RecordSize(self):
        """(read-only) Size of each record in ByteStream (Integer). Same as NumChannels."""
        return self._lib.Monitors_Get_RecordSize()

    def SampleCount(self):
        """(read-only) Number of Samples in Monitor at Present"""
        return self._lib.Monitors_Get_SampleCount()

    def Terminal(self, *args):
        """Terminal number of element being monitored."""
        # Getter
        if len(args) == 0:
            return self._lib.Monitors_Get_Terminal()

        # Setter
        Value, = args
        self._lib.Monitors_Set_Terminal(Value)
        self.CheckForError()

    def dblFreq(self):
        """(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)"""
        return self._get_float64_array(self._lib.Monitors_Get_dblFreq)

    def dblHour(self):
        """(read-only) Array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq)"""
        return self._get_float64_array(self._lib.Monitors_Get_dblHour)


_Monitors = IMonitors(api_util)

# For backwards compatibility, bind to the default instance
Channel = _Monitors.Channel
Process = _Monitors.Process
ProcessAll = _Monitors.ProcessAll
Reset = _Monitors.Reset
ResetAll = _Monitors.ResetAll
Sample = _Monitors.Sample
SampleAll = _Monitors.SampleAll
Save = _Monitors.Save
SaveAll = _Monitors.SaveAll
Show = _Monitors.Show
AllNames = _Monitors.AllNames
ByteStream = _Monitors.ByteStream
Count = _Monitors.Count
Element = _Monitors.Element
FileName = _Monitors.FileName
FileVersion = _Monitors.FileVersion
First = _Monitors.First
Header = _Monitors.Header
Mode = _Monitors.Mode
Name = _Monitors.Name
Next = _Monitors.Next
NumChannels = _Monitors.NumChannels
RecordSize = _Monitors.RecordSize
SampleCount = _Monitors.SampleCount
Terminal = _Monitors.Terminal
dblFreq = _Monitors.dblFreq
dblHour = _Monitors.dblHour
AsMatrix = _Monitors.AsMatrix
Idx = _Monitors.Idx
_columns = _Monitors._columns
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
    "AsMatrix",
    "Idx",
]
