# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import (
    lib,
    codec,
    CheckForError,
    get_string,
    get_int32_array,
    get_string_array,
)


def BuildYMatrix(BuildOption, AllocateVI):
    CheckForError(lib.Solution_BuildYMatrix(BuildOption, AllocateVI))


def CheckControls():
    CheckForError(lib.Solution_CheckControls())


def CheckFaultStatus():
    CheckForError(lib.Solution_CheckFaultStatus())


def Cleanup():
    CheckForError(lib.Solution_Cleanup())


def DoControlActions():
    CheckForError(lib.Solution_DoControlActions())


def FinishTimeStep():
    CheckForError(lib.Solution_FinishTimeStep())


def InitSnap():
    CheckForError(lib.Solution_InitSnap())


def SampleControlDevices():
    CheckForError(lib.Solution_SampleControlDevices())


def SampleDoControlActions():
    CheckForError(lib.Solution_Sample_DoControlActions())


def Solve():
    CheckForError(lib.Solution_Solve())


def SolveDirect():
    CheckForError(lib.Solution_SolveDirect())


def SolveNoControl():
    CheckForError(lib.Solution_SolveNoControl())


def SolvePFlow():
    CheckForError(lib.Solution_SolvePflow())


def SolvePlusControl():
    CheckForError(lib.Solution_SolvePlusControl())


def SolveSnap():
    CheckForError(lib.Solution_SolveSnap())


def AddType(*args):
    """Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_AddType())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_AddType(Value))


def Algorithm(*args):
    """Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Algorithm())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Algorithm(Value))


def Capkvar(*args):
    """Capacitor kvar for adding capacitors in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Capkvar())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Capkvar(Value))


def ControlActionsDone(*args):
    """Flag indicating the control actions are done."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_ControlActionsDone()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_ControlActionsDone(Value))


def ControlIterations(*args):
    """Value of the control iteration counter"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_ControlIterations())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_ControlIterations(Value))


def ControlMode(*args):
    """{dssStatic* | dssEvent | dssTime}  Modes for control devices"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_ControlMode())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_ControlMode(Value))


def Converged(*args):
    """Flag to indicate whether the circuit solution converged"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Converged()) != 0

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Converged(Value))


def DefaultDaily(*args):
    """Default daily load shape (defaults to "Default")"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Solution_Get_DefaultDaily()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Solution_Set_DefaultDaily(Value))


def DefaultYearly(*args):
    """Default Yearly load shape (defaults to "Default")"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Solution_Get_DefaultYearly()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Solution_Set_DefaultYearly(Value))


def EventLog():
    """(read-only) Array of strings containing the Event Log"""
    return CheckForError(get_string_array(lib.Solution_Get_EventLog))


def Frequency(*args):
    """Set the Frequency for next solution"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Frequency())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Frequency(Value))


def GenMult(*args):
    """Default Multiplier applied to generators (like LoadMult)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_GenMult())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_GenMult(Value))


def GenPF(*args):
    """PF for generators in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_GenPF())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_GenPF(Value))


def GenkW(*args):
    """Generator kW for AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_GenkW())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_GenkW(Value))


def Hour(*args):
    """Set Hour for time series solutions."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Hour())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Hour(Value))


def IntervalHrs(*args):
    """
    Get/Set the Solution.IntervalHrs variable used for devices that integrate / custom solution algorithms
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_IntervalHrs())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_IntervalHrs(Value))


def Iterations():
    """(read-only) Number of iterations taken for last solution. (Same as TotalIterations)"""
    return CheckForError(lib.Solution_Get_Iterations())


def LDCurve(*args):
    """Load-Duration Curve name for LD modes"""
    # Getter
    if len(args) == 0:
        return get_string(CheckForError(lib.Solution_Get_LDCurve()))

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    CheckForError(lib.Solution_Set_LDCurve(Value))


def LoadModel(*args):
    """Load Model: {dssPowerFlow (default) | dssAdmittance}"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_LoadModel())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_LoadModel(Value))


def LoadMult(*args):
    """Default load multiplier applied to all non-fixed loads"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_LoadMult())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_LoadMult(Value))


def MaxControlIterations(*args):
    """Maximum allowable control iterations"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_MaxControlIterations())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_MaxControlIterations(Value))


def MaxIterations(*args):
    """Max allowable iterations."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_MaxIterations())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_MaxIterations(Value))


def MinIterations(*args):
    """Minimum number of iterations required for a power flow solution."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_MinIterations())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_MinIterations(Value))


def Mode(*args):
    """Set present solution mode (by a text code - see DSS Help)"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Mode())

    # Setter
    Mode, = args
    CheckForError(lib.Solution_Set_Mode(Mode))


def ModeID():
    """(read-only) ID (text) of the present solution mode"""
    return get_string(CheckForError(lib.Solution_Get_ModeID()))


def MostIterationsDone():
    """(read-only) Max number of iterations required to converge at any control iteration of the most recent solution."""
    return CheckForError(lib.Solution_Get_MostIterationsDone())


def Number(*args):
    """Number of solutions to perform for Monte Carlo and time series simulations"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Number())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Number(Value))


