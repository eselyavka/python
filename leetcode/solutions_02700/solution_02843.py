import unittest


class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        for i in range(low, high + 1):
            str_i = str(i)

            if len(str_i) % 2 == 0:
                half = len(str_i) // 2
                left = str_i[:half]
                right = str_i[half:]
                if sum([int(c) for c in left]) == sum([int(c) for c in right]):
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countSymmetricIntegers(self):
        solution = Solution()
        self.assertEqual(solution.countSymmetricIntegers(1, 100), 9)


if __name__ == '__main__':
    unittest.main()
