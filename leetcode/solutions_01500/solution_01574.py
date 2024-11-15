import unittest


class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        if n == 1:
            return 0

        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        if right == 0:
            return 0

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left] >= arr[left - 1]):
            while right < n and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_findLengthOfShortestSubarray(self):
        solution = Solution()
        self.assertEqual(solution.findLengthOfShortestSubarray([6, 3, 10, 11, 15, 20, 13, 3, 18, 12]), 8)


if __name__ == '__main__':
    unittest.main()
