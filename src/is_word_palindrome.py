#!/usr/bin/env python3

"""Module for src.is_word_palindrome."""

import sys


def solution(raw_word):
    word = raw_word.lower().strip()
    return all(word[i] == word[-(i + 1)] for i in range(len(word) // 2))

def solution_reversed(raw_word):
    word = raw_word.lower().strip()
    return list(word) == list(reversed(word))

def solution_slice(raw_word):
    word = raw_word.lower().strip()
    return word == word[::-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        IS_PALINDROME = "is" if solution_slice(sys.argv[1]) else "is not a"
        print(f"The word '{sys.argv[1]}' {IS_PALINDROME} palindrome")
    else:
        raise ValueError('Only one word at a time supported')
