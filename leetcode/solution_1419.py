import unittest


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        if len(croakOfFrogs) < 5:
            return -1

        c = r = o = a = k = frogs = ans = 0

        for i in croakOfFrogs:
            if i == "c":
                c, frogs = c + 1, frogs + 1
                ans = max(ans, frogs)
            elif i == "r":
                r += 1
            elif i == "o":
                o += 1
            elif i == "a":
                a += 1
            else:
                k += 1
                frogs -= 1

            if c < r or r < o or o < a or a < k:
                return -1

        if frogs == 0 and c == r == o == a == k:
            return ans

        return -1


class TestSolution(unittest.TestCase):
    def test_minNumberOfFrogs(self):
        solution = Solution()
        self.assertEqual(solution.minNumberOfFrogs("crcoakroak"), 2)


if __name__ == '__main__':
    unittest.main()
