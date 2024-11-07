import unittest


class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = set()

        def rec(i, k, n, acc, ans):
            if len(acc) == n:
                ans.add(acc)
                return

            if not 0 <= i < 10:
                return

            acc += str(i)

            rec(i + k, k, n, acc, ans)
            rec(i - k, k, n, acc, ans)

        for i in range(1, 10):
            rec(i, k, n, "", ans)

        return [int(x) for x in ans]


class TestSolution(unittest.TestCase):
    def test_numsSameConsecDiff(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.numsSameConsecDiff(3, 7)), [181, 292, 707, 818, 929])


if __name__ == '__main__':
    unittest.main()
