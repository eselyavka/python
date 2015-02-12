#!/usr/bin/env python

hbase_server='localhost'
thrift_port='9090'

import sys,os,stat,pprint,pickle
from hbase import Hbase
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase.ttypes import *
from optparse import OptionParser

transport = TSocket.TSocket(hbase_server, thrift_port)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)

def _user_from_row(self, row):
  user = {}
  for col,cell in row.columns.items():
    print  col + '=' + cell.value

def main():
  try:
    transport.open()
  except:
    sys.exit("connection to %s with port %s failed" % (hbase_server,thrift_port))

  test_data = client.getRow('TABLENAME', '296244')
  columns = ['location_info', 'login_info', 'req_info', 'user_info']
  scanner = client.scannerOpen('TABLENAME','',columns)
  row = client.scannerGet(scanner)
  print type(row)
  print row
  #while row:
  #  yield _user_from_row(row[0])
  #  row = self.client.scannerGet(scanner)  
  client.scannerClose(scanner)
   
#  for col,cell in test_data[0].columns.items():
#    print col
#    print col + '=' + cell.value
#  print (test_data[0])
  try:
    transport.close()
  except:
    sys.exit("can't close connection to %s with port %s" % (hbase_server,thrift_port))

if __name__ == "__main__":
    sys.exit(main())
