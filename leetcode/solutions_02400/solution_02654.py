import unittest


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def gcd(a, b):
            if a == 0:
                return b

            return gcd(b % a, a)

        ones = nums.count(1)

        if ones:
            return n - ones

        best = float("inf")
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        return (best - 1) + (n - 1) if best != float("inf") else -1


class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations([2, 6, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
