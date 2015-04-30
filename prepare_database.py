#!/usr/bin/env python

import os
import sys
import getopt
import re
import fileinput
import logging
from ExtractFile import ExtractFile 
from FileOperations import FileOperations

logging.basicConfig(filename='prepare_database.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def process_config(config, logFileName, port='5433'):
    with open(config, 'r+') as fconf:
      lines = fconf.readlines()
      fconf.seek(0)
      fconf.truncate()
      for line in lines:
        if (re.search(r'^[#]?port.+', line)):
            fconf.write(re.sub(r'^[#]?port.+', 'port = ' + port, line))
        elif (re.search(r'^[#]?log_filename.+', line)):
            fconf.write(re.sub(r'^[#]?log_filename.+', 'log_filename = \'postgresql-' + logFileName + '.log\'', line))
        elif (re.search(r'^[#]?stats_temp_directory.+', line)):
            fconf.write(re.sub(r'^[#]?stats_temp_directory.+', 'stats_temp_directory = \'/ramdisk/pgstat/' + logFileName + '\'', line))
        else:
            fconf.write(line)

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
        ExtractFile(BaseBackupArch, Directory)

        logging.info('Succefully extracted basebackup archive file: %s into directory: %s' % (BaseBackupArch, Directory))
        fop = FileOperations(Directory)

        if DatabaseUser and DatabaseGroup:
          fop.setFileOwner(DatabaseUser, DatabaseGroup)
          fop.setFilePerm()
        elif DatabaseUser:
          fop.setFileOwner(user=DatabaseUser)
          fop.setFilePerm()
        elif DatabaseGroup:
          fop.setFileOwner(group=DatabaseGroup)
          fop.setFilePerm()
        else:
          fop.setFileOwner()
          fop.setFilePerm()

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
                if Directory.endswith('/'):
                    process_config(config=PostgresConfig, logFileName=Directory.split('/')[-2], port=PostgresPort)
                else:
                    process_config(config=PostgresConfig, logFileName=Directory.split('/')[-1], port=PostgresPort)
            else:
                if PostgresPort:
                    if Directory.endswith('/'):
                        process_config(config=PostgresConfig, logFileName=Directory.split('/')[-2])
                    else:
                        process_config(config=PostgresConfig, logFileName=Directory.split('/')[-1])
          else:
            logging.error('%s no such file' % PostgresConfig)
      else:
        logging.error('Check archive file or directory have an absolute path')
        sys.exit(2)
    else:
      logging.error('Check archive file or directory exists')
      sys.exit(2)

if __name__=='__main__':
    main(sys.argv[1:])
