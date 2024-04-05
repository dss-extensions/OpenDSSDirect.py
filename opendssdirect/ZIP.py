from ._utils import api_util
from .Bases import Base
from typing import List as List_

class IZIP(Base):
    __slots__ = []
    __name__ = "ZIP"
    _api_prefix = "ZIP"
    _columns = []

    """
    ZIP allows controlling the ZIP-compressed file functions from AltDSS/DSS C-API.

    It allows opening a ZIP file, and loading circuits directly from it, without requiring extracting the contents to files before reading.

    The implementation provides a specialization which allows more efficient access if the ZIP file is open and reused for many circuits. 
    Doing so reduces the overhead of the initial opening and indexing of the file contents.

    *Not available when using EPRI's OpenDSS distribution.*

    (**API Extension**)
    """

    def Open(self, FileName: str):
        """
        Opens and prepares a ZIP file to be used by the DSS text parser.
        Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
        Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
        The limitations should be removed in a future revision.

        **(API Extension)**
        """
        self._lib.ZIP_Open(FileName)

    def Close(self):
        """
        Closes the current open ZIP file

        **(API Extension)**
        """
        self._lib.ZIP_Close()

    def Redirect(self, FileInZip: str):
        """
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths. The only exceptions are
        memory-mapped files.

        **(API Extension)**
        """
        self._lib.ZIP_Redirect(FileInZip)

    def Extract(self, FileName: str) -> bytes:
        """
        Extracts the contents of the file "FileName" from the current (open) ZIP file.
        Returns a byte-string.

        **(API Extension)**
        """
        api_util = self._api_util
        if not isinstance(FileName, bytes):
            FileName = FileName.encode(api_util.codec)

        api_util.lib_unpatched.ZIP_Extract_GR(FileName)
        api_util._check_for_error()
        ptr, cnt = api_util.gr_int8_pointers
        return bytes(api_util.ffi.buffer(ptr[0], cnt[0]))


    def List(self, regexp: str="") -> List_[str]:
        """
        List of strings consisting of all names match the regular expression provided in regexp.
        If no expression is provided, all names in the current open ZIP are returned.

        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on
        the expression syntax and options.

        **(API Extension)**
        """
        if regexp is None or not regexp:
            regexp = b""

        return self._lib.ZIP_List(regexp)

    def Contains(self, Name: str) -> bool:
        """
        Check if the given path name is present in the current ZIP file.

        **(API Extension)**
        """
        return self._lib.ZIP_Contains(Name)


_ZIP = IZIP(api_util)

# For backwards compatibility, bind to the default instance
Close = _ZIP.Close
Contains = _ZIP.Contains
Extract = _ZIP.Extract
List = _ZIP.List
Open = _ZIP.Open
Redirect = _ZIP.Redirect
_columns = _ZIP._columns
__all__ = ["Close", "Contains", "Extract", "List", "Open", "Redirect"]
