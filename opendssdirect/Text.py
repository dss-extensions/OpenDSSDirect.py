from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IText(Base):
    __slots__ = []

    __name__ = "Text"
    _api_prefix = "Text"
    _columns = []

    def Command(self, *args):
        """
        Input command string for the DSS.

        Original COM help: https://opendss.epri.com/Command1.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.Text_Get_Command()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Text_Set_Command(Value))

    def Result(self):
        """
        Result string for the last command.

        Original COM help: https://opendss.epri.com/Result.html
        """
        return self._get_string(self._check_for_error(self._lib.Text_Get_Result()))

    def Commands(self, Value):
        """
        Runs a list of strings or a large string as commands directly in the DSS engine.
        Intermediate results (from Text.Result) are ignored.

        Value can be a list of strings, or a single large string (usually faster).

        **(API Extension)**
        """
        if isinstance(Value, str) or isinstance(Value, bytes):
            if not isinstance(Value, bytes):
                Value = Value.encode(self._api_util.codec)
            self._check_for_error(self._lib.Text_CommandBlock(Value))
        else:
            self._check_for_error(
                self._set_string_array(self._lib.Text_CommandArray, Value)
            )


_Text = IText(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Command = _Text.Command
Result = _Text.Result
Commands = _Text.Commands
_columns = _Text._columns
__all__ = ["Command", "Result", "Commands"]
