#!/usr/bin/env python

import os
import sys
import shutil
import getopt
import prepare_database as pd
import logging
import subprocess
import socket
import smtplib
import time
import distutils.spawn as ds
from html import HTML
import database

#TODO one module with prepare_database

port = '5433'
version = '9.1'
Directory = None
BaseBackupArch = None
pgUser = 'postgres'
pgPass = 'postgres'
host = '127.0.0.1'
pgBin = 'pg_ctl'
statisticFileName = '/tmp/pgstat'
try:
    sender = os.getlogin() + '@' + socket.gethostname()
except OSError:
    sender = 'cron'
receivers = ['evg.selyavka@gmail.com','aladin@okko.tv','sburdakov@okko.tv']
mailServer = 'relay.spb.play.dc'


class Error(Exception):
   """Base class for other exceptions"""
   pass

class DirectoryNotExists(Error):
    """Raised when directory doesn't exists"""
    pass

class DirectoryPathIsNotAbs(Error):
    """Raised when directory path isn't absolute"""
    pass

def usage():
    print """%s, usage\n
              -h/--help - display this help\n
              <-a/--archive> - basebackup archive\n
              <-d/--directory> - directory where to restore\n
              [-u/--user] - postgresql user, default is postgres\n
              [-w/--password] - postgresql user password, default is postgres\n
              [-p/--port] - postgresql listen port, default is 5433\n
              [-v/--version] - postgres version, default is 9.1\n
              """ % os.path.abspath(__file__) 
    sys.exit(0)

def getAbsPath(version):
    path = ['/usr/lib/postgresql/' + version + '/bin/' + pgBin, '/usr/pgsql-' + version + '/bin']
    for p in path:
        if os.access(p, os.X_OK):
            return os.path.abspath(p)

def generateExecutable():
    global version
    global pgBin

    if version:
        if ds.find_executable(pgBin) is not None:
            return os.path.abspath(ds.find_executable(pgBin))
        else:
            return getAbsPath(version)
    else:
        return getAbsPath('9.1')

        
def getDatabases(user, passwd, host, port):
    ch = database.DB('postgres', user, passwd, host, port)
    logging.debug('ch: %s', ch)
    if ch.conn is not None:
        curr = ch.conn.cursor()
        curr.execute('SELECT datname FROM pg_database WHERE datname NOT IN (%s, %s, %s)', ('postgres', 'template0', 'template1'))
        databases = curr.fetchall()
        curr.close()
        del ch
        return databases
    else:
        logging.error('Can\'t connect to postgresql cluster due to timeout')
        return None
     

def getSampleStatistics(user, passwd, host, port):
    statistics = dict()
    bufDic = dict()
    databases = getDatabases(user, passwd, host, port)
    if databases is not None:
        query = '''WITH allTables AS (
      SELECT c.relname AS tablename
      FROM pg_catalog.pg_class c
      LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
      WHERE c.relkind IN (
      'r'
      ,''
      )
      AND n.nspname <> 'pg_catalog'
      AND n.nspname <> 'information_schema'
      AND n.nspname !~ '^pg_toast'
      AND pg_catalog.pg_table_is_visible(c.oid)
      ORDER BY tablename
      )
      SELECT relname
      ,n_live_tup
      FROM pg_stat_user_tables
      WHERE relname IN (
      SELECT tablename
      FROM allTables
      )
    '''

        for e in databases:
            for d in e:
                ch = database.DB(d, user, passwd, host, port)
                curr = ch.conn.cursor()
                curr.execute(query)
                bufDic[d] = curr.fetchall()
                logging.debug('Db statistics dict %s' % bufDic)
                statistics.update(bufDic)
                curr.close()
                del ch
        return statistics
    else:
        logging.error('Can\'t fetch list of existing databases for generate statistics')
        return None

