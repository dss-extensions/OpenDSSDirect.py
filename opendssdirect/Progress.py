from ._utils import api_util
from .Bases import Base


class IProgress(Base):
    __slots__ = []

    __name__ = "Progress"
    _api_prefix = "DSSProgress"
    _columns = []

    def Close(self):
        """
        Close progress form

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.
        """
        self._lib.DSSProgress_Close()

    def Show(self):
        """
        Show progress form

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.
        """
        self._lib.DSSProgress_Show()

    def Caption(self, Value):
        """
        Set the caption to appear on the bottom of the DSS Progress form.

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.

        Original COM help: https://opendss.epri.com/Caption.html
        """
        self._lib.DSSProgress_Set_Caption(Value)

    def PctProgress(self, Value):
        """
        Set the percent progress to indicate [0..100] on the progress form.

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.

        Original COM help: https://opendss.epri.com/PctProgress.html
        """
        self._lib.DSSProgress_Set_PctProgress(Value)


_Progress = IProgress(api_util)

# For backwards compatibility, bind to the default instance
Caption = _Progress.Caption
Close = _Progress.Close
PctProgress = _Progress.PctProgress
Show = _Progress.Show
_columns = _Progress._columns
__all__ = ["Caption", "Close", "PctProgress", "Show"]
