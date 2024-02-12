import numpy as np
from ._utils import DSSException, api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


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

        Original COM help: https://opendss.epri.com/Channel.html
        """
        num_channels = self._check_for_error(self._lib.Monitors_Get_NumChannels())
        if Index < 1 or Index > num_channels:
            raise DSSException(
                0,
                'Monitors.Channel: Invalid channel index ({}), monitor "{}" has {} channels.'.format(
                    Index, self.Name, num_channels
                ),
            )
        ffi = self._api_util.ffi
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
        ptr, cnt = self._api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return np.zeros((1,), dtype=np.float32)
        ptr = ptr[0]
        record_size = ffi.cast("int32_t*", ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        return data[Index + 1 :: record_size].copy()

    def AsMatrix(self):
        """
        Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1).
        If you need multiple channels, prefer using this function as it processes the monitor byte-stream once.

        **(API Extension)**
        """
        ffi = self._api_util.ffi
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
        ptr, cnt = self._api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return None
        ptr = ptr[0]
        record_size = ffi.cast("int32_t*", ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def Process(self):
        """
        Post-process monitor samples taken so far, e.g., Pst for mode=4.

        Original COM help: https://opendss.epri.com/Process.html
        """
        self._check_for_error(self._lib.Monitors_Process())

    def ProcessAll(self):
        """
        Post-process all monitor samples taken so far, e.g., Pst for mode=4.

        Original COM help: https://opendss.epri.com/ProcessAll.html
        """
        self._check_for_error(self._lib.Monitors_ProcessAll())

    def Reset(self):
        """
        Reset active Monitor object.

        Original COM help: https://opendss.epri.com/Reset3.html
        """
        self._check_for_error(self._lib.Monitors_Reset())

    def ResetAll(self):
        """
        Reset all Monitor objects.

        Original COM help: https://opendss.epri.com/ResetAll1.html
        """
        self._check_for_error(self._lib.Monitors_ResetAll())

    def Sample(self):
        """
        Instruct the active Monitor to take a sample of the present state.

        Original COM help: https://opendss.epri.com/Sample2.html
        """
        self._check_for_error(self._lib.Monitors_Sample())

    def SampleAll(self):
        """
        Instruct all Monitor objects to take a sample of the present state.

        Original COM help: https://opendss.epri.com/SampleAll1.html
        """
        self._check_for_error(self._lib.Monitors_SampleAll())

    def Save(self):
        """
        Instructs the active monitor to save its current sample buffer to its monitor stream.

        After the data is on the stream, you can access the ByteStream or channel data.

        **Most standard solution modes do this automatically.**

        Original COM help: https://opendss.epri.com/Save1.html
        """
        self._check_for_error(self._lib.Monitors_Save())

    def SaveAll(self):
        """
        Instructs the all monitor objects to save their current sample buffers to the respective monitor streams.

        **Most standard solution modes do this automatically.**

        Original COM help: https://opendss.epri.com/SaveAll1.html
        """
        self._check_for_error(self._lib.Monitors_SaveAll())

    def Show(self):
        """
        Convert the monitor data to text and displays it with the text editor.

        Original COM help: https://opendss.epri.com/Show3.html
        """
        self._check_for_error(self._lib.Monitors_Show())

    def ByteStream(self):
        """
        Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)

        Original COM help: https://opendss.epri.com/ByteStream.html
        """
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
        return self._get_int8_gr_array()

    def Element(self, *args):
        """
        Full object name of element being monitored.

        Original COM help: https://opendss.epri.com/Element.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Monitors_Get_Element())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Monitors_Set_Element(Value))

    def FileName(self):
        """
        Name of CSV file associated with active Monitor.

        Original COM help: https://opendss.epri.com/FileName.html
        """
        return self._get_string(self._check_for_error(self._lib.Monitors_Get_FileName()))

    def FileVersion(self):
        """
        Monitor File Version (integer)

        Original COM help: https://opendss.epri.com/FileVersion.html
        """
        return self._check_for_error(self._lib.Monitors_Get_FileVersion())

    def Header(self):
        """
        Header string;  Array of strings containing Channel names

        Original COM help: https://opendss.epri.com/Header.html
        """
        return self._check_for_error(self._get_string_array(self._lib.Monitors_Get_Header))

    def Mode(self, *args):
        """
        Set Monitor mode (bitmask integer - see DSS Help)

        Original COM help: https://opendss.epri.com/Mode1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Monitors_Get_Mode())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Monitors_Set_Mode(Value))

    def NumChannels(self):
        """
        Number of Channels in the active Monitor

        Original COM help: https://opendss.epri.com/NumChannels.html
        """
        return self._check_for_error(self._lib.Monitors_Get_NumChannels())

    def RecordSize(self):
        """
        Size of each record in ByteStream (Integer). Same as NumChannels.

        Original COM help: https://opendss.epri.com/RecordSize.html
        """
        return self._check_for_error(self._lib.Monitors_Get_RecordSize())

    def SampleCount(self):
        """
        Number of Samples in Monitor at Present

        Original COM help: https://opendss.epri.com/SampleCount.html
        """
        return self._check_for_error(self._lib.Monitors_Get_SampleCount())

    def Terminal(self, *args):
        """
        Terminal number of element being monitored.

        Original COM help: https://opendss.epri.com/Terminal.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Monitors_Get_Terminal())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Monitors_Set_Terminal(Value))

    def dblFreq(self):
        """
        Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)

        Original COM help: https://opendss.epri.com/dblFreq.html
        """
        self._check_for_error(self._lib.Monitors_Get_dblFreq_GR())
        return self._get_float64_gr_array()

    def dblHour(self):
        """
        Array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq)

        Original COM help: https://opendss.epri.com/dblHour.html
        """
        self._check_for_error(self._lib.Monitors_Get_dblHour_GR())
        return self._get_float64_gr_array()


_Monitors = IMonitors(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
