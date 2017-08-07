#!/usr/bin/python

import sys

def _exchange(arr, i, j, acc):
    arr[i], arr[j] = arr[j], arr[i]
    acc.add(''.join(arr))

def _exchanger(arr, i, j, acc):
    if i == j:
        pass
    else:
        for k in range(i, j+1):
            _exchange(arr, i, k, acc)
            _exchanger(arr, i+1, j, acc)
            _exchange(arr, i, k, acc)

def permutation(word):
    mas = list(word)
    mas_size = len(mas)
    acc = set()
    _exchanger(mas, 0, (mas_size - 1), acc)
    return acc

if __name__ == '__main__':
    if len(sys.argv) > 2:
        T = int(sys.argv[1])
        for t in range(1, T+1):
            _word = sys.argv[1+t].upper()
            res = permutation(_word)
            print "Source Word: '{}'\n{}".format(
                _word,
                "\n".join(sorted(res)))
    else:
        raise ValueError('Please provide number of tries and word(s)')
