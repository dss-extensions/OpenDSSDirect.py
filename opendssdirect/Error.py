from ._utils import lib, get_string, Base


def Description():
    """(read-only) Description of error for last operation"""
    return get_string(lib.Error_Get_Description())


def Number():
    """(read-only) Error Number (returns current value and then resets to zero)"""
    return lib.Error_Get_Number()


def EarlyAbort(*args):
    """
    EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return lib.Error_Get_EarlyAbort() != 0

    # Setter
    Value, = args
    lib.Error_Set_EarlyAbort(Value)


def ExtendedErrors(*args):
    """
    Controls whether the extended error mechanism is used. Defaults to True.

    Extended errors are errors derived from checks across the API to ensure
    a valid state. Although many of these checks are already present in the 
    original/official COM interface, the checks do not produce any error 
    message. An error value can be returned by a function but this value
    can, for many of the functions, be a valid value. As such, the user
    has no means to detect an invalid API call. 

    Extended errors use the Error interface to provide a more clear message
    and should help users, especially new users, to find usage issues earlier.

    At Python level, an exception is raised when an error is detected through
    the Error interface.

    The current default state is ON. For compatibility, the user can turn it
    off to restore the previous behavior.

    (API Extension)

    """
    # Getter
    if len(args) == 0:
        return lib.Error_Get_ExtendedErrors() != 0

    # Setter
    Value, = args
    lib.Error_Set_ExtendedErrors(Value)


def UseExceptions(*args):
    """
    Controls whether the automatic error checking mechanism is enable, i.e., if
    the DSS engine errors (from the `Error` interface) are mapped exception when
    detected. 
    
    **When disabled, the user takes responsibility for checking for errors.**
    This can be done through the `Error` interface. When `Error.Number` is not
    zero, there should be an error message in `Error.Description`. This is compatible
    with the behavior on the official OpenDSS (Windows-only COM implementation) when 
    `AllowForms` is disabled.

    Users can also use the DSS command `Export ErrorLog` to inspect for errors.

    **WARNING:** This is a global setting, affects all DSS instances from DSS-Python 
    and OpenDSSDirect.py.

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return Base._use_exceptions

    # Setter
    value, = args
    Base._enable_exceptions(bool(value))


_columns = ["Description", "Number", "EarlyAbort", "ExtendedErrors", "UseExceptions"]
__all__ = ["Description", "Number", "EarlyAbort", "ExtendedErrors", "UseExceptions"]
