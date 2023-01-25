import unittest
from collections import defaultdict, Counter
from itertools import combinations


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """

        h = defaultdict(list)
        for u, _, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            h[u].append(w)

        pattern = Counter()
        for k, v in h.items():
            pattern.update(set(combinations(v, 3)))

        ans = tuple(["z" * 10] * 3)
        max_ = float("-inf")
        for k, v in pattern.items():
            if v > max_:
                ans = k
                max_ = v
            if v == max_:
                ans = min(ans, k)

        return ans


class TestSolution(unittest.TestCase):
    def test_mostVisitedPattern(self):
        solution = Solution()
        self.assertTupleEqual(solution.mostVisitedPattern(
            ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            ["home", "about", "career", "home", "cart", "maps", "home",
             "home", "about", "career"]), ("home", "about", "career"))


if __name__ == '__main__':
    unittest.main()
