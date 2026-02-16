import warnings
from ._utils import api_util, dss_py
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
        self._lib.DSS_ClearAll()

    def Reset(self):
        """
        This is a no-op function, does nothing. Left for compatibility.

        Original COM help: https://opendss.epri.com/Reset1.html
        """
        self._lib.DSS_Reset()

    def SetActiveClass(self, ClassName):
        return self._lib.DSS_SetActiveClass(ClassName)

    def Start(self, code):
        """
        This is a no-op function, does nothing. Left for compatibility.

        Calling `Start` in AltDSS/DSS-Extensions is required but that is already
        handled automatically, so the users do not need to call it manually,
        unless using AltDSS/DSS C-API directly without further tools.

        On EPRI's OpenDSS, `Start` also does nothing at all in the current
        Delphi versions. It is required for OpenDSS-C, but also handled behind
        the scenes on DSS-Extensions.

        Original COM help: https://opendss.epri.com/Start.html
        """
        return self._lib.DSS_Start(code)

    def Classes(self):
        """
        List of DSS intrinsic classes (names of the classes)

        Original COM help: https://opendss.epri.com/Classes1.html
        """
        return self._lib.DSS_Get_Classes()

    def DataPath(self, *args):
        """
        DSS Data File Path.  Default path for reports, etc. from DSS

        Original COM help: https://opendss.epri.com/DataPath.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_DataPath()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_DataPath(Value)

    def DefaultEditor(self):
        """
        Returns the path name for the default text editor.

        Original COM help: https://opendss.epri.com/DefaultEditor.html
        """
        return self._lib.DSS_Get_DefaultEditor()

    def NumCircuits(self):
        """
        Number of Circuits currently defined

        Original COM help: https://opendss.epri.com/NumCircuits.html
        """
        return self._lib.DSS_Get_NumCircuits()

    def NumClasses(self):
        """
        Number of DSS intrinsic classes

        Original COM help: https://opendss.epri.com/NumClasses.html
        """
        return self._lib.DSS_Get_NumClasses()

    def NumUserClasses(self):
        """
        Number of user-defined classes

        Original COM help: https://opendss.epri.com/NumUserClasses.html
        """
        return self._lib.DSS_Get_NumUserClasses()

    def UserClasses(self):
        """
        List of user-defined classes

        Original COM help: https://opendss.epri.com/UserClasses.html
        """
        return self._lib.DSS_Get_UserClasses()

    def Version(self):
        """
        Get version string for the DSS.

        Original COM help: https://opendss.epri.com/Version.html
        """
        return dss_py.DSS.Version + f"\nOpenDSSDirect.py version: {__version__}"

    def AllowForms(self, *args):
        """
        Indicates whether text output is allowed or forms are used.  Disable to silence most output.

        Currently, forms/windows are only used for EPRI's OpenDSS distribution on Windows.

        Original COM help: https://opendss.epri.com/AllowForms.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_AllowForms()

        # Setter
        (value,) = args
        self._lib.DSS_Set_AllowForms(value)

    def AllowEditor(self, *args):
        """
        Gets/sets whether running the external editor for "Show" is allowed

        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        **Deprecated:** Use `Settings.AllowEditor()` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            warnings.warn(
                '"AllowEditor" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.AllowEditor` instead.',
                DeprecationWarning,
                stacklevel=2,
            )
            return self._lib.DSS_Get_AllowEditor()

        # Setter
        (value,) = args
        self._lib.DSS_Set_AllowEditor(value)

    def ShowPanel(self):
        if self._api_util._is_oddie:
            self._lib.Text_Set_Command("panel")

        return 0

    def NewCircuit(self, name: str):
        """
        Make a new circuit.

        Original COM help: https://opendss.epri.com/NewCircuit.html

        **Deprecated**: Use `OpenDSSDirect.NewCircuit()` directly (`NewCircuit()` in the parent object).
        """
        warnings.warn(
            '"NewCircuit" was moved to the parent object in the OpenDSSDirect class. This method still works, but will be removed in a future release. Please use `...AllowEditor` instead.',
            DeprecationWarning,
            stacklevel=2,
        )
        self._lib.DSS_NewCircuit(name)
        return "New Circuit" # self.ActiveCircuit

    def LegacyModels(self, *args):
        """
        LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
        StorageControl.
        In EPRI's OpenDSS version 9.0, the old models were removed. They were temporarily present here
        but were also removed in DSS C-API v0.13.0.

        **NOTE**: this property will be removed for v1.0. It is left to avoid breaking the current API too soon.

        **(API Extension)**
        """
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_LegacyModels()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_LegacyModels(Value)

    def AllowChangeDir(self, *args):
        """
        If disabled, the engine will not change the active working directory during execution. E.g. a "compile"
        command will not "chdir" to the file path.

        If you have issues with long paths, enabling this might help in some scenarios.

        Defaults to True (allow changes, backwards compatible) in the 0.10.x versions of DSS C-API.
        This might change to False in future versions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_CHANGE_DIR. Set it to 0 to
        disallow changing the active working directory.

        **Deprecated:** Use `Settings.AllowChangeDir` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        warnings.warn(
            '"AllowChangeDir" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.AllowChangeDir` instead.',
            DeprecationWarning,
            stacklevel=2,
        )
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_AllowChangeDir()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_AllowChangeDir(Value)

    def AllowDOScmd(self, *args):
        """
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        **Deprecated:** Use `Settings.AllowDOScmd` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        warnings.warn(
            '"AllowDOScmd" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.AllowDOScmd` instead.',
            DeprecationWarning,
            stacklevel=2,
        )
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_AllowDOScmd()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_AllowDOScmd(Value)

    def COMErrorResults(self, *args):
        """
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with
        EPRI's OpenDSS COM interface.

        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (`COMErrorResults(False)`), the function will return "[]", an array with 0 elements.
        - In the enabled state (`COMErrorResults(True)`), the function will return "[0.0]" instead. This should
        be compatible with the return value of EPRI's OpenDSS COM interface.

        Defaults to false (disabled state) in AltDSS since the v0.15.x series.

        This does not affect the results when using EPRI's OpenDSS distribution through Oddie.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 1 enables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **Deprecated:** Use `Settings.COMErrorResults` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        warnings.warn(
            '"COMErrorResults" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.COMErrorResults` instead.',
            DeprecationWarning,
            stacklevel=2,
        )
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_COMErrorResults()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_COMErrorResults(Value)

    def AdvancedTypes(self, *args):
        """
        When enabled, there are **two side-effects**:

        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).

        As a result, for example, `OpenDSSDirect.CktElement.Yprim()` is returned as a complex matrix instead
        of a plain array.

        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to **False** for backwards compatibility.*

        **Deprecated:** Use `Settings.AdvancedTypes` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        warnings.warn('"AdvancedTypes" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.AdvancedTypes` instead.', DeprecationWarning, stacklevel=2)

        # Getter
        if len(args) == 0:
            return self._lib.advanced_types

        # Setter
        (Value,) = args
        self._lib.advanced_types = bool(Value)

    def CompatFlags(self, *args):
        """
        Controls some compatibility flags introduced to toggle some behavior from EPRI's OpenDSS.

        **THE FLAGS ARE GLOBAL, affecting all AltDSS engines in the process.**
        CompatFlags for Oddie-loaded instances (OpenDSS and OpenDSS-C engines) are handled by the Oddie code itself,
        so it is global for each Oddie library.

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        See the enumeration `DSSCompatFlags` for available flags, including description.

        **Deprecated:** Use `Settings.CompatFlags` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        """
        warnings.warn(
            '"CompatFlags" was moved to the Settings interface. This method still works, but will be removed in a future release. Please use `...Settings.CompatFlags` instead.',
            DeprecationWarning,
            stacklevel=2,
        )
        # Getter
        if len(args) == 0:
            return self._lib.DSS_Get_CompatFlags()

        # Setter
        (Value,) = args
        self._lib.DSS_Set_CompatFlags(Value)


_Basic = IBasic(api_util)

# For backwards compatibility, bind to the default instance
AdvancedTypes = _Basic.AdvancedTypes
AllowChangeDir = _Basic.AllowChangeDir
AllowDOScmd = _Basic.AllowDOScmd
AllowEditor = _Basic.AllowEditor
AllowForms = _Basic.AllowForms
COMErrorResults = _Basic.COMErrorResults
Classes = _Basic.Classes
ClearAll = _Basic.ClearAll
CompatFlags = _Basic.CompatFlags
DataPath = _Basic.DataPath
DefaultEditor = _Basic.DefaultEditor
LegacyModels = _Basic.LegacyModels
NewCircuit = _Basic.NewCircuit
NumCircuits = _Basic.NumCircuits
NumClasses = _Basic.NumClasses
NumUserClasses = _Basic.NumUserClasses
Reset = _Basic.Reset
SetActiveClass = _Basic.SetActiveClass
ShowPanel = _Basic.ShowPanel
Start = _Basic.Start
UserClasses = _Basic.UserClasses
Version = _Basic.Version
_columns = _Basic._columns
__all__ = [
    "AdvancedTypes",
    "AllowChangeDir",
    "AllowDOScmd",
    "AllowEditor",
    "AllowForms",
    "COMErrorResults",
    "Classes",
    "ClearAll",
    "CompatFlags",
    "DataPath",
    "DefaultEditor",
    "LegacyModels",
    "NewCircuit",
    "NumCircuits",
    "NumClasses",
    "NumUserClasses",
    "Reset",
    "SetActiveClass",
    "ShowPanel",
    "Start",
    "UserClasses",
    "Version",
]
