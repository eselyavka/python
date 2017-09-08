#!/usr/bin/env python
import sys

def solution(raw_word):
    word = raw_word.lower().strip()
    word_len = len(word)
    equals = False
    for i in range(word_len):
        j = (i+1)/-1
        equals = word[i] == word[j]

        if not equals:
            return equals

    return equals

def solution_reversed(raw_word):
    word = raw_word.lower().strip()
    return list(word) == list(reversed(word))

def solution_slice(raw_word):
    word = raw_word.lower().strip()
    return word == word[::-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        IS_PALINDROME = "is" if solution_slice(sys.argv[1]) else "is not a"
        print "The word '{}' {} palindrome".format(sys.argv[1], IS_PALINDROME)
    else:
        raise ValueError('Only one word at a time supported')
