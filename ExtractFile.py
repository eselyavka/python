#!/usr/bin/env python

import os
import tarfile
import zipfile
import FileOperations

class ExtractFile():
    def __init__(self, path, toDirectory):
        if path.endswith('.zip'):
            opener, mode = zipfile.ZipFile, 'r'
        elif path.endswith('.tar.gz') or path.endswith('.tgz'):
            opener, mode = tarfile.open, 'r:gz'
        elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
            opener, mode = tarfile.open, 'r:bz2'
        else: 
            raise ValueError, 'Could not extract %s as no appropriate extractor is found' % path

        cwd = os.getcwd()
        if os.access(toDirectory, os.R_OK|os.W_OK):
            os.chdir(toDirectory)
            try:
                file = opener(path, mode)
                try: file.extractall()
                finally: file.close()
            finally:
                os.chdir(cwd)
        else:
            raise FileOperations.DirectoryIsNotAccessible, 'Can\'t access to %s' % toDirectory
