import unittest


class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """

        n = len(satisfaction)

        satisfaction.sort()

        if satisfaction[-1] <= 0:
            return 0

        ans = 0

        i = 0
        while i < n:
            local_ans = satisfaction[i]
            j = i + 1
            k = 2
            while j < n:
                local_ans += satisfaction[j] * k
                k += 1
                j += 1

            ans = max(ans, local_ans)
            i += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_maxSatisfaction(self):
        solution = Solution()
        self.assertEqual(solution.maxSatisfaction([-1, -8, 0, 5, -9]), 14)


if __name__ == '__main__':
    unittest.main()