def generateHTML(unionTablesSet, requestedTablesDict, readTablesDict, diffRequestedTableDict = None, diffReadTableDict = None):
    h = HTML()
    t = h.table(border='1', cellpadding='1', cellspacing='1', style='width: 500px;')
    r = t.tr
    r.td('Requested from Backup', colspan='3')
    r.td('Read from previous Backup', colspan='3')
    r.td('Difference', colspan='3')
    r = t.tr
    r.td('Database')
    r.td('Table')
    r.td('Live')
    r.td('Database')
    r.td('Table')
    r.td('Live')
    r.td('Count')
    for v in unionTablesSet:
        try:
            diff = requestedTablesDict[v] - readTablesDict[v]
        except KeyError:
            diff = 0
        r = t.tr
        r.td(v.split(":")[0])
        r.td(v.split(":")[1])
        r.td(str(requestedTablesDict[v]))
        r.td(v.split(":")[0])
        r.td(v.split(":")[1])
        r.td(str(readTablesDict[v]))
        if diff > 0:
            r.td(str(diff),bgcolor='green')
        elif diff < 0:
            r.td(str(diff),bgcolor='red')
        else:
            r.td(str(diff))
    if diffRequestedTableDict is not None and diffReadTableDict is None:
        for k in diffRequestedTableDict.keys():
            r = t.tr(bgcolor='red')
            r.td(k.split(":")[0])
            r.td(k.split(":")[1])
            r.td(str(diffRequestedTableDict[k]))
            r.td('Can''t find corresponding table in file', colspan='4')
    elif diffReadTableDict is not None and diffRequestedTableDict is None:
        for k in diffReadTableDict.keys():
            r = t.tr(bgcolor='red')
            r.td('Can''t find corresponding table in requested database', colspan='3')
            r.td(k.split(":")[0])
            r.td(k.split(":")[1])
            r.td(str(diffReadTableDict[k]))
            r.td(' ')
    elif diffReadTableDict is not None and diffRequestedTableDict is not None:
        for k in diffRequestedTableDict.keys():
            r = t.tr(bgcolor='red')
            r.td(k.split(":")[0])
            r.td(k.split(":")[1])
            r.td(str(diffRequestedTableDict[k]))
            r.td('Can''t find corresponding table in file', colspan='4')
        for k in diffReadTableDict.keys():
            r = t.tr(bgcolor='red')
            r.td('Can''t find corresponding table in requested database', colspan='3')
            r.td(k.split(":")[0])
            r.td(k.split(":")[1])
            r.td(str(diffReadTableDict[k]))
            r.td(' ')
    return str(t)
        

def sendEmail(sender, receivers, mailServer, html):
    message = '''From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: Database restore statistics
''' % (sender, ','.join(receivers))
    try:
        smtpObj = smtplib.SMTP(mailServer)
        smtpObj.sendmail(sender, receivers, message+html)
        logging.info('Successfully sent email')
    except SMTPException:
        logging.error('Error: unable to send email')
   
def compareStatistics(statistics, fileName, port):
    if statistics is None:
        return "<h1>Can't generate report, statistics is unavailable</h1>"
    firstTime = False
    requestedStatList = list()
    readStatList = list()
    result = ''

    try:
        f = open(fileName + "_" + port, 'r+')
        logging.debug('File %s successfully open' % (fileName + "_" + port))
    except IOError:
        firstTime = True
        try:
            f = open(fileName + "_" + port, 'w+')
            logging.debug('File %s successfully open in first time' % (fileName + "_" + port))
        except IOError:
            raise IOError, "Can't open file %s" % (fileName + "_" + port)

    for d in statistics.keys():
        for tables in statistics[d]:
                requestedStatList.append(d + ":" + tables[0] + ":" + str(tables[1]) + "\n")

    if firstTime:
        readStatList = requestedStatList
    else:
        readStatList = f.readlines()

    requestedTablesDict = dict()
    readTablesDict = dict()

    for s in requestedStatList:
        requestedTablesDict[s.split(":")[0] + ":" + s.split(":")[1]] = long(s.split(":")[2].replace("\n",""))

    for s in readStatList:
        readTablesDict[s.split(":")[0] + ":" + s.split(":")[1]] = long(s.split(":")[2].replace("\n",""))
    
    requestedTablesSet = set(requestedTablesDict.keys()) - set(readTablesDict.keys())
    readTablesDiffSet = set(readTablesDict.keys()) - set(requestedTablesDict.keys())
    unionTablesSet = set(readTablesDict.keys()) & set(requestedTablesDict.keys())

    if requestedTablesSet is not None and readTablesDiffSet is None:
        diffRequestedTableDict = dict()
        for e in requestedTablesSet:
            diffRequestedTableDict[e] = requestedTablesDict[e]

        result = generateHTML(unionTablesSet, requestedTablesDict, readTablesDict, diffRequestedTableDict)

    elif readTablesDiffSet is not None and requestedTablesSet is None:
        diffReadTableDict = dict()
        for e in readTablesDiffSet:
            diffReadTableDict[e] = readTablesDict[e]

        result = generateHTML(unionTablesSet, requestedTablesDict, readTablesDict, None, diffReadTableDict)

    elif requestedTablesSet is not None and readTablesDiffSet is not None:

        diffRequestedTableDict = dict()
        for e in requestedTablesSet:
            diffRequestedTableDict[e] = requestedTablesDict[e]
        diffReadTableDict = dict()

        for e in readTablesDiffSet:
            diffReadTableDict[e] = readTablesDict[e]

        result = generateHTML(unionTablesSet, requestedTablesDict, readTablesDict, diffRequestedTableDict, diffReadTableDict)

    else:
       result = generateHTML(unionTablesSet, requestedTablesDict, readTablesDict)

    f.seek(0,0)
    f.truncate()
    f.writelines(requestedStatList)
    f.close()
    return result

