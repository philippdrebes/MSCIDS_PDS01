
##########################################################
# a real world example for mulitple inheritance          #
#                                                        #
# https://docs.python.org/3/library/pathlib.html         #
#                                                        #
##########################################################

# Attention: Here you don't see all the code
# goto:      https://github.com/python/cpython/blob/3.9/Lib/pathlib.py

class PurePath( object ):
    """Base class for manipulating paths without I/O."""
    pass


class PurePosixPath( PurePath ):
    """PurePath subclass for non-Windows systems."""
    pass


class PureWindowsPath( PurePath ):
    """PurePath subclass for Windows systems."""
    pass


class Path( PurePath ):
    """PurePath subclass that can make system calls."""
    pass


class PosixPath( Path, PurePosixPath ):
    """Path subclass for non-Windows systems.
    On a POSIX system, instantiating a Path should return this object."""
    pass


class WindowsPath( Path, PureWindowsPath ):
    """Path subclass for Windows systems.
    On a Windows system, instantiating a Path should return this object."""
    pass
