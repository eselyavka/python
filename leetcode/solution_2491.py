import unittest
from collections import defaultdict
from functools import reduce


class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)

        if n == 2:
            return reduce(lambda x, y: x * y, skill)

        l = 0
        r = n - 1

        skill.sort()

        d = defaultdict(list)
        while l <= r:
            sum_ = skill[l] + skill[r]
            d[sum_].append((skill[l], skill[r]))
            l += 1
            r -= 1

        if len(d) > 1:
            return -1

        return reduce(lambda x, y: x + y, [t[0] * t[1] for t in d.popitem()[1]])


class TestSolution(unittest.TestCase):
    def test_dividePlayers(self):
        solution = Solution()
        self.assertEqual(solution.dividePlayers([3, 2, 5, 1, 3, 4]), 22)


if __name__ == '__main__':
    unittest.main()
