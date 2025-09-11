import unittest


class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        seen = []

        k = 0
        for num in nums:
            if num >= 0:
                seen = [num] + seen
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans


class TestSolution(unittest.TestCase):
    def test_lastVisitedIntegers(self):
        solution = Solution()
        self.assertEqual(solution.lastVisitedIntegers([1, 2, -1, -1, -1]), [2, 1, -1])


if __name__ == '__main__':
    unittest.main()
