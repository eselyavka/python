import unittest


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        n = len(time)
        if n == 1:
            return 0
        ans = 0
        arr = [0] * 60
        for i in range(n):
            div_60 = time[i] % 60
            if div_60 == 0:
                ans += arr[0]
            else:
                close = (60 - div_60)
                ans += arr[close]
            arr[div_60] += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_numPairsDivisibleBy60(self):
        solution = Solution()
        self.assertEqual(solution.numPairsDivisibleBy60([30,20,150,100,40]), 3)


if __name__ == '__main__':
    unittest.main()