# TODO multi thread support

def analyzeDb(user, passwd, host, port):
    databases = getDatabases(user, passwd, host, port)
    logging.debug('Database list %s' % databases)
    if databases is not None:
        for e in databases:
            for d in e:
                ch = database.DB(d, user, passwd, host, port)
                curr = ch.conn.cursor()
                logging.debug('Perform ANALYZE on %s database' % d)
                curr.execute('ANALYZE')
                curr.close()
                del ch
    else:
        logging.error('Can\'t fetch list of existing databases in cluster for analyze execution')

def stopPostgres():
    global Directory

    FNULL = open(os.devnull, 'w')

    pgExecutable = generateExecutable()

    if os.path.exists(pgExecutable):
       try:
           subprocess.check_call([pgExecutable, 'stop', '-D', Directory, '-m', 'fast'], stdout=FNULL, stderr=subprocess.STDOUT)
           logging.info("Postmaster is stoped in directory %s" % Directory)
       except subprocess.CalledProcessError:
           logging.info("Postmaster already stoped in directory %s" % Directory)
       except Exception:
           raise
    else:
        raise OSError, 'File %s doesn\'t exists' % pgExecutable

def startPostgres():
    global Directory

    FNULL = open(os.devnull, 'w')

    pgExecutable = generateExecutable()

    if os.path.exists(pgExecutable):
       try:
           subprocess.check_call([pgExecutable, 'start', '-D', Directory], stdout=FNULL, stderr=subprocess.STDOUT)
           logging.info("Postmaster is started in directory %s" % Directory)
       except subprocess.CalledProcessError:
           logging.info("Postmaster can't start in directory %s, check postmaster log output" % Directory)
       except Exception:
           raise
    else:
        raise OSError, 'File %s doesn\'t exists' % pgExecutable

def createLinks(linkName):
    global Directory 
    dirs = os.listdir( Directory )
    flag = None
    if not os.path.exists(Directory + '/' + linkName):
        for file in dirs:
            if file.endswith('.simple'):
                try: 
                    flag = True
                    os.symlink(Directory + '/' + file, Directory + '/' + linkName)
                except:
                    raise
        if not flag:
            logging.info("Can't find autovacuum.conf.simple in %s" % Directory)    

def cleanupArgv(argvList, itemsList):
    for item in itemsList:
        if item in argvList:
            argvList.remove(item)
    return argvList

def checkDir(path):
    if os.path.exists(path):
        if os.path.isabs(path):
            pass
        else:
            raise DirectoryPathIsNotAbs, "Path %s isn\'t absolute" % path
    else:
        raise DirectoryNotExists, "Directory %s doesn't exists" % path

def mkDir(path):
    try:
        checkDir(path)
    except DirectoryPathIsNotAbs, e:
        raise DirectoryPathIsNotAbs, e
    except DirectoryNotExists:
        os.mkdir(path)

def rmDir(path):
    try:
        checkDir(path)
        shutil.rmtree(path)
    except DirectoryPathIsNotAbs, e:
        raise DirectoryPathIsNotAbs, e
    except DirectoryNotExists, e:
        mkDir(path)
        chmodDir(path)

def chmodDir(path, perm = 0700):
    try:
        checkDir(path)
        os.chmod(Directory, perm)
    except DirectoryPathIsNotAbs, e:
        raise DirectoryPathIsNotAbs, e
    except DirectoryNotExists, e:
        raise DirectoryNotExists, e 

def main(argv):
    global Directory
    global BaseBackupArch
    global port
    global version
    global pgUser
    global pgPass
   
    try:
        opts, args = getopt.getopt(argv,"h:a:d:u:w:p:v",["help=","archive=","directory=","user","password","port=","version="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if len(opts) == 0 or len(opts) == 1:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-a", "--archive"):
            BaseBackupArch = arg
        elif opt in ("-d", "--directory"):
            Directory = arg
        elif opt in ("-u", "--user"):
            pgUser = arg
        elif opt in ("-w", "--password"):
            pgPass = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-v", "--version"):
            version = arg
        else:
            assert False, "unhandled option"

    if Directory is None or BaseBackupArch is None:
        usage()

    stopPostgres()
    rmDir(Directory)
    mkDir(Directory)
    chmodDir(Directory)
    pd.main(cleanupArgv(argv, ["-v", "--version","-w", "--password", "-u", "--user"]))
    # createLinks('autovacuum.conf')
    startPostgres()
    analyzeDb(pgUser, pgPass, host, port)
    statStr = compareStatistics(getSampleStatistics(pgUser, pgPass, host, port), statisticFileName, port)
    sendEmail(sender, receivers, mailServer, statStr)

if __name__=='__main__':
    main(sys.argv[1:])
