import unittest
from collections import Counter


class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        if num == ("0" * len(num)):
            return "0"

        cnt = Counter(num)
        m = len(num)
        ans = ["" for _ in range(m)]

        l = 0
        r = m - 1
        mid = None
        for i in "9876543210":
            if i in cnt:
                occ = cnt[i]
                # even
                if occ % 2 == 0:
                    while occ != 0:
                        ans[l] = i
                        ans[r] = i
                        occ -= 2
                        l += 1
                        r -= 1
                # odd
                else:
                    if mid is None:
                        mid = m // 2
                        ans[mid] = i
                    occ -= 1
                    while occ != 0:
                        ans[l] = i
                        ans[r] = i
                        occ -= 2
                        l += 1
                        r -= 1
        l = 0
        r = m - 1
        i = 0

        while i < m:
            if ans[l] == "0":
                ans[l] = ""
                ans[r] = ""
                l += 1
                r -= 1
            i += 1

        return "".join(ans)


class TestSolution(unittest.TestCase):
    def test_largestPalindromic(self):
        solution = Solution()
        self.assertEqual(solution.largestPalindromic("444947137"), "7449447")


if __name__ == '__main__':
    unittest.main()
