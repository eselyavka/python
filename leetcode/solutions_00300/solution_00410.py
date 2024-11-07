import unittest


class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) == k:
            return max(nums)

        def binary_search(target, nums, k):
            cnt = 1
            sub_sum = 0

            for num in nums:
                if num > target:
                    return False

                sub_sum += num

                if sub_sum > target:
                    cnt += 1
                    sub_sum = num

            if cnt <= k:
                return True

            return False

        start = max(nums)
        end = sum(nums)

        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if binary_search(mid, nums, k):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans


class TestSolution(unittest.TestCase):
    def test_splitArray(self):
        solution = Solution()
        self.assertEqual(solution.splitArray([7, 2, 5, 10, 8], 2), 18)


if __name__ == '__main__':
    unittest.main()
