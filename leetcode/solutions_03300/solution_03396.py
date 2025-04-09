import unittest


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        operations = 0
        i = 0

        while i < n:
            seen = set()
            duplicate_found = False

            for j in range(i, n):
                if nums[j] in seen:
                    duplicate_found = True
                    break
                seen.add(nums[j])

            if not duplicate_found:
                return operations

            i += 3
            operations += 1

        return operations


class TestSolution(unittest.TestCase):
    def test_minimumOperations(self):
        solution = Solution()
        self.assertEqual(solution.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]), 2)


if __name__ == '__main__':
    unittest.main()
