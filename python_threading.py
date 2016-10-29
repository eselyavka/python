#!/usr/bin/env python
"""
Simple threading example with gettid support.
"""

import threading
import ctypes
import time

class Worker(threading.Thread):
    def __init__(self, name, sleep_time, syscall):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time
        self.syscall = syscall
    def run(self):
        print "Starting " + self.name + " pid: " + str(self.syscall(186))
        task(self.sleep_time)
        print "Exiting " + self.name

def task(delay):
    time.sleep(delay)

def main():
    """
    CLI entry point.
    """
    libc = ctypes.CDLL(None)
    syscall = libc.syscall
    threads = [Worker("thread_{0}".format(i),
                      60,
                      syscall) for i in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
