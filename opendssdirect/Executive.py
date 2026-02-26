from ._utils import api_util
from .Bases import Base


class IExecutive(Base):
    __slots__ = []

    __name__ = "Executive"
    _api_prefix = "DSS_Executive"
    _columns = ["NumCommands", "NumOptions"]

    def Command(self, i):
        """
        Get i-th command

        Original COM help: https://opendss.epri.com/Command.html
        """
        return self._lib.DSS_Executive_Get_Command(i)

    def CommandHelp(self, i):
        """
        Get help string for i-th command

        Original COM help: https://opendss.epri.com/CommandHelp.html
        """
        return self._lib.DSS_Executive_Get_CommandHelp(i)

    def Option(self, i):
        """
        Get i-th option

        Original COM help: https://opendss.epri.com/Option.html
        """
        return self._lib.DSS_Executive_Get_Option(i)

    def OptionHelp(self, i):
        """
        Get help string for i-th option

        Original COM help: https://opendss.epri.com/OptionHelp.html
        """
        return self._lib.DSS_Executive_Get_OptionHelp(i)

    def OptionValue(self, i):
        """
        Get present value of i-th option

        Original COM help: https://opendss.epri.com/OptionValue.html
        """
        return self._lib.DSS_Executive_Get_OptionValue(i)

    def NumCommands(self):
        """
        Number of DSS Executive Commands

        Original COM help: https://opendss.epri.com/NumCommands.html
        """
        return self._lib.DSS_Executive_Get_NumCommands()

    def NumOptions(self):
        """
        Number of DSS Executive Options

        Original COM help: https://opendss.epri.com/NumOptions.html
        """
        return self._lib.DSS_Executive_Get_NumOptions()


_Executive = IExecutive(api_util)

# For backwards compatibility, bind to the default instance
Command = _Executive.Command
CommandHelp = _Executive.CommandHelp
NumCommands = _Executive.NumCommands
NumOptions = _Executive.NumOptions
Option = _Executive.Option
OptionHelp = _Executive.OptionHelp
OptionValue = _Executive.OptionValue
_columns = _Executive._columns
__all__ = [
    "Command",
    "CommandHelp",
    "NumCommands",
    "NumOptions",
    "Option",
    "OptionHelp",
    "OptionValue",
]
