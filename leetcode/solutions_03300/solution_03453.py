import unittest


class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total_area = 0
        high = float("-inf")
        low = float("+inf")
        for x, y, l in squares:
            total_area += l * l
            high = max(high, y + l)
            low = min(low, y)

        target = total_area / 2.0

        h = None
        for _ in range(60):
            h = (high + low) / 2.0
            below = 0
            for x, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    below += l * l
                else:
                    below += l * (h - y)

            if below >= target:
                high = h
            else:
                low = h

        return h


class TestSolution(unittest.TestCase):
    def test_separateSquares(self):
        solution = Solution()
        self.assertEqual(round(solution.separateSquares([[0, 0, 2], [1, 1, 1]]), 5), 1.16667)  # add assertion here


if __name__ == '__main__':
    unittest.main()
