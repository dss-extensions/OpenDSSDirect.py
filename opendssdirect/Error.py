from ._utils import api_util
from .Bases import Base


class IError(Base):
    __slots__ = []

    __name__ = "Error"
    _api_prefix = "Error"
    _columns = ["Description", "Number", "EarlyAbort"]

    def Description(self):
        """
        Description of error for last operation

        Original COM help: https://opendss.epri.com/Description1.html
        """
        return self._lib.Error_Get_Description()

    def Number(self):
        """
        Error Number (returns current value and then resets to zero)

        Original COM help: https://opendss.epri.com/Number.html
        """
        return self._lib.Error_Get_Number()

    def EarlyAbort(self, *args):
        """
        EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Error_Get_EarlyAbort()

        # Setter
        (Value,) = args
        self._lib.Error_Set_EarlyAbort(Value)

    def ExtendedErrors(self, *args):
        """
        Controls whether the extended error mechanism is used. Defaults to True.

        Extended errors are errors derived from checks across the API to ensure
        a valid state. Although many of these checks are already present in the
        original/EPRI's COM interface, the checks do not produce any error
        message. An error value can be returned by a function but this value
        can, for many of the functions, be a valid value. As such, the user
        has no means to detect an invalid API call.

        Extended errors use the Error interface to provide a more clear message
        and should help users, especially new users, to find usage issues earlier.

        At Python level, an exception is raised when an error is detected through
        the Error interface.

        The current default state is ON. For compatibility, the user can turn it
        off to restore the previous behavior.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.Error_Get_ExtendedErrors()

        # Setter
        (Value,) = args
        self._lib.Error_Set_ExtendedErrors(Value)

    def UseExceptions(self, *args):
        """
        Controls whether the automatic error checking mechanism is enable, i.e., if
        the DSS engine errors (from the `Error` interface) are mapped exception when
        detected.

        **When disabled, the user takes responsibility for checking for errors.**
        This can be done through the `Error` interface. When `Error.Number` is not
        zero, there should be an error message in `Error.Description`. This is compatible
        with the behavior on EPRI's OpenDSS (Windows-only COM implementation) when
        `AllowForms` is disabled.

        Users can also use the DSS command `Export ErrorLog` to inspect for errors.

        With EPRI's OpenDSS engines, in contrast to our main AltDSS engine, users are
        also required to set `AllowForms` to `False`, otherwise the engine does not
        populate the Error.Number API and the error is consumed by the popup form or
        terminal message.

        **NOTE:** this used to be a global settings. Since OpenDSSDirect.py v0.10.0,
        it only affects the target instance.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.using_exceptions

        # Setter
        (value,) = args
        self._lib.using_exceptions = value


_Error = IError(api_util)

# For backwards compatibility, bind to the default instance
Description = _Error.Description
EarlyAbort = _Error.EarlyAbort
ExtendedErrors = _Error.ExtendedErrors
Number = _Error.Number
UseExceptions = _Error.UseExceptions
_columns = _Error._columns
__all__ = ["Description", "EarlyAbort", "ExtendedErrors", "Number", "UseExceptions"]
