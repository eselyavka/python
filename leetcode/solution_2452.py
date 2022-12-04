import unittest


class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """

        def compare(s1, s2):
            i = 0
            edits = 0
            while i < len(s1):
                if s1[i] != s2[i]:
                    edits += 1
                    if edits > 2:
                        return -1
                i += 1

            return edits

        ans = []
        for q in queries:
            flag = False
            for d in dictionary:
                q_cmp = compare(q, d)
                if q_cmp >= 0:
                    flag = True
            if flag:
                ans.append(q)

        return ans


class TestSolution(unittest.TestCase):
    def test_twoEditWords(self):
        solution = Solution()
        self.assertListEqual(solution.twoEditWords(["word", "note", "ants", "wood"],
                                                   ["wood", "joke", "moat"]),
                             ["word", "note", "wood"])


if __name__ == '__main__':
    unittest.main()
