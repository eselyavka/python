import unittest


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)

        if n == 1:
            return ""

        arr = list(palindrome)
        i = 0
        while i < n:
            if arr[i] != "a":
                arr[i] = "a"
                break
            i += 1

        if "".join(arr) == "".join(arr[::-1]):
            return palindrome[:-1] + "b"

        return "".join(arr)


class TestSolution(unittest.TestCase):
    def test_breakPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.breakPalindrome("abccba"), "aaccba")


if __name__ == '__main__':
    unittest.main()
