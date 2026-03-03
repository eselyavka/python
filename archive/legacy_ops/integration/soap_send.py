#!/usr/bin/env python3

"""Module for archive.legacy_ops.integration.soap_send."""

import sys
import http.client
import socket
import time

host = 'localhost'
port = 8080
relativeUri = '/someurl/someurl'
hostname = socket.gethostname()

if sys.argv[1]:
    fileName = sys.argv[1]
else:
    raise ValueError('Need filename as argument')

def request(data):
    webservice = http.client.HTTPConnection(host, port)
    webservice.putrequest("POST", relativeUri)
    webservice.putheader("Host", hostname)
    webservice.putheader("User-Agent", "Python post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", str(len(data)))
    webservice.putheader("SOAPAction", "\"\"")
    webservice.endheaders()
    webservice.send(data)
    response = webservice.getresponse()
    print(response.status, response.reason)
    res = response.read()
    print(res)
    webservice.close()

def readFile(filename=None):
    if filename:
        with open(filename, 'r', encoding='utf-8') as lines:
            for line in lines:
                request(line)
                time.sleep(1)
    else:
        raise ValueError('Filename can\'t be None')

def main():
    readFile(fileName)

if __name__ == '__main__':
    main()
