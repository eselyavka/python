import unittest


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.nums.sort()

        self.k = k

    def binary_search(self, val):
        l = 0
        r = len(self.nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.nums[mid] == val:
                return mid

            if self.nums[mid] > val:
                r = mid - 1
            else:
                l = mid + 1

        return r + 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        idx = self.binary_search(val)
        self.nums.insert(idx, val)

        return self.nums[-self.k]


class TestSolution(unittest.TestCase):
    def test_KthLargest(self):
        solution = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(solution.add(3), 4)
        self.assertEqual(solution.add(5), 5)
        self.assertEqual(solution.add(10), 5)
        self.assertEqual(solution.add(9), 8)
        self.assertEqual(solution.add(4), 8)


if __name__ == '__main__':
    unittest.main()
