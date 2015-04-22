import psycopg2
import random
import logging
import time

logging = logging.getLogger(__name__)

class DB():
    conn = None
    delay = 0.1
    maxDelay = 900
    factor = 2.7
    jitter = 0.1

    def __init__(self, database, user, password, host, port):
        while (self.delay <= self.maxDelay):
            try:
                self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
                logging.debug("Connect to db %s successfull on port %s" % (database,port))
                break
            except psycopg2.Error, e:
                logging.debug("Delay:%s;Can't connect to db %s on port %s(ErrCode:%s, ErrMessage:%s)" % (str(self.delay),database,port,e.pgcode,e.pgerror))
                time.sleep(self.delay)
                self.delay = min(self.delay*self.factor, self.maxDelay)
                self.delay = self.delay + random.normalvariate(self.delay, self.jitter)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
