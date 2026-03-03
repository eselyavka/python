#!/usr/bin/env python3

"""Module for archive.legacy_ops.integration.log_cleaner."""

# pylint: disable=missing-function-docstring

import os
import sys
import getopt
from datetime import date, timedelta
import time

USAGE = (
    '%s -d <comma separate log directory path> --dir=<comma separate log directory path>, '
    '-t [time to delete older logs in UNIXTIME] --time=[time to delete older logs in UNIXTIME]'
)

def check_directory(directory):
    return os.path.isabs(directory) and os.path.isdir(directory)

def listDir(directory, unix_time):
    items = os.listdir(directory)
    for item in items:
        if os.stat(directory + '/' + item).st_mtime < unix_time:
            print(directory + '/' + item)
            # os.remove(directory + '/' + item)

def checkUnixTime(unix_time):
    try:
        return int(unix_time) // 1000000000 == 1
    except ValueError:
        print(f'time variable {unix_time} is not in unixtime')
        sys.exit(2)

def readDir(dirs, unix_time):
    for directory in dirs.split(','):
        if check_directory(directory):
            listDir(directory, unix_time)
        else:
            print(f"Directory {directory} doesn't exists")

def main(argv):
    TimeArg = date.today() - timedelta(days = 3)
    UnixTimeArg = int(time.mktime(TimeArg.timetuple()))
    try:
        opts, _args = getopt.getopt(argv,"hd:t:",["dir=", "time="])
    except getopt.GetoptError:
        print(USAGE % os.path.abspath(__file__))
        sys.exit(2)
    if len(opts) == 0:
        print(USAGE % os.path.abspath(__file__))
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(USAGE % os.path.abspath(__file__))
        elif opt in ('-d', '--dir'):
            DirArg = arg
        elif opt in ('-t', '--time'):
            UnixTimeArg = arg
            checkUnixTime(UnixTimeArg)
        else:
            assert False, 'unhandled option'

    readDir(DirArg, UnixTimeArg)
    checkUnixTime(UnixTimeArg)


if __name__ == '__main__':
    main(sys.argv[1:])
