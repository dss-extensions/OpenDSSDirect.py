from ._utils import CheckForError, api_util, Base


class ICtrlQueue(Base):
    __slots__ = []
    __name__ = "CtrlQueue"
    _api_prefix = "CtrlQueue"
    _columns = ["Queue", "DeviceHandle", "QueueSize", "ActionCode", "NumActions"]

    def ClearActions(self):
        self.CheckForError(self._lib.CtrlQueue_ClearActions())

    def ClearQueue(self):
        self.CheckForError(self._lib.CtrlQueue_ClearQueue())

    def Delete(self, ActionHandle):
        self.CheckForError(self._lib.CtrlQueue_Delete(ActionHandle))

    def DoAllQueue(self):
        self.CheckForError(self._lib.CtrlQueue_DoAllQueue())

    def Show(self):
        self.CheckForError(self._lib.CtrlQueue_Show())

    def ActionCode(self):
        """(read-only) Code for the active action. Long integer code to tell the control device what to do"""
        return self.CheckForError(self._lib.CtrlQueue_Get_ActionCode())

    def DeviceHandle(self):
        """(read-only) Handle (User defined) to device that must act on the pending action."""
        return self.CheckForError(self._lib.CtrlQueue_Get_DeviceHandle())

    def NumActions(self):
        """(read-only) Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)"""
        return self.CheckForError(self._lib.CtrlQueue_Get_NumActions())

    def Push(self, Hour, Seconds, ActionCode, DeviceHandle):
        """Push a control action onto the DSS control queue by time, action code, and device handle (user defined). Returns Control Queue handle."""
        return self.CheckForError(
            self._lib.CtrlQueue_Push(Hour, Seconds, ActionCode, DeviceHandle)
        )

    def PopAction(self):
        """(read-only) Pops next action off the action list and makes it the active action. Returns zero if none."""
        return self.CheckForError(self._lib.CtrlQueue_Get_PopAction())

    def Queue(self):
        """(read-only) Array of strings containing the entire queue in CSV format"""
        return self.CheckForError(self._get_string_array(self._lib.CtrlQueue_Get_Queue))

    def QueueSize(self):
        """(read-only) Number of items on the OpenDSS control Queue"""
        return self.CheckForError(self._lib.CtrlQueue_Get_QueueSize())

    def Action(self, Param1):
        """(write-only) Set the active action by index"""
        self.CheckForError(self._lib.CtrlQueue_Set_Action(Param1))


_CtrlQueue = ICtrlQueue(api_util)

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
