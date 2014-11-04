#!/usr/bin/env python

# This script copies tables (either whole or partially) across HBase clusters
# It is to be run from the destination cluster
# Requires thrift servers to be running on both clusters
# Requires full network access from destination to origin (not only thrift port)
# This is for running the MR jobs remotely

# config
source_hbase_server = 'source_thrift_server'
source_thrift_port = 9090
source_hftp_server = 'source_hdfs_datanode'
source_hftp_port = 50070
source_hadoop_bin = '/usr/local/hadoop/bin/hadoop'
source_hbase_jar = '/usr/local/hbase/hbase-0.20.3.jar'
source_export_path = '/export' # path in hdfs
source_ssh_port = 22
source_ssh_user = 'hadoop'
dest_hbase_server = '127.0.0.1'
dest_thrift_port = 9090
dest_hadoop_bin = '/usr/bin/hadoop'
dest_hbase_jar = '/usr/lib/hbase/hbase-0.90.3-cdh3u1.jar'
dest_import_path = '/import' # path in hdfs
no_of_versions = 3

logdir = '/var/log/hbase_migrate'
logfile = 'hbase_migrate.log'
loglevel = 1

import sys,os
from itertools import imap
# hbase and thrift are available from easy_install
from hbase import Hbase
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase.ttypes import *
from optparse import OptionParser

# define logger
import logging
# get file location from config
logfilename = "%s/%s" % (logdir, logfile)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logfilename,
                    filemode='a')
logger = logging.getLogger("hbase_migrate")
# check config file for reporting level
if loglevel == 1:
   logger.setLevel(logging.DEBUG)
else:
   logger.setLevel(logging.ERROR)

# connect to servers
source_transport = TSocket.TSocket(source_hbase_server, source_thrift_port)
source_transport = TTransport.TBufferedTransport(source_transport)
source_protocol = TBinaryProtocol.TBinaryProtocol(source_transport)
source_client = Hbase.Client(source_protocol)

dest_transport = TSocket.TSocket(dest_hbase_server, dest_thrift_port)
dest_transport = TTransport.TBufferedTransport(dest_transport)
dest_protocol = TBinaryProtocol.TBinaryProtocol(dest_transport)
dest_client = Hbase.Client(dest_protocol)

def parse_args():
    usage = "%prog table_name [ begin_timestamp [[ end_timestamp ]] ]\n\
              If 'all' is specified as <table_name>, all tables will be handled. \n\
              If only one timestamp is provided, it will be used as the start point \n\
              and all records from this point in time and forward will be copied."
    parser = OptionParser(usage=usage)

    options, args = parser.parse_args()
    logger.debug('arguments passed: %s' % args)

    if len(args) == 1:
        # only the table name was passed
        logger.debug('table: %s passed' % args[0])
        try:
            type(args[0]) == str
        except:
            logger.error('bad argument passed')
            parser.error('timestamp must be an integer')
    elif len(args) == 2:
        # this means only the begin timestamp was passed
        # so we process all the records from then to infinity
        # first though check if the timestamp is really something semblant of a timestamp
        try:
            type(args[0]) == str
            int(args[1])
        except:
            logger.error('bad argument passed')
            parser.error('timestamp must be an integer')
    elif len(args) == 3:
        # both timestamps were passed, we should handle all the records in between
        try:
            type(args[0]) == str
            int(args[1])
            int(args[2])
        except:
            logger.error('bad argument passed')
            parser.error('timestamps must be integers')
    else:
        parser.error("Must supply table name, and optional timestamps. Use --help for usage instructions.")

    return options, args


def check_table_exists(table_name):
    """Verify existence of table and return error if doesn't exist."""
    try:
        table_list = source_client.getTableNames()
    except:
        logger.error('failed to get list of tables')
    if table_name in table_list:
        logger.debug('%s found in table_list' % table_name)
        return True
    else:
        logger.error('%s not found in table_list' % table_name)
        return False


def get_tables():
    """'all' was passed, get the list of tables from the origin server."""
    try:
        table_list = source_client.getTableNames()
        return table_list
    except:
        logger.error('failed to get list of tables')


