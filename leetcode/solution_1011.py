import unittest


class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        if len(weights) == days:
            return max(weights)

        minw = max(weights)
        maxw = sum(weights)

        def binary_search(target, weights, days):
            cnt = 1
            sub_sum = 0
            for weight in weights:
                if weight > target:
                    return False

                sub_sum += weight

                if sub_sum > target:
                    cnt += 1
                    sub_sum = weight

            if cnt <= days:
                return True

            return False

        ans = 0
        while minw <= maxw:
            mid = (minw + maxw) // 2
            if binary_search(mid, weights, days):
                ans = mid
                maxw = mid - 1
            else:
                minw = mid + 1

        return ans


class TestSolution(unittest.TestCase):
    def test_shipWithinDays(self):
        solution = Solution()
        self.assertEqual(solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)


if __name__ == '__main__':
    unittest.main()
