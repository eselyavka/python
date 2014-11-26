#!/usr/bin/env python

import sys 
import httplib
import socket
import time

host = 'localhost'
port = 8080
relativeUri = '/someurl/someurl'
hostname = socket.gethostname()

if sys.argv[1]:
    fileName = sys.argv[1]
else:
   raise ValueError, 'Need filename as argument'

def request(data):

    global host
    global port
    global relativeUri
    global hostname

    webservice = httplib.HTTPConnection(host,port)
    webservice.putrequest("POST", relativeUri)
    webservice.putheader("Host", hostname)
    webservice.putheader("User-Agent", "Python post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(data))
    webservice.putheader("SOAPAction", "\"\"")
    webservice.endheaders()
    webservice.send(data)
    response = webservice.getresponse()
    print response.status, response.reason
    res = response.read()
    print res
    webservice.close()

def readFile(fileName=None):
    
    if fileName:
        with(open(fileName,'r')) as lines:
            for line in lines:
                request(line)
                time.sleep(1)
    else:
        raise ValueError, 'Filename can\'t be None'

def main():

    global fileName

    readFile(fileName)

if __name__=='__main__':
    main()
