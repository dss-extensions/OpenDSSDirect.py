from ._utils import  api_util, Iterable


class ILoadShape(Iterable):
    __slots__ = []
    __name__ = "LoadShape"
    _api_prefix = "LoadShapes"
    _columns = [
        "Name",
        "Idx",
        "UseActual",
        "Npts",
        "HrInterval",
        "MinInterval",
        "SInterval",
        "PBase",
        "PMult",
        "QBase",
        "QMult",
        "TimeArray",
    ]

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)
        return self.CheckForError(self._lib.LoadShapes_New(Name))

    def Normalize(self):
        self.CheckForError(self._lib.LoadShapes_Normalize())

    def HrInterval(self, *args):
        """Fixed interval time value, hours."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_HrInterval())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_HrInterval(Value))

    def MinInterval(self, *args):
        """Fixed Interval time value, in minutes"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_MinInterval())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_MinInterval(Value))

    def Npts(self, *args):
        """Get/set Number of points in active Loadshape."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_Npts())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_Npts(Value))

    def PBase(self, *args):
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_PBase())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_PBase(Value))

    def PMult(self, *args):
        """Array of doubles for the P multiplier in the Loadshape."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.LoadShapes_Get_Pmult)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount))

    def QBase(self, *args):
        """Base for normalizing Q curve. If left at zero, the peak value is used."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_Qbase())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_Qbase(Value))

    def QMult(self, *args):
        """Array of doubles containing the Q multipliers."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.LoadShapes_Get_Qmult)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount))

    def TimeArray(self, *args):
        """Time array in hours correscponding to P and Q multipliers when the Interval=0."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.LoadShapes_Get_TimeArray)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount))

    def UseActual(self, *args):
        """Boolean flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_UseActual()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_UseActual(Value))

    def SInterval(self, *args):
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.LoadShapes_Get_SInterval())

        # Setter
        Value, = args
        self.CheckForError(self._lib.LoadShapes_Set_SInterval(Value))


_LoadShape = ILoadShape(api_util)

# For backwards compatibility, bind to the default instance
New = _LoadShape.New
Normalize = _LoadShape.Normalize
AllNames = _LoadShape.AllNames
Count = _LoadShape.Count
First = _LoadShape.First
HrInterval = _LoadShape.HrInterval
MinInterval = _LoadShape.MinInterval
Name = _LoadShape.Name
Next = _LoadShape.Next
Npts = _LoadShape.Npts
PBase = _LoadShape.PBase
PMult = _LoadShape.PMult
QBase = _LoadShape.QBase
QMult = _LoadShape.QMult
TimeArray = _LoadShape.TimeArray
UseActual = _LoadShape.UseActual
SInterval = _LoadShape.SInterval
Idx = _LoadShape.Idx
_columns = _LoadShape._columns
__all__ = [
    "New",
    "Normalize",
    "AllNames",
    "Count",
    "First",
    "HrInterval",
    "MinInterval",
    "Name",
    "Next",
    "Npts",
    "PBase",
    "PMult",
    "QBase",
    "QMult",
    "TimeArray",
    "UseActual",
    "SInterval",
    "Idx",
]
