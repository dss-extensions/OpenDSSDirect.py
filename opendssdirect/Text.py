from ._utils import  api_util, Base


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


_Text = IText(api_util)

# For backwards compatibility, bind to the default instance
Command = _Text.Command
Result = _Text.Result
_columns = _Text._columns
__all__ = ["Command", "Result"]
