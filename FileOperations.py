import os
import sys
from pwd import getpwnam 
from grp import getgrnam

class Error(Exception):
   """Base class for other exceptions"""
   pass

class DirectoryNotExists(Error):
    """Raised when directory doesn't exists"""
    pass

class DirectoryPathIsNotAbs(Error):
    """Raised when directory path isn't absolute"""
    pass

class DirectoryIsNotAccessible(Error):
    """Raise when directory isn't accessible"""
    pass

class FileOperations():
    """Common class for file operations"""

    dfile = None

    def __init__(self, dfile):
        self.dfile = dfile

    def setFileOwner(self, user='postgres', group='postgres'):
        try:
            os.chown(self.dfile, getpwnam(user).pw_uid, getgrnam(group).gr_gid)
        except KeyError:
            print 'Can\'t access unix user and password database', sys.exc_info()[0]
            raise
        except OSError:
            print 'Can\'t change owner/group for target', sys.exc_info()[0]
            raise
 
    def setFilePerm(self, perm=0700):
        try:
            os.chmod(self.dfile, perm)
        except OSError:
            print 'Can\'t change permissions for target', sys.exc_info()[0]
