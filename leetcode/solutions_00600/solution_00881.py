import unittest


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0

        people.sort()

        while people:
            curr = people.pop()

            next_ = 0 if not people else people.pop(0)

            if curr + next_ > limit:
                people.insert(0, next_)

            ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_numRescueBoats(self):
        solution = Solution()
        self.assertEqual(solution.numRescueBoats([3, 2, 2, 1], 3), 3)


if __name__ == '__main__':
    unittest.main()
