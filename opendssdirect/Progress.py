from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IProgress(Base):
    __slots__ = []

    __name__ = "Progress"
    _api_prefix = "DSSProgress"
    _columns = []

    def Close(self):
        self._check_for_error(self._lib.DSSProgress_Close())

    def Show(self):
        self._check_for_error(self._lib.DSSProgress_Show())

    def Caption(self, Value):
        """
        (write-only) Caption to appear on the bottom of the DSS Progress form.

        Original COM help: https://opendss.epri.com/Caption.html
        """
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.DSSProgress_Set_Caption(Value))

    def PctProgress(self, Value):
        """
        (write-only) Percent progress to indicate [0..100]

        Original COM help: https://opendss.epri.com/PctProgress.html
        """
        self._check_for_error(self._lib.DSSProgress_Set_PctProgress(Value))


_Progress = IProgress(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Close = _Progress.Close
Show = _Progress.Show
Caption = _Progress.Caption
PctProgress = _Progress.PctProgress
_columns = _Progress._columns
__all__ = ["Close", "Show", "Caption", "PctProgress"]
