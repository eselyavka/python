import unittest


class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        row_freq = {i: 0 for i in range(m)}
        col_freq = {j: 0 for j in range(n)}

        vals = {}
        for i in range(m):
            for j in range(n):
                vals[mat[i][j]] = (i, j)

        ans = 0
        for idx, item in enumerate(arr):
            x, y = vals[item]
            row_freq[x] += 1
            col_freq[y] += 1
            if row_freq[x] == n or col_freq[y] == m:
                return idx

        return ans


class TestSolution(unittest.TestCase):
    def test_firstCompleteIndex(self):
        solution = Solution()
        self.assertEqual(solution.firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]), 2)


if __name__ == '__main__':
    unittest.main()
