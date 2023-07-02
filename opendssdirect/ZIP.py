from ._utils import api_util, Base


class IZIP(Base):
    __slots__ = []
    __name__ = "ZIP"
    _api_prefix = "ZIP"
    _columns = []

    _columns = []

    def Open(self, FileName):
        """
        Opens and prepares a ZIP file to be used by the DSS text parser.
        Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
        Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
        The limitations should be removed in a future revision.

        (API Extension)
        """
        if type(FileName) is not bytes:
            FileName = FileName.encode(self._api_util.codec)
        self.CheckForError(self._lib.ZIP_Open(FileName))

    def Close(self):
        """
        Closes the current open ZIP file

        (API Extension)
        """
        self.CheckForError(self._lib.ZIP_Close())

    def Redirect(self, FileInZip):
        """
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths. The only exceptions are
        memory-mapped files.

        (API Extension)
        """
        if type(FileInZip) is not bytes:
            FileName = FileInZip.encode(self._api_util.codec)
        self.CheckForError(self._lib.ZIP_Redirect(FileInZip))

    def Extract(self, FileName):
        """
        Extracts the contents of the file "FileName" from the current (open) ZIP file.
        Returns a byte-string.

        (API Extension)
        """
        api_util = self._api_util
        ptr = api_util.ffi.new("int8_t**")
        cnt = api_util.ffi.new("int32_t[4]")
        if type(FileName) is not bytes:
            FileName = FileName.encode(api_util.codec)
        self.CheckForError(self._lib.ZIP_Extract(ptr, cnt, FileName))
        result = bytes(api_util.ffi.buffer(ptr[0], cnt[0]))
        self._lib.DSS_Dispose_PByte(ptr)
        return result

    def List(self, regexp=None):
        """
        List of strings consisting of all names match the regular expression provided in regexp.
        If no expression is provided, all names in the current open ZIP are returned.

        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on
        the expression syntax and options.

        (API Extension)
        """
        if regexp is None or not regexp:
            regexp = self._api_util.ffi.NULL
        elif type(regexp) is not bytes:
            regexp = regexp.encode(self._api_util.codec)
        return self.CheckForError(self._get_string_array(self._lib.ZIP_List, regexp))

    def Contains(self, Name):
        """
        Check if the given path name is present in the current ZIP file.

        (API Extension)
        """
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)
        return self.CheckForError(self._lib.ZIP_Contains(Name)) != 0


_ZIP = IZIP(api_util)

# For backwards compatibility, bind to the default instance
Open = _ZIP.Open
Close = _ZIP.Close
Redirect = _ZIP.Redirect
Extract = _ZIP.Extract
List = _ZIP.List
Contains = _ZIP.Contains
_columns = _ZIP._columns
__all__ = ["Open", "Close", "Redirect", "Extract", "List", "Contains"]
