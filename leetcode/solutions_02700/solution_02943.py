import unittest


class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        hBars.sort()
        vBars.sort()

        best = 1
        curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1

            best = max(best, curr)

        hGap = best + 1

        best = 1
        curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1

            best = max(best, curr)

        vGap = best + 1

        ans = min(hGap, vGap)

        return ans * ans


class TestSolution(unittest.TestCase):
    def test_maximizeSquareHoleArea(self):
        solution = Solution()
        self.assertEqual(solution.maximizeSquareHoleArea(3, 13, [2, 4, 3], [4, 6, 7, 12, 10, 13, 2]), 9)


if __name__ == '__main__':
    unittest.main()
