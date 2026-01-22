import unittest


class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        def check_is_non_decreasing(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i] < arr[i - 1]:
                    return False

            return True

        while not check_is_non_decreasing(nums) and len(nums) > 1:
            min_ = float("+inf")
            idxs = None
            for i in range(1, len(nums)):
                s = nums[i - 1] + nums[i]
                if s < min_:
                    idxs = (i - 1, i)
                    min_ = s
            x, y = idxs
            nums = nums[:x] + [nums[x] + nums[y]] + nums[y + 1:]
            ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_minimumPairRemoval(self):
        solution = Solution()
        self.assertEqual(solution.minimumPairRemoval([5, 2, 3, 1]), 2)


if __name__ == '__main__':
    unittest.main()
