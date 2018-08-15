# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def BuildYMatrix(BuildOption, AllocateVI):
    lib.Solution_BuildYMatrix(BuildOption, AllocateVI)


def CheckControls():
    lib.Solution_CheckControls()


def CheckFaultStatus():
    lib.Solution_CheckFaultStatus()


def Cleanup():
    lib.Solution_Cleanup()


def DoControlActions():
    lib.Solution_DoControlActions()


def FinishTimeStep():
    lib.Solution_FinishTimeStep()


def InitSnap():
    lib.Solution_InitSnap()


def SampleControlDevices():
    lib.Solution_SampleControlDevices()


def SampleDoControlActions():
    lib.Solution_Sample_DoControlActions()


def Solve():
    lib.Solution_Solve()


def SolveDirect():
    lib.Solution_SolveDirect()


def SolveNoControl():
    lib.Solution_SolveNoControl()


def SolvePFlow():
    lib.Solution_SolvePflow()


def SolvePlusControl():
    lib.Solution_SolvePlusControl()


def SolveSnap():
    lib.Solution_SolveSnap()


def AddType(*args):
    """Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_AddType()

    # Setter
    Value, = args
    lib.Solution_Set_AddType(Value)


def Algorithm(*args):
    """Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Algorithm()

    # Setter
    Value, = args
    lib.Solution_Set_Algorithm(Value)


def Capkvar(*args):
    """Capacitor kvar for adding capacitors in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Capkvar()

    # Setter
    Value, = args
    lib.Solution_Set_Capkvar(Value)


def ControlActionsDone(*args):
    """Flag indicating the control actions are done."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlActionsDone() != 0

    # Setter
    Value, = args
    lib.Solution_Set_ControlActionsDone(Value)


def ControlIterations(*args):
    """Value of the control iteration counter"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlIterations()

    # Setter
    Value, = args
    lib.Solution_Set_ControlIterations(Value)


def ControlMode(*args):
    """{dssStatic* | dssEvent | dssTime}  Modes for control devices"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_ControlMode()

    # Setter
    Value, = args
    lib.Solution_Set_ControlMode(Value)


def Converged(*args):
    """Flag to indicate whether the circuit solution converged"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Converged() != 0

    # Setter
    Value, = args
    lib.Solution_Set_Converged(Value)


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


def GenMult(*args):
    """Default Multiplier applied to generators (like LoadMult)"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenMult()

    # Setter
    Value, = args
    lib.Solution_Set_GenMult(Value)


def GenPF(*args):
    """PF for generators in AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenPF()

    # Setter
    Value, = args
    lib.Solution_Set_GenPF(Value)


def GenkW(*args):
    """Generator kW for AutoAdd mode"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_GenkW()

    # Setter
    Value, = args
    lib.Solution_Set_GenkW(Value)


def Hour(*args):
    """Set Hour for time series solutions."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Hour()

    # Setter
    Value, = args
    lib.Solution_Set_Hour(Value)


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


def LoadModel(*args):
    """Load Model: {dssPowerFlow (default) | dssAdmittance}"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_LoadModel()

    # Setter
    Value, = args
    lib.Solution_Set_LoadModel(Value)


def LoadMult(*args):
    """Default load multiplier applied to all non-fixed loads"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_LoadMult()

    # Setter
    Value, = args
    lib.Solution_Set_LoadMult(Value)


def MaxControlIterations(*args):
    """Maximum allowable control iterations"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MaxControlIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MaxControlIterations(Value)


def MaxIterations(*args):
    """Max allowable iterations."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MaxIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MaxIterations(Value)


def MinIterations(*args):
    """
    (read) Minimum number of iterations required for a power flow solution.
    (write) Mininum number of iterations required for a power flow solution.
    """
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_MinIterations()

    # Setter
    Value, = args
    lib.Solution_Set_MinIterations(Value)


def Mode(*args):
    """Set present solution mode (by a text code - see DSS Help)"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Mode()

    # Setter
    Mode, = args
    lib.Solution_Set_Mode(Mode)


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


def Seconds(*args):
    """Seconds from top of the hour."""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_Seconds()

    # Setter
    Value, = args
    lib.Solution_Set_Seconds(Value)


def StepSize(*args):
    """Time step size in sec"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_StepSize()

    # Setter
    Value, = args
    lib.Solution_Set_StepSize(Value)


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


def DblHour(*args):
    """Hour as a double, including fractional part"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_dblHour()

    # Setter
    Value, = args
    lib.Solution_Set_dblHour(Value)


def PctGrowth(*args):
    """Percent default  annual load growth rate"""
    # Getter
    if len(args) == 0:
        return lib.Solution_Get_pctGrowth()

    # Setter
    Value, = args
    lib.Solution_Set_pctGrowth(Value)


def StepSizeHr(Value):
    """(write-only) Set Stepsize in Hr"""
    lib.Solution_Set_StepsizeHr(Value)


def StepSizeMin(Value):
    """(write-only) Set Stepsize in minutes"""
    lib.Solution_Set_StepsizeMin(Value)


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
]
