import unittest


class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero_cnt = s.count("0")
        one_cnt = 0

        ans = len(s) - zero_cnt

        for c in s:
            if c == "0":
                zero_cnt -= 1
            else:
                ans = min(ans, zero_cnt + one_cnt)
                one_cnt += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_minFlipsMonoIncr(self):
        solution = Solution()
        self.assertEqual(solution.minFlipsMonoIncr("00110"), 1)


if __name__ == '__main__':
    unittest.main()
