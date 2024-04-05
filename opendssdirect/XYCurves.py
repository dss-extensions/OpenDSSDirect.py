from ._utils import api_util
from .Bases import Iterable


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
        """
        Get/Set Number of points in X-Y curve

        Original COM help: https://opendss.epri.com/Npts1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Npts()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_Npts(Value)

    def XArray(self, *args):
        """
        Get/set X values as an array of doubles. When setting, remember to set Npts to max number expected values.

        Original COM help: https://opendss.epri.com/Xarray.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Xarray_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.XYCurves_Set_Xarray(ValuePtr, ValueCount)

    def XScale(self, *args):
        """
        Factor to scale X values from original curve

        Original COM help: https://opendss.epri.com/Xscale.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Xscale()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_Xscale(Value)

    def XShift(self, *args):
        """
        Amount to shift X value from original curve

        Original COM help: https://opendss.epri.com/Xshift.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Xshift()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_Xshift(Value)

    def YArray(self, *args):
        """
        Get/set Y values as an array of doubles. When setting, remember to set Npts to max number expected values.

        Original COM help: https://opendss.epri.com/Yarray.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Yarray_GR()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.XYCurves_Set_Yarray(ValuePtr, ValueCount)

    def YScale(self, *args):
        """
        Factor to scale Y values from original curve

        Original COM help: https://opendss.epri.com/Yscale.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Yscale()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_Yscale(Value)

    def YShift(self, *args):
        """
        Amount to shift Y value from original curve

        Original COM help: https://opendss.epri.com/Yshift.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_Yshift()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_Yshift(Value)

    def X(self, *args):
        """
        Set X value or get interpolated value after setting Y

        Original COM help: https://opendss.epri.com/x4.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_x()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_x(Value)

    def Y(self, *args):
        """
        Set Y value or get interpolated Y value after setting X

        Original COM help: https://opendss.epri.com/y1.html
        """
        # Getter
        if len(args) == 0:
            return self._lib.XYCurves_Get_y()

        # Setter
        (Value,) = args
        self._lib.XYCurves_Set_y(Value)


_XYCurves = IXYCurves(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _XYCurves.AllNames
Count = _XYCurves.Count
First = _XYCurves.First
Idx = _XYCurves.Idx
Name = _XYCurves.Name
Next = _XYCurves.Next
Npts = _XYCurves.Npts
X = _XYCurves.X
XArray = _XYCurves.XArray
XScale = _XYCurves.XScale
XShift = _XYCurves.XShift
Y = _XYCurves.Y
YArray = _XYCurves.YArray
YScale = _XYCurves.YScale
YShift = _XYCurves.YShift
_columns = _XYCurves._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "Idx",
    "Name",
    "Next",
    "Npts",
    "X",
    "XArray",
    "XScale",
    "XShift",
    "Y",
    "YArray",
    "YScale",
    "YShift",
]
