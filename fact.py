"""Different factorial functions implementations"""

import timeit
import math

def fact1(number):
    """Function one"""
    if number < 1:
        return 1
    else:
        fact = number*fact1(number-1)
        return fact

def fact2(xrange_list):
    """Function two"""
    if not xrange_list:
        return 1
    else:
        return xrange_list[0] * fact2(xrange_list[1:])

def fact3(number):
    """Function three"""
    return reduce(lambda x, y: x*y, [x for x in xrange(1, number+1)])

def fact4(number):
    """Function four"""
    fact = 1
    for x in xrange(1, number+1):
        fact = fact*x
    return fact

def fact5(number):
    """Function five"""
    return math.factorial(number)

def wrapper(func, *vargs, **kwargs):
    """Wrap factorial function with arguments
       to function without argument for further
       passing into timeit module"""
    def wrapped():
        """Executes factorial function with arguments"""
        return func(*vargs, **kwargs)
    return wrapped

FACTORIAL_NUMBER = 6

WRAPPED_FACT1 = wrapper(fact1, FACTORIAL_NUMBER)
WRAPPED_FACT2 = wrapper(fact2, [x for x in xrange(1, FACTORIAL_NUMBER+1)])
WRAPPED_FACT3 = wrapper(fact3, FACTORIAL_NUMBER)
WRAPPED_FACT4 = wrapper(fact4, FACTORIAL_NUMBER)
WRAPPED_FACT5 = wrapper(fact5, FACTORIAL_NUMBER)

RESULT = dict()

RESULT[fact1.__name__] = timeit.timeit(WRAPPED_FACT1, number=100000)
RESULT[fact2.__name__] = timeit.timeit(WRAPPED_FACT2, number=100000)
RESULT[fact3.__name__] = timeit.timeit(WRAPPED_FACT3, number=100000)
RESULT[fact4.__name__] = timeit.timeit(WRAPPED_FACT4, number=100000)
RESULT[fact5.__name__] = timeit.timeit(WRAPPED_FACT5, number=100000)

print RESULT
