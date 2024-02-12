# import warnings
from ._utils import api_util, dss_py, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base
try:
    from ._version import __version__
except:
    __version__ = '0.0dev'

# from dss import DSSCompatFlags


class IBasic(Base):
    __name__ = "Basic"
    _api_prefix = "DSS"
    _columns = [
        "Version",
        "Classes",
        "NumUserClasses",
        "DataPath",
        "NumClasses",
        "NumCircuits",
        "UserClasses",
        "DefaultEditor",
    ]
    __slots__ = []

    def ClearAll(self):
        self._check_for_error(self._lib.DSS_ClearAll())

    def Reset(self):
        """
        This is a no-op function, does nothing. Left for compatibility.

        Original COM help: https://opendss.epri.com/Reset1.html
        """
        self._check_for_error(self._lib.DSS_Reset())

    def SetActiveClass(self, ClassName):
        if not isinstance(ClassName, bytes):
            ClassName = ClassName.encode(self._api_util.codec)
        return self._check_for_error(self._lib.DSS_SetActiveClass(ClassName))

    def Start(self, code):
        """
        This is a no-op function, does nothing. Left for compatibility.

        Calling `Start` in AltDSS/DSS-Extensions is required but that is already
        handled automatically, so the users do not need to call it manually,
        unless using AltDSS/DSS C-API directly without further tools.

        On the official OpenDSS, `Start` also does nothing at all in the current
        versions.

        Original COM help: https://opendss.epri.com/Start.html
        """
        return self._check_for_error(self._lib.DSS_Start(code)) != 0

    def Classes(self):
        """
        List of DSS intrinsic classes (names of the classes)

        Original COM help: https://opendss.epri.com/Classes1.html
        """
        return self._check_for_error(self._get_string_array(self._lib.DSS_Get_Classes))

    def DataPath(self, *args):
        """
        DSS Data File Path.  Default path for reports, etc. from DSS

        Original COM help: https://opendss.epri.com/DataPath.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(self._check_for_error(self._lib.DSS_Get_DataPath()))

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.DSS_Set_DataPath(Value))

    def DefaultEditor(self):
        """
        Returns the path name for the default text editor.

        Original COM help: https://opendss.epri.com/DefaultEditor.html
        """
        return self._get_string(self._check_for_error(self._lib.DSS_Get_DefaultEditor()))

    def NumCircuits(self):
        """
        Number of Circuits currently defined

        Original COM help: https://opendss.epri.com/NumCircuits.html
        """
        return self._check_for_error(self._lib.DSS_Get_NumCircuits())

    def NumClasses(self):
        """
        Number of DSS intrinsic classes

        Original COM help: https://opendss.epri.com/NumClasses.html
        """
        return self._check_for_error(self._lib.DSS_Get_NumClasses())

    def NumUserClasses(self):
        """
        Number of user-defined classes

        Original COM help: https://opendss.epri.com/NumUserClasses.html
        """
        return self._check_for_error(self._lib.DSS_Get_NumUserClasses())

    def UserClasses(self):
        """
        List of user-defined classes

        Original COM help: https://opendss.epri.com/UserClasses.html
        """
        return self._check_for_error(self._get_string_array(self._lib.DSS_Get_UserClasses))

    def Version(self):
        """
        Get version string for the DSS.

        Original COM help: https://opendss.epri.com/Version.html
        """
        return dss_py.DSS.Version + f"\nOpenDSSDirect.py version: {__version__}"

    def AllowForms(self, *args):
        """
        Gets/sets whether text output is allowed (DSS-Extensions) or general forms/windows are shown (official OpenDSS).

        Original COM help: https://opendss.epri.com/AllowForms.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_AllowForms()) != 0

        # Setter
        (value,) = args
        self._check_for_error(self._lib.DSS_Set_AllowForms(value))

    def AllowEditor(self, *args):
        """
        Gets/sets whether running the external editor for "Show" is allowed

        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_AllowEditor()) != 0

        # Setter
        (value,) = args
        self._check_for_error(self._lib.DSS_Set_AllowEditor(value))

    def ShowPanel(self):
        return 0

    def NewCircuit(self, name):
        if not isinstance(name, bytes):
            name = name.encode(self._api_util.codec)
        self._check_for_error(self._lib.DSS_NewCircuit(name))
        return "New Circuit" # self.ActiveCircuit

    def LegacyModels(self, *args):
        """
        LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
        StorageControl.
        In the official OpenDSS version 9.0, the old models were removed. They were temporarily present here
        but were also removed in DSS C-API v0.13.0.

        **NOTE**: this property will be removed for v1.0. It is left to avoid breaking the current API too soon.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_LegacyModels()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_LegacyModels(Value))

    def AllowChangeDir(self, *args):
        """
        If disabled, the engine will not change the active working directory during execution. E.g. a "compile"
        command will not "chdir" to the file path.

        If you have issues with long paths, enabling this might help in some scenarios.

        Defaults to True (allow changes, backwards compatible) in the 0.10.x versions of DSS C-API.
        This might change to False in future versions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_CHANGE_DIR. Set it to 0 to
        disallow changing the active working directory.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_AllowChangeDir()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_AllowChangeDir(Value))

    def AllowDOScmd(self, *args):
        """
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_AllowDOScmd()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_AllowDOScmd(Value))

    def COMErrorResults(self, *args):
        """
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with the
        official OpenDSS COM interface.

        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (`COMErrorResults(False)`), the function will return "[]", an array with 0 elements.
        - In the enabled state (`COMErrorResults(True)`), the function will return "[0.0]" instead. This should
        be compatible with the return value of the official COM interface.

        Defaults to True/1 (enabled state) in the v0.12.x series. This will change to false in future series.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 0 disables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_COMErrorResults()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_COMErrorResults(Value))

    def AdvancedTypes(self, *args):
        """
        When enabled, there are two side-effects:

        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).

        As a result, for example, `OpenDSSDirect.CktElement.Yprim()` is returned as a complex matrix instead
        of a plain array.

        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to `False` for backwards compatibility.*

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            arr_dim = self._check_for_error(self._lib.DSS_Get_EnableArrayDimensions()) != 0
            allow_complex = self._api_util._allow_complex
            return arr_dim and allow_complex

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_EnableArrayDimensions(Value))
        self._api_util._allow_complex = bool(Value)

    def CompatFlags(self, *args):
        """
        Controls some compatibility flags introduced to toggle some behavior from the official OpenDSS.

        **THE FLAGS ARE GLOBAL, affecting all DSS engines in the process.**

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        See the enumeration `DSSCompatFlags` for available flags, including description.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.DSS_Get_CompatFlags())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.DSS_Set_CompatFlags(Value))


_Basic = IBasic(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
ClearAll = _Basic.ClearAll
Reset = _Basic.Reset
SetActiveClass = _Basic.SetActiveClass
Start = _Basic.Start
Classes = _Basic.Classes
DataPath = _Basic.DataPath
DefaultEditor = _Basic.DefaultEditor
NumCircuits = _Basic.NumCircuits
NumClasses = _Basic.NumClasses
NumUserClasses = _Basic.NumUserClasses
UserClasses = _Basic.UserClasses
Version = _Basic.Version
AllowForms = _Basic.AllowForms
ShowPanel = _Basic.ShowPanel
NewCircuit = _Basic.NewCircuit
AllowEditor = _Basic.AllowEditor
LegacyModels = _Basic.LegacyModels
AllowChangeDir = _Basic.AllowChangeDir
AllowDOScmd = _Basic.AllowDOScmd
COMErrorResults = _Basic.COMErrorResults
AdvancedTypes = _Basic.AdvancedTypes
CompatFlags = _Basic.CompatFlags
_columns = _Basic._columns
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
    "AllowDOScmd",
    "COMErrorResults",
    "AdvancedTypes",
    "CompatFlags",
]
