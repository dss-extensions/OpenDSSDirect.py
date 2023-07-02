from ._utils import  api_util, Base


class IReduceCkt(Base):
    """Circuit Reduction interface"""

    __name__ = "ReduceCkt"
    _api_prefix = "ReduceCkt"
    _columns = []

    __slots__ = []

    def Zmag(self, *args):
        """Zmag (ohms) for Reduce Option for Z of short lines"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.ReduceCkt_Get_Zmag())

        # Setter
        Value, = args
        self.CheckForError(self._lib.ReduceCkt_Set_Zmag(Value))

    def KeepLoad(self, *args):
        """Keep load flag (T/F) for Reduction options that remove branches"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.ReduceCkt_Get_KeepLoad()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.ReduceCkt_Set_KeepLoad(bool(Value)))

    def EditString(self, *args):
        """Edit String for RemoveBranches functions"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.ReduceCkt_Get_EditString())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.ReduceCkt_Set_EditString(Value))

    def StartPDElement(self, *args):
        """Start element for Remove Branch function"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.ReduceCkt_Get_StartPDElement())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.ReduceCkt_Set_StartPDElement(Value))

    def EnergyMeter(self, *args):
        """Name of Energymeter to use for reduction"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.ReduceCkt_Get_EnergyMeter())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.ReduceCkt_Set_EnergyMeter(Value))

    def SaveCircuit(self, CktName):
        """
        Save present (reduced) circuit
        Filename is listed in the Text Result interface
        """
        if type(CktName) is not bytes:
            CktName = CktName.encode(self._api_util.codec)
        self.CheckForError(self._lib.ReduceCkt_SaveCircuit(CktName))

    def DoDefault(self):
        """Do Default Reduction algorithm"""
        self.CheckForError(self._lib.ReduceCkt_DoDefault())

    def DoShortLines(self):
        """Do ShortLines algorithm: Set Zmag first if you don't want the default"""
        self.CheckForError(self._lib.ReduceCkt_DoShortLines())

    def DoDangling(self):
        """Reduce Dangling Algorithm; branches with nothing connected"""
        self.CheckForError(self._lib.ReduceCkt_DoDangling())

    def DoLoopBreak(self):
        self.CheckForError(self._lib.ReduceCkt_DoLoopBreak())

    def DoParallelLines(self):
        self.CheckForError(self._lib.ReduceCkt_DoParallelLines())

    def DoSwitches(self):
        self.CheckForError(self._lib.ReduceCkt_DoSwitches())

    def Do1phLaterals(self):
        self.CheckForError(self._lib.ReduceCkt_Do1phLaterals())

    def DoBranchRemove(self):
        self.CheckForError(self._lib.ReduceCkt_DoBranchRemove())


_ReduceCkt = IReduceCkt(api_util)

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
