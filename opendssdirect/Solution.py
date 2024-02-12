from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base
from dss import ControlModes, SolutionAlgorithms, SolveModes


class ISolution(Base):
    __slots__ = []

    __name__ = "Solution"
    _api_prefix = "Solution"
    _columns = [
        "MinIterations",
        "MaxIterations",
        "MaxControlIterations",
        "TotalIterations",
        "ControlIterations",
        "MostIterationsDone",
        "Number",
        "ProcessTime",
        "AddType",
        "GenkW",
        "DblHour",
        "Capkvar",
        "Seconds",
        "GenMult",
        "DefaultYearly",
        "IntervalHrs",
        "Converged",
        "ModeID",
        "TimeTimeStep",
        "TotalTime",
        "LoadModel",
        "EventLog",
        "Iterations",
        "GenPF",
        "Frequency",
        "LoadMult",
        "Random",
        "PctGrowth",
        "Year",
        "Algorithm",
        "Hour",
        "Convergence",
        "ControlMode",
        "LDCurve",
        "StepSize",
        "DefaultDaily",
        "ControlActionsDone",
        "Mode",
        "SystemYChanged",
    ]

    def BuildYMatrix(self, BuildOption, AllocateVI):
        self._check_for_error(self._lib.Solution_BuildYMatrix(BuildOption, AllocateVI))

    def CheckControls(self):
        self._check_for_error(self._lib.Solution_CheckControls())

    def CheckFaultStatus(self):
        self._check_for_error(self._lib.Solution_CheckFaultStatus())

    def Cleanup(self):
        self._check_for_error(self._lib.Solution_Cleanup())

    def DoControlActions(self):
        self._check_for_error(self._lib.Solution_DoControlActions())

    def FinishTimeStep(self):
        self._check_for_error(self._lib.Solution_FinishTimeStep())

    def InitSnap(self):
        self._check_for_error(self._lib.Solution_InitSnap())

    def SampleControlDevices(self):
        self._check_for_error(self._lib.Solution_SampleControlDevices())

    def SampleDoControlActions(self):
        self._check_for_error(self._lib.Solution_Sample_DoControlActions())

    def Solve(self):
        self._check_for_error(self._lib.Solution_Solve())

    def SolveDirect(self):
        self._check_for_error(self._lib.Solution_SolveDirect())

    def SolveNoControl(self):
        self._check_for_error(self._lib.Solution_SolveNoControl())

    def SolvePFlow(self):
        self._check_for_error(self._lib.Solution_SolvePflow())

    def SolvePlusControl(self):
        self._check_for_error(self._lib.Solution_SolvePlusControl())

    def SolveSnap(self):
        self._check_for_error(self._lib.Solution_SolveSnap())

    def AddType(self, *args):
        """
        Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}

        Original COM help: https://opendss.epri.com/AddType.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_AddType())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_AddType(Value))

    def Algorithm(self, *args):
        """
        Base Solution algorithm

        Original COM help: https://opendss.epri.com/Algorithm.html
        """
        # Getter
        if len(args) == 0:
            return SolutionAlgorithms(
                self._check_for_error(self._lib.Solution_Get_Algorithm())
            )

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Algorithm(Value))

    def Capkvar(self, *args):
        """
        Capacitor kvar for adding capacitors in AutoAdd mode

        Original COM help: https://opendss.epri.com/Capkvar.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Capkvar())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Capkvar(Value))

    def ControlActionsDone(self, *args):
        """
        Flag indicating the control actions are done.

        Original COM help: https://opendss.epri.com/ControlActionsDone.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_ControlActionsDone()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_ControlActionsDone(Value))

    def ControlIterations(self, *args):
        """
        Value of the control iteration counter

        Original COM help: https://opendss.epri.com/ControlIterations.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_ControlIterations())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_ControlIterations(Value))

    def ControlMode(self, *args):
        """
        Modes for control devices

        Original COM help: https://opendss.epri.com/ControlMode.html
        """
        # Getter
        if len(args) == 0:
            return ControlModes(
                self._check_for_error(self._lib.Solution_Get_ControlMode())
            )

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_ControlMode(Value))

    def Converged(self, *args):
        """
        Flag to indicate whether the circuit solution converged

        Original COM help: https://opendss.epri.com/Converged.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Converged()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Converged(Value))

    def DefaultDaily(self, *args):
        """
        Default daily load shape (defaults to "Default")

        Original COM help: https://opendss.epri.com/DefaultDaily.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Solution_Get_DefaultDaily())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Solution_Set_DefaultDaily(Value))

    def DefaultYearly(self, *args):
        """
        Default Yearly load shape (defaults to "Default")

        Original COM help: https://opendss.epri.com/DefaultYearly.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Solution_Get_DefaultYearly())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Solution_Set_DefaultYearly(Value))

    def EventLog(self):
        """
        Array of strings containing the Event Log

        Original COM help: https://opendss.epri.com/EventLog.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Solution_Get_EventLog)
        )

    def Frequency(self, *args):
        """
        Set the Frequency for next solution

        Original COM help: https://opendss.epri.com/Frequency1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Frequency())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Frequency(Value))

    def GenMult(self, *args):
        """
        Default Multiplier applied to generators (like LoadMult)

        Original COM help: https://opendss.epri.com/GenMult.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_GenMult())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_GenMult(Value))

    def GenPF(self, *args):
        """
        PF for generators in AutoAdd mode

        Original COM help: https://opendss.epri.com/GenPF.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_GenPF())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_GenPF(Value))

    def GenkW(self, *args):
        """
        Generator kW for AutoAdd mode

        Original COM help: https://opendss.epri.com/GenkW.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_GenkW())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_GenkW(Value))

    def Hour(self, *args):
        """
        Set Hour for time series solutions.

        Original COM help: https://opendss.epri.com/Hour.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Hour())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Hour(Value))

    def IntervalHrs(self, *args):
        """
        Get/Set the Solution.IntervalHrs variable used for devices that integrate / custom solution algorithms
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_IntervalHrs())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_IntervalHrs(Value))

    def Iterations(self):
        """
        Number of iterations taken for last solution. (Same as Totaliterations)

        Original COM help: https://opendss.epri.com/Iterations.html
        """
        return self._check_for_error(self._lib.Solution_Get_Iterations())

    def LDCurve(self, *args):
        """
        Load-Duration Curve name for LD modes

        Original COM help: https://opendss.epri.com/LDCurve.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.Solution_Get_LDCurve())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.Solution_Set_LDCurve(Value))

    def LoadModel(self, *args):
        """
        Load Model: {dssPowerFlow (default) | dssAdmittance}

        Original COM help: https://opendss.epri.com/LoadModel.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_LoadModel())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_LoadModel(Value))

    def LoadMult(self, *args):
        """
        Default load multiplier applied to all non-fixed loads

        Original COM help: https://opendss.epri.com/LoadMult.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_LoadMult())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_LoadMult(Value))

    def MaxControlIterations(self, *args):
        """
        Maximum allowable control iterations

        Original COM help: https://opendss.epri.com/MaxControlIterations.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_MaxControlIterations())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_MaxControlIterations(Value))

    def MaxIterations(self, *args):
        """
        Max allowable iterations.

        Original COM help: https://opendss.epri.com/MaxIterations.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_MaxIterations())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_MaxIterations(Value))

    def MinIterations(self, *args):
        """
        Minimum number of iterations required for a power flow solution.

        Original COM help: https://opendss.epri.com/MinIterations.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_MinIterations())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_MinIterations(Value))

    def Mode(self, *args):
        """
        Set present solution mode

        Original COM help: https://opendss.epri.com/Mode2.html
        """
        # Getter
        if len(args) == 0:
            return SolveModes(self._check_for_error(self._lib.Solution_Get_Mode()))

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Mode(Value))

    def ModeID(self):
        """
        ID (text) of the present solution mode

        Original COM help: https://opendss.epri.com/ModeID.html
        """
        return self._get_string(self._check_for_error(self._lib.Solution_Get_ModeID()))

    def MostIterationsDone(self):
        """
        Max number of iterations required to converge at any control iteration of the most recent solution.

        Original COM help: https://opendss.epri.com/MostIterationsDone.html
        """
        return self._check_for_error(self._lib.Solution_Get_MostIterationsDone())

    def Number(self, *args):
        """
        Number of solutions to perform for Monte Carlo and time series simulations

        Original COM help: https://opendss.epri.com/Number1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Number())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Number(Value))

    def ProcessTime(self):
        """
        Gets the time required to perform the latest solution (Read only)

        Original COM help: https://opendss.epri.com/Process_Time.html
        """
        return self._check_for_error(self._lib.Solution_Get_Process_Time())

    def Random(self, *args):
        """
        Randomization mode for random variables "Gaussian" or "Uniform"

        Original COM help: https://opendss.epri.com/Random.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Random())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Random(Value))

    def Seconds(self, *args):
        """
        Seconds from top of the hour.

        Original COM help: https://opendss.epri.com/Seconds.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Seconds())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Seconds(Value))

    def StepSize(self, *args):
        """
        Time step size in sec

        Original COM help: https://opendss.epri.com/StepSize.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_StepSize())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_StepSize(Value))

    def SystemYChanged(self):
        """
        Flag that indicates if elements of the System Y have been changed by recent activity.

        Original COM help: https://opendss.epri.com/SystemYChanged.html
        """
        return self._check_for_error(self._lib.Solution_Get_SystemYChanged() != 0)

    def TimeTimeStep(self):
        """
        Get the solution process time + sample time for time step

        Original COM help: https://opendss.epri.com/Time_of_Step.html
        """
        return self._check_for_error(self._lib.Solution_Get_Time_of_Step())

    def Convergence(self, *args):
        """
        Solution convergence tolerance.

        Original COM help: https://opendss.epri.com/Tolerance.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Tolerance())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Tolerance(Value))

    def TotalTime(self, *args):
        """
        Gets/sets the accumulated time of the simulation

        This accumulator has to be reset manually.

        Original COM help: https://opendss.epri.com/Total_Time.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Total_Time())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Total_Time(Value))

    def TotalIterations(self):
        """
        Total iterations including control iterations for most recent solution.

        Original COM help: https://opendss.epri.com/Totaliterations.html
        """
        return self._check_for_error(self._lib.Solution_Get_Totaliterations())

    def Year(self, *args):
        """
        Set year for planning studies

        Original COM help: https://opendss.epri.com/Year.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_Year())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_Year(Value))

    def DblHour(self, *args):
        """
        Hour as a double, including fractional part

        Original COM help: https://opendss.epri.com/dblHour1.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_dblHour())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_dblHour(Value))

    def PctGrowth(self, *args):
        """
        Percent default  annual load growth rate

        Original COM help: https://opendss.epri.com/pctGrowth.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.Solution_Get_pctGrowth())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.Solution_Set_pctGrowth(Value))

    def StepSizeHr(self, Value):
        """(write-only) Set Stepsize in Hr"""
        self._check_for_error(self._lib.Solution_Set_StepsizeHr(Value))

    def StepSizeMin(self, Value):
        """(write-only) Set Stepsize in minutes"""
        self._check_for_error(self._lib.Solution_Set_StepsizeMin(Value))

    def BusLevels(self):
        """
        Bus levels for all the buses in the model.

        The bus levels are calculated after calculating the incidence branch-to-node (B2N)
        matrix and they represent the distance from the buses to a reference that goes from
        the feeder head to the farthest bus in the model. The bus level index matches with
        the bus list obtained with the circuit interface.

        Original COM help: https://opendss.epri.com/BusLevels.html
        """
        self._check_for_error(self._lib.Solution_Get_BusLevels_GR())
        return self._get_int32_gr_array()

    def IncMatrix(self):
        """
        Incidence branch-to-node (B2N) matrix calculated for the model as a vector of integers.

        The vector represents a sparse matrix (non-zero values are the only ones delivered) and
        can be interpreted as follows: The first element is the row number, the second one is
        the column and the third is the value, this way, by dividing the number of elements
        in the array by 3 the user can obtain the number of rows in case of wanting to sort
        the vector values within a matrix.

        Original COM help: https://opendss.epri.com/IncMatrix.html
        """
        self._check_for_error(self._lib.Solution_Get_IncMatrix_GR())
        return self._get_int32_gr_array()

    def IncMatrixCols(self):
        """
        Names of the columns of the branch-to-node (B2N) matrix.

        Original COM help: https://opendss.epri.com/IncMatrixCols.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Solution_Get_IncMatrixCols)
        )

    def IncMatrixRows(self):
        """
        Names of the rows of the branch-to-node (B2N) matrix.

        Original COM help: https://opendss.epri.com/IncMatrixRows.html
        """
        return self._check_for_error(
            self._get_string_array(self._lib.Solution_Get_IncMatrixRows)
        )

    def Laplacian(self):
        """
        Laplacian matrix calculated in OpenDSS based on the latest branch-to-node (B2N) matrix.

        The vector represents a sparse matrix (non-zero values are the only ones delivered) and
        can be interpreted as follows: The first element is the row number, the second one is
        the column and the third is the value, this way, by dividing the number of elements
        in the array by 3 the user can obtain the number of rows in case of wanting to sort
        the vector values within a matrix. The tables for the columns and rows are the same
        as the columns for the B2N columns (square matrix).

        Original COM help: https://opendss.epri.com/Laplacian.html
        """
        self._check_for_error(self._lib.Solution_Get_Laplacian_GR())
        return self._get_int32_gr_array()


