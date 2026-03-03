#!/usr/bin/env python3

"""Module for archive.legacy_ops.hadoop.compaction."""

# pylint: disable=bad-indentation,wrong-import-position,wrong-import-order,wildcard-import
# pylint: disable=deprecated-module,bare-except,consider-using-f-string,unused-import
# pylint: disable=superfluous-parens,missing-timeout,ungrouped-imports,unused-variable

hbase_server='localhost'
thrift_port='9090'
hbase_master_ui='http://localhost:60010/table.jsp'

import os
import sys

from optparse import OptionParser

import requests
from bs4 import BeautifulSoup
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

def parse_args():
  usage = "usage: %prog <filename>"
  parser = OptionParser(usage=usage)
  options, args = parser.parse_args()
  if len(args) == 1:
    return options, args
  else:
    parser.error("incorrect number of arguments")

def main():
  try:
    transport.open()
  except:
    sys.exit("connection to %s with port %s failed" % (hbase_server,thrift_port))

  _options, args = parse_args()

  hbase_tables = client.getTableNames()

  if os.path.isfile(args[0]):
    with open(args[0],'r') as f:
      for line in f:
        table = line.strip()
        if (table in hbase_tables):
          table_keys = {'name':table}
          r =  requests.get(hbase_master_ui, params=table_keys)
          soup = BeautifulSoup(r.text)
          tables = soup.findAll( "table" )
          rows = tables[0].findAll( "tr" )
          cells = rows[2].findAll( "td" )
          compaction_status = cells[1].contents[0]
          if (compaction_status != 'NONE'):
            print ("can't major_compact table: %s, compaction status is not NONE" % table)
          else:
            client.majorCompact(table)
            #print table
        else:
          print ("no such '%s' table in hbase" % table)
  else:
    sys.exit("file %s doesn't exists" % args[0])

  try:
    transport.close()
  except:
    sys.exit("can't close connection to %s with port %s" % (hbase_server,thrift_port))

if __name__ == "__main__":
    sys.exit(main())
