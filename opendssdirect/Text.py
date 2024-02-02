from ._utils import api_util, Base, OPENDSSDIRECT_PY_USE_NUMPY


class IText(Base):
    __slots__ = []
    __name__ = "Text"
    _api_prefix = "Text"
    _columns = []

    def Command(self, *args):
        """Input command string for the DSS."""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Text_Get_Command()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Text_Set_Command(Value))

    def Result(self):
        """(read-only) Result string for the last command."""
        return self._get_string(self.CheckForError(self._lib.Text_Get_Result()))

    def Commands(self, Value):
        """
        Runs a list of strings or a large string as commands directly in the DSS engine.
        Intermediate results (from Text.Result) are ignored.

        Value can be a list of strings, or a single large string (usually faster).

        (API Extension)
        """
        if isinstance(Value, str) or isinstance(Value, bytes):
            if type(Value) is not bytes:
                Value = Value.encode(self._api_util.codec)
            self.CheckForError(self._lib.Text_CommandBlock(Value))
        else:
            self.CheckForError(
                self._set_string_array(self._lib.Text_CommandArray, Value)
            )


_Text = IText(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Command = _Text.Command
Result = _Text.Result
Commands = _Text.Commands
_columns = _Text._columns
__all__ = ["Command", "Result", "Commands"]
