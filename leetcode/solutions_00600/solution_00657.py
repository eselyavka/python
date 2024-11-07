#!/usr/bin/env python

class Solution657(object):
    def judge_circle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start = [0, 0]
        for move in moves:
            if move.lower() in 'u':
                start[0] += 1
            elif move.lower() in 'd':
                start[0] -= 1
            elif move.lower() in 'r':
                start[1] += 1
            elif move.lower() in 'l':
                start[1] -= 1
            else:
                raise ValueError("inacceptable movement")
        return start == [0, 0]
