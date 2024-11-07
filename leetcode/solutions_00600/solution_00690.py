#!/usr/bin/env python

import unittest

class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        res = 0
        for employee in employees:
            if employee.id == id:
                res += employee.importance
                for subordinate in employee.subordinates:
                    res += self.getImportance(
                        employees,
                        subordinate)
        return res


class TestSolution(unittest.TestCase):

    def test_getImportance(self):
        employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
        employees2 = [Employee(1, 5, [2, 3]), Employee(2, 3, [4]), Employee(3, 4, []), Employee(4, 1, [])]
        solution = Solution()
        self.assertEqual(solution.getImportance(employees, 1), 11)
        self.assertEqual(solution.getImportance(employees2, 1), 13)

if __name__ == '__main__':
    unittest.main()
