import unittest


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        m = len(nums)
        i = 0

        while i < m:
            if nums[i] == 0:
                n = 0
                k = i
                while k < len(nums) and nums[k] == 0:
                    n += 1
                    k += 1

                ans += (n * (n + 1)) / 2
                i = k
                continue
            i += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_zeroFilledSubarray(self):
        solution = Solution()
        self.assertEqual(solution.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]), 6)


if __name__ == '__main__':
    unittest.main()
