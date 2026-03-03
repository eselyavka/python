#!/usr/bin/env python3

"""Module for archive.legacy_ops.integration.read_keys."""

# pylint: disable=import-error

import os
import re
import redis

pattern = re.compile('^SET$')

redisFilePath = '/var/lib/redis'
redisFileName = 'appendonly.aof'

conn = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict')

def redisDelKey(key):
    conn.delete(key)

def readRedisFile():
    if os.path.isfile(redisFilePath + '/' + redisFileName):
        with open(redisFilePath + '/' + redisFileName, 'r', encoding='utf-8') as lines:
            for line in lines:
                if pattern.match(line.strip('\n')):
                    if int(next(lines).strip('\n').replace('$', '')) == 36:
                        uuid = next(lines).strip('\n')
                        redisDelKey(uuid)
                        print(f'Key {uuid} deleted')
    else:
        raise IOError(f'Check file {redisFilePath}/{redisFileName} exists')

def main():
    readRedisFile()

if __name__ == '__main__':
    main()
