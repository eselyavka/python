import unittest


class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]
        for num in nums:
            i = 0
            while i < len(res):
                row = res[i]
                if num not in row:
                    row.append(num)
                    break
                else:
                    if (i + 1) == len(res):
                        res.append([num])
                        i += 1
                i += 1

        return res


class TestSolution(unittest.TestCase):
    def test_findMatrix(self):
        solution = Solution()
        self.assertEqual(solution.findMatrix([1, 3, 4, 1, 2, 3, 1]), [[1, 3, 4, 2], [1, 3], [1]])


if __name__ == '__main__':
    unittest.main()
