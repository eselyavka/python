import unittest


class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(box)
        n = len(box[0])

        for i in range(m):
            l = r = 0
            while l < n:
                if box[i][l] == ".":
                    box[i][l], box[i][r] = box[i][r], box[i][l]
                    r += 1
                if box[i][l] == "*":
                    r = l + 1
                l += 1

        res = [[None for _ in range(m)] for _ in range(n)]
        k = 0
        for i in range(m - 1, -1, -1):
            for j in range(n):
                res[j][k] = box[i][j]
            k += 1

        return res


class TestSolution(unittest.TestCase):
    def test_rotateTheBox(self):
        solution = Solution()
        self.assertEqual(solution.rotateTheBox([["#", ".", "*", "."],
                                                ["#", "#", "*", "."]]),
                         [["#", "."],
                          ["#", "#"],
                          ["*", "*"],
                          [".", "."]])


if __name__ == '__main__':
    unittest.main()
