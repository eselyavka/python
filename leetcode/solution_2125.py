import unittest
from collections import defaultdict


class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        rows = len(bank)

        d = defaultdict(int)

        for i in range(rows):
            d[i] = bank[i].count("1")

        ans = 0

        while rows > -1:
            k = rows - 1
            while k > -1:
                if d[k]:
                    break
                k -= 1

            ans += d[rows] * d[k]
            rows -= 1

        return ans


class TestSolution(unittest.TestCase):
    def test_numberOfBeams(self):
        solution = Solution()
        self.assertEqual(solution.numberOfBeams(["011001", "000000", "010100", "001000"]), 8)


if __name__ == '__main__':
    unittest.main()
