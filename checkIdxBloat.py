#!/usr/bin/env python
import psycopg2
import logging
import getopt
import os
import sys

file = None
host = 'localhost'
dbname = 'database'
user = 'user'
password = 'password'
host = 'localhost'
port = 5432
critical = 90
warning = 60
verbose = None

logging.basicConfig(level = logging.DEBUG)

def usage():
    print 'Usage ' + sys.argv[0] + ' <-f/--file> <-H/--host> <-d/--dbname> [-u/--user] [-p/--password] [-o/--port] [-c/--critical] [-w/--warning] [-v/--verbose] -h/--help'
    print '\t -f File with sql predefined query'
    print '\t -H Database server host to connect'
    print '\t -d Database to connect'
    print '\t -u DB user'
    print '\t -p DB password'
    print '\t -o DB port'
    print '\t -c Critical percent of bloating idx, default is 90%, critical threashold smaller then 50% is the same as 50%'
    print '\t -w Warning percent of bloating idx, default is 60%, warning threashold smaller then 50% is the same as 50%'
    print '\t -v Some verbose output'
    print '\t -h Print this help'
  
def parseArg():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hf:H:d:u:p:o:w:c:v', ["help", "file=", "host=", "dbname=", "user=", "password=", "port=", "warning=", "critical=", "verbose"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    if len(opts) < 3:
        usage()
        sys.exit(2)

    global file
    global host
    global dbname
    global user
    global password
    global port
    global host
    global critical
    global warning
    global verbose
  
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file = a        
        elif o in ("-H", "--host"):
            host = a        
        elif o in ("-d", "--dbname"):
            dbname = a
        elif o in ("-u", "--user"):
            user = a
        elif o in ("-p", "--password"):
            password = a
        elif o in ("-o", "--port"):
            port = int(a)
        elif o in ("-c", "--critical"):
            critical = int(a)
        elif o in ("-w", "--warning"):
            warning = int(a)
        else:
            assert False, "unhandled option"

def readSqlFileName( sqlFile = None ):
    if sqlFile:
        if os.path.isabs(sqlFile):
            if os.path.isfile(sqlFile):
                with open(sqlFile, 'r') as f:
                    sqlQuery = f.read()
                return sqlQuery
            else:
                logging.error('File %s not exist' % sqlFile)
                sys.exit(3)
        else: 
            if verbose: logging.error('Specified absolute pathname for %s' % sqlFile)
            sys.exit(3)    
    else:
        if verbose: logging.error('Argument not specified')
        sys.exit(3)

def dbQuery(query, user, password, dbname, host, port):
    try:
      conn = psycopg2.connect("host=%s port=%d dbname=%s user=%s password=%s" % ( host, port, dbname, user, password ))
      curs = conn.cursor()
      try:
        curs.execute(query)
        rows = curs.fetchall()
        curs.close()
        conn.close()
        return rows
      except StandardError, e:
        logging.error('Can''t execute query: %s' % query)
        if verbose: logging.error('Postgresql error code: %s' % e.pgcode)
        if verbose: logging.error('Postgresql error message: %s' % e.pgerror)
        curs.close()
        conn.close()
        sys.exit(1)
    except:
      logging.error('Can''t create DB connection')
      sys.exit(1)

def nagiosStringComposition( severityList, severityName ):
    if severityList:
        severityStr = ''
        for item in severityList:
            if ( item == severityList[-1] ):
                severityStr += item
            else:
                severityStr += item 
                severityStr += ','
        return severityName +': ' + severityStr
    else:
        if verbose: logging.debug('Empty severity list in nagiosStringComposition')
        print 'UNKNOWN'

def nagiosOutput( queryData ):
    warnList = []
    critList = []
    unknownList = []

    global file
    global warning
    global critical

    if queryData:
        for r in queryData:
            if ( warning <= float(r[4]) <= critical ):
                warnList.append(r[3])
            elif ( float(r[4]) > critical ):
                critList.append(r[3])
            else:
                unknownList.append(r[3])
    else:
        if verbose: logging.debug('Empty query result')
        print 'OK'
        return
  
    if critList:
         if verbose: logging.debug('Critical list: ' % critList)
         print nagiosStringComposition( critList, 'CRITICAL' )  
         return
    elif warnList:
         if verbose: logging.debug('Warning list: ' % warnList)
         print nagiosStringComposition( warnList, 'WARNING' )
         return
    elif unknownList:
         if verbose: logging.debug('Unknown list: ' % unknownList)
         print nagiosStringComposition( unknownList, 'UNKNOWN' )
         return
    else:
        if verbose: logging.debug('Unexpected values in query: %s' % readSqlFileName(file))
        print 'UNKNOWN'
        return

def main():
    parseArg( )
    query = readSqlFileName( file )
    resList = dbQuery( query, user, password, dbname, host, port )
    nagiosOutput( resList )

if __name__=='__main__':
    main()
