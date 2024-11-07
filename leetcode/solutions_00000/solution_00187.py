import unittest


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if len(s) <= 10:
            return []

        l, r = 0, 9
        hashmap = set()
        ans = set()

        while r < n:
            sub = s[l:r + 1]
            if sub in hashmap:
                ans.add(sub)

            hashmap.add(sub)

            l += 1
            r += 1

        return list(ans)


class TestSolution(unittest.TestCase):
    def test_findRepeatedDnaSequences(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")),
                             sorted(["AAAAACCCCC", "CCCCCAAAAA"]))


if __name__ == '__main__':
    unittest.main()
