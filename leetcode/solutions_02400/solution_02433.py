import unittest


class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n = len(pref)

        ans = [None for _ in range(n)]
        ans[0] = pref[0]

        for i in range(1, n):
            ans[i] = pref[i - 1] ^ pref[i]

        return ans


class TestSolution(unittest.TestCase):
    def test_findArray(self):
        solution = Solution()
        self.assertListEqual(solution.findArray([5, 2, 0, 3, 1]), [5, 7, 2, 3, 2])


if __name__ == '__main__':
    unittest.main()
