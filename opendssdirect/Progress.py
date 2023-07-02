from ._utils import codec, CheckForError, api_util, Base


class IProgress(Base):
    __slots__ = []
    _api_prefix = "DSSProgress"
    _columns = []

    def Close(self):
        self.CheckForError(self._lib.DSSProgress_Close())

    def Show(self):
        self.CheckForError(self._lib.DSSProgress_Show())

    def Caption(self, Value):
        """(write-only) Caption to appear on the bottom of the DSS Progress form."""
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.DSSProgress_Set_Caption(Value))

    def PctProgress(self, Value):
        """(write-only) Percent progress to indicate [0..100]"""
        self.CheckForError(self._lib.DSSProgress_Set_PctProgress(Value))


_Progress = IProgress(api_util)

# For backwards compatibility, bind to the default instance
Close = _Progress.Close
Show = _Progress.Show
Caption = _Progress.Caption
PctProgress = _Progress.PctProgress
_columns = _Progress._columns
__all__ = ["Close", "Show", "Caption", "PctProgress"]
