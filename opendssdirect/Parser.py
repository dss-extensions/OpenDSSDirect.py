from ._utils import api_util, Base, OPENDSSDIRECT_PY_USE_NUMPY


class IParser(Base):
    __slots__ = []
    __name__ = "Parser"
    _api_prefix = "Parser"
    _columns = [
        "Delimiters",
        "EndQuote",
        "CmdString",
        "BeginQuote",
        "WhiteSpace",
        "AutoIncrement",
    ]

    def Matrix(self, ExpectedOrder):
        """(read-only) Use this property to parse a Matrix token in OpenDSS format.  Returns square matrix of order specified. Order same as default Fortran order: column by column."""
        self.CheckForError(self._lib.Parser_Get_Matrix_GR(ExpectedOrder))
        return self._get_float64_gr_array()

    def SymMatrix(self, ExpectedOrder):
        """(read-only) Use this property to parse a matrix token specified in lower triangle form. Symmetry is forced."""
        self.CheckForError(self._lib.Parser_Get_SymMatrix_GR(ExpectedOrder))
        return self._get_float64_gr_array()

    def Vector(self, ExpectedSize):
        """(read-only) Returns token as array of doubles. For parsing quoted array syntax."""
        self.CheckForError(self._lib.Parser_Get_Vector_GR(ExpectedSize))
        return self._get_float64_gr_array()

    def ResetDelimiters(self):
        self.CheckForError(self._lib.Parser_ResetDelimiters())

    def AutoIncrement(self, *args):
        """Default is FALSE. If TRUE parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Parser_Get_AutoIncrement()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Parser_Set_AutoIncrement(Value))

    def BeginQuote(self, *args):
        """
        Get/Set String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Parser_Get_BeginQuote())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Parser_Set_BeginQuote(Value))

    def CmdString(self, *args):
        """String to be parsed. Loading this string resets the Parser to the beginning of the line. Then parse off the tokens in sequence."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Parser_Get_CmdString())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Parser_Set_CmdString(Value))

    def DblValue(self):
        """(read-only) Return next parameter as a double."""
        return self.CheckForError(self._lib.Parser_Get_DblValue())

    def Delimiters(self, *args):
        """String defining hard delimiters used to separate token on the command string. Default is , and =. The = separates token name from token value. These override whitesspace to separate tokens."""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Parser_Get_Delimiters())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Parser_Set_Delimiters(Value))

    def EndQuote(self, *args):
        """String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')]}"""
        # Getter
        if len(args) == 0:
            return self._get_string(self.CheckForError(self._lib.Parser_Get_EndQuote()))

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Parser_Set_EndQuote(Value))

    def IntValue(self):
        """(read-only) Return next parameter as a long integer."""
        return self.CheckForError(self._lib.Parser_Get_IntValue())

    def NextParam(self):
        """(read-only) Get next token and return tag name (before = sign) if any. See AutoIncrement."""
        return self._get_string(self.CheckForError(self._lib.Parser_Get_NextParam()))

    def StrValue(self):
        """(read-only) Return next parameter as a string"""
        return self._get_string(self.CheckForError(self._lib.Parser_Get_StrValue()))

    def WhiteSpace(self, *args):
        """
        Get/set the characters used for White space in the command string.  Default is blank and Tab.
        """
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.Parser_Get_WhiteSpace())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.Parser_Set_WhiteSpace(Value))


_Parser = IParser(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Matrix = _Parser.Matrix
SymMatrix = _Parser.SymMatrix
Vector = _Parser.Vector
ResetDelimiters = _Parser.ResetDelimiters
AutoIncrement = _Parser.AutoIncrement
BeginQuote = _Parser.BeginQuote
CmdString = _Parser.CmdString
DblValue = _Parser.DblValue
Delimiters = _Parser.Delimiters
EndQuote = _Parser.EndQuote
IntValue = _Parser.IntValue
NextParam = _Parser.NextParam
StrValue = _Parser.StrValue
WhiteSpace = _Parser.WhiteSpace
_columns = _Parser._columns
__all__ = [
    "Matrix",
    "SymMatrix",
    "Vector",
    "ResetDelimiters",
    "AutoIncrement",
    "BeginQuote",
    "CmdString",
    "DblValue",
    "Delimiters",
    "EndQuote",
    "IntValue",
    "NextParam",
    "StrValue",
    "WhiteSpace",
]
