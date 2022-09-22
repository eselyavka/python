#!/usr/bin/env python

import unittest


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = "/"
        tokens = [t for t in path.split("/") if t not in ["","."]]
        dirs = []

        for token in tokens:
            if token ==  "..":
                if dirs:
                    dirs.pop()
            else:
                dirs.append(token)

        return res + '/'.join(dirs)


class Solution2(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = path.split('/')
        res = []
        i, j = len(tokens) - 1 if tokens[len(tokens)-1] != '' else len(tokens) - 2, 0

        while j <= i:
            if tokens[j] in ['.', '']:
                j += 1
                continue

            if tokens[j] == '..':
                try:
                    res.pop()
                except IndexError:
                    pass
                j += 1
                continue

            res.append(tokens[j])
            j += 1

        return '/' + '/'.join(res)


class TestSolution(unittest.TestCase):
    def test_simplifyPath(self):
        solution = Solution()
        self.assertEqual(solution.simplifyPath('/home/'), '/home')
        self.assertEqual(solution.simplifyPath('/a/./b/../../c/'), '/c')
        self.assertEqual(solution.simplifyPath('/home//foo/'), '/home/foo')
        self.assertEqual(solution.simplifyPath('/../'), '/')
        self.assertEqual(solution.simplifyPath('/'), '/')
        self.assertEqual(solution.simplifyPath('///'), '/')
        self.assertEqual(solution.simplifyPath('/..'), '/')

        solution2 = Solution()
        self.assertEqual(solution2.simplifyPath('/home/'), '/home')
        self.assertEqual(solution2.simplifyPath('/a/./b/../../c/'), '/c')
        self.assertEqual(solution2.simplifyPath('/home//foo/'), '/home/foo')
        self.assertEqual(solution2.simplifyPath('/../'), '/')
        self.assertEqual(solution2.simplifyPath('/'), '/')
        self.assertEqual(solution2.simplifyPath('///'), '/')
        self.assertEqual(solution2.simplifyPath('/..'), '/')


if __name__ == '__main__':
    unittest.main()
