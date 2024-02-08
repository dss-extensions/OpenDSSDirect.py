from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Iterable


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
        """Create a new LoadShape, with default parameters"""
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)
        return self._check_for_error(self._lib.LoadShapes_New(Name))

    def Normalize(self):
        """Normalize the LoadShape data inplace"""
        self._check_for_error(self._lib.LoadShapes_Normalize())

    def HrInterval(self, *args):
        """
        Fixed interval time value, in hours.

        Original COM help: https://opendss.epri.com/HrInterval.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_HrInterval())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_HrInterval(Value))

    def MinInterval(self, *args):
        """
        Fixed Interval time value, in minutes

        Original COM help: https://opendss.epri.com/MinInterval.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_MinInterval())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_MinInterval(Value))

    def Npts(self, *args):
        """
        Get/set Number of points in active Loadshape.

        Original COM help: https://opendss.epri.com/Npts.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_Npts())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_Npts(Value))

    def PBase(self, *args):
        """
        Base P value for normalization. Default is zero, meaning the peak will be used.

        Original COM help: https://opendss.epri.com/Pbase.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_PBase())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_PBase(Value))

    def PMult(self, *args):
        """
        Array of doubles for the P multiplier in the Loadshape.

        Original COM help: https://opendss.epri.com/Pmult.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LoadShapes_Get_Pmult_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount))

    def QBase(self, *args):
        """
        Base for normalizing Q curve. If left at zero, the peak value is used.

        Original COM help: https://opendss.epri.com/Qbase.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_Qbase())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_Qbase(Value))

    def QMult(self, *args):
        """
        Array of doubles containing the Q multipliers.

        Original COM help: https://opendss.epri.com/Qmult.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LoadShapes_Get_Qmult_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount))

    def TimeArray(self, *args):
        """
        Time array in hours corresponding to P and Q multipliers when the Interval=0.

        Original COM help: https://opendss.epri.com/TimeArray.html
        """
        # Getter
        if len(args) == 0:
            self._check_for_error(self._lib.LoadShapes_Get_TimeArray_GR())
            return self._get_float64_gr_array()

        # Setter
        (Value,) = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount))

    def UseActual(self, *args):
        """
        Boolean flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

        Original COM help: https://opendss.epri.com/UseActual.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_UseActual()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_UseActual(Value))

    def SInterval(self, *args):
        """
        Fixed interval time value, in seconds.

        Original COM help: https://opendss.epri.com/Sinterval.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.LoadShapes_Get_SInterval())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.LoadShapes_Set_SInterval(Value))

    def UseFloat32(self):
        """
        Converts the current LoadShape data to float32/single precision.
        If there is no data or the data is already represented using float32, nothing is done.

        **(API Extension)**
        """
        self._check_for_error(self._lib.LoadShapes_UseFloat32())

    def UseFloat64(self):
        """
        Converts the current LoadShape data to float64/double precision.
        If there is no data or the data is already represented using float64, nothing is done.

        **(API Extension)**
        """
        self._check_for_error(self._lib.LoadShapes_UseFloat64())


_LoadShape = ILoadShape(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

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
UseFloat32 = _LoadShape.UseFloat32
UseFloat64 = _LoadShape.UseFloat64
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
    "UseFloat32",
    "UseFloat64",
]
