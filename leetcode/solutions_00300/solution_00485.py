import unittest


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_ones, prev_ones = 0, 0

        for num in nums:
            if num == 1:
                running_ones += 1
            else:
                prev_ones = max(prev_ones, running_ones)
                running_ones = 0

        return max(running_ones, prev_ones)


class TestSolution(unittest.TestCase):
    def test_findMaxConsecutiveOnes(self):
        solution = Solution()
        self.assertEqual(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)


if __name__ == '__main__':
    unittest.main()
