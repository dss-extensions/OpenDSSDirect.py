from ._utils import lib, CheckForError, get_int32_array


def CreateActor():
    CheckForError(lib.Parallel_CreateActor())


def Wait():
    CheckForError(lib.Parallel_Wait())


def ActiveActor(*args):
    """Gets/sets the ID of the Active Actor"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Parallel_Get_ActiveActor())

    # Setter
    Value, = args
    CheckForError(lib.Parallel_Set_ActiveActor(Value))


def ActiveParallel(*args):
    """
    (read) Sets ON/OFF (1/0) Parallel features of the Engine
    (write) Delivers if the Parallel features of the Engine are Active
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Parallel_Get_ActiveParallel())

    # Setter
    Value, = args
    CheckForError(lib.Parallel_Set_ActiveParallel(Value))


def ActorCPU(*args):
    """Gets/sets the CPU of the Active Actor"""
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Parallel_Get_ActorCPU())

    # Setter
    Value, = args
    CheckForError(lib.Parallel_Set_ActorCPU(Value))


def ActorProgress():
    """(read-only) Gets the progress of all existing actors in pct"""
    return get_int32_array(lib.Parallel_Get_ActorProgress)


def ActorStatus():
    """(read-only) Gets the status of each actor"""
    return get_int32_array(lib.Parallel_Get_ActorStatus)


def ConcatenateReports(*args):
    """
    Controls the ConcatenateReports option (1=enabled, 0=disabled)
    """
    # Getter
    if len(args) == 0:
        return CheckForError(lib.Parallel_Get_ConcatenateReports())

    # Setter
    Value, = args
    CheckForError(lib.Parallel_Set_ConcatenateReports(Value))


def NumCPUs():
    """(read-only) Delivers the number of CPUs on the current PC"""
    return CheckForError(lib.Parallel_Get_NumCPUs())


def NumCores():
    """(read-only) Delivers the number of Cores of the local PC"""
    return CheckForError(lib.Parallel_Get_NumCores())


def NumOfActors():
    """(read-only) Gets the number of Actors created"""
    return CheckForError(lib.Parallel_Get_NumOfActors())


_columns = []
__all__ = [
    "CreateActor",
    "Wait",
    "ActiveActor",
    "ActiveParallel",
    "ActorCPU",
    "ActorProgress",
    "ActorStatus",
    "ConcatenateReports",
    "NumCPUs",
    "NumCores",
    "NumOfActors",
]
