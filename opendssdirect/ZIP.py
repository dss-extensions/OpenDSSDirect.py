from ._utils import api_util, OPENDSSDIRECT_PY_USE_NUMPY
from .Bases import Base

class IZIP(Base):
    __slots__ = []
    __name__ = "ZIP"
    _api_prefix = "ZIP"
    _columns = []

    def Open(self, FileName):
        """
        Opens and prepares a ZIP file to be used by the DSS text parser.
        Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
        Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
        The limitations should be removed in a future revision.

        **(API Extension)**
        """
        if not isinstance(FileName, bytes):
            FileName = FileName.encode(self._api_util.codec)
        self._check_for_error(self._lib.ZIP_Open(FileName))

    def Close(self):
        """
        Closes the current open ZIP file

        **(API Extension)**
        """
        self._check_for_error(self._lib.ZIP_Close())

    def Redirect(self, FileInZip):
        """
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths. The only exceptions are
        memory-mapped files.

        **(API Extension)**
        """
        if not isinstance(FileInZip, bytes):
            FileInZip = FileInZip.encode(self._api_util.codec)
        self._check_for_error(self._lib.ZIP_Redirect(FileInZip))

    def Extract(self, FileName):
        """
        Extracts the contents of the file "FileName" from the current (open) ZIP file.
        Returns a byte-string.

        **(API Extension)**
        """
        api_util = self._api_util
        if not isinstance(FileName, bytes):
            FileName = FileName.encode(api_util.codec)
        self._check_for_error(self._lib.ZIP_Extract_GR(FileName))
        ptr, cnt = api_util.gr_int8_pointers
        return bytes(api_util.ffi.buffer(ptr[0], cnt[0]))

    def List(self, regexp=None):
        """
        List of strings consisting of all names match the regular expression provided in regexp.
        If no expression is provided, all names in the current open ZIP are returned.

        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on
        the expression syntax and options.

        **(API Extension)**
        """
        if regexp is None or not regexp:
            regexp = self._api_util.ffi.NULL
        elif not isinstance(regexp, bytes):
            regexp = regexp.encode(self._api_util.codec)
        return self._check_for_error(self._get_string_array(self._lib.ZIP_List, regexp))

    def Contains(self, Name):
        """
        Check if the given path name is present in the current ZIP file.

        **(API Extension)**
        """
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)
        return self._check_for_error(self._lib.ZIP_Contains(Name)) != 0


_ZIP = IZIP(api_util, prefer_lists=not OPENDSSDIRECT_PY_USE_NUMPY)

# For backwards compatibility, bind to the default instance
Open = _ZIP.Open
Close = _ZIP.Close
Redirect = _ZIP.Redirect
Extract = _ZIP.Extract
List = _ZIP.List
Contains = _ZIP.Contains
_columns = _ZIP._columns
__all__ = ["Open", "Close", "Redirect", "Extract", "List", "Contains"]
