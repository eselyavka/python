#!/usr/bin/env python

import unittest


class Solution2(object):
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


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtracking(target, idx, local_ans, ans):
            local_sum = sum(local_ans)

            if idx >= len(candidates) or local_sum > target:
                return

            if local_sum == target:
                ans.append(local_ans[:])
                return

            local_ans.append(candidates[idx])

            backtracking(target, idx, local_ans, ans)

            local_ans.pop()

            backtracking(target, idx + 1, local_ans, ans)

        local_ans = []
        ans = []

        backtracking(target, 0, local_ans, ans)

        return ans


class TestSolution(unittest.TestCase):

    def test_combinationSum(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.combinationSum([2, 3, 6, 7], 7)), sorted([[7], [2, 2, 3]]))

        solution2 = Solution2()
        self.assertListEqual(sorted(solution2.combinationSum([2, 3, 6, 7], 7)), sorted([[7], [2, 2, 3]]))


if __name__ == '__main__':
    unittest.main()
