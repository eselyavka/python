import unittest


class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """

        def to_min(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        start = to_min(loginTime)
        end = to_min(logoutTime)

        if end < start:
            end += 24 * 60

        start = ((start + 14) // 15) * 15
        end = (end // 15) * 15

        return max(0, (end - start) // 15)


class TestSolution(unittest.TestCase):
    def test_numberOfRounds(self):
        solution = Solution()
        self.assertEqual(solution.numberOfRounds("09:31", "10:14"), 1)


if __name__ == '__main__':
    unittest.main()
