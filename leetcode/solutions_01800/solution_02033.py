import unittest


class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flatten = sorted([num for row in grid for num in row])
        rem = flatten[0] % x

        for num in flatten:
            if num % x != rem:
                return -1

        mid_idx = len(flatten) // 2

        goal = flatten[mid_idx]
        ops = 0
        for num in flatten:
            ops += abs(goal - num) // x

        return ops


class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations([[2, 4], [6, 8]], 2), 4)


if __name__ == '__main__':
    unittest.main()
