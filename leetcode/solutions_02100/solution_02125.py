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


class Solution2(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        prev_row_dev_cnt = 0
        ans = 0
        for row in bank:
            running_dev_cnt = 0
            no_beams = True
            for c in row:
                if c == "1":
                    no_beams = False
                    running_dev_cnt += 1
                    ans += prev_row_dev_cnt
            if not no_beams:
                prev_row_dev_cnt = running_dev_cnt

        return ans


class TestSolution(unittest.TestCase):
    def test_numberOfBeams(self):
        solution = Solution()
        self.assertEqual(solution.numberOfBeams(["011001", "000000", "010100", "001000"]), 8)
        
        solution2 = Solution2()
        self.assertEqual(solution2.numberOfBeams(["011001", "000000", "010100", "001000"]), 8)


if __name__ == '__main__':
    unittest.main()
