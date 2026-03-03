#!/usr/bin/env python3

"""Module for archive.legacy_ops.postgres.file_operations."""

import os
import sys
from grp import getgrnam
from pwd import getpwnam

class Error(Exception):
    """Base class for other exceptions."""

class DirectoryNotExists(Error):
    """Raised when directory doesn't exist."""

class DirectoryPathIsNotAbs(Error):
    """Raised when directory path isn't absolute."""

class DirectoryIsNotAccessible(Error):
    """Raised when directory isn't accessible."""

class FileOperations():
    """Common class for file operations"""

    dfile = None

    def __init__(self, dfile):
        self.dfile = dfile

    def setFileOwner(self, user='postgres', group='postgres'):
        try:
            os.chown(self.dfile, getpwnam(user).pw_uid, getgrnam(group).gr_gid)
        except KeyError:
            print("Can't access unix user and password database", sys.exc_info()[0])
            raise
        except OSError:
            print("Can't change owner/group for target", sys.exc_info()[0])
            raise

    def setFilePerm(self, perm=0o700):
        try:
            os.chmod(self.dfile, perm)
        except OSError:
            print("Can't change permissions for target", sys.exc_info()[0])
