#!/usr/bin/env python
import json
import requests
import time
import signal
import sys


url='http://example.com:50030/metrics?format=json'
user='eselyavka'
sleepInterval=1
reportFile='jobReport.dat'

def signalHandler(signum, stack):
    print 'Received: %s, exiting...' % signum
    sys.exit(0);

def writeReport( mapJobCount, reduceJobCount ):
    with (open(reportFile,'a+')) as fh:
        fh.write(str(int(time.time())) + ',' + str(mapJobCount) + "," + str(reduceJobCount) + '\n')

def requestForJson():
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(sleepInterval)
        resp = requests.get(url)

    data=json.loads(resp.text)

    mapJobCount=0
    reduceJobCount=0

    for scheduler,sdict in data.items():
        if scheduler == 'fairscheduler':
            for pools,plist in sdict.items():
                if pools == 'pools':
                    for jobs in plist:
                            if jobs[0]['name'] == user: 
                                if jobs[0]['taskType'] == 'MAP':
                                    if jobs[1]['runningTasks'] > 0:
                                        mapJobCount+=jobs[1]['runningTasks']
                                if jobs[0]['taskType'] == 'REDUCE':
                                    if jobs[1]['runningTasks'] > 0:
                                        reduceJobCount+=jobs[1]['runningTasks']
    writeReport(mapJobCount, reduceJobCount)

def main():
    signal.signal(signal.SIGUSR1, signalHandler);
    requestForJson()

    while True:
        time.sleep(sleepInterval)
        requestForJson()

if __name__=='__main__':
    main()
