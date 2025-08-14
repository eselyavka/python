import unittest


class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)

        res = ""
        for i in range(n - 2):
            s = num[i:i + 3]
            if s[0] == s[1] == s[2] and s > res:
                res = s
        return res


class TestSolution(unittest.TestCase):
    def test_largestGoodInteger(self):
        solution = Solution()
        self.assertEqual(solution.largestGoodInteger("6777133339"), "777")


if __name__ == '__main__':
    unittest.main()
