import unittest


class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def gcd(a, b):
            if a == 0:
                return b

            return gcd(b % a, a)

        n = len(nums)
        ans, curr = 0, 0

        for i in range(n):
            ans += int(nums[i] == k)
            curr = nums[i]
            for j in range(i + 1, n):
                curr = gcd(curr, nums[j])
                if curr == k:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_subarrayGCD(self):
        solution = Solution()
        self.assertEqual(solution.subarrayGCD([9, 3, 1, 2, 6, 3], 3), 4)


if __name__ == '__main__':
    unittest.main()
