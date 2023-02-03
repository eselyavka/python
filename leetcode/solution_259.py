import unittest


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if n < 3:
            return 0

        nums.sort()
        ans = 0

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_threeSumSmaller(self):
        solution = Solution()
        self.assertEqual(solution.threeSumSmaller([-2, 0, 1, 3], 2), 2)


if __name__ == '__main__':
    unittest.main()
