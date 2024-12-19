import heapq
import unittest
from collections import Counter
from string import ascii_lowercase


class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        cnt = Counter(s)
        heap = []

        for c in cnt:
            idx = ord("a") - ord(c)
            heapq.heappush(heap, (idx, cnt[c]))

        ans = ""
        while heap:
            curr_code, curr_cnt = heapq.heappop(heap)
            curr_chr = ascii_lowercase[-curr_code]
            rep = min(curr_cnt, repeatLimit)
            ans += curr_chr * rep

            if curr_cnt > rep and heap:
                next_code, next_cnt = heapq.heappop(heap)
                next_char = ascii_lowercase[-next_code]
                ans += next_char
                if next_cnt > 1:
                    heapq.heappush(heap, (next_code, next_cnt - 1))
                heapq.heappush(heap, (curr_code, curr_cnt - rep))

        return ans


class TestSolution(unittest.TestCase):
    def test_repeatLimitedString(self):
        solution = Solution()
        self.assertEqual(solution.repeatLimitedString("cczazcc", 3), "zzcccac")


if __name__ == '__main__':
    unittest.main()
