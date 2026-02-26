import numpy as np
from ._utils import api_util
from .Bases import Base
from dss import SparseSolverOptions


class IYMatrix(Base):
    """
    YMatrix provides access to some lower-level solution aspects.

    Part of this class is ported from the original OpenDSSDirect.DLL back in 2017, but 
    part is new. Since this is not exposed in the official COM API, it is marked as an extension.

    (**API Extension**)
    """

    __slots__ = []

    __name__ = "YMatrix"
    _api_prefix = "YMatrix"
    _columns = []

    def getYsparse(self, factor=True):
        """
        Return as (data, indices, indptr) that can fed into `scipy.sparse.csc_matrix`
        """

        api_util = self._api_util
        ffi = api_util.ffi
        lib = api_util.lib_unpatched

        nBus = ffi.new("uint32_t*")
        nBus[0] = 0
        nNz = ffi.new("uint32_t*")
        nNz[0] = 0
        ColPtr = ffi.new("int32_t**")
        RowIdxPtr = ffi.new("int32_t**")
        cValsPtr = ffi.new("double**")
        lib.YMatrix_GetCompressedYMatrix(
            api_util.ctx, factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr
        )
        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.frombuffer(
                    ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=complex
                ).copy(),
                np.frombuffer(
                    ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32
                ).copy(),
                np.frombuffer(
                    ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32
                ).copy(),
            )
        lib.DSS_Dispose_PInteger(ColPtr)
        lib.DSS_Dispose_PInteger(RowIdxPtr)
        lib.DSS_Dispose_PDouble(cValsPtr)
        api_util._check_for_error()
        return res

    def ZeroInjCurr(self):
        self._lib.YMatrix_ZeroInjCurr()

    def GetSourceInjCurrents(self):
        self._lib.YMatrix_GetSourceInjCurrents()

    def GetPCInjCurr(self):
        self._lib.YMatrix_GetPCInjCurr()

    def BuildYMatrixD(self, BuildOps, AllocateVI):
        self._lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI)

    def AddInAuxCurrents(self, SType):
        self._lib.YMatrix_AddInAuxCurrents(SType)

    def IVector(self):
        """Get access to the internal Current pointer"""
        IvectorPtr = self._api_util.ffi.new("double**")
        self._lib.YMatrix_getIpointer(IvectorPtr)
        return IvectorPtr[0]

    def VVector(self):
        """Get access to the internal Voltage pointer"""
        VvectorPtr = self._api_util.ffi.new("double**")
        self._lib.YMatrix_getVpointer(VvectorPtr)
        return VvectorPtr[0]

    def SolveSystem(self, NodeV=None):
        if NodeV is not None and type(NodeV) is not np.ndarray:
            NodeV = np.array(NodeV)
        if NodeV is None:
            NodeVPtr = self._api_util.ffi.NULL
        else:
            NodeVPtr = self._api_util.ffi.cast("double *", NodeV.ctypes.data)

        return self._lib.YMatrix_SolveSystem(NodeVPtr)


    def SystemYChanged(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_SystemYChanged()

        # Setter
        (value,) = args
        self._lib.YMatrix_Set_SystemYChanged(value)

    def UseAuxCurrents(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_UseAuxCurrents()

        # Setter
        (value,) = args
        self._lib.YMatrix_Set_UseAuxCurrents(value)

    def SolverOptions(self, *args):
        """Sparse solver options. See the enumeration SparseSolverOptions"""
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_SolverOptions()

        # Setter
        (Value,) = args
        self._lib.YMatrix_Set_SolverOptions(Value)

    def getI(self):
        """Get the data from the internal Current pointer"""
        IvectorPtr = self.IVector()
        return self._api_util.ffi.unpack(
            IvectorPtr, 2 * (self._lib.Circuit_Get_NumNodes() + 1)
        )

    def getV(self):
        """Get the data from the internal Voltage pointer"""
        VvectorPtr = self.VVector()
        return self._api_util.ffi.unpack(
            VvectorPtr, 2 * (self._lib.Circuit_Get_NumNodes() + 1)
        )

    def CheckConvergence(self):
        return self._lib.YMatrix_CheckConvergence()

    def SetGeneratordQdV(self):
        self._lib.YMatrix_SetGeneratordQdV()

    def LoadsNeedUpdating(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_LoadsNeedUpdating()

        # Setter
        (value,) = args
        self._lib.YMatrix_Set_LoadsNeedUpdating(value)

    def SolutionInitialized(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_SolutionInitialized()

        # Setter
        (value,) = args
        self._lib.YMatrix_Set_SolutionInitialized(value)

    def Iteration(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.YMatrix_Get_Iteration()

        # Setter
        (value,) = args
        self._lib.YMatrix_Set_Iteration(value)


_YMatrix = IYMatrix(api_util)

# For backwards compatibility, bind to the default instance
AddInAuxCurrents = _YMatrix.AddInAuxCurrents
BuildYMatrixD = _YMatrix.BuildYMatrixD
CheckConvergence = _YMatrix.CheckConvergence
GetPCInjCurr = _YMatrix.GetPCInjCurr
GetSourceInjCurrents = _YMatrix.GetSourceInjCurrents
IVector = _YMatrix.IVector
Iteration = _YMatrix.Iteration
LoadsNeedUpdating = _YMatrix.LoadsNeedUpdating
SetGeneratordQdV = _YMatrix.SetGeneratordQdV
SolutionInitialized = _YMatrix.SolutionInitialized
SolveSystem = _YMatrix.SolveSystem
SolverOptions = _YMatrix.SolverOptions
SystemYChanged = _YMatrix.SystemYChanged
UseAuxCurrents = _YMatrix.UseAuxCurrents
VVector = _YMatrix.VVector
ZeroInjCurr = _YMatrix.ZeroInjCurr
getI = _YMatrix.getI
getV = _YMatrix.getV
getYsparse = _YMatrix.getYsparse
_columns = _YMatrix._columns
__all__ = [
    "AddInAuxCurrents",
    "BuildYMatrixD",
    "CheckConvergence",
    "GetPCInjCurr",
    "GetSourceInjCurrents",
    "IVector",
    "Iteration",
    "LoadsNeedUpdating",
    "SetGeneratordQdV",
    "SolutionInitialized",
    "SolveSystem",
    "SolverOptions",
    "SystemYChanged",
    "UseAuxCurrents",
    "VVector",
    "ZeroInjCurr",
    "getI",
    "getV",
    "getYsparse",
]
