#!/usr/bin/env python
import sys
import timeit

def wrapper(func, *args, **kwds):
    def wrapped():
        return func(*args, **kwds)
    return wrapped

def recursion_lcs(seq1, seq2, m, n):
    if m == 0 or n == 0:
        return 0
    elif seq1[m-1] == seq2[n-1]:
        return 1 + recursion_lcs(seq1, seq2, m-1, n-1)
    else:
        return max(recursion_lcs(seq1, seq2, m, n-1), recursion_lcs(seq1, seq2, m-1, n))

def lcs(seq1, seq2):
    dict_letters = {letter:None for letter in seq1}

    cnt = 0
    for letter in seq2:
        if dict_letters.has_key(letter):
            cnt += 1
    return cnt

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError

    CALL_COUNT = 10000
    W_LCS = wrapper(lcs, sys.argv[1], sys.argv[2])
    W_RECURSION_LCS = wrapper(recursion_lcs,
                              sys.argv[1],
                              sys.argv[2],
                              len(sys.argv[1]),
                              len(sys.argv[2]))
    print timeit.timeit(W_LCS, number=CALL_COUNT)
    print timeit.timeit(W_RECURSION_LCS, number=CALL_COUNT)
