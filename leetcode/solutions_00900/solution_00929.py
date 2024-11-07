#!/usr/bin/env python

import unittest


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniq = set()
        for email in emails:
            local_name, domain = email.split('@')
            real_name = local_name.split('+')[0].replace('.', '')
            uniq.add(''.join([real_name, '@', domain]))

        return len(uniq)


class TestSolution(unittest.TestCase):
    def test_numUniqueEmails(self):
        solution = Solution()
        self.assertEqual(solution.numUniqueEmails(["test.email+alex@leetcode.com",
                                                   "test.e.mail+bob.cathy@leetcode.com",
                                                   "testemail+david@lee.tcode.com"]), 2)


if __name__ == '__main__':
    unittest.main()
