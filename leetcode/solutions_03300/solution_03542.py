import unittest


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for num in nums:
            if num == 0:
                stack = []
                continue

            while stack and stack[-1] > num:
                stack.pop()

            if not stack or stack[-1] < num:
                ans += 1
                stack.append(num)

        return ans


class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations([1, 2, 1, 2, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
