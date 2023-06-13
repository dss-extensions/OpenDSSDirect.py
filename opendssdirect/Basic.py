from ._utils import lib, codec, CheckForError, get_string, get_string_array


def ClearAll():
    CheckForError(lib.DSS_ClearAll())


def Reset():
    CheckForError(lib.DSS_Reset())


def SetActiveClass(ClassName):
    if type(ClassName) is not bytes:
        ClassName = ClassName.encode(codec)
    return CheckForError(lib.DSS_SetActiveClass(ClassName))


def Start(code):
    return CheckForError(lib.DSS_Start(code)) != 0


def Classes():
    """(read-only) List of DSS intrinsic classes (names of the classes)"""
    return CheckForError(get_string_array(lib.DSS_Get_Classes))


def DataPath(*args):
    """DSS Data File Path.  Default path for reports, etc. from DSS"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.DSS_Get_DataPath()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.DSS_Set_DataPath(Value))


def DefaultEditor():
    """(read-only) Returns the path name for the default text editor."""
    return get_string(CheckForError(lib.DSS_Get_DefaultEditor()))


def NumCircuits():
    """(read-only) Number of Circuits currently defined"""
    return CheckForError(lib.DSS_Get_NumCircuits())


def NumClasses():
    """(read-only) Number of DSS intrinsic classes"""
    return CheckForError(lib.DSS_Get_NumClasses())


def NumUserClasses():
    """(read-only) Number of user-defined classes"""
    return CheckForError(lib.DSS_Get_NumUserClasses())


def UserClasses():
    """(read-only) List of user-defined classes"""
    return CheckForError(get_string_array(lib.DSS_Get_UserClasses))


def Version():
    """(read-only) Get version string for the DSS."""
    return get_string(CheckForError(lib.DSS_Get_Version()))


def AllowForms(*args):
    """Gets/sets whether text output is allowed"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_AllowForms()) != 0

    # Setter
    value, = args
    CheckForError(lib.DSS_Set_AllowForms(value))


def ShowPanel():
    # warnings.warn('ShowPanel is not implemented.')
    return 0


def NewCircuit(name):
    if type(name) is not bytes:
        name = name.encode(codec)

    lib.DSS_NewCircuit(name)
    error_num = lib.Error_Get_Number()
    if error_num:
        raise RuntimeError(
            "[ERROR {}] {}".format(error_num, get_string(lib.Error_Get_Description()))
        )

    return "New Circuit"


def AllowEditor(*args):
    """
    Gets/sets whether running the external editor for "Show" is allowed

    AllowEditor controls whether the external editor is used in commands like "Show".
    If you set to 0 (false), the editor is not executed. Note that other side effects,
    such as the creation of files, are not affected.
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_AllowEditor()) != 0

    # Setter
    value, = args
    CheckForError(lib.DSS_Set_AllowEditor(value))


def LegacyModels(*args):
    """
    LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
    StorageControl.
    In the official OpenDSS version 9.0, the old models were removed. They were temporarily present here
    but were also removed in DSS C-API v0.13.0.
        
    **NOTE**: this function will be removed for v1.0. It is left to avoid breaking the current API too soon.

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_LegacyModels()) != 0

    # Setter
    Value, = args
    CheckForError(lib.DSS_Set_LegacyModels(Value))


def AllowChangeDir(*args):
    """
    If disabled, the engine will not change the active working directory during execution. E.g. a "compile"
    command will not "chdir" to the file path.

    If you have issues with long paths, enabling this might help in some scenarios.

    Defaults to True (allow changes, backwards compatible) in the 0.10.x versions of DSS C-API.
    This might change to False in future versions.

    This can also be set through the environment variable DSS_CAPI_ALLOW_CHANGE_DIR. Set it to 0 to
    disallow changing the active working directory.

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_AllowChangeDir()) != 0

    # Setter
    Value, = args
    CheckForError(lib.DSS_Set_AllowChangeDir(Value))


def CompatFlags(*args):
    """
    Controls some compatibility flags introduced to toggle some behavior from the official OpenDSS.

    **THESE FLAGS ARE GLOBAL, affecting all DSS engines in the process.**

    The current bit flags are:

    - 0x1 (bit 0): If enabled, don't check for NaNs in the inner solution loop. This can lead to various errors.
        This flag is useful for legacy applications that don't handle OpenDSS API errors properly. Through the 
        development of DSS-Extensions, we noticed this is actually a quite common issue.
    - 0x2 (bit 1): Toggle worse precision for certain aspects of the engine. For example, the sequence-to-phase 
        (`As2p`) and sequence-to-phase (`Ap2s`) transform matrices. On DSS C-API, we fill the matrix explicitly
        using higher precision, while numerical inversion of an initially worse precision matrix is used in the 
        official OpenDSS. We will introduce better precision for other aspects of the engine in the future, 
        so this flag can be used to toggle the old/bad values where feasible.
    - 0x4 (bit 2): Toggle some InvControl behavior introduced in OpenDSS 9.6.1.1. It could be a regression 
        but needs further investigation, so we added this flag in the time being.
    - 0x8 (bit 3): When using "save circuit", the official OpenDSS always includes the "CalcVoltageBases" command
        in the saved script. We found that it is not always a good idea, so we removed the command (leaving it 
        commented). Use this flag to enable the command in the saved script.

    These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
    when we remove a compatibility flag, it will have no effect but will also not affect anything else
    besides raising an error if the user tries to toggle a flag that was available in a previous version.

    We expect to keep a very limited number of flags. Since the flags are more transient than the other
    options/flags, it was preferred to add this generic function instead of a separate function per
    flag.

    Related enumeration: DSSCompatFlags

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_CompatFlags())

    # Setter
    Value, = args
    CheckForError(lib.DSS_Set_CompatFlags(Value))



_columns = [
    "Classes",
    "DataPath",
    "DefaultEditor",
    "NumCircuits",
    "NumClasses",
    "NumUserClasses",
    "UserClasses",
    "Version",
]
__all__ = [
    "ClearAll",
    "Reset",
    "SetActiveClass",
    "Start",
    "Classes",
    "DataPath",
    "DefaultEditor",
    "NumCircuits",
    "NumClasses",
    "NumUserClasses",
    "UserClasses",
    "Version",
    "AllowForms",
    "ShowPanel",
    "NewCircuit",
    "AllowEditor",
    "LegacyModels",
    "AllowChangeDir",
]
