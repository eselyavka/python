#!/usr/bin/env python

import os
import sys
import getopt
import re
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText

LogLineRe = re.compile(r'''(?P<ts>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})       #ts
                             \s+
                             \[\s?
                             (?P<level>\w+)                                           #LogLevel
                             \s?\]
                             \s+
                             (?P<string>.+)                                           #Other
''',re.VERBOSE);

LogLineReHadoop = re.compile(r'''.+                                                   #All before searching context
                             hadoop\.native\.lib\s?is\s?deprecated                    #Searching context
                             .+                                                       #All after searching context
''',re.VERBOSE);

def dictify_logline(Line):
    Match = LogLineRe.match(Line)
    if Match is not None:
        GroupDict = Match.groupdict()
        return GroupDict
    else:
        return {'ts':None,
                'level':None,
                'string':None,
        }

def open_file(LogFile, LogLevel):
    ArrLogLevel = LogLevel.split(',')
    ReportDict = {}
    i=1
    with open(LogFile, 'r') as f:
        ReadData = f.readlines()
        for Line in ReadData:
            ErrorList = []
            LineDict = dictify_logline(Line)
            if len(ArrLogLevel) > 1:
                for Level in ArrLogLevel:
                    if LineDict['level'] is not None and LineDict['level'] == Level:
                        ErrorList.append(LineDict['ts'])
                        ErrorList.append(LineDict['level'])
                        ErrorList.append(LineDict['string'])
                        ReportDict[i] = ErrorList
            elif len(ArrLogLevel) == 1:
                if LineDict['level'] is not None and LineDict['level'] == ArrLogLevel[0]:
                    ErrorList.append(LineDict['ts'])
                    ErrorList.append(LineDict['level'])
                    ErrorList.append(LineDict['string'])
                    ReportDict[i] = ErrorList
            else:
                assert False, 'unhandled error level'
            i += 1
    return ReportDict

def check_file(LogFile):
   if (os.path.isfile(LogFile) and os.path.isabs(LogFile)):
       return True
   else:
       return False

def get_time(TsFile):
    Ts = str(datetime.now())
    if os.path.isfile(TsFile):
        with open(TsFile, 'r') as f:
            Ts = f.readline()
    with open(TsFile, 'w') as f:
        f.write(str(datetime.now()))
    return Ts

def make_report(Report, Time, Recipients, NoTime):
    Msg=''
    for StrNum, Data in Report.items():
        HadoopDeprMatch = LogLineReHadoop.match(Data[2])
        if not HadoopDeprMatch:
            if datetime.strptime(Data[0], '%Y-%m-%d %H:%M:%S.%f') > datetime.strptime(Time, '%Y-%m-%d %H:%M:%S.%f') and not NoTime:
                Buf = "String Number: %s\nDate: %s\nLevel: %s\nError: %s\n" % (StrNum, Data[0], Data[1], Data[2])
                StrSep = "=" * len("Error: "+Data[2]) + "\n"
                Str = Buf + StrSep 
                Msg += Str
            elif NoTime:
                Buf = "String Number: %s\nDate: %s\nLevel: %s\nError: %s\n" % (StrNum, Data[0], Data[1], Data[2])
                StrSep = "=" * len("Error: "+Data[2]) + "\n"
                Str = Buf + StrSep 
                Msg += Str
    if not len(Msg) == 0:
        print Msg
        if Recipients is not None:
            ArrRecipients = Recipients.split(',')
            for Recipient in ArrRecipients:
                MsgHeader = MIMEText(Msg,_subtype='plain',_charset='utf-8')
                MsgHeader['Subject'] = 'ERROR'
                try:
                    User = os.getlogin()
                except EnvironmentError:
                    User = 'crontab'
                MsgHeader['From'] = User + '@' + os.uname()[1]
                MsgHeader['To'] = Recipient 
                Server = smtplib.SMTP('mail.example.com')
                Server.sendmail( User + '@' + os.uname()[1], Recipient, MsgHeader.as_string() )
                Server.quit()

def main(argv):
    LogFile = ''
    LogLevel = 'ERROR'
    TsFile = '/opt/ts_file/parse.ts'
    Recipients = None
    NoTime = False
    try:
        opts, args = getopt.getopt(argv,"hf:l:t:n",["file=", "level=", "to=", "notime"])
    except getopt.GetoptError:
        print '%s -f <log file path> --file=<log file path>, -l [comma separate log level, default ERROR] --level=[comma separate log level, default ERROR] -t [comma separate email to send report] --to=[comma separate email to send report] -n [parse all file without ts label] --notime [parse all file without ts label]'  % os.path.abspath(__file__)
        sys.exit(2)
    if len(opts) == 0:
        print '%s -f <log file path> --file=<log file path>, -l [comma separate log level, default ERROR] --level=[comma separate log level, default ERROR] -t [comma separate email to send report] --to=[comma separate email to send report] -n [parse all file without ts label] --notime [parse all file without ts label]' % os.path.abspath(__file__)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print '%s -f <log file path> --file=<log file path>, -l [comma separate log level, default ERROR] --level=[comma separate log level, default ERROR] -t [comma separate email to send report] --to=[comma separate email to send report] -n [parse all file without ts label] --notime [parse all file without ts label]' % os.path.abspath(__file__)
        elif opt in ('-f', '--file'):
            LogFile = arg
        elif opt in ('-l', '--level'):
            LogLevel = arg
        elif opt in ('-t', '--to'):
            Recipients = arg
        elif opt in ('-n', '--notime'):
            NoTime = True
        else:
            assert False, 'unhandled option'
    if check_file(LogFile):
        Report = open_file(LogFile, LogLevel)
        CurrTime = get_time(TsFile)
        make_report(Report, CurrTime, Recipients, NoTime)
    else:
        print 'Check logfile: %s exists or path to logfile is absolute' % LogFile
        sys.exit(3)

if __name__=='__main__':
    main(sys.argv[1:])
