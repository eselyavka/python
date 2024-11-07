import bisect
import unittest


class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        candles = []
        for idx, c in enumerate(s):
            if c == "|":
                candles.append(idx)

        ans = []
        for query in queries:
            start, end = query

            start_idx = bisect.bisect_left(candles, start)
            end_idx = bisect.bisect(candles, end) - 1

            if end_idx <= start_idx:
                ans.append(0)
                continue

            ans.append(candles[end_idx] - candles[start_idx] - (end_idx - start_idx))

        return ans


class TestSolution(unittest.TestCase):
    def test_platesBetweenCandles(self):
        solution = Solution()
        self.assertListEqual(solution.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]), [2, 3])


if __name__ == '__main__':
    unittest.main()
