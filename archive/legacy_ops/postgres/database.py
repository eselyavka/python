#!/usr/bin/env python3

"""Module for archive.legacy_ops.postgres.database."""

import logging
import random
import time

import psycopg2

# pylint: disable=too-many-arguments

logging = logging.getLogger(__name__)

class DB():
    def __init__(self, database, user, password, host, port):
        self.conn = None
        self.delay = 1
        self.maxDelay = 900
        self.factor = 0.95
        self.jitter = 0.1
        while self.delay <= self.maxDelay:
            try:
                self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
                logging.debug("Connect to db %s successfull on port %s", database, port)
                break
            except psycopg2.Error as e:
                logging.debug(
                    "Delay:%s;Can't connect to db %s on port %s(ErrCode:%s, ErrMessage:%s)",
                    self.delay,
                    database,
                    port,
                    e.pgcode,
                    e.pgerror,
                )
                time.sleep(self.delay)
                self.delay = min(self.delay * self.factor, self.maxDelay)
                self.delay = self.delay + random.gauss(self.delay, self.jitter)
                logging.debug("DelaySet:%s", self.delay)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
