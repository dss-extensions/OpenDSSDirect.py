from ._utils import CheckForError, api_util, Base


class IExecutive(Base):
    __slots__ = []
    _api_prefix = "DSS_Executive"
    _columns = ["NumCommands", "NumOptions"]

    def Command(self, i):
        """(read-only) Get i-th command"""
        return self._get_string(
            self.CheckForError(self._lib.DSS_Executive_Get_Command(i))
        )

    def CommandHelp(self, i):
        """(read-only) Get help string for i-th command"""
        return self._get_string(
            self.CheckForError(self._lib.DSS_Executive_Get_CommandHelp(i))
        )

    def Option(self, i):
        """(read-only) Get i-th option"""
        return self._get_string(
            self.CheckForError(self._lib.DSS_Executive_Get_Option(i))
        )

    def OptionHelp(self, i):
        """(read-only) Get help string for i-th option"""
        return self._get_string(
            self.CheckForError(self._lib.DSS_Executive_Get_OptionHelp(i))
        )

    def OptionValue(self, i):
        """(read-only) Get present value of i-th option"""
        return self._get_string(
            self.CheckForError(self._lib.DSS_Executive_Get_OptionValue(i))
        )

    def NumCommands(self):
        """(read-only) Number of DSS Executive Commands"""
        return self.CheckForError(self._lib.DSS_Executive_Get_NumCommands())

    def NumOptions(self):
        """(read-only) Number of DSS Executive Options"""
        return self.CheckForError(self._lib.DSS_Executive_Get_NumOptions())


_Executive = IExecutive(api_util)

# For backwards compatibility, bind to the default instance
Command = _Executive.Command
CommandHelp = _Executive.CommandHelp
Option = _Executive.Option
OptionHelp = _Executive.OptionHelp
OptionValue = _Executive.OptionValue
NumCommands = _Executive.NumCommands
NumOptions = _Executive.NumOptions
_columns = _Executive._columns
__all__ = [
    "Command",
    "CommandHelp",
    "Option",
    "OptionHelp",
    "OptionValue",
    "NumCommands",
    "NumOptions",
]
