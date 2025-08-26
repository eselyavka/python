import unittest


class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        diag_length = -1.0
        ans = -1.0
        for item in dimensions:
            length, width = item
            curr_diag_length = (length ** 2 + width ** 2) ** 0.5
            if curr_diag_length > diag_length:
                diag_length = curr_diag_length
                ans = length * width
            elif curr_diag_length == diag_length and ans < length * width:
                ans = length * width

        return ans


class TestSolution(unittest.TestCase):
    def test_areaOfMaxDiagonal(self):
        solution = Solution()
        self.assertEqual(solution.areaOfMaxDiagonal([[9, 3], [8, 6]]), 48)


if __name__ == '__main__':
    unittest.main()