def copy_table(table_name, begin_timestamp="", end_timestamp=""):
    """export the table to hdfs, use hftp to hdfs copy to destination server
       and then import to hbase"""
    logger.debug('was passed table: %s will try to copy to %s' % (table_name, dest_hbase_server))

    # export to hfds on source
    try:
        # clean export dir before actually exporting
        logger.debug('deleting hdfs dir on source: %s/%s' % (source_export_path, table_name))
        delete_exportdir_command = 'ssh -p %s %s@%s "%s dfs -rmr %s/%s"' % (
        source_ssh_port, source_ssh_user, source_hbase_server, source_hadoop_bin, source_export_path, table_name)
        os.popen(delete_exportdir_command)
    except:
        logger.debug('problem deleting %s/%s on source hdfs server' % (source_export_path, table_name))
    try:
        # we'll pass empty strings instead of timestamps if not specified because they are optional
        export_command = 'ssh -p %s %s@%s "%s jar %s export %s %s/%s %s %s %s"' % (
        source_ssh_port, source_ssh_user, source_hbase_server, source_hadoop_bin,
        source_hbase_jar, table_name, source_export_path, table_name, no_of_versions, begin_timestamp, end_timestamp)
        logger.debug('attempting to run: %s' % export_command)
        os.popen(export_command)
    except:
        logger.error('problem exporting table: "%s" on source server to hdfs - aborting' % table_name)
        sys.exit()
    # perform distcp hftp to hdfs pull
    try:
        # please remember this script should be run on the destination server
        distcp_command = 'su - hdfs -c \'%s distcp -overwrite -p "hftp://%s:%s%s/%s" "hdfs://localhost%s/%s"\'' % (
        dest_hadoop_bin, source_hftp_server, source_hftp_port, source_export_path, table_name,
        dest_import_path, table_name)
        logger.debug('attempting to run: %s' % distcp_command)
        os.popen(distcp_command)
    except:
        logger.error('problem performing distcp for table: "%s" - aborting' % table_name)
        sys.exit()

    try:
        # get column families and definitions and create on dest server
        # must be created before attempting to import
        desc = source_client.getColumnDescriptors(table_name)
        column_families = []
        for name,cf in desc.items():
            # parse origin schema and make nice for create
            cf.name = '%s:' % name
            # little patch due to inconsistencies in API
            if cf.bloomFilterType == 'false':
                cf.bloomFilterType = 'NONE'
            column_families.append(cf)
        dest_client.createTable(table_name, column_families)
        logger.debug('created table %s' % table_name)

    except AlreadyExists, tx:
        logger.debug ('table %s exists already... %s' % (table_name, tx.message))
        
    try:
        # run the local import
        import_command = 'su - hbase  -c "%s jar %s import %s %s/%s"' % (
        dest_hadoop_bin, dest_hbase_jar, table_name, dest_import_path, table_name)
        logger.debug('attempting to run: %s' % import_command)
        os.popen(import_command)
    except:
        logger.error('problem importing table: "%s" - aborting' % table_name)
        sys.exit()

def main():

    try:
        source_transport.open()
    except:
        print("connection to %s with port %s failed" % (source_hbase_server,source_thrift_port))

    try:
        dest_transport.open()
    except:
        print("connection to %s with port %s failed" % (dest_hbase_server,dest_thrift_port))
    options, args = parse_args()
    table_name = args[0]
        
    if table_name == 'all':
        # handle all the tables
        table_list = get_tables()
        # here we differentiate between the cases (if timestamps were provied or not at runtime)
        if len(args) == 3:
            begin_timestamp = args[1]
            end_timestamp = args[2]
            for table in table_list:
                copy_table(table, begin_timestamp, end_timestamp)
        elif len(args) == 2:
            begin_timestamp = args[1]
            for table in table_list:
                copy_table(table, begin_timestamp)
        else:
            for table in table_list:
                copy_table(table)

    elif check_table_exists(table_name):
        # handle a single table copy
        if len(args) == 3:
            begin_timestamp = args[1]
            end_timestamp = args[2]
            copy_table(table_name, begin_timestamp, end_timestamp)
        elif len(args) == 2:
            begin_timestamp = args[1]
            copy_table(table_name, begin_timestamp)
        else:
            copy_table(table_name)
    else:
        # should probably not reach this point...
        logger.error('something went wrong with main operation')


if __name__ == "__main__":
    sys.exit(main())
