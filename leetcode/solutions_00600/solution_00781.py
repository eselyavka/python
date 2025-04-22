import unittest
from collections import Counter


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        c = Counter(answers)
        ans = 0
        for k, v in c.items():
            group_size = k + 1
            num_groups = (v + group_size - 1) / group_size
            ans += num_groups * group_size
        return ans


class TestSolution(unittest.TestCase):
    def test_numRabbits(self):
        solution = Solution()
        self.assertEqual(solution.numRabbits([1, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
