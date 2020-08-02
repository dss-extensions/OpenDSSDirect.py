# -*- coding: utf-8 -*-
from __future__ import absolute_import
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
    If enabled, the legacy/deprecated models for PVSystem, InvControl, Storage and StorageControl are used.
    In the official OpenDSS version 9.0, the old models where removed. They are temporarily present here
    but may be removed in the near future. If they are important to you, please open an issue on GitHub
    or contact the authors from DSS Extensions: https://github.com/dss-extensions/

    After toggling LegacyModels, run a "clear" command and the models will be loaded accordingly.
    Defaults to False. 

    This can also be enabled by setting the environment variable DSS_CAPI_LEGACY_MODELS to 1.

    (API Extension)
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.DSS_Get_LegacyModels()) != 0

    # Setter
    Value, = args
    return CheckForError(lib.DSS_Set_LegacyModels(Value))


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
]
