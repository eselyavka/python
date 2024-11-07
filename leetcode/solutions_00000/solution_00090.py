import unittest


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        ans = []
        local_ans = []

        def dfs(i):
            if i >= len(nums):
                ans.append(local_ans[:])
                return

            local_ans.append(nums[i])
            dfs(i + 1)

            local_ans.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)

        return ans


class TestSolution(unittest.TestCase):
    def test_subsetsWithDup(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.subsetsWithDup([1, 2, 2])),
                             sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
