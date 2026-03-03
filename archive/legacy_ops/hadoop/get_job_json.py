#!/usr/bin/env python3

"""Module for archive.legacy_ops.hadoop.get_job_json."""

# pylint: disable=too-many-nested-blocks
import json
import signal
import sys
import time

import requests

url = 'http://example.com:50030/metrics?format=json'
user = 'eselyavka'
sleepInterval = 1
reportFile = 'jobReport.dat'

def signalHandler(signum, _stack):
    print(f'Received: {signum}, exiting...')
    sys.exit(0)

def writeReport(mapJobCount, reduceJobCount):
    with open(reportFile, 'a+', encoding='utf-8') as fh:
        fh.write(f"{int(time.time())},{mapJobCount},{reduceJobCount}\n")

def requestForJson():
    try:
        resp = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        resp = requests.get(url, timeout=10)

    data = json.loads(resp.text)
    mapJobCount = 0
    reduceJobCount = 0

    for scheduler, scheduler_dict in data.items():
        if scheduler == 'fairscheduler':
            for pools, pool_list in scheduler_dict.items():
                if pools == 'pools':
                    for jobs in pool_list:
                        job_meta = jobs[0]
                        job_stats = jobs[1]
                        if job_meta['name'] == user and job_meta['taskType'] == 'MAP' and job_stats['runningTasks'] > 0:
                            mapJobCount += job_stats['runningTasks']
                        if job_meta['name'] == user and job_meta['taskType'] == 'REDUCE' and job_stats['runningTasks'] > 0:
                            reduceJobCount += job_stats['runningTasks']
    writeReport(mapJobCount, reduceJobCount)

def main():
    signal.signal(signal.SIGUSR1, signalHandler)
    requestForJson()

    while True:
        time.sleep(sleepInterval)
        requestForJson()

if __name__ == '__main__':
    main()
