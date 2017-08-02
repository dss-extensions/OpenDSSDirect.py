
Solution
========


.. automodule:: opendssdirect.Solution
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Solution.AddType

    The type of device to add in AutoAdd Mode: {dssGen (default)|dssCap}.Modifies the type of device to add in AutoAdd Mode: {dssGen (default)|dssCap}.

.. function:: opendssdirect.Solution.Algorithm

    The base solution algorithm: {dssNormalSolve | dssNewtonSolve}.Modifies the base solution algorithm: {dssNormalSolve | dssNewtonSolve}.

.. function:: opendssdirect.Solution.BuildYMatrix

    Forces building of the System Y matrix according to the argument: {1= series elements only | 2= Whole Y matrix}.

.. function:: opendssdirect.Solution.Capkvar

    The capacitor kvar for adding in AutoAdd mode.Set the capacitor kvar for adding in AutoAdd mode.

.. function:: opendssdirect.Solution.CheckControls

    Performs the normal process for sampling and executing Control Actions and Fault Status and rebuilds Y if necessary.

.. function:: opendssdirect.Solution.CheckFaultStatus

    Executes status check on all fault objects defined in the circuit. Returns 0.

.. function:: opendssdirect.Solution.Cleanup

    Update storage, invcontrol, etc., at end of time step.

.. function:: opendssdirect.Solution.ControlActionsDone

    Indicates that the control actions are done: {1 done, 0 not done}.Modifies the flag to indicate that the control actions are done: {1 done, 0 not done}.

.. function:: opendssdirect.Solution.ControlIterations

    The current value of the control iteration counter.Modifies the current value of the control iteration counter.

.. function:: opendssdirect.Solution.ControlMode

    The mode for control devices: {dssStatic (default) | dssEvent | dssTime}.Modifies the mode for control devices: {dssStatic (default) | dssEvent | dssTime}.

.. function:: opendssdirect.Solution.Converged

    Indicates whether the circuit solution converged (1 converged | 0 not converged).Modifies the converged flag (1 converged | 0 not converged).

.. function:: opendssdirect.Solution.Convergence

    The solution convergence tolerance.Set the solution convergence tolerance.

.. function:: opendssdirect.Solution.DblHour

    The hour as a double, including fractional part.Set the hour as a double, including fractional part.

.. function:: opendssdirect.Solution.DefaultDaily

    The default daily load shape (defaults to 'Default').Set the default daily load shape (defaults to 'Default').

.. function:: opendssdirect.Solution.DefaultYearly

    The default yearly load shape (defaults to 'Default').Set the default yearly load shape (defaults to 'Default').

.. function:: opendssdirect.Solution.DoControlActions

    Pops control actions off the control queue and dispatches to the proper control element.

.. function:: opendssdirect.Solution.EventLog

    Returns an array of strings containing the Event Log.

.. function:: opendssdirect.Solution.FinishTimeStep

    Call cleanup, sample Monitors, and increment time at end of time step.

.. function:: opendssdirect.Solution.Frequency

    The frequency for the next solution.Set the frequency for the next solution.

.. function:: opendssdirect.Solution.GenMult

    The default multiplier applied to generators (like LoadMult).Set the default multiplier applied to generators (like LoadMult).

.. function:: opendssdirect.Solution.GenPF

    The pf for generators in AutoAdd mode.Set the pf for generators in AutoAdd mode.

.. function:: opendssdirect.Solution.GenkW

    The generator kW for AutoAdd mode.Set the generator kW for AutoAdd mode.

.. function:: opendssdirect.Solution.Hour

    The present hour (See DSS help).Modifies the present hour (See DSS help).

.. function:: opendssdirect.Solution.InitSnap

    Initializes some variables for snap shot power flow. SolveSnap does this automatically.

.. function:: opendssdirect.Solution.Iterations

    Return the number of iterations taken for the last solution.

