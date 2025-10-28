import unittest


class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)

        def simulate(start, step):
            a = nums[:]
            rem = total
            i = start
            s = step

            while 0 <= i < n:
                if a[i] == 0:
                    i += s
                else:
                    a[i] -= 1
                    rem -= 1
                    s = -s
                    i += s

            return rem == 0

        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                if simulate(i, -1):
                    ans += 1
                if simulate(i, +1):
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countValidSelections(self):
        solution = Solution()
        self.assertEqual(solution.countValidSelections([1, 0, 2, 0, 3]), 2)


if __name__ == '__main__':
    unittest.main()
