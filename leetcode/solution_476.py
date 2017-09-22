#!/usr/bin/env python

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        complement = b''
        for bit in bin(num)[2:]:
            if bit == '1':
                complement += b'0'
            else:
                complement += b'1'
        return int(complement, 2)
