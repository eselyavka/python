import unittest


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False

        def leading_ones_byte(x):
            if x & 0b10000000 == 0:
                return 0
            if x & 0b11100000 == 0b11000000:
                return 2
            if x & 0b11110000 == 0b11100000:
                return 3
            if x & 0b11111000 == 0b11110000:
                return 4
            return -1

        n = len(data)
        i = 0
        while i < n:
            ones = leading_ones_byte(data[i])
            if ones == -1:
                return False

            if ones == 1 or ones > 4:
                return False

            if ones == 0:
                i += 1
                continue

            if i + ones > n:
                return False

            for j in range(1, ones):
                if not (data[i + j] & 0b11000000) == 0b10000000:
                    return False

            i += ones

        return True


class TestSolution(unittest.TestCase):
    def test_validUtf8(self):
        solution = Solution()
        self.assertTrue(solution.validUtf8([197, 130, 1]))


if __name__ == '__main__':
    unittest.main()
