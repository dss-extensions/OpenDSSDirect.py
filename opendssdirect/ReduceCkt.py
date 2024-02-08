from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base


class IReduceCkt(Base):
    """Circuit Reduction interface"""

    __slots__ = []

    __name__ = "ReduceCkt"
    _api_prefix = "ReduceCkt"
    _columns = []


    def Zmag(self, *args):
        """
        Zmag (ohms) for Reduce Option for Z of short lines

        Original COM help: https://opendss.epri.com/Zmag.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.ReduceCkt_Get_Zmag())

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.ReduceCkt_Set_Zmag(Value))

    def KeepLoad(self, *args):
        """
        Keep load flag for Reduction options that remove branches

        Original COM help: https://opendss.epri.com/KeepLoad.html
        """
        # Getter
        if len(args) == 0:
            return self._check_for_error(self._lib.ReduceCkt_Get_KeepLoad()) != 0

        # Setter
        (Value,) = args
        self._check_for_error(self._lib.ReduceCkt_Set_KeepLoad(bool(Value)))

    def EditString(self, *args):
        """
        Edit String for RemoveBranches functions

        Original COM help: https://opendss.epri.com/EditString.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.ReduceCkt_Get_EditString())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.ReduceCkt_Set_EditString(Value))

    def StartPDElement(self, *args):
        """
        Start element for Remove Branch function

        Original COM help: https://opendss.epri.com/StartPDElement.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.ReduceCkt_Get_StartPDElement())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.ReduceCkt_Set_StartPDElement(Value))

    def EnergyMeter(self, *args):
        """
        Name of EnergyMeter to use for reduction

        Original COM help: https://opendss.epri.com/EnergyMeter1.html
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self._check_for_error(self._lib.ReduceCkt_Get_EnergyMeter())
            )

        # Setter
        (Value,) = args
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
        self._check_for_error(self._lib.ReduceCkt_Set_EnergyMeter(Value))

    def SaveCircuit(self, CktName):
        """
        Save present (reduced) circuit
        Filename is listed in the Text Result interface
        """
        if not isinstance(CktName, bytes):
            CktName = CktName.encode(self._api_util.codec)
        self._check_for_error(self._lib.ReduceCkt_SaveCircuit(CktName))

    def DoDefault(self):
        """
        Do Default Reduction algorithm

        Original COM help: https://opendss.epri.com/DoDefault.html
        """
        self._check_for_error(self._lib.ReduceCkt_DoDefault())

    def DoShortLines(self):
        """
        Do ShortLines algorithm: Set Zmag first if you don't want the default

        Original COM help: https://opendss.epri.com/DoShortLines.html
        """
        self._check_for_error(self._lib.ReduceCkt_DoShortLines())

    def DoDangling(self):
        """
        Reduce Dangling Algorithm; branches with nothing connected

        Original COM help: https://opendss.epri.com/DoDangling.html
        """
        self._check_for_error(self._lib.ReduceCkt_DoDangling())

    def DoLoopBreak(self):
        """
        Break (disable) all the loops found in the active circuit.

        Disables one of the Line objects at the head of a loop to force the circuit to be radial.
        """
        self._check_for_error(self._lib.ReduceCkt_DoLoopBreak())

    def DoParallelLines(self):
        """
        Merge all parallel lines found in the circuit to facilitate its reduction.
        """
        self._check_for_error(self._lib.ReduceCkt_DoParallelLines())

    def DoSwitches(self):
        """
        Merge Line objects in which the IsSwitch property is true with the down-line Line object.
        """
        self._check_for_error(self._lib.ReduceCkt_DoSwitches())

    def Do1phLaterals(self):
        """
        Remove all 1-phase laterals in the active EnergyMeter's zone.

        Loads and other shunt elements are moved to the parent 3-phase bus.
        """
        self._check_for_error(self._lib.ReduceCkt_Do1phLaterals())

    def DoBranchRemove(self):
        """
        Remove (disable) all branches down-line from the active PDElement.

        Circuit must have an EnergyMeter on this branch.
        If KeepLoad=Y (default), a new Load element is defined and kW, kvar are set to present power flow solution for the first element eliminated.
        The EditString is applied to each new Load element defined.
        """
        self._check_for_error(self._lib.ReduceCkt_DoBranchRemove())


_ReduceCkt = IReduceCkt(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Zmag = _ReduceCkt.Zmag
KeepLoad = _ReduceCkt.KeepLoad
EditString = _ReduceCkt.EditString
StartPDElement = _ReduceCkt.StartPDElement
EnergyMeter = _ReduceCkt.EnergyMeter
SaveCircuit = _ReduceCkt.SaveCircuit
DoDefault = _ReduceCkt.DoDefault
DoShortLines = _ReduceCkt.DoShortLines
DoDangling = _ReduceCkt.DoDangling
DoLoopBreak = _ReduceCkt.DoLoopBreak
DoParallelLines = _ReduceCkt.DoParallelLines
DoSwitches = _ReduceCkt.DoSwitches
Do1phLaterals = _ReduceCkt.Do1phLaterals
DoBranchRemove = _ReduceCkt.DoBranchRemove
_columns = _ReduceCkt._columns
__all__ = [
    "Zmag",
    "KeepLoad",
    "EditString",
    "StartPDElement",
    "EnergyMeter",
    "SaveCircuit",
    "DoDefault",
    "DoShortLines",
    "DoDangling",
    "DoLoopBreak",
    "DoParallelLines",
    "DoSwitches",
    "Do1phLaterals",
    "DoBranchRemove",
]
