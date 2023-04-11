import unittest


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        local_ans = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtracking(pos):
            if pos >= len(s):
                ans.append(local_ans[:])
                return

            for i in range(pos, len(s)):
                if is_palindrome(pos, i):
                    local_ans.append(s[pos:i + 1])
                    backtracking(i + 1)
                    local_ans.pop()

        backtracking(0)

        return ans


class TestSolution(unittest.TestCase):
    def test_partition(self):
        solution = Solution()
        self.assertListEqual(solution.partition("aab"), sorted([["a", "a", "b"], ["aa", "b"]]))


if __name__ == '__main__':
    unittest.main()
