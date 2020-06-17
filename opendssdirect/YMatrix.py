# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy as np
from .Circuit import NumNodes
from ._utils import lib, ffi, CheckForError


def getYsparse(factor=True):
    """Return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix"""
    nBus = ffi.new("uint32_t*")
    nBus[0] = 0
    nNz = ffi.new("uint32_t*")
    nNz[0] = 0

    ColPtr = ffi.new("int32_t**")
    RowIdxPtr = ffi.new("int32_t**")
    cValsPtr = ffi.new("double**")

    lib.YMatrix_GetCompressedYMatrix(factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)

    if not nBus[0] or not nNz[0]:
        res = None
    else:
        # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
        res = (
            np.frombuffer(
                ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=np.complex
            ).copy(),
            np.frombuffer(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32).copy(),
            np.frombuffer(
                ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32
            ).copy(),
        )

    lib.DSS_Dispose_PInteger(ColPtr)
    lib.DSS_Dispose_PInteger(RowIdxPtr)
    lib.DSS_Dispose_PDouble(cValsPtr)

    return res


def ZeroInjCurr():
    lib.YMatrix_ZeroInjCurr()


def GetSourceInjCurrents():
    lib.YMatrix_GetSourceInjCurrents()


def GetPCInjCurr():
    lib.YMatrix_GetPCInjCurr()


def BuildYMatrixD(BuildOps, AllocateVI):
    lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI)


def AddInAuxCurrents(SType):
    lib.YMatrix_AddInAuxCurrents(SType)


def IVector():
    """Get access to the internal Current pointer"""
    IvectorPtr = ffi.new("double**")
    lib.YMatrix_getIpointer(IvectorPtr)
    return IvectorPtr[0]


def VVector():
    """Get access to the internal Voltage pointer"""
    VvectorPtr = ffi.new("double**")
    lib.YMatrix_getVpointer(VvectorPtr)
    return VvectorPtr[0]


def getI():
    """Get the data from the internal Current pointer"""
    IvectorPtr = IVector()
    return ffi.unpack(IvectorPtr, (NumNodes() + 1) * 2)


def getV():
    """Get the data from the internal Voltage pointer"""
    VvectorPtr = VVector()
    return ffi.unpack(VvectorPtr, (NumNodes() + 1) * 2)


def SolveSystem(NodeV):
    if type(NodeV) is not np.ndarray:
        NodeV = np.array(NodeV)

    NodeV = ffi.cast("double *", NodeV.ctypes.data)
    NodeVPtr = ffi.new("double**")
    NodeVPtr[0] = NodeV
    result = lib.YMatrix_SolveSystem(NodeVPtr)
    return result


def SystemYChanged(*args):
    # Getter
    if len(args) == 0:
        return lib.YMatrix_Get_SystemYChanged()

    # Setter
    value, = args
    lib.YMatrix_Set_SystemYChanged(value)
    CheckForError()


def UseAuxCurrents(*args):
    # Getter
    if len(args) == 0:
        return lib.YMatrix_Get_UseAuxCurrents()

    # Setter
    value, = args
    lib.YMatrix_Set_UseAuxCurrents(value)
    CheckForError()


_columns = []
__all__ = [
    "getYsparse",
    "getV",
    "getI",
    "ZeroInjCurr",
    "GetSourceInjCurrents",
    "GetPCInjCurr",
    "BuildYMatrixD",
    "AddInAuxCurrents",
    "IVector",
    "VVector",
    "SolveSystem",
    "SystemYChanged",
    "UseAuxCurrents",
]
