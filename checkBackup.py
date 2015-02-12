#!/usr/bin/env python

import os
import sys
import shutil
import getopt
import prepare_database as pd
import logging
import subprocess
import psycopg2
import socket
import smtplib

#TODO one module with prepare_database

port = "5433"
version = "9.1"
Directory = None
BaseBackupArch = None
pgUser = "postgres"
pgPass = "postgres"
host = "127.0.0.1"
statisticFileName = "/tmp/pgstat"
sender = os.getlogin() + "@" + socket.gethostname()
receivers = ["user@example.com"]
mailServer = "relay@example.com"


class Error(Exception):
   """Base class for other exceptions"""
   pass

class DirectoryNotExists(Error):
    """Raised when directory doesn't exists"""
    pass

class DirectoryPathIsNotAbs(Error):
    """Raised when directory path isn't absolute"""
    pass

class db():
    conn = None
    def __init__(self, database, user, password, host, port):
        try:
            self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        except:
            raise RuntimeError, "Unable connect to database %s" % database

    def __del__(self):
        if self.conn:
            self.conn.close()

def usage():
    print """%s, usage\n
              -h/--help - display this help\n
              <-a/--archive> - basebackup archive\n
              <-d/--directory> - directory where to restore\n
              [-u/--user] - postgresql user, default is postgres\n
              [-p/--password] - postgresql user password, default is postgres\n
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

        
def getDatabases(user, passwd, host, port):
    conn = db("postgres", user, passwd, host, port)
    curr = conn.conn.cursor()
    curr.execute("SELECT datname FROM pg_database WHERE datname NOT IN (%s, %s, %s)", ('postgres', 'template0', 'template1'))
    databases = curr.fetchall()
    curr.close()
    del conn
    return databases

def getSampleStatistics(user, passwd, host, port):
    statistics = dict()
    bufDic = dict()
    databases = getDatabases(user, passwd, host, port)
    query = """WITH allTables AS (
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
"""

    for e in databases:
        for d in e:
            conn = db(d, user, passwd, host, port)
            curr = conn.conn.cursor()
            curr.execute(query)
            bufDic[d] = curr.fetchall()
            statistics.update(bufDic)
            curr.close()
            del conn
    return statistics

def generateHTML(requestedTablesDict, readTablesDict, diffRequestedTableDict = None, diffReadTableDict = None):
    concateStr = """<table border='1' cellpadding="1" cellspacing="1" style="width: 500px;">
<tbody>
<tr>
<td colspan="3">Requested from Backup</td>
<td colspan="3">Read from previous Backup</td>
<td colspan="3">Difference</td>
</tr>
<tr>
<td>Database</td>
<td>Table</td>
<td>Live tuple</td>
<td>Database</td>
<td>Table</td>
<td>Live tuple</td>
<td>Count</td>
</tr>"""

    for v in requestedTablesDict.keys():
        concateStr += "<tr>"
        try:
            diff = requestedTablesDict[v] - readTablesDict[v]
        except KeyError:
            diff = 0
        if diff < 0:
            diffStr = "<td bgcolor=\"red\">" + str(diff) + "</td>"
        elif diff > 0:
            diffStr = "<td bgcolor=\"green\">" + str(diff) + "</td>"
        else:
            diffStr = "<td>" + str(diff) + "</td>"
        concateStr += "<td>" + v.split(":")[0] + "</td>" + "<td>" + v.split(":")[1] + "</td>" + "<td>" + str(requestedTablesDict[v]) + "</td>" + "<td>" + v.split(":")[0] + "</td>" + "<td>" + v.split(":")[1] + "</td>" + "<td>" + str(requestedTablesDict[v]) + "</td>" + diffStr
        concateStr += "</tr>"
    if diffRequestedTableDict and not diffReadTableDict:
        for k in diffRequestedTableDict.keys():
            concateStr += "<tr bgcolor=\"red\">"
            concateStr += "<td>" + k.split(":")[0] + "</td>" + "<td>" + k.split(":")[1] + "</td>" + "<td>" + str(diffRequestedTableDict[k]) + "</td>" + "<td colspan=\"4\">Can't find corresponding table in file</td>"
            concateStr += "</tr>"
    elif diffReadTableDict and not diffRequestedTableDict:
        for k in diffReadTableDict.keys():
            concateStr += "<tr bgcolor=\"red\">"
            concateStr += "<td colspan=\"3\">Can't find corresponding table in requested database</td>" + "<td>" + k.split(":")[0] + "</td>" + "<td>" + k.split(":")[1] + "</td>" + "<td>" + str(diffReadTableDict[k]) + "</td><td>&nbsp;</td>"
            concateStr += "</tr>"
    elif diffReadTableDict and diffRequestedTableDict:
        for k in diffRequestedTableDict.keys():
            concateStr += "<tr bgcolor=\"red\">"
            concateStr += "<td>" + k.split(":")[0] + "</td>" + "<td>" + k.split(":")[1] + "</td>" + "<td>" + str(diffRequestedTableDict[k]) + "</td>" + "<td colspan=\"4\">Can't find corresponding table in file</td>"
            concateStr += "</tr>"
        for k in diffReadTableDict.keys():
            concateStr += "<tr bgcolor=\"red\">"
            concateStr += "<td colspan=\"3\">Can't find corresponding table in requested database</td>" + "<td>" + k.split(":")[0] + "</td>" + "<td>" + k.split(":")[1] + "</td>" + "<td>" + str(diffReadTableDict[k]) + "</td><td>&nbsp;</td>"
            concateStr += "</tr>"
    concateStr += """</tbody> 
</table>"""
    return concateStr

def sendEmail(sender, receivers, mailServer, html):
    message = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: Database restore statistics
""" % (sender, ",".join(receivers))
    try:
        smtpObj = smtplib.SMTP(mailServer)
        smtpObj.sendmail(sender, receivers, message+html)
        logging.info("Successfully sent email")
    except SMTPException:
        logging.error("Error: unable to send email")
   
def compareStatistics(statistics, fileName, port):
    firstTime = False
    requestedStatList = list()
    readStatList = list()
    result = ""
    try:
        f = open(fileName + "_" + port, 'r+')
    except IOError:
        firstTime = True
        try:
            f = open(fileName + "_" + port, 'w+')
        except IOError:
            raise IOError, "Can't open file %s" % fileName + "_" + port
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
    
    if (set(requestedTablesDict.keys()) - set(readTablesDict.keys())) and not (set(readTablesDict.keys()) - set(requestedTablesDict.keys())):
        diffRequestedTableDict = dict()
        for e in (set(requestedTablesDict.keys()) - set(readTablesDict.keys())):
            diffRequestedTableDict[e] = requestedTablesDict[e]

            result = generateHTML(requestedTablesDict, readTablesDict, diffRequestedTableDict)

    elif (set(readTablesDict.keys()) - set(requestedTablesDict.keys())) and not (set(requestedTablesDict.keys()) - set(readTablesDict.keys())):
        diffReadTableDict = dict()
        for e in (set(readTablesDict.keys()) - set(requestedTablesDict.keys())):
            diffReadTableDict[e] = readTablesDict[e]

            result = generateHTML(requestedTablesDict, readTablesDict, None, diffReadTableDict)

    elif (set(requestedTablesDict.keys()) - set(readTablesDict.keys())) and (set(readTablesDict.keys()) - set(requestedTablesDict.keys())):
        diffRequestedTableDict = dict()
        for e in (set(requestedTablesDict.keys()) - set(readTablesDict.keys())):
            diffRequestedTableDict[e] = requestedTablesDict[e]
        diffReadTableDict = dict()

        for e in (set(readTablesDict.keys()) - set(requestedTablesDict.keys())):
            diffReadTableDict[e] = readTablesDict[e]

        result = generateHTML(requestedTablesDict, readTablesDict, diffRequestedTableDict, diffReadTableDict)

    else:
       result = generateHTML(requestedTablesDict, readTablesDict)

    f.seek(0,0)
    f.truncate()
    f.writelines(requestedStatList)
    f.close()
    return result

# TODO multi thread support

def analyzeDb(user, passwd, host, port):
    databases = getDatabases(user, passwd, host, port)
    for e in databases:
        for d in e:
            conn = db(d, user, passwd, host, port)
            curr = conn.conn.cursor()
            curr.execute("ANALYZE")
            curr.close()
            del conn

def stopPostgres():
    global Directory

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

def rmDir(path):
    try:
        checkDir(path)
        shutil.rmtree(path)
    except DirectoryPathIsNotAbs, e:
        raise DirectoryPathIsNotAbs, e
    except DirectoryNotExists, e:
        raise DirectoryNotExists, e

def mkDir(path):
    try:
        checkDir(path)
    except DirectoryPathIsNotAbs, e:
        raise DirectoryPathIsNotAbs, e
    except DirectoryNotExists:
        os.mkdir(path)

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
        opts, args = getopt.getopt(argv,"h:a:d:p:v",["help=","archive=","directory=","port=","version="])
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
        elif opt in ("-p", "--password"):
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
    pd.main(cleanupArgv(argv, ["-v", "--version"]))
    createLinks('autovacuum.conf')
    startPostgres()
    analyzeDb(pgUser, pgPass, host, port)
    statStr = compareStatistics(getSampleStatistics(pgUser, pgPass, host, port),statisticFileName, port)
    sendEmail(sender, receivers, mailServer, statStr)

if __name__=='__main__':
    main(sys.argv[1:])
