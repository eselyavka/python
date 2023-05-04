import unittest
from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)

        R = deque()
        D = deque()

        for idx, c in enumerate(senate):
            if c == "R":
                R.append(idx)
            else:
                D.append(idx)

        while R and D:
            r_idx = R.popleft()
            d_idx = D.popleft()

            if r_idx < d_idx:
                R.append(r_idx + n)
            else:
                D.append(d_idx + n)

        return "Radiant" if R else "Dire"


class TestSolution(unittest.TestCase):
    def test_predictPartyVictory(self):
        solution = Solution()
        self.assertEqual(solution.predictPartyVictory("RDD"), "Dire")


if __name__ == '__main__':
    unittest.main()
