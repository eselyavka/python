#!/usr/bin/env python

import unittest

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {1: "1",
             2: "11",
             3: "21",
             4: "1211",
             5: "111221",
             6: "312211",
             7: "13112221",
             8: "1113213211",
             9: "31131211131221",
             10: "13211311123113112211"}

        if n in d:
            return d[n]

        def calc(num):
            i, size = 1, len(num)
            res = ''
            cnt = 1
            while i < size:
                if num[i-1] != num[i]:
                    res += str(cnt) + num[i-1]
                    cnt = 1
                else:
                    cnt += 1

                if i == size - 1:
                    res += str(cnt) + num[i]

                i += 1

            return res

        prev = None

        for i in range(10, n+1):
            if not prev:
                prev = d[i]
            else:
                prev = calc(prev)

        return prev

class TestSolution(unittest.TestCase):
    def test_countAndSay(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(1), "1")
        self.assertEqual(solution.countAndSay(4), "1211")
        self.assertEqual(solution.countAndSay(11),
                         "11131221133112132113212221")
        self.assertEqual(solution.countAndSay(15),
                         "311311222113111231131112132112311321322112111312211312111322212311322113212221")

if __name__ == '__main__':
    unittest.main()
