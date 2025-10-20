import unittest


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0

        for op in operations:
            if '++' in op:
                ans += 1
            else:
                ans -= 1

        return ans


class TestSolution(unittest.TestCase):
    def test_finalValueAfterOperations(self):
        solution = Solution()
        self.assertEqual(solution.finalValueAfterOperations(["--X", "X++", "X++"]), 1)


if __name__ == '__main__':
    unittest.main()
