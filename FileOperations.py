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

    def __init__(self):
        pass

    def setFileOwner(self, sfile, user, group=-1):
        try:
            os.chown(sfile, getpwnam(user).pw_uid, getgrnam(group).gr_gid)
        except KeyError:
            print 'Can\'t access unix user and password database', sys.exc_info()[0]
            raise
        except OSError:
            print 'Can\'t change owner/group for target', sys.exc_info()[0]
            raise
 
    def setFilePerm(self, sfile, perm):
        try:
            os.chmod(sfile, perm)
        except OSError:
            print 'Can\'t change permissions for target', sys.exc_info()[0]
