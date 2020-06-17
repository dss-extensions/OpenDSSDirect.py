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
    lib.Solution_BuildYMatrix(BuildOption, AllocateVI)
    CheckForError()


def CheckControls():
    lib.Solution_CheckControls()
    CheckForError()


def CheckFaultStatus():
    lib.Solution_CheckFaultStatus()
    CheckForError()


def Cleanup():
    lib.Solution_Cleanup()
    CheckForError()


def DoControlActions():
    lib.Solution_DoControlActions()
    CheckForError()


def FinishTimeStep():
    lib.Solution_FinishTimeStep()
    CheckForError()


def InitSnap():
    lib.Solution_InitSnap()
    CheckForError()


def SampleControlDevices():
    lib.Solution_SampleControlDevices()
    CheckForError()


def SampleDoControlActions():
    lib.Solution_Sample_DoControlActions()
    CheckForError()


def Solve():
    lib.Solution_Solve()
    CheckForError()


def SolveDirect():
    lib.Solution_SolveDirect()
    CheckForError()


def SolveNoControl():
    lib.Solution_SolveNoControl()
    CheckForError()


def SolvePFlow():
    lib.Solution_SolvePflow()
    CheckForError()


def SolvePlusControl():
    lib.Solution_SolvePlusControl()
    CheckForError()


def SolveSnap():
    lib.Solution_SolveSnap()
    CheckForError()


def AddType(*args):
    """Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_AddType()

    # Setter
    Value, = args
    lib.Solution_Set_AddType(Value)
    CheckForError()


def Algorithm(*args):
    """Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Algorithm()

    # Setter
    Value, = args
    lib.Solution_Set_Algorithm(Value)
    CheckForError()


def Capkvar(*args):
    """Capacitor kvar for adding capacitors in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Capkvar()

    # Setter
    Value, = args
    lib.Solution_Set_Capkvar(Value)
    CheckForError()


def ControlActionsDone(*args):
    """Flag indicating the control actions are done."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlActionsDone() != 0

    # Setter
    Value, = args
    lib.Solution_Set_ControlActionsDone(Value)
    CheckForError()


def ControlIterations(*args):
    """Value of the control iteration counter"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlIterations()

    # Setter
    Value, = args
    lib.Solution_Set_ControlIterations(Value)
    CheckForError()


def ControlMode(*args):
    """{dssStatic* | dssEvent | dssTime}  Modes for control devices"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlMode()

    # Setter
    Value, = args
    lib.Solution_Set_ControlMode(Value)
    CheckForError()


def Converged(*args):
    """Flag to indicate whether the circuit solution converged"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Converged() != 0

    # Setter
    Value, = args
    lib.Solution_Set_Converged(Value)
    CheckForError()


def DefaultDaily(*args):
    """Default daily load shape (defaults to "Default")"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Solution_Get_DefaultDaily())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.Solution_Set_DefaultDaily(Value)
    CheckForError()


def DefaultYearly(*args):
    """Default Yearly load shape (defaults to "Default")"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Solution_Get_DefaultYearly())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.Solution_Set_DefaultYearly(Value)
    CheckForError()


def EventLog():
    """(read-only) Array of strings containing the Event Log"""
    return get_string_array(lib.Solution_Get_EventLog)


def Frequency(*args):
    """Set the Frequency for next solution"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Frequency()

    # Setter
    Value, = args
    lib.Solution_Set_Frequency(Value)
    CheckForError()


def GenMult(*args):
    """Default Multiplier applied to generators (like LoadMult)"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenMult()

    # Setter
    Value, = args
    lib.Solution_Set_GenMult(Value)
    CheckForError()


def GenPF(*args):
    """PF for generators in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenPF()

    # Setter
    Value, = args
    lib.Solution_Set_GenPF(Value)
    CheckForError()


def GenkW(*args):
    """Generator kW for AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenkW()

    # Setter
    Value, = args
    lib.Solution_Set_GenkW(Value)
    CheckForError()


def Hour(*args):
    """Set Hour for time series solutions."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Hour()

    # Setter
    Value, = args
    lib.Solution_Set_Hour(Value)
    CheckForError()


def IntervalHrs(*args):
    """
    (read) Get/Set the Solution.IntervalHrs variable used for devices that integrate
    (write) Get/Set the Solution.IntervalHrs variable for custom solution algorithms
    """
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_IntervalHrs()

    # Setter
    Value, = args
    lib.Solution_Set_IntervalHrs(Value)
    CheckForError()


def Iterations():
    """(read-only) Number of iterations taken for last solution. (Same as TotalIterations)"""
    return lib.Solution_Get_Iterations()


