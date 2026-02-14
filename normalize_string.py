import unittest


class Solution(object):
    def normalizeString(self, s):
        """
        Will normalize string s
        """
        idx = 0
        n = len(s)
        nums = []
        chars = []

        def is_num_starts(i):
            if i >= n:
                return False
            if s[i].isdigit():
                return True
            if s[i] == "." and i + 1 < n and s[i + 1].isdigit():
                return True
            return False

        while idx < n:
            if s[idx].isalpha() and s[idx] != ".":
                chars.append(s[idx])
                idx += 1
                continue

            if is_num_starts(idx):
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
                    nums.append(float(num) if "." in num else int(num))

                continue
            idx += 1
        left = "".join(sorted(chars))
        if not nums:
            return left

        right = " ".join([str(x) for x in sorted(nums)])

        return left + (" " if left else "") + right


class TestSolution(unittest.TestCase):
    def test_normalizeString(self):
        solution = Solution()
        self.assertEqual(solution.normalizeString("abc12xyz3.5def2"), "abcdefxyz 2 3.5 12")
        self.assertEqual(solution.normalizeString("ba12ab3"), "aabb 3 12")
        self.assertEqual(solution.normalizeString("a5.b"), "ab 5.0")
        self.assertEqual(solution.normalizeString("a.b"), "ab")
        self.assertEqual(solution.normalizeString("a1..2b"), "ab 0.2 1.0")


if __name__ == '__main__':
    unittest.main()
