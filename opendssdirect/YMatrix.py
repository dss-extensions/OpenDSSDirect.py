import numpy as np
from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base
from dss import SparseSolverOptions


class IYMatrix(Base):
    __slots__ = []

    __name__ = "YMatrix"
    _api_prefix = "YMatrix"
    _columns = []

    def getYsparse(self, factor=True):
        """Return as (data, indices, indptr) that can fed into `scipy.sparse.csc_matrix`"""
        ffi = self._api_util.ffi
        nBus = ffi.new("uint32_t*")
        nBus[0] = 0
        nNz = ffi.new("uint32_t*")
        nNz[0] = 0
        ColPtr = ffi.new("int32_t**")
        RowIdxPtr = ffi.new("int32_t**")
        cValsPtr = ffi.new("double**")
        self._lib.YMatrix_GetCompressedYMatrix(
            factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr
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
        self._lib.DSS_Dispose_PInteger(ColPtr)
        self._lib.DSS_Dispose_PInteger(RowIdxPtr)
        self._lib.DSS_Dispose_PDouble(cValsPtr)
        self._check_for_error()
        return res

    def ZeroInjCurr(self):
        self._check_for_error(self._lib.YMatrix_ZeroInjCurr())

    def GetSourceInjCurrents(self):
        self._check_for_error(self._lib.YMatrix_GetSourceInjCurrents())

    def GetPCInjCurr(self):
        self._check_for_error(self._lib.YMatrix_GetPCInjCurr())

    def BuildYMatrixD(self, BuildOps, AllocateVI):
        self._check_for_error(self._lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI))

    def AddInAuxCurrents(self, SType):
        self._check_for_error(self._lib.YMatrix_AddInAuxCurrents(SType))

    def IVector(self):
        """Get access to the internal Current pointer"""
        IvectorPtr = self._api_util.ffi.new("double**")
        self._check_for_error(self._lib.YMatrix_getIpointer(IvectorPtr))
        return IvectorPtr[0]

    def VVector(self):
        """Get access to the internal Voltage pointer"""
        VvectorPtr = self._api_util.ffi.new("double**")
        self._check_for_error(self._lib.YMatrix_getVpointer(VvectorPtr))
        return VvectorPtr[0]

    def SolveSystem(self, NodeV=None):
        if NodeV is not None and type(NodeV) is not np.ndarray:
            NodeV = np.array(NodeV)
        if NodeV is None:
            NodeVPtr = self._api_util.ffi.NULL
        else:
            NodeVPtr = self._api_util.ffi.cast("double *", NodeV.ctypes.data)
        result = self._check_for_error(self._lib.YMatrix_SolveSystem(NodeVPtr))
        return result

    def SystemYChanged(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.YMatrix_Get_SystemYChanged() != 0)

        # Setter
        (value,) = args
        self._check_for_error(self._lib.YMatrix_Set_SystemYChanged(value))

    def UseAuxCurrents(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.YMatrix_Get_UseAuxCurrents() != 0)

        # Setter
        (value,) = args
        self._check_for_error(self._lib.YMatrix_Set_UseAuxCurrents(value))

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
            IvectorPtr, 2 * self._check_for_error(self._lib.Circuit_Get_NumNodes() + 1)
        )

    def getV(self):
        """Get the data from the internal Voltage pointer"""
        VvectorPtr = self.VVector()
        return self._api_util.ffi.unpack(
            VvectorPtr, 2 * self._check_for_error(self._lib.Circuit_Get_NumNodes() + 1)
        )

    def CheckConvergence(self):
        return self._check_for_error(self._lib.YMatrix_CheckConvergence() != 0)

    def SetGeneratordQdV(self):
        self._check_for_error(self._lib.YMatrix_SetGeneratordQdV())

    def LoadsNeedUpdating(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.YMatrix_Get_LoadsNeedUpdating() != 0)

        # Setter
        (value,) = args
        self._check_for_error(self._lib.YMatrix_Set_LoadsNeedUpdating(value))

    def SolutionInitialized(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.YMatrix_Get_SolutionInitialized() != 0)

        # Setter
        (value,) = args
        self._check_for_error(self._lib.YMatrix_Set_SolutionInitialized(value))

    def Iteration(self, *args):
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.YMatrix_Get_Iteration())

        # Setter
        (value,) = args
        self._check_for_error(self._lib.YMatrix_Set_Iteration(value))


_YMatrix = IYMatrix(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
getYsparse = _YMatrix.getYsparse
getV = _YMatrix.getV
getI = _YMatrix.getI
ZeroInjCurr = _YMatrix.ZeroInjCurr
GetSourceInjCurrents = _YMatrix.GetSourceInjCurrents
GetPCInjCurr = _YMatrix.GetPCInjCurr
BuildYMatrixD = _YMatrix.BuildYMatrixD
AddInAuxCurrents = _YMatrix.AddInAuxCurrents
IVector = _YMatrix.IVector
VVector = _YMatrix.VVector
SolveSystem = _YMatrix.SolveSystem
SystemYChanged = _YMatrix.SystemYChanged
UseAuxCurrents = _YMatrix.UseAuxCurrents
SolverOptions = _YMatrix.SolverOptions
CheckConvergence = _YMatrix.CheckConvergence
SetGeneratordQdV = _YMatrix.SetGeneratordQdV
LoadsNeedUpdating = _YMatrix.LoadsNeedUpdating
SolutionInitialized = _YMatrix.SolutionInitialized
Iteration = _YMatrix.Iteration
_columns = _YMatrix._columns
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
    "SolverOptions",
    "CheckConvergence",
    "SetGeneratordQdV",
    "LoadsNeedUpdating",
    "SolutionInitialized",
    "Iteration",
]
