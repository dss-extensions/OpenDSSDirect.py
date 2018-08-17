# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    get_string,
    get_string_array,
    get_float64_array,
    prepare_float64_array,
)
from ._utils import codec


def New(Name):
    if type(Name) is not bytes:
        Name = Name.encode(codec)

    return lib.LoadShapes_New(Name)


def Normalize():
    lib.LoadShapes_Normalize()


def AllNames():
    """(read-only) Array of strings containing names of all Loadshape objects currently defined."""
    return get_string_array(lib.LoadShapes_Get_AllNames)


def Count():
    """(read-only) Number of Loadshape objects currently defined in Loadshape collection"""
    return lib.LoadShapes_Get_Count()


def First():
    """(read-only) Set the first loadshape active and return integer index of the loadshape. Returns 0 if none."""
    return lib.LoadShapes_Get_First()


def HrInterval(*args):
    """Fixed interval time value, hours."""
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_HrInterval()

    # Setter
    Value, = args
    lib.LoadShapes_Set_HrInterval(Value)


def MinInterval(*args):
    """Fixed Interval time value, in minutes"""
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_MinInterval()

    # Setter
    Value, = args
    lib.LoadShapes_Set_MinInterval(Value)


def Name(*args):
    """
    (read) Get the Name of the active Loadshape
    (write) Set the active Loadshape by name
    """
    # Getter
    if len(args) == 0:
        return get_string(lib.LoadShapes_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.LoadShapes_Set_Name(Value)


def Next():
    """(read-only) Advance active Loadshape to the next on in the collection. Returns 0 if no more loadshapes."""
    return lib.LoadShapes_Get_Next()


def Npts(*args):
    """
    (read) Get Number of points in active Loadshape.
    (write) Set number of points to allocate for active Loadshape.
    """
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_Npts()

    # Setter
    Value, = args
    lib.LoadShapes_Set_Npts(Value)


def PBase(*args):
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_PBase()

    # Setter
    Value, = args
    lib.LoadShapes_Set_PBase(Value)


def PMult(*args):
    """
    (read) Array of Doubles for the P multiplier in the Loadshape.
    (write) Array of doubles containing the P array for the Loadshape.
    """
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_Pmult)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount)


def QBase(*args):
    """Base for normalizing Q curve. If left at zero, the peak value is used."""
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_Qbase()

    # Setter
    Value, = args
    lib.LoadShapes_Set_Qbase(Value)


def QMult(*args):
    """Array of doubles containing the Q multipliers."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_Qmult)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)


def TimeArray(*args):
    """Time array in hours correscponding to P and Q multipliers when the Interval=0."""
    # Getter
    if len(args) == 0:
        return get_float64_array(lib.LoadShapes_Get_TimeArray)

    # Setter
    Value, = args
    Value, ValuePtr, ValueCount = prepare_float64_array(Value)
    lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount)


def UseActual(*args):
    """T/F flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier."""
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_UseActual() != 0

    # Setter
    Value, = args
    lib.LoadShapes_Set_UseActual(Value)


def SInterval(*args):
    # Getter
    if len(args) == 0:
        return lib.LoadShapes_Get_sInterval()

    # Setter
    Value, = args
    lib.LoadShapes_Set_Sinterval(Value)


_columns = [
    "HrInterval",
    "MinInterval",
    "Name",
    "Npts",
    "PBase",
    "PMult",
    "QBase",
    "QMult",
    "TimeArray",
    "UseActual",
    "SInterval",
]
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
]
