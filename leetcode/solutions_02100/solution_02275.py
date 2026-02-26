import unittest


class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        ans = 0
        for b in range(0, 32):
            cnt = 0
            mask = 1 << b
            for x in candidates:
                if x & mask:
                    cnt += 1
            ans = max(ans, cnt)

        return ans


class TestSolution(unittest.TestCase):
    def test_largestCombination(self):
        solution = Solution()
        self.assertEqual(solution.largestCombination([16, 17, 71, 62, 12, 24, 14]), 4)


if __name__ == '__main__':
    unittest.main()
