#!/usr/bin/env python3

"""Print transaction deltas from pg_stat_database."""

import logging
import signal
import sys
import time

import psycopg2

# pylint: disable=fixme,implicit-str-concat

# TODO add support arguments in script with getopt

globalHost = 'localhost'
globalPort = 5433
globalDatabase = 'template1'
globalUser = 'postgres'
globalPassword = 'postgres'

logging.basicConfig(level=logging.DEBUG)

def exitHandler(signum, _frame):
    logging.error('Exiting with signal %s', signum)
    sys.exit(0)

def dbConnect(host='localhost', port=5432, database='template1', user='postgres', password='postgres'):
    try:
        conn = psycopg2.connect(
            f"host={host} port={port:d} dbname={database} user={user} password={password}"
        )
        return conn
    except psycopg2.Error:
        logging.error('Can''t create DB connection')
        sys.exit(1)

def dbDisconnect(connHandler):
    try:
        connHandler.close()
    except psycopg2.Error:
        logging.error('Can''t close connection to DB')

def calculateTrx():
    lastTupleList = getTrx()
    while True:
        time.sleep(5)
        newTupleList = getTrx()
        for index, newTuple in enumerate(newTupleList):
            lastTuple = lastTupleList[index]
            trxNum = int(newTuple[2]) - int(lastTuple[2])
            print(
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}: {newTuple[0]}: "
                f"{trxNum}: {'#' * int(round(trxNum / 10))}"
            )
        print('\n\n')
        lastTupleList = newTupleList

signal.signal(signal.SIGTERM, exitHandler)
signal.signal(signal.SIGINT, exitHandler)

def getTrx():
    query = "SELECT datname as dbname, extract('epoch' from current_timestamp) as ts, (xact_commit+xact_rollback) as total FROM pg_stat_database WHERE datname NOT IN ('template0','template1','postgres')"
    conn = dbConnect(
        host=globalHost, port=globalPort, database=globalDatabase, user=globalUser, password=globalPassword
    )
    curs = conn.cursor()

    try:
        curs.execute(query)
        rows = curs.fetchall()
        curs.close()
        dbDisconnect(conn)
        return rows
    except psycopg2.Error:
        logging.error('Can''t execute query: %s', query)
        curs.close()
        dbDisconnect(conn)
        sys.exit(1)

def main():
    calculateTrx()

if __name__ == '__main__':
    main()
