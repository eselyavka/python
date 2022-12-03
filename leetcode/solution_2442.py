import unittest


class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def reverse(n):
            rev = 0
            while n != 0:
                mod = n % 10
                rev = rev * 10 + mod
                n = n // 10

            return rev

        ans = set()

        for num in nums:
            ans.add(num)
            rev = reverse(num)
            ans.add(rev)

        return len(ans)


class TestSolution(unittest.TestCase):
    def test_countDistinctIntegers(self):
        solution = Solution()
        self.assertEqual(solution.countDistinctIntegers([1, 13, 10, 12, 31]), 6)


if __name__ == '__main__':
    unittest.main()
