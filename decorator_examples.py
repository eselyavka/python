#!/usr/bin/env python

def my_dec2(func):
    def wrapped(*args):
        print 'call to my_dec2'
        return func(*args)
    return wrapped

def my_dec(func):
    def wrapped(*args):
        print 'call to my_dec'
        return func(*args)
    return wrapped

@my_dec
@my_dec2
def spam(a,b,c):
    return a+b+c
