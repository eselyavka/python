#!/usr/bin/env python

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import logging
from flumelogger import handler

schema = avro.schema.parse(open("log.avsc").read())

def writeFile():
    writer = DataFileWriter(open("part-00000.avro", "w"), DatumWriter(), schema)
    writer.append({"logline": "2016\t30"})
    writer.close()


def sendData():
    fh = handler.FlumeHandler(host='localhost', port=6666, type='ng', headers={'application': 'Skyline.Analyzer'})
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.info("python is cool")


#def sendFile():
#    client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])
#    requestor = ipc.Requestor(PROTOCOL, client)
#     
#    event = dict()
#
#    event['headers'] = {'name': 'abc', 'address': 'zyx'}
#    event['body'] = bytes('hello')
#    
#    params = dict()
#
#    params['event'] = event
#
#    print("Result : " + requestor.request('append', params))
#
#    client.close()

def readFile():
    reader = DataFileReader(open("part-00000.avro", "r"), DatumReader())
    for user in reader:
        print user
    reader.close()

def main():
    sendData()
    writeFile()
    readFile()

if __name__=='__main__':
    main()

