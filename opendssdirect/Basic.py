# import warnings
from ._utils import api_util, Base, dss_py
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
        self.CheckForError(self._lib.DSS_ClearAll())

    def Reset(self):
        self.CheckForError(self._lib.DSS_Reset())

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(self._api_util.codec)
        return self.CheckForError(self._lib.DSS_SetActiveClass(ClassName))

    def Start(self, code):
        return self.CheckForError(self._lib.DSS_Start(code)) != 0

    def Classes(self):
        """(read-only) List of DSS intrinsic classes (names of the classes)"""
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_Classes))

    def DataPath(self, *args):
        """DSS Data File Path.  Default path for reports, etc. from DSS"""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.DSS_Get_DataPath()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.DSS_Set_DataPath(Value))

    def DefaultEditor(self):
        """(read-only) Returns the path name for the default text editor."""
        return self._get_string(self.CheckForError(self._lib.DSS_Get_DefaultEditor()))

    def NumCircuits(self):
        """(read-only) Number of Circuits currently defined"""
        return self.CheckForError(self._lib.DSS_Get_NumCircuits())

    def NumClasses(self):
        """(read-only) Number of DSS intrinsic classes"""
        return self.CheckForError(self._lib.DSS_Get_NumClasses())

    def NumUserClasses(self):
        """(read-only) Number of user-defined classes"""
        return self.CheckForError(self._lib.DSS_Get_NumUserClasses())

    def UserClasses(self):
        """(read-only) List of user-defined classes"""
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_UserClasses))


    def Version(self):
        """(read-only) Get version string for the DSS."""
        return dss_py.DSS.Version + f"\nOpenDSSDirect.py version: {__version__}"

    def AllowForms(self, *args):
        """Gets/sets whether text output is allowed"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.DSS_Get_AllowForms()) != 0

        # Setter
        value, = args
        self.CheckForError(self._lib.DSS_Set_AllowForms(value))

    def AllowEditor(self, *args):
        """
        Gets/sets whether running the external editor for "Show" is allowed

        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.DSS_Get_AllowEditor()) != 0

        # Setter
        value, = args
        self.CheckForError(self._lib.DSS_Set_AllowEditor(value))

    def ShowPanel(self):
        # warnings.warn("ShowPanel is not implemented.")
        return 0

    def NewCircuit(self, name):
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)
        self.CheckForError(self._lib.DSS_NewCircuit(name))
        return "New Circuit" # self.ActiveCircuit

    def LegacyModels(self, *args):
        """
        LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
        StorageControl.
        In the official OpenDSS version 9.0, the old models were removed. They were temporarily present here
        but were also removed in DSS C-API v0.13.0.

        **NOTE**: this property will be removed for v1.0. It is left to avoid breaking the current API too soon.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.DSS_Get_LegacyModels()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.DSS_Set_LegacyModels(Value))

    def AllowChangeDir(self, *args):
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
            return self.CheckForError(self._lib.DSS_Get_AllowChangeDir()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.DSS_Set_AllowChangeDir(Value))

    def AllowDOScmd(self, *args):
        """
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        (API Extension)
        """
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.DSS_Get_AllowDOScmd()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.DSS_Set_AllowDOScmd(Value))

    # def Plotting(self):
    #     """
    #     Shortcut for the plotting module. This property is equivalent to:

    #     ```
    #     from dss import plot
    #     return plot
    #     ```

    #     Gives access to the `enable()` and `disable()` functions.
    #     Requires matplotlib and SciPy to be installed, hence it is an
    #     optional feature.

    #     (API Extension)
    #     """
    #     from dss import plot

    #     return plot

    def AdvancedTypes(self, *args):
        '''
        When enabled, there are **two side-effects**:
        
        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).
        
        As a result, for example, `opendssdirect.CktElement.Yprim()` is returned as a complex matrix instead
        of a plain array.
        
        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to **False** for backwards compatibility.*
        
        (API Extension)
        '''

        # Getter
        if len(args) == 0:
            arr_dim = self.CheckForError(self._lib.DSS_Get_EnableArrayDimensions()) != 0
            allow_complex = self._api_util._allow_complex
            return arr_dim and allow_complex

        # Setter
        Value, = args
        self.CheckForError(self._lib.DSS_Set_EnableArrayDimensions(Value))
        self._api_util._allow_complex = bool(Value)


    def CompatFlags(self, *args):
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
            return self.CheckForError(self._lib.DSS_Get_CompatFlags())

        # Setter
        Value, = args
        self.CheckForError(self._lib.DSS_Set_CompatFlags(Value))


_Basic = IBasic(api_util)

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
# Plotting = _Basic.Plotting
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
    # "Plotting",
    "CompatFlags",
]
