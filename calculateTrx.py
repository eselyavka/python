#!/usr/bin/env python
import psycopg2
import logging
import signal,os,sys
import time 
import datetime

#TODO add support arguments in script with getopt

globalHost = 'localhost'
globalPort = 5433
globalDatabase = 'template1'
globalUser = 'postgres'
globalPassword = 'postgres'

logging.basicConfig(level = logging.DEBUG)

def exitHandler(signum, frame):
    logging.error('Exiting with signal %s' % signum)
    sys.exit(0)

def dbConnect(host = 'localhost', port = 5432, database='template1', user='postgres', password='postgres'):
    try:
        conn = psycopg2.connect("host=%s port=%d dbname=%s user=%s password=%s" % ( host, port, database, user, password ))
        return conn
    except:
        logging.error('Can''t create DB connection')
        sys.exit(1)

def dbDisconnect( connHandler ):
    try:
        connHandler.close()
    except:
        logging.error('Can''t close connection to DB')


def calculateTrx():
    lastTupleList = getTrx()
    while True:
        time.sleep(5)
        newTupleList = getTrx()
        for t in range(0,len(newTupleList)):
            lastTuple = lastTupleList[t]
            newTuple = newTupleList[t]
            tsInterval = long(newTuple[1]) - long(lastTuple[1])
            trxNum = long(newTuple[2]) - long(lastTuple[2])
            print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + ': ' + str(newTuple[0]) + ': ' + str(trxNum) + ': ' + '#'*int(round(trxNum/10))
        print '\n\n'
        lastTupleList = newTupleList

signal.signal(signal.SIGTERM, exitHandler)
signal.signal(signal.SIGINT, exitHandler)

def getTrx():

    query = "SELECT datname as dbname, extract('epoch' from current_timestamp) as ts, (xact_commit+xact_rollback) as total FROM pg_stat_database WHERE datname NOT IN ('template0','template1','postgres')"
    conn = dbConnect( port = globalPort )
    curs = conn.cursor()

    try:
        curs.execute(query)
        rows = curs.fetchall()
        curs.close()
        dbDisconnect(conn)
        return rows
    except:
        logging.error('Can''t execute query: %s' % query)
        curs.close()
        dbDisconnect(conn)
        sys.exit(1)
        
def main():
    calculateTrx()

if __name__=='__main__':
    main()