_Solution = ISolution(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
BuildYMatrix = _Solution.BuildYMatrix
CheckControls = _Solution.CheckControls
CheckFaultStatus = _Solution.CheckFaultStatus
Cleanup = _Solution.Cleanup
DoControlActions = _Solution.DoControlActions
FinishTimeStep = _Solution.FinishTimeStep
InitSnap = _Solution.InitSnap
SampleControlDevices = _Solution.SampleControlDevices
SampleDoControlActions = _Solution.SampleDoControlActions
Solve = _Solution.Solve
SolveDirect = _Solution.SolveDirect
SolveNoControl = _Solution.SolveNoControl
SolvePFlow = _Solution.SolvePFlow
SolvePlusControl = _Solution.SolvePlusControl
SolveSnap = _Solution.SolveSnap
AddType = _Solution.AddType
Algorithm = _Solution.Algorithm
Capkvar = _Solution.Capkvar
ControlActionsDone = _Solution.ControlActionsDone
ControlIterations = _Solution.ControlIterations
ControlMode = _Solution.ControlMode
Converged = _Solution.Converged
DefaultDaily = _Solution.DefaultDaily
DefaultYearly = _Solution.DefaultYearly
EventLog = _Solution.EventLog
Frequency = _Solution.Frequency
GenMult = _Solution.GenMult
GenPF = _Solution.GenPF
GenkW = _Solution.GenkW
Hour = _Solution.Hour
IntervalHrs = _Solution.IntervalHrs
Iterations = _Solution.Iterations
LDCurve = _Solution.LDCurve
LoadModel = _Solution.LoadModel
LoadMult = _Solution.LoadMult
MaxControlIterations = _Solution.MaxControlIterations
MaxIterations = _Solution.MaxIterations
MinIterations = _Solution.MinIterations
Mode = _Solution.Mode
ModeID = _Solution.ModeID
MostIterationsDone = _Solution.MostIterationsDone
Number = _Solution.Number
ProcessTime = _Solution.ProcessTime
Random = _Solution.Random
Seconds = _Solution.Seconds
StepSize = _Solution.StepSize
SystemYChanged = _Solution.SystemYChanged
TimeTimeStep = _Solution.TimeTimeStep
Convergence = _Solution.Convergence
TotalTime = _Solution.TotalTime
TotalIterations = _Solution.TotalIterations
Year = _Solution.Year
DblHour = _Solution.DblHour
PctGrowth = _Solution.PctGrowth
StepSizeHr = _Solution.StepSizeHr
StepSizeMin = _Solution.StepSizeMin
BusLevels = _Solution.BusLevels
IncMatrix = _Solution.IncMatrix
IncMatrixCols = _Solution.IncMatrixCols
IncMatrixRows = _Solution.IncMatrixRows
Laplacian = _Solution.Laplacian
_columns = _Solution._columns
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
