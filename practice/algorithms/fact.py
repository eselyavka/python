#!/usr/bin/env python3

"""Different factorial function implementations."""

from functools import reduce
import math
import operator
import timeit


def fact1(number):
    """Recursive factorial."""
    if number < 1:
        return 1
    return number * fact1(number - 1)


def fact2(numbers):
    """Recursive factorial over a sequence."""
    if not numbers:
        return 1
    return numbers[0] * fact2(numbers[1:])


def fact3(number):
    """Factorial using reduce."""
    return reduce(operator.mul, range(1, number + 1), 1)


def fact4(number):
    """Iterative factorial."""
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


def fact5(number):
    """Stdlib factorial."""
    return math.factorial(number)


def wrapper(func, *args, **kwargs):
    """Bind arguments for timeit."""

    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def benchmark(number=6, iterations=100000):
    """Return benchmark timings for each implementation."""
    wrapped_fact1 = wrapper(fact1, number)
    wrapped_fact2 = wrapper(fact2, list(range(1, number + 1)))
    wrapped_fact3 = wrapper(fact3, number)
    wrapped_fact4 = wrapper(fact4, number)
    wrapped_fact5 = wrapper(fact5, number)

    return {
        fact1.__name__: timeit.timeit(wrapped_fact1, number=iterations),
        fact2.__name__: timeit.timeit(wrapped_fact2, number=iterations),
        fact3.__name__: timeit.timeit(wrapped_fact3, number=iterations),
        fact4.__name__: timeit.timeit(wrapped_fact4, number=iterations),
        fact5.__name__: timeit.timeit(wrapped_fact5, number=iterations),
    }


if __name__ == "__main__":
    print(benchmark())
