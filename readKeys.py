import os
import re
import redis

pattern = re.compile('^SET$')

redisFilePath = '/var/lib/redis'
redisFileName = 'appendonly.aof'

conn = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict')

def redisDelKey( key ):
    global conn
    conn.delete(key)

def readRedisFile():
    if os.path.isfile(redisFilePath + '/' + redisFileName):
        with(open(redisFilePath + '/' + redisFileName, 'r')) as lines:
            for line in lines:
                if pattern.match(line.strip('\n')):
                    if int(lines.next().strip('\n').replace('$', '')) == 36:
                        uuid = lines.next().strip('\n')
                        redisDelKey(uuid)
                        print 'Key %s deleted' % uuid
    else:
      raise IOError, 'Check file %s exists' % redisFilePath + '/' + redisFileName

def main():
    readRedisFile()

if __name__=='__main__':
    main()
