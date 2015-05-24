#!/usr/bin/env python
import json
import requests
import time
import signal
import sys

url='http://example.com:50030'
user='eselyavka'
sleepInterval=1

def signalHandler(signum, stack):
    print 'Received: %s, exiting...' % signum
    sys.exit(0);

def writeRepor( jobCount=0 ):
    with (open('jobReport.txt','a+')) as fh:
        fh.write(str(int(time.time())) + ',' + str(jobCount) + '\n') 

def requestForJson():
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(sleepInterval)
        resp = requests.get(url)

    data=json.loads(resp.text)
    
    for scheduler,skey in data.iteritems():
        if scheduler == 'fairscheduler':
            for pools,pkey in skey.iteritems():
                if pools == 'pools':
                    for jobs,jobskey in pkey:
                        if jobs['name'] == user:
                            for job in jobskey.iteritems():
                                if job[0] == 'runningTasks' and job[1] > 0:
                                    writeRepor(job[1])

def main():
    signal.signal(signal.SIGUSR1, signalHandler);
    requestForJson()

    while True:
        time.sleep(sleepInterval)
        requestForJson()

if __name__=='__main__':
    main()
