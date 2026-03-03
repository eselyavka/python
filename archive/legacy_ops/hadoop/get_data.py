#!/usr/bin/env python3

"""Module for archive.legacy_ops.hadoop.get_data."""

# pylint: disable=bad-indentation,wrong-import-position,wrong-import-order,wildcard-import
# pylint: disable=deprecated-module,bare-except,consider-using-f-string,unused-import
# pylint: disable=unused-variable,unused-argument,ungrouped-imports,broad-exception-caught

hbase_server='localhost'
thrift_port='9090'

import sys

from optparse import OptionParser
from hbase import Hbase
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase.ttypes import *

transport = TSocket.TSocket(hbase_server, thrift_port)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)

def _user_from_row(row):
  user = {}
  for col,cell in list(row.columns.items()):
    print(col + '=' + cell.value)

def main():
  try:
    transport.open()
  except Exception:
    sys.exit("connection to %s with port %s failed" % (hbase_server,thrift_port))

  test_data = client.getRow('TABLENAME', '296244')
  columns = ['location_info', 'login_info', 'req_info', 'user_info']
  scanner = client.scannerOpen('TABLENAME','',columns)
  row = client.scannerGet(scanner)
  print(type(row))
  print(row)
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
  except Exception:
    sys.exit("can't close connection to %s with port %s" % (hbase_server,thrift_port))

if __name__ == "__main__":
    sys.exit(main())
