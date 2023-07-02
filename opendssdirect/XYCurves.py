from ._utils import CheckForError, api_util, Iterable


class IXYCurves(Iterable):
    __slots__ = []
    __name__ = "XYCurves"
    _api_prefix = "XYCurves"
    _columns = [
        "Name",
        "Idx",
        "Npts",
        "XArray",
        "XScale",
        "XShift",
        "YArray",
        "YScale",
        "YShift",
        "X",
        "Y",
    ]

    def Npts(self, *args):
        """Get/Set Number of points in X-Y curve"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_Npts())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_Npts(Value))

    def XArray(self, *args):
        """Get/set X values as a Array of doubles. Set Npts to max number expected if setting"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.XYCurves_Get_Xarray)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.XYCurves_Set_Xarray(ValuePtr, ValueCount))

    def XScale(self, *args):
        """Factor to scale X values from original curve"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_Xscale())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_Xscale(Value))

    def XShift(self, *args):
        """Amount to shift X value from original curve"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_Xshift())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_Xshift(Value))

    def YArray(self, *args):
        """Get/Set Y values in curve; Set Npts to max number expected if setting"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.XYCurves_Get_Yarray)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.XYCurves_Set_Yarray(ValuePtr, ValueCount))

    def YScale(self, *args):
        """Factor to scale Y values from original curve"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_Yscale())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_Yscale(Value))

    def YShift(self, *args):
        """Amount to shift Y valiue from original curve"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_Yshift())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_Yshift(Value))

    def X(self, *args):
        """Set X value or get interpolated value after setting Y"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_x())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_x(Value))

    def Y(self, *args):
        """Set Y value or get interpolated Y value after setting X"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.XYCurves_Get_y())

        # Setter
        Value, = args
        self.CheckForError(self._lib.XYCurves_Set_y(Value))


_XYCurves = IXYCurves(api_util)

# For backwards compatibility, bind to the default instance
Count = _XYCurves.Count
First = _XYCurves.First
Name = _XYCurves.Name
Next = _XYCurves.Next
Npts = _XYCurves.Npts
XArray = _XYCurves.XArray
XScale = _XYCurves.XScale
XShift = _XYCurves.XShift
YArray = _XYCurves.YArray
YScale = _XYCurves.YScale
YShift = _XYCurves.YShift
X = _XYCurves.X
Y = _XYCurves.Y
Idx = _XYCurves.Idx
AllNames = _XYCurves.AllNames
_columns = _XYCurves._columns
__all__ = [
    "Count",
    "First",
    "Name",
    "Next",
    "Npts",
    "XArray",
    "XScale",
    "XShift",
    "YArray",
    "YScale",
    "YShift",
    "X",
    "Y",
    "Idx",
    "AllNames",
]
