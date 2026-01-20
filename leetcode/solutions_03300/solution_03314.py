import unittest


class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                r = (num ^ (num + 1)).bit_length() - 1
                ans.append(num - (1 << (r - 1)))

        return ans


class TestSolution(unittest.TestCase):
    def test_minBitwiseArray(self):
        solution = Solution()
        self.assertListEqual(solution.minBitwiseArray([2, 3, 5, 7]), [-1, 1, 4, 3])


if __name__ == '__main__':
    unittest.main()
