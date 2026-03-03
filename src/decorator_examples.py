#!/usr/bin/env python3

"""Module for src.decorator_examples."""

from functools import wraps

def my_dec2(func):
    @wraps(func)
    def wrapped(*args):
        print('call to my_dec2')
        return func(*args)
    return wrapped

def my_dec(func):
    @wraps(func)
    def wrapped(*args):
        print('call to my_dec')
        return func(*args)
    return wrapped

@my_dec
@my_dec2
def spam(a, b, c):
    return a + b + c
