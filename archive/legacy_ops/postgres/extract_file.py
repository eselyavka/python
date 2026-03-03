#!/usr/bin/env python3

"""Module for archive.legacy_ops.postgres.extract_file."""

import os
import tarfile
import zipfile

try:
    from . import file_operations
except ImportError:  # pragma: no cover
    import file_operations

class ExtractFile():
    def __init__(self, path, toDirectory):
        if path.endswith('.zip'):
            opener, mode = zipfile.ZipFile, 'r'
        elif path.endswith('.tar.gz') or path.endswith('.tgz'):
            opener, mode = tarfile.open, 'r:gz'
        elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
            opener, mode = tarfile.open, 'r:bz2'
        else:
            raise ValueError(f'Could not extract {path} as no appropriate extractor is found')

        cwd = os.getcwd()
        if os.access(toDirectory, os.R_OK | os.W_OK):
            os.chdir(toDirectory)
            try:
                archive_file = opener(path, mode)
                try:
                    archive_file.extractall()
                finally:
                    archive_file.close()
            finally:
                os.chdir(cwd)
        else:
            raise file_operations.DirectoryIsNotAccessible(f"Can't access to {toDirectory}")
