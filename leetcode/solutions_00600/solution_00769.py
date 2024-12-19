import unittest


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        ans, max_so_far = 0, -1
        for i in range(n):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far == i:
                ans += 1
        return ans


class TestSolution(unittest.TestCase):
    def test_maxChunksToSorted(self):
        solution = Solution()
        self.assertEqual(solution.maxChunksToSorted([1, 0, 2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
