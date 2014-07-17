#!/usr/bin/env python

import os
import sys
import getopt
import tarfile
import zipfile
from pwd import getpwnam 
from grp import getgrnam
import re
import fileinput
import logging

logging.basicConfig(filename='prepare_database.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def extract_file(path, to_directory):
    if path.endswith('.zip'):
      opener, mode = zipfile.ZipFile, 'r'
    elif path.endswith('.tar.gz') or path.endswith('.tgz'):
      opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
      opener, mode = tarfile.open, 'r:bz2'
    else: 
      raise ValueError, "Could not extract %s as no appropriate extractor is found" % path

    cwd = os.getcwd()
    os.chdir(to_directory)
    
    try:
        file = opener(path, mode)
        try: file.extractall()
        finally: file.close()
    finally:
        os.chdir(cwd)

def directory_perm(dir, user='postgres', group='postgres'):
    try:
      os.chmod(dir, 0700)
      os.chown(dir, getpwnam(user).pw_uid, getgrnam(group).gr_gid)
    except Exception:
      print "Unexpected error:", sys.exc_info()[0]
      raise

def process_config(config, port='5433'):
   
    with open(config, 'r+') as fconf:
      lines = fconf.readlines()
      fconf.seek(0)
      fconf.truncate()
      for line in lines:
        fconf.write(re.sub(r'^[#]?port.+', 'port = ' + port, line))

def main(argv):
    BaseBackupArch = ''
    Directory = ''
    DatabaseUser = ''
    DatabaseGroup = ''
    PostgresConfig = ''
    PostgresPort = ''
    try:
      opts, args = getopt.getopt(argv,"ha:d:u:g:c:p:",["archive=","directory=","user=","group=","config=","port="])
    except getopt.GetoptError:
      print '%s -a <basebackup tar archive> -d <new PGDATA directory> [-u <postgres user, default postgres> -g <postgres group, default postgres>, -c <path to postgres config, default in new PGDATA dir> -p <port for new pg_cluster, default 5433>]' % os.path.abspath(__file__)
      sys.exit(2)
    if len(opts) == 0:
      print '%s -a <basebackup tar archive> -d <new PGDATA directory> [-u <postgres user, default postgres> -g <postgres group, default postgres>, -c <path to postgres config, default in new PGDATA dir> -p <port for new pg_cluster, default 5433>]' % os.path.abspath(__file__)
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print '%s -a <basebackup tar archive> -d <new PGDATA directory> [-u <postgres user, default postgres> -g <postgres group, default postgres>, -c <path to postgres config, default in new PGDATA dir> -p <port for new pg_cluster, default 5433>]' % os.path.abspath(__file__)
         sys.exit()
      elif opt in ("-a", "--archive"):
         BaseBackupArch = arg
      elif opt in ("-d", "--directory"):
         Directory = arg
      elif opt in ("-u", "--user"):
         DatabaseUser = arg
      elif opt in ("-g", "--group"):
         DatabaseGroup = arg
      elif opt in ("-c", "--config"):
         PostgresConfig = arg
      elif opt in ("-p", "--port"):
         PostgresPort = arg

    if (os.path.isfile(BaseBackupArch) and os.path.exists(Directory)):
      if (os.path.isabs(BaseBackupArch) and os.path.isabs(Directory)):
        extract_file(BaseBackupArch, Directory)

        logging.info('Succefully extracted basebackup archive file: %s into directory: %s' % (BaseBackupArch, Directory))

        if DatabaseUser and DatabaseGroup:
          directory_perm(Directory, DatabaseUser, DatabaseGroup)
        elif DatabaseUser:
          directory_perm(Directory, user=DatabaseUser)
        elif DatabaseGroup:
          directory_perm(Directory, group=DatabaseGroup)
        else:
          directory_perm(Directory)

        logging.info('Succefully prepare new PGDATA directory: %s' % Directory)

        if PostgresConfig:
          if os.path.isfile(PostgresConfig):
            if PostgresPort:
              process_config(PostgresConfig,PostgresPort)
            else:
              process_config(PostgresConfig)
          else:
            logging.error('%s no such file' % PostgresConfig)
        else:
          if Directory.endswith("/"):
              PostgresConfig=Directory + 'postgresql.conf'
          else:
              PostgresConfig=Directory + '/postgresql.conf'
          if os.path.isfile(PostgresConfig):
            if PostgresPort:
              process_config(PostgresConfig,PostgresPort)
            else:
              process_config(PostgresConfig)
          else:
            logging.error('%s no such file' % PostgresConfig)
      else:
        logging.error('Check archive file or directory have an absolute path')
        sys.exit(2)
    else:
      logging.error('Check archive file or directory exists')
      sys.exit(2)

if __name__=='__main__':
    ain(sys.argv[1:])
