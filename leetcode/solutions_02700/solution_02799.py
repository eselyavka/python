import unittest


class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(set(nums))
        n = len(nums)
        ans = 0
        for i in range(n - k + 1):
            sub_arr = {nums[i]}
            for j in range(i + 1, n):
                if len(sub_arr) == k:
                    ans += 1
                sub_arr.add(nums[j])

            if len(sub_arr) == k:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countCompleteSubarrays(self):
        solution = Solution()
        actual = solution.countCompleteSubarrays([1, 3, 1, 2, 2])
        self.assertEqual(actual, 4)


if __name__ == '__main__':
    unittest.main()
