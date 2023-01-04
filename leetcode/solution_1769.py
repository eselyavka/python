import unittest


class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ans = [0 for _ in range(n)]

        s = set()
        for i in range(n):
            if boxes[i] == "1":
                s.add(i)

        for i in range(n):
            buf = 0
            for j in s:
                if i == j:
                    continue
                buf += abs(i - j)
            ans[i] = buf

        return ans


class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertListEqual(solution.minOperations("001011"), [11, 8, 5, 4, 3, 4])


if __name__ == '__main__':
    unittest.main()
