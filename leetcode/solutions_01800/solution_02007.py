import unittest
from collections import Counter


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        n = len(changed)

        if n % 2 != 0:
            return []

        freq = Counter(changed)
        changed.sort()

        ans = []
        for num in changed:
            if num in freq and freq[num] > 0:
                freq[num] -= 1
                double_num = 2 * num
                if double_num in freq and freq[double_num] > 0:
                    ans.append(num)
                    freq[double_num] -= 1
                else:
                    return []

        return ans


class TestSolution(unittest.TestCase):
    def test_findOriginalArray(self):
        solution = Solution()
        self.assertEqual(solution.findOriginalArray([1, 3, 4, 2, 6, 8]), [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
