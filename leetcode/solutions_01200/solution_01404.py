import unittest


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """

        steps = 0
        carry = 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            bit = (ord(s[i]) - ord("0")) + carry

            if not bit % 2:
                steps += 1
            else:
                steps += 2
                carry = 1

        return steps + carry


class TestSolution(unittest.TestCase):
    def test_numSteps(self):
        solution = Solution()
        self.assertEqual(solution.numSteps("1101"), 6)


if __name__ == '__main__':
    unittest.main()
