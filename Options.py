import getopt

class Options():
    archiveDir = None
    dataDir = None
    user = None
    group = None
    configFile = None
    port = None

    def __init__(self, archiveDir, dataDir, user = 'postgres', group = 'postgres', configFile = ):
        this.archiveDir = archiveDir
        this.dataDir = dataDir
    

