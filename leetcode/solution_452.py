import unittest


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        if n == 1:
            return 1

        points.sort(key=lambda t: t[1])

        ans = 1
        _, pxe = points[0]
        for i in range(1, n):
            xs, xe = points[i]
            if xs <= pxe:
                continue

            ans += 1
            pxe = xe

        return ans


class TestSolution(unittest.TestCase):
    def test_findMinArrowShots(self):
        solution = Solution()
        self.assertEqual(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)


if __name__ == '__main__':
    unittest.main()
