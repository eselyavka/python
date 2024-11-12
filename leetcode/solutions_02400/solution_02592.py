import unittest


class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        res = 0
        for num in nums:
            if num > nums[res]:
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def test_maximizeGreatness(self):
        solution = Solution()
        self.assertEqual(solution.maximizeGreatness([1, 3, 5, 2, 1, 3, 1]), 4)


if __name__ == '__main__':
    unittest.main()
