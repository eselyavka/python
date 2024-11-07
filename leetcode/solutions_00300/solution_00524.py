#!/usr/bin/env python

import unittest

class Solution(object):

    def isSubstring(self, s, ds):
        if not (s or ds):
            return False

        j = 0

        for i in range(len(s)):
            if j == len(ds):
                return True

            if s[i] == ds[j]:
                j += 1
        return len(ds) == j

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        res = ''

        d.sort()

        for item in d:
            if len(item) > len(res):
                if self.isSubstring(s, item):
                    res = item
        return res

class TestSolution(unittest.TestCase):

    def test_findLongestWord(self):
        s = "abpcplea"
        d = ["ale", "apple", "monkey", "plea"]

        s1 = "abpcplea"
        d1 = ["a", "b", "c"]

        s2 = "ssss"
        d2 = []

        s3 = ""
        d3 = ["a", "b", "c"]

        s4 = "aaa"
        d4 = ["aaa", "aa", "a"]

        s5 = "aewfafwafjlwajflwajflwafj"
        d5 = ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]

        s6 = "okbmfyugqqongobwofraotanviqjraaktmmwyxzdnnwwaqsnvfxwngglybtiqwblprgvbgmolotnppzbovnstxmcmocixresdpojmntcdkyjzgbhhigkiyatrgzayivjyqiopvvdftkbsgwgnidsecvydvltaxxywydawrsseyolixznuyhjolngdsmjhepregixtklanjjggzssrbtmhhpamcfeghgssmrjrpelabojfhkdfvscjwhqxubwrhryqmtkiksljezeembngdjyhgmdzahxvvpkqwvhkqlensuxbrcdctqojqnlogjbpovdsbvurwcoehtmtkwxswrwhszuyesdqspnwqxlmjxrbdqbnbbyxhhlabxrdjxtjgpugojsexmrhrfzryapdzglalqzuzfpxeaemjkyfhpbnmdxjtxnxyjecfsapcjyglmtivnsfalpxzdkylgcixjljaqjwminyaodeekpzzpchhceguzayeul"
        d6 = ["zwdtunyhlcvcyisvbdkkdyllvclyibsxeultrxwbqvvckxvlxczprqjhtufyeghmvcwyghnnaqgfhvynmhhmnqbdffbsudebahyyzhyqlslqptnpzjmusrdawpgfasmzggekczmorgxmvozodbemygtlqgoqjuhdfjilrcofkhhhbdrbkbhzdgjnytbldbsfzrnzmmnezecowchvefzidbfxampshxqjaqkufvsmkaetswxvlozpralniascugwratxuvkbfeevrhhoudfogpwokacspazysfnxprecwhozmwselunjvyvbdrquozjisjmba", "mfuraildmrjhdjtctdxejgdurr"]

        solution = Solution()
        self.assertEqual(solution.findLongestWord(s, d), "apple")
        self.assertEqual(solution.findLongestWord(s1, d1), "a")
        self.assertEqual(solution.findLongestWord(s2, d2), "")
        self.assertEqual(solution.findLongestWord(s3, d3), "")
        self.assertEqual(solution.findLongestWord(s4, d4), "aaa")
        self.assertEqual(solution.findLongestWord(s5, d5), "ewaf")
        self.assertEqual(solution.findLongestWord(s6, d6), "mfuraildmrjhdjtctdxejgdurr")

if __name__ == '__main__':
    unittest.main()
