import unittest


class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """

        n = len(heights)

        while volume > 0:
            idx = k

            # left
            while idx > 0 and heights[idx] >= heights[idx - 1]:
                idx -= 1

            # right
            while idx < n - 1 and heights[idx] >= heights[idx + 1]:
                idx += 1

            # left
            while idx > k and heights[idx] >= heights[idx - 1]:
                idx -= 1

            heights[idx] += 1
            volume -= 1

        return heights


class TestSolution(unittest.TestCase):
    def test_pourWater(self):
        solution = Solution()
        self.assertListEqual(solution.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3), [2, 2, 2, 3, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
