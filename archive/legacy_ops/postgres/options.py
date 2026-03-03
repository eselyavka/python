#!/usr/bin/env python3

"""Module for archive.legacy_ops.postgres.options."""

class Options():  # pylint: disable=too-many-arguments
    """Option container for restore preparation scripts."""

    archiveDir = None
    dataDir = None
    user = None
    group = None
    configFile = None
    port = None

    def __init__(self, archiveDir, dataDir, user='postgres', group='postgres', configFile=None):
        self.archiveDir = archiveDir
        self.dataDir = dataDir
        self.user = user
        self.group = group

        if configFile is None:
            if self.dataDir.endswith('/'):
                self.configFile = self.dataDir + 'postgresql.conf'
            else:
                self.configFile = self.dataDir + '/postgresql.conf'
        else:
            self.configFile = configFile
