import unittest


class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        no_parity = []
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                no_parity.append(i)

        def binary_search(s, e, arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                idx = arr[mid]

                if idx < s:
                    l = mid + 1
                elif idx > e:
                    r = mid - 1
                else:
                    return True

            return False

        ans = []
        for query in queries:
            left, right = query
            bad_idx_exists = binary_search(left + 1, right, no_parity)
            if bad_idx_exists:
                ans.append(False)
            else:
                ans.append(True)

        return ans


class TestSolution(unittest.TestCase):
    def test_isArraySpecial(self):
        solution = Solution()
        self.assertListEqual(solution.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]), [False, True])


if __name__ == '__main__':
    unittest.main()
