# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string_array


def ClearActions():
    lib.CtrlQueue_ClearActions()


def ClearQueue():
    lib.CtrlQueue_ClearQueue()


def Delete(ActionHandle):
    lib.CtrlQueue_Delete(ActionHandle)


def DoAllQueue():
    lib.CtrlQueue_DoAllQueue()


def Show():
    lib.CtrlQueue_Show()


def ActionCode():
    """(read-only) Code for the active action. Long integer code to tell the control device what to do"""
    return lib.CtrlQueue_Get_ActionCode()


def DeviceHandle():
    """(read-only) Handle (User defined) to device that must act on the pending action."""
    return lib.CtrlQueue_Get_DeviceHandle()


def NumActions():
    """(read-only) Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)"""
    return lib.CtrlQueue_Get_NumActions()


def PopAction():
    """(read-only) Pops next action off the action list and makes it the active action. Returns zero if none."""
    return lib.CtrlQueue_Get_PopAction()


def Queue():
    """(read-only) Array of strings containing the entire queue in CSV format"""
    return get_string_array(lib.CtrlQueue_Get_Queue)


def QueueSize():
    """(read-only) Number of items on the OpenDSS control Queue"""
    return lib.CtrlQueue_Get_QueueSize()


def Action(Param1):
    """(write-only) Set the active action by index"""
    lib.CtrlQueue_Set_Action(Param1)


_columns = ["ActionCode", "DeviceHandle", "NumActions", "Queue", "QueueSize"]
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
]
