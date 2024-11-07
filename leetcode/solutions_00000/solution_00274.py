import unittest


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)

        ans = 0
        for idx, num in enumerate(citations):
            if num > idx:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_hIndex(self):
        solution = Solution()
        self.assertEqual(solution.hIndex([3, 0, 6, 1, 5]), 3)


if __name__ == '__main__':
    unittest.main()
