from ._utils import lib, ffi, api_util, codec, CheckForError, get_string_array


def Open(FileName):
    """
    Opens and prepares a ZIP file to be used by the DSS text parser.
    Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
    Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
    The limitations should be removed in a future revision.

    (API Extension)
    """
    if type(FileName) is not bytes:
        FileName = FileName.encode(codec)
    CheckForError(lib.ZIP_Open(FileName))


def Close():
    """
    Closes the current open ZIP file

    (API Extension)
    """
    CheckForError(lib.ZIP_Close())


def Redirect(FileInZip):
    """
    Runs a "Redirect" command inside the current (open) ZIP file.
    In the current implementation, all files required by the script must
    be present inside the ZIP, using relative paths. The only exceptions are
    memory-mapped files.

    (API Extension)
    """
    if type(FileInZip) is not bytes:
        FileName = FileInZip.encode(codec)
    CheckForError(lib.ZIP_Redirect(FileInZip))


def Extract(FileName):
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
    CheckForError(lib.ZIP_Extract(ptr, cnt, FileName))
    result = bytes(api_util.ffi.buffer(ptr[0], cnt[0]))
    lib.DSS_Dispose_PByte(ptr)
    return result


def List(regexp=None):
    """
    List of strings consisting of all names match the regular expression provided in regexp.
    If no expression is provided, all names in the current open ZIP are returned.

    See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on
    the expression syntax and options.

    (API Extension)
    """
    if regexp is None or not regexp:
        regexp = ffi.NULL
    elif type(regexp) is not bytes:
        regexp = regexp.encode(codec)
    return CheckForError(get_string_array(lib.ZIP_List, regexp))


def Contains(Name):
    """
    Check if the given path name is present in the current ZIP file.

    (API Extension)
    """
    if type(Name) is not bytes:
        Name = Name.encode(codec)
    return CheckForError(lib.ZIP_Contains(Name)) != 0


_columns = []
__all__ = ["Open", "Close", "Redirect", "Extract", "List", "Contains"]
