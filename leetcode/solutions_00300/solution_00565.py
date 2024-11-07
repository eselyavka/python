#!/usr/bin/env python

import unittest
import sys
from functools import wraps
import time

sys.path.append('/Users/eseliavka/tmp/')
IS_BIG_ARR = True

try:
    from arr import BIG_ARR
except ImportError:
    IS_BIG_ARR = False

def timing(func):
    @wraps(func)
    def wrapper(*args, **kw_args):
        start = time.time()
        res = func(*args, **kw_args)
        diff = time.time() - start

        print 'Elapsed {}'.format(diff)

        return res

    return wrapper

class Solution(object):
    def dfs(self, nums, idx):
        visited, stack = set(), [idx]
        while stack:
            num = stack.pop()
            if num not in visited:
                visited.add(num)
                num = nums[num]
                stack.append(num)

        return visited

    @timing
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            _dfs = self.dfs(nums, num)
            visited = visited | _dfs
            res = max(res, len(_dfs))

        return res

class TestSolution(unittest.TestCase):

    def test_arrayNesting(self):
        solution = Solution()
        self.assertEqual(solution.arrayNesting([5, 4, 0, 3, 1, 6, 2]), 4)
        self.assertEqual(solution.arrayNesting([0, 2, 1]), 2)
        if IS_BIG_ARR:
            self.assertEqual(solution.arrayNesting(BIG_ARR), 7011)

if __name__ == '__main__':
    unittest.main()
