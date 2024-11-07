import collections
import unittest


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.Counter(arr)
        diff = k

        for item, cnt in sorted(d.items(), key=lambda t: t[1]):
            diff -= cnt
            if diff >= 0:
                d.pop(item)
            else:
                return len(d)

        return len(d)


class TestSolution(unittest.TestCase):
    def test_findLeastNumOfUniqueInts(self):
        solution = Solution()
        self.assertEqual(solution.findLeastNumOfUniqueInts([5, 5, 4], 1), 1)


if __name__ == '__main__':
    unittest.main()
