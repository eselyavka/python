#!/usr/bin/env python

import os
import sys
import shutil
import getopt
import prepare_database as pd
import logging
import subprocess

#TODO one module with prepare_database

version = '9.1'
Directory = None

def usage():
    print """%s, usage\n
              -h/--help - display this help\n
              <-a/--archive> - basebackup archive\n
              <-d/--directory> - directory where to restore\n
              [-p/--port] - postgresql listen port, default is 5433\n
              [-v/--version] - postgres version, default is 9.1\n
              """ % os.path.abspath(__file__) 
    sys.exit(0)

def generateBinDir():
    global version

    if version: 
        return '/usr/pgsql-' + version + '/bin'
    else:
        return '/usr/pgsql-9.1/bin'
 
def getSampleStatistics(tablesList):
    pass

def analyzeDb(dbList):
    pass

def stopPostgres():
    FNULL = open(os.devnull, 'w')

    pgBinDir = generateBinDir()

    if os.path.exists(pgBinDir):
       try:
           subprocess.check_call([pgBinDir+'/'+'pg_ctl', 'stop', '-D', Directory, '-m', 'fast'], stdout=FNULL, stderr=subprocess.STDOUT)
           logging.info("Postmaster is stoped")
       except subprocess.CalledProcessError:
           logging.info("Postmaster already stoped")
       except Exception:
           raise
    else:
        raise OSError, 'Directory %s doesn\'t exists' % pgBinDir

def startPostgres():
    global Directory

    FNULL = open(os.devnull, 'w')

    pgBinDir = generateBinDir()

    if os.path.exists(pgBinDir):
       try:
           subprocess.check_call([pgBinDir+'/'+'pg_ctl', 'start', '-D', Directory], stdout=FNULL, stderr=subprocess.STDOUT)
           logging.info("Postmaster is started")
       except subprocess.CalledProcessError:
           logging.info("Postmaster can't start, check postmaster log output")
       except Exception:
           raise
    else:
        raise OSError, 'Directory %s doesn\'t exists' % pgBinDir

def createLinks(linkName):
    global Directory 
    dirs = os.listdir( Directory )
    if not os.path.exists(Directory + '/' + linkName):
        for file in dirs:
            if file.endswith('.simple'):
                try: 
                    print Directory + '/' + file
                    print Directory + '/' + linkName
                    os.symlink(Directory + '/' + file, Directory + '/' + linkName)
                except:
                    raise 
            else:
                logging.info("Can't find autovacuum.conf.simple or autovacuum.conf.peak in %s" % Directory)    

def cleanupArgv(argvList, itemsList):
    for item in itemsList:
        if item in argvList:
            argvList.remove(item)
    return argvList

def main(argv):
    global Directory
    global port
    global version
   
    try:
        opts, args = getopt.getopt(argv,"h:a:d:p:v",["help=","archive=","directory=","port=","version="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if len(opts) == 0 or len(opts) == 1:
        usage()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-a", "--archive"):
            BaseBackupArch = arg
        elif opt in ("-d", "--directory"):
            Directory = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-v", "--version"):
            version = arg
        else:
            assert False, "unhandled option"
    
    if os.path.exists(Directory):
        if os.path.isabs(Directory):
            try:
                stopPostgres()
                shutil.rmtree(Directory)
                os.mkdir(Directory)
                os.chmod(Directory, 0700)
                pass
            except:
                raise
        else:
            raise OSError, "Path %s isn\'t absolute" % Directory
    else:
        try:
            os.mkdir(Directory)
            os.chmod(Directory, 0700)
        except:
            raise

    pd.main(cleanupArgv(argv, ["-v", "--version"]))
    
    createLinks('autovacuum.conf')
   
    startPostgres()

if __name__=='__main__':
    main(sys.argv[1:])
