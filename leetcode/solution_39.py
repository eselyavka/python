#!/usr/bin/env python

import unittest


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        count_of_candidate = [0 for _ in range(len(candidates))]

        def perebor(k, current_target, candidates, count_of_candidate, res):
            if k == len(candidates):
                if current_target == 0:
                    buf = []
                    for i, candidate in enumerate(candidates):
                        for _ in range(count_of_candidate[i]):
                            buf.append(candidate)
                    res.append(buf)
                return

            count_of_candidate[k] = 0

            while current_target - count_of_candidate[k] * candidates[k] >= 0:
                perebor(k + 1,
                        current_target - count_of_candidate[k] * candidates[k],
                        candidates,
                        count_of_candidate,
                        res)
                count_of_candidate[k] += 1

        perebor(0, target, candidates, count_of_candidate, res)

        return res


class TestSolution(unittest.TestCase):

    def test_combinationSum(self):
        solution = Solution()
        self.assertListEqual(solution.combinationSum([2, 3, 6, 7], 7), [[7], [2, 2, 3]])


if __name__ == '__main__':
    unittest.main()
