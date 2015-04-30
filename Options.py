import getopt

class Options():
    archiveDir = None
    dataDir = None
    user = None
    group = None
    configFile = None
    port = None

    def __init__(self, archiveDir, dataDir, user = 'postgres', group = 'postgres', configFile = None):
        this.archiveDir = archiveDir
        this.dataDir = dataDir
        this.user = user
        this.group = group

        if configFile is None:
            if this.dataDir.endswith('/'):
                this.configFile = this.dataDir + 'postgresql.conf'
            else:
                this.configFile = this.dataDir + '/postgresql.conf'
        else:
            this.configFile = configFile
