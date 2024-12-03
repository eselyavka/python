import unittest


class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans = [""] * (len(s) + len(spaces))

        space_idx = 0
        string_idx = 0
        i = 0
        while i < len(s):
            if space_idx < len(spaces) and i == spaces[space_idx]:
                ans[string_idx] = " "
                string_idx += 1
                space_idx += 1
            ans[string_idx] = s[i]
            i += 1
            string_idx += 1

        return "".join(ans)


class TestSolution(unittest.TestCase):
    def test_addSpaces(self):
        solution = Solution()
        self.assertEqual(solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]), "Leetcode Helps Me Learn")


if __name__ == '__main__':
    unittest.main()
