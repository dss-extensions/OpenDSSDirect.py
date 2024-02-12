from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class ICtrlQueue(Base):
    __slots__ = []

    __name__ = "CtrlQueue"
    _api_prefix = "CtrlQueue"
    _columns = ["Queue", "DeviceHandle", "QueueSize", "ActionCode", "NumActions"]

    def ClearActions(self):
        """
        Clear all actions from the Control Proxy's Action List (they are popped off the list).

        Original COM help: https://opendss.epri.com/ClearActions.html
        """
        self._check_for_error(self._lib.CtrlQueue_ClearActions())

    def ClearQueue(self):
        """
        Clear the control queue.

        Original COM help: https://opendss.epri.com/ClearQueue.html
        """
        self._check_for_error(self._lib.CtrlQueue_ClearQueue())

    def Delete(self, ActionHandle):
        """
        Delete an Action from the DSS Control Queue by the handle that is returned when the action is added.

        (The Push function returns the handle.)

        Original COM help: https://opendss.epri.com/Delete.html
        """
        self._check_for_error(self._lib.CtrlQueue_Delete(ActionHandle))

    def DoAllQueue(self):
        """
        Execute all actions currently on the Control Queue.

        Side effect: clears the queue.

        Original COM help: https://opendss.epri.com/DoAllQueue.html
        """
        self._check_for_error(self._lib.CtrlQueue_DoAllQueue())

    def Show(self):
        """
        Export the queue to a CSV table and show it.

        Original COM help: https://opendss.epri.com/Show.html
        """
        self._check_for_error(self._lib.CtrlQueue_Show())

    def ActionCode(self):
        """
        Code for the active action. Integer code to tell the control device what to do.

        Use this to determine what the user-defined controls are supposed to do.
        It can be any 32-bit integer of the user's choosing and is the same value that the control pushed onto the control queue earlier.

        Original COM help: https://opendss.epri.com/ActionCode.html
        """
        return self._check_for_error(self._lib.CtrlQueue_Get_ActionCode())

    def DeviceHandle(self):
        """
        Handle (User defined) to device that must act on the pending action.

        The user-written code driving the interface may support more than one
        control element as necessary to perform the simulation. This handle is
        an index returned to the user program that lets the program know which
        control is to perform the active action.

        Original COM help: https://opendss.epri.com/DeviceHandle.html
        """
        return self._check_for_error(self._lib.CtrlQueue_Get_DeviceHandle())

    def NumActions(self):
        """
        Number of Actions on the current action list (that have been popped off the control queue by CheckControlActions)

        Original COM help: https://opendss.epri.com/NumActions.html
        """
        return self._check_for_error(self._lib.CtrlQueue_Get_NumActions())

    def Push(self, Hour, Seconds, ActionCode, DeviceHandle):
        """
        Push a control action onto the DSS control queue by time, action code, and device handle (user defined). Returns Control Queue handle.

        Original COM help: https://opendss.epri.com/Push.html
        """
        return self._check_for_error(
            self._lib.CtrlQueue_Push(Hour, Seconds, ActionCode, DeviceHandle)
        )

    def PopAction(self):
        """
        Pops next action off the action list and makes it the active action. Returns zero if none.

        Original COM help: https://opendss.epri.com/PopAction.html
        """
        return self._check_for_error(self._lib.CtrlQueue_Get_PopAction())

    def Queue(self):
        """
        Array of strings containing the entire queue in CSV format

        Original COM help: https://opendss.epri.com/Queue.html
        """
        return self._check_for_error(self._get_string_array(self._lib.CtrlQueue_Get_Queue))

    def QueueSize(self):
        """
        Number of items on the OpenDSS control Queue

        Original COM help: https://opendss.epri.com/QueueSize.html
        """
        return self._check_for_error(self._lib.CtrlQueue_Get_QueueSize())

    def Action(self, Param1):
        """
        (write-only) Set the active action by index

        Original COM help: https://opendss.epri.com/Action.html
        """
        self._check_for_error(self._lib.CtrlQueue_Set_Action(Param1))


_CtrlQueue = ICtrlQueue(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
ClearActions = _CtrlQueue.ClearActions
ClearQueue = _CtrlQueue.ClearQueue
Delete = _CtrlQueue.Delete
DoAllQueue = _CtrlQueue.DoAllQueue
Show = _CtrlQueue.Show
ActionCode = _CtrlQueue.ActionCode
DeviceHandle = _CtrlQueue.DeviceHandle
NumActions = _CtrlQueue.NumActions
PopAction = _CtrlQueue.PopAction
Queue = _CtrlQueue.Queue
QueueSize = _CtrlQueue.QueueSize
Action = _CtrlQueue.Action
Push = _CtrlQueue.Push
_columns = _CtrlQueue._columns
__all__ = [
    "ClearActions",
    "ClearQueue",
    "Delete",
    "DoAllQueue",
    "Show",
    "ActionCode",
    "DeviceHandle",
    "NumActions",
    "PopAction",
    "Queue",
    "QueueSize",
    "Action",
    "Push",
]
