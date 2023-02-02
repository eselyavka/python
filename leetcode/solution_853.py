import unittest


class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        n = len(position)

        pos_and_speed = sorted(zip(position, speed), key=lambda t: t[0])

        stack = []
        for i in range(n - 1, -1, -1):
            if stack and float(target - stack[-1][0]) / float(stack[-1][1]) >= float(
                    target - pos_and_speed[i][0]) / float(pos_and_speed[i][1]):
                continue
            stack.append(pos_and_speed[i])

        return len(stack)


class TestSolution(unittest.TestCase):
    def test_carFleet(self):
        solution = Solution()
        self.assertEqual(solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)


if __name__ == '__main__':
    unittest.main()
