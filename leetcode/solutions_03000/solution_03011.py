import unittest


class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_bits = bin(nums[0]).count("1")
        curr_max = nums[0]
        curr_min = nums[0]

        prev_max = float("-inf")

        for i in range(1, len(nums)):
            curr_set_bits = bin(nums[i]).count("1")
            if set_bits == curr_set_bits:
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
            else:
                if curr_min < prev_max:
                    return False

                prev_max = curr_max

                curr_max = nums[i]
                curr_min = nums[i]

                set_bits = curr_set_bits

        if curr_min < prev_max:
            return False

        return True


class TestSolution(unittest.TestCase):
    def test_canSortArray(self):
        solution = Solution()
        self.assertTrue(solution.canSortArray([8, 4, 2, 30, 15]))


if __name__ == '__main__':
    unittest.main()
