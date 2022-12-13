import collections
import unittest


class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        d = collections.defaultdict(int)

        for num in nums:
            d[num % space] += 1

        total_max = max(d.values())

        ans = float("+inf")
        for num in nums:
            if d[num % space] == total_max:
                ans = min(ans, num)

        return ans


class TestSolution(unittest.TestCase):
    def test_destroyTargets(self):
        solution = Solution()
        self.assertEqual(solution.destroyTargets([3, 7, 8, 1, 1, 5], 2), 1)


if __name__ == '__main__':
    unittest.main()
