import unittest


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []
        local_ans = []

        n = len(candidates)

        candidates.sort()

        def backtracking(pos):
            if sum(local_ans) > target:
                return

            if sum(local_ans) == target:
                ans.append(local_ans[:])
                return

            prev = -1
            for i in range(pos, n):
                if prev == candidates[i]:
                    continue

                local_ans.append(candidates[i])
                backtracking(i + 1)
                local_ans.pop()

                prev = candidates[i]

        backtracking(0)

        return ans


class TestSolution(unittest.TestCase):
    def test_combinationSum2(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)), sorted([
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]))


if __name__ == '__main__':
    unittest.main()
