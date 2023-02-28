import unittest
from collections import Counter


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        if len(tasks) == 1:
            return -1

        freq = Counter(tasks)

        ans = 0

        for cnt in freq.values():
            if cnt == 1:
                return -1

            if cnt % 3 == 0:
                ans += cnt // 3
            else:
                ans += cnt // 3 + 1

        return ans


class TestSolution(unittest.TestCase):
    def test_minimumRounds(self):
        solution = Solution()
        self.assertEqual(solution.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
