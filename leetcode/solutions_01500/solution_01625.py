import unittest


class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        seen = set()

        def dfs(s, a, b):
            if s in seen:
                return

            rotate_op_applied = s[n - b:] + s[:n - b]

            arr_s = list(s)

            for idx, c in enumerate(arr_s):
                if idx % 2 == 1:
                    add_op = str((int(c) + a) % 10)
                    arr_s[idx] = add_op

            add_op_applied = ''.join(arr_s)

            seen.add(s)

            dfs(rotate_op_applied, a, b)
            dfs(add_op_applied, a, b)

        dfs(s, a, b)

        return min(seen)


class TestSolution(unittest.TestCase):
    def test_findLexSmallestString(self):
        solution = Solution()
        self.assertEqual(solution.findLexSmallestString("5525", 9, 2), "2050")


if __name__ == '__main__':
    unittest.main()
