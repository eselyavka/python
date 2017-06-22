import unittest

class Solution(object):

    def __init__(self):
        self.core_types = [int, float, long]

    def isNumber(self, s, core_types=None):
        """
        :type s: str
        :rtype: bool
        """

        if core_types is None:
            core_types = self.core_types

        if core_types:
            try:
                for t in core_types:
                    if t(s.strip()) or t(s.strip()) == 0:
                        return True
            except ValueError:
                return self.isNumber(s, core_types[1:])
        return False

class TestSolution(unittest.TestCase):

    def test_is_number(self):
        solution = Solution()
        self.assertTrue(all([solution.isNumber(n) for n in ["0", " 0.1", "2e10"]]))

    def test_is_NaN(self):
        solution = Solution()
        self.assertFalse(reduce(
            lambda x, y: x and y,
            [solution.isNumber(n) for n in ["abc", "1 a"]]))

if __name__ == '__main__':
    unittest.main()
