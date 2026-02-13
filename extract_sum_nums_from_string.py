import unittest


class Solution:
    def extractSum(self, s):
        """
        Will extract and sum numbers from random string
        """
        nums = []
        n = len(s)
        idx = 0

        def is_num_starts(i):
            if i >= n:
                return False
            if s[i].isdigit():
                return True
            if s[i] == "." and i + 1 < n and s[i + 1].isdigit():
                return True

            return False

        while idx < n:
            sign = 1

            if s[idx] == "-" and idx + 1 < n and (s[idx + 1].isdigit() or s[idx + 1] == "."):
                sign = -1
                idx += 1

            if is_num_starts(idx) or (idx < n and s[idx] == "." and idx + 1 < n and s[idx + 1].isdigit()):
                tokens = []

                while idx < n and s[idx].isdigit():
                    tokens.append(s[idx])
                    idx += 1

                if idx < n and s[idx] == ".":
                    tokens.append(".")
                    idx += 1
                    while idx < n and s[idx].isdigit():
                        tokens.append(s[idx])
                        idx += 1

                num = "".join(tokens)
                if num != "." and num != "":
                    nums.append(sign * float(num))

                continue
            idx += 1

        return sum(nums)


class TestSolution(unittest.TestCase):
    def test_extractSum(self):
        solution = Solution()
        self.assertEqual(solution.extractSum("abc12.5xyz3def-7.25gh0"), 8.25)


if __name__ == '__main__':
    unittest.main()
