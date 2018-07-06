#!/usr/bin/python

import sys

def permutate(word):
    res = set()

    def _exchange(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        res.add(''.join(arr))

    def _permutate(arr, l, r):
        if l == r:
            return
        else:
            for i in range(l, r+1):
                _exchange(arr, i, l)
                _permutate(arr, l+1, r)
                _exchange(arr, i, l)

    arr_word = list(word)

    _permutate(arr_word, 0, len(arr_word) - 1)

    return res

if __name__ == '__main__':
    if len(sys.argv) > 2:
        T = int(sys.argv[1])
        for t in range(1, T+1):
            _word = sys.argv[1+t].upper()
            result = permutate(_word)
            print "Source Word: '{}'\n{}".format(
                _word,
                "\n".join(sorted(result)))
    else:
        raise ValueError('Please provide number of tries and word(s)')
