import unittest


class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        arr_vertical = sorted(rectangles, key=lambda rect: rect[0])
        arr_horizontal = sorted(rectangles, key=lambda rect: rect[1])

        end_x = arr_vertical[0][2]
        res_vert = 0
        for i in range(1, len(rectangles)):
            start_x = arr_vertical[i][0]
            if start_x >= end_x:
                res_vert += 1
            end_x = max(end_x, arr_vertical[i][2])

        end_y = arr_horizontal[0][3]
        res_hor = 0
        for i in range(1, len(rectangles)):
            start_y = arr_horizontal[i][1]
            if start_y >= end_y:
                res_hor += 1
            end_y = max(end_y, arr_horizontal[i][3])

        return res_vert >= 2 or res_hor >= 2


class TestSolution(unittest.TestCase):
    def test_checkValidCuts(self):
        solution = Solution()
        self.assertTrue(solution.checkValidCuts(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))


if __name__ == '__main__':
    unittest.main()