def ProcessTime():
    """(read-only) Gets the time required to perform the latest solution (Read only)"""
    return CheckForError(lib.Solution_Get_Process_Time())


def Random(*args):
    """Randomization mode for random variables "Gaussian" or "Uniform\""""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Random())

    # Setter
    Random, = args
    CheckForError(lib.Solution_Set_Random(Random))


def Seconds(*args):
    """Seconds from top of the hour."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Seconds())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Seconds(Value))


def StepSize(*args):
    """Time step size in sec"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_StepSize())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_StepSize(Value))


def SystemYChanged():
    """(read-only) Flag that indicates if elements of the System Y have been changed by recent activity."""
    return CheckForError(lib.Solution_Get_SystemYChanged()) != 0


def TimeTimeStep():
    """(read-only) Get the solution process time + sample time for time step"""
    return CheckForError(lib.Solution_Get_Time_of_Step())


def Convergence(*args):
    """Solution convergence tolerance."""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Tolerance())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Tolerance(Value))


def TotalTime(*args):
    """
    Gets/sets the accumulated time of the simulation
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Total_Time())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Total_Time(Value))


def TotalIterations():
    """(read-only) Total iterations including control iterations for most recent solution."""
    return CheckForError(lib.Solution_Get_Totaliterations())


def Year(*args):
    """Set year for planning studies"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_Year())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_Year(Value))


def DblHour(*args):
    """Hour as a double, including fractional part"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_dblHour())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_dblHour(Value))


def PctGrowth(*args):
    """Percent default  annual load growth rate"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Solution_Get_pctGrowth())

    # Setter
    Value, = args
    CheckForError(lib.Solution_Set_pctGrowth(Value))


def StepSizeHr(Value):
    """(write-only) Set Stepsize in Hr"""
    CheckForError(lib.Solution_Set_StepsizeHr(Value))


def StepSizeMin(Value):
    """(write-only) Set Stepsize in minutes"""
    CheckForError(lib.Solution_Set_StepsizeMin(Value))


def BusLevels():
    return get_int32_array(lib.Solution_Get_BusLevels)


def IncMatrix():
    return get_int32_array(lib.Solution_Get_IncMatrix)


def IncMatrixCols():
    return CheckForError(get_string_array(lib.Solution_Get_IncMatrixCols))


def IncMatrixRows():
    return CheckForError(get_string_array(lib.Solution_Get_IncMatrixRows))


def Laplacian():
    return get_int32_array(lib.Solution_Get_Laplacian)


_columns = [
    "AddType",
    "Algorithm",
    "Capkvar",
    "ControlActionsDone",
    "ControlIterations",
    "ControlMode",
    "Converged",
    "DefaultDaily",
    "DefaultYearly",
    "EventLog",
    "Frequency",
    "GenMult",
    "GenPF",
    "GenkW",
    "Hour",
    "IntervalHrs",
    "Iterations",
    "LDCurve",
    "LoadModel",
    "LoadMult",
    "MaxControlIterations",
    "MaxIterations",
    "MinIterations",
    "Mode",
    "ModeID",
    "MostIterationsDone",
    "Number",
    "ProcessTime",
    "Random",
    "Seconds",
    "StepSize",
    "SystemYChanged",
    "TimeTimeStep",
    "Convergence",
    "TotalTime",
    "TotalIterations",
    "Year",
    "DblHour",
    "PctGrowth",
]
__all__ = [
    "BuildYMatrix",
    "CheckControls",
    "CheckFaultStatus",
    "Cleanup",
    "DoControlActions",
    "FinishTimeStep",
    "InitSnap",
    "SampleControlDevices",
    "SampleDoControlActions",
    "Solve",
    "SolveDirect",
    "SolveNoControl",
    "SolvePFlow",
    "SolvePlusControl",
    "SolveSnap",
    "AddType",
    "Algorithm",
    "Capkvar",
    "ControlActionsDone",
    "ControlIterations",
    "ControlMode",
    "Converged",
    "DefaultDaily",
    "DefaultYearly",
    "EventLog",
    "Frequency",
    "GenMult",
    "GenPF",
    "GenkW",
    "Hour",
    "IntervalHrs",
    "Iterations",
    "LDCurve",
    "LoadModel",
    "LoadMult",
    "MaxControlIterations",
    "MaxIterations",
    "MinIterations",
    "Mode",
    "ModeID",
    "MostIterationsDone",
    "Number",
    "ProcessTime",
    "Random",
    "Seconds",
    "StepSize",
    "SystemYChanged",
    "TimeTimeStep",
    "Convergence",
    "TotalTime",
    "TotalIterations",
    "Year",
    "DblHour",
    "PctGrowth",
    "StepSizeHr",
    "StepSizeMin",
    "BusLevels",
    "IncMatrix",
    "IncMatrixCols",
    "IncMatrixRows",
    "Laplacian",
]
