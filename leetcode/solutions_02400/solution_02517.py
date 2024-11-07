import unittest


class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()

        if k == 2:
            return price[-1] - price[0]

        n = len(price)

        def check(target):
            prev = price[0]
            cnt = 1
            for i in range(1, n):
                diff = price[i] - prev
                if diff >= target:
                    prev = price[i]
                    cnt += 1
                if cnt == k:
                    return True

            return cnt == k

        low, high = 0, price[-1] - price[0]

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


class TestSolution(unittest.TestCase):
    def test_maximumTastiness(self):
        solution = Solution()
        self.assertEqual(solution.maximumTastiness([13, 5, 1, 8, 21, 2], 3), 8)


if __name__ == '__main__':
    unittest.main()
