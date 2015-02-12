#!/usr/bin/env python

import os
import sys
import getopt
from datetime import date, timedelta
import time 

def check_directory(dir):
   return os.path.isabs(dir) & os.path.isdir(dir)  

def listDir(dir, time):
    items = os.listdir(dir)
    for item in items:
        if(os.stat(dir + '/' + item).st_mtime < time):
            print dir + '/' + item
            #os.remove(dir + '/' + item)

def checkUnixTime(time):
    try:
        if (long(time)/1000000000) == 1:
            return True
        else:
            return False
    except ValueError:
        print 'time variable %s is not in unixtime' % time
        sys.exit(2)

def readDir(dirs, time):
    for dir in (dirs.split(',')):
        if (check_directory(dir)):
            listDir(dir, time)
        else:
            print 'Directory %s doesn''t exists' % dir

def main(argv):
    TimeArg = date.today() - timedelta(days = 3)
    UnixTimeArg = long(time.mktime(TimeArg.timetuple()))
    try:
        opts, args = getopt.getopt(argv,"hd:t:",["dir=", "time="])
    except getopt.GetoptError:
        print '%s -d <comma separate log directory path> --dir=<comma separate log directory path>, -t [time to delete older logs in UNIXTIME] --time=[time to delete older logs in UNIXTIME]'  % os.path.abspath(__file__)
        sys.exit(2)
    if len(opts) == 0:
        print '%s -d <comma separate log directory path> --dir=<comma separate log directory path>, -t [time to delete older logs in UNIXTIME] --time=[time to delete older logs in UNIXTIME]'  % os.path.abspath(__file__)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print '%s -d <comma separate log directory path> --dir=<comma separate log directory path>, -t [time to delete older logs in UNIXTIME] --time=[time to delete older logs in UNIXTIME]'  % os.path.abspath(__file__)
        elif opt in ('-d', '--dir'):
            DirArg = arg
        elif opt in ('-t', '--time'):
            UnixTimeArg = arg
            checkUnixTime(UnixTimeArg)
        else:
            assert False, 'unhandled option'

    readDir(DirArg, UnixTimeArg)
    checkUnixTime(UnixTimeArg)


if __name__=='__main__':
    main(sys.argv[1:])