def LDCurve(*args):
    """Load-Duration Curve name for LD modes"""
    # Getter
    if len(args) == 0:
        return get_string(lib.Solution_Get_LDCurve())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)
    lib.Solution_Set_LDCurve(Value)
    CheckForError()


def LoadModel(*args):
    """Load Model: {dssPowerFlow (default) | dssAdmittance}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_LoadModel()

    # Setter
    Value, = args
    lib.Solution_Set_LoadModel(Value)
    CheckForError()


def LoadMult(*args):
    """Default load multiplier applied to all non-fixed loads"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_LoadMult()

    # Setter
    Value, = args
    lib.Solution_Set_LoadMult(Value)
    CheckForError()


def MaxControlIterations(*args):
    """Maximum allowable control iterations"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MaxControlIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MaxControlIterations(Value)
    CheckForError()


def MaxIterations(*args):
    """Max allowable iterations."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MaxIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MaxIterations(Value)
    CheckForError()


def MinIterations(*args):
    """Minimum number of iterations required for a power flow solution."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MinIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MinIterations(Value)
    CheckForError()


def Mode(*args):
    """Set present solution mode (by a text code - see DSS Help)"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Mode()

    # Setter
    Mode, = args
    lib.Solution_Set_Mode(Mode)
    CheckForError()


def ModeID():
    """(read-only) ID (text) of the present solution mode"""
    return get_string(lib.Solution_Get_ModeID())


def MostIterationsDone():
    """(read-only) Max number of iterations required to converge at any control iteration of the most recent solution."""
    return lib.Solution_Get_MostIterationsDone()


def Number(*args):
    """Number of solutions to perform for Monte Carlo and time series simulations"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Number()

    # Setter
    Value, = args
    lib.Solution_Set_Number(Value)
    CheckForError()


def ProcessTime():
    """(read-only) Gets the time required to perform the latest solution (Read only)"""
    return lib.Solution_Get_Process_Time()


def Random(*args):
    '''Randomization mode for random variables "Gaussian" or "Uniform"'''
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Random()

    # Setter
    Random, = args
    lib.Solution_Set_Random(Random)
    CheckForError()


def Seconds(*args):
    """Seconds from top of the hour."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Seconds()

    # Setter
    Value, = args
    lib.Solution_Set_Seconds(Value)
    CheckForError()


def StepSize(*args):
    """Time step size in sec"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_StepSize()

    # Setter
    Value, = args
    lib.Solution_Set_StepSize(Value)
    CheckForError()


def SystemYChanged():
    """(read-only) Flag that indicates if elements of the System Y have been changed by recent activity."""
    return lib.Solution_Get_SystemYChanged() != 0


def TimeTimeStep():
    """(read-only) Get the solution process time + sample time for time step"""
    return lib.Solution_Get_Time_of_Step()


def Convergence(*args):
    """Solution convergence tolerance."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Tolerance()

    # Setter
    Value, = args
    lib.Solution_Set_Tolerance(Value)
    CheckForError()


def TotalTime(*args):
    """
    (read) Gets the accumulated time of the simulation
    (write) Sets the Accumulated time of the simulation
    """
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Total_Time()

    # Setter
    Value, = args
    lib.Solution_Set_Total_Time(Value)
    CheckForError()


def TotalIterations():
    """(read-only) Total iterations including control iterations for most recent solution."""
    return lib.Solution_Get_Totaliterations()


def Year(*args):
    """Set year for planning studies"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Year()

    # Setter
    Value, = args
    lib.Solution_Set_Year(Value)
    CheckForError()


def DblHour(*args):
    """Hour as a double, including fractional part"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_dblHour()

    # Setter
    Value, = args
    lib.Solution_Set_dblHour(Value)
    CheckForError()


def PctGrowth(*args):
    """Percent default  annual load growth rate"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_pctGrowth()

    # Setter
    Value, = args
    lib.Solution_Set_pctGrowth(Value)
    CheckForError()


def StepSizeHr(Value):
    """(write-only) Set Stepsize in Hr"""
    lib.Solution_Set_StepsizeHr(Value)
    CheckForError()


def StepSizeMin(Value):
    """(write-only) Set Stepsize in minutes"""
    lib.Solution_Set_StepsizeMin(Value)
    CheckForError()


def BusLevels():
    return get_int32_array(lib.Solution_Get_BusLevels)


def IncMatrix():
    return get_int32_array(lib.Solution_Get_IncMatrix)


def IncMatrixCols():
    return get_string_array(lib.Solution_Get_IncMatrixCols)


def IncMatrixRows():
    return get_string_array(lib.Solution_Get_IncMatrixRows)


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
