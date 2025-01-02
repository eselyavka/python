import unittest


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = -1
        one_cnt = 0
        for i in range(n):
            if s[i] == "1":
                one_cnt += 1
        zero_cnt = 0
        for i in range(n - 1):
            if s[i] == "0":
                zero_cnt += 1
            else:
                one_cnt -= 1

            ans = max(ans, zero_cnt + one_cnt)

        return ans


class TestSolution(unittest.TestCase):
    def test_maxScore(self):
        solution = Solution()
        self.assertEqual(solution.maxScore("011101"), 5)


if __name__ == '__main__':
    unittest.main()