.. function:: opendssdirect.Solution.LDCurve

    The Load-Duration Curve name for LD modes.Set the Load-Duration Curve name for LD modes.

.. function:: opendssdirect.Solution.LoadModel

    The Load Model: {dssPowerFlow (default)|dssAdmittance}.Modifies the Load Model: {dssPowerFlow (default)|dssAdmittance}.

.. function:: opendssdirect.Solution.LoadMult

    The default load multiplier applied to all non-fixed loads.Set the default load multiplier applied to all non-fixed loads.

.. function:: opendssdirect.Solution.MaxControlIterations

    The maximum allowable control iterations.Modifies the maximum allowable control iterations.

.. function:: opendssdirect.Solution.MaxIterations

    The Maximum number of iterations used to solve the circuit.Modifies the Maximum number of iterations used to solve the circuit.

.. function:: opendssdirect.Solution.Mode

    The present solution mode (See DSS help).Modifies the present solution mode (See DSS help).

.. function:: opendssdirect.Solution.ModeID

    The ID (text) of the present solution mode.

.. function:: opendssdirect.Solution.MostIterationsDone

    The max number of iterations required to converge at any control iteration of the most recent solution.

.. function:: opendssdirect.Solution.Number

    The number of solutions to perform for MonteCarlo and time series simulations.Modifies the number of solutions to perform for MonteCarlo and time series simulations.

.. function:: opendssdirect.Solution.PctGrowth

    The percent default annual load growth rate.Set the percent default annual load growth rate.

.. function:: opendssdirect.Solution.ProcessTime

    The time required (microseconds) to perform the latest solution time step, this time does not includes the time required for sampling meters/monitors.

.. function:: opendssdirect.Solution.Random

    The randomization mode for random variables 'Gaussian' or 'Uniform'.Modifies the randomization mode for random variables 'Gaussian' or 'Uniform'.

.. function:: opendssdirect.Solution.SampleControlDevices

    Executes a sampling of all intrinsic control devices, which push control actions into the control queue.

.. function:: opendssdirect.Solution.SampleDoControlActions

    Sample controls and then process the control queue for present control mode and dispatch control actions. Returns 0.

.. function:: opendssdirect.Solution.Seconds

    The seconds from top of the hour.Set the seconds from top of the hour.

.. function:: opendssdirect.Solution.Solve

    Executes the solution for the present solution mode. Returns 0.

.. function:: opendssdirect.Solution.SolveDirect

    Executes a direct solution from the system Y matrix, ignoring compensation currents of loads, generators (includes Yprim only).

.. function:: opendssdirect.Solution.SolveNoControl

    Is similar to SolveSnap except no control actions are checked or executed.

.. function:: opendssdirect.Solution.SolvePFlow

    Solves using present power flow method. Iterative solution rather than direct solution.

.. function:: opendssdirect.Solution.SolvePlusControl

    Executes a power flow solution (SolveNoControl) plus executes a CheckControlActions that executes any pending control actions.

.. function:: opendssdirect.Solution.StepSize

    The step size for the next solution.Set the step size for the next solution.

.. function:: opendssdirect.Solution.StepSizeHr

    Set the step size in Hours.

.. function:: opendssdirect.Solution.StepSizeMin

    Set the step size in minutes.

.. function:: opendssdirect.Solution.SystemYChanged

    Indicates if elements of the System Y have been changed by recent activity. If changed returns 1; otherwise 0.

.. function:: opendssdirect.Solution.TimeTimeStep

    The time required (microseconds) to perform the latest solution time step including the time required for sampling meters/monitors

.. function:: opendssdirect.Solution.TotalIterations

    The total iterations including control iterations for most recent solution.

.. function:: opendssdirect.Solution.TotalTime

    Get the accumulated time required (microseconds) to perform the simulation.Set the accumulated time required (microseconds) to perform the simulation.

.. function:: opendssdirect.Solution.Year

    The present Year (See DSS help).Modifies the present Year (See DSS help).

