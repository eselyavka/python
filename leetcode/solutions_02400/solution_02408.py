import unittest
from collections import defaultdict


class SQL(object):

    def __init__(self, names, columns):
        """
        :type names: List[str]
        :type columns: List[int]
        """
        self.names = names
        self.columns = columns
        self.storage = defaultdict(list)

    def insertRow(self, name, row):
        """
        :type name: str
        :type row: List[str]
        :rtype: None
        """
        self.storage[name].append(row)

    def deleteRow(self, name, rowId):
        """
        :type name: str
        :type rowId: int
        :rtype: None
        """
        self.storage[name][rowId - 1] = None

    def selectCell(self, name, rowId, columnId):
        """
        :type name: str
        :type rowId: int
        :type columnId: int
        :rtype: str
        """
        if self.storage[name][rowId - 1] is not None:
            return self.storage[name][rowId - 1][columnId - 1]
        return ""


class TestSolution(unittest.TestCase):
    def test_SQL(self):
        solution = SQL(["one", "two", "three"], [2, 3, 1])
        solution.insertRow("two", ["first", "second", "third"])
        self.assertEqual(solution.selectCell("two", 1, 3), "third")
        solution.insertRow("two", ["fourth", "fifth", "sixth"])
        solution.deleteRow("two", 1)
        self.assertIsNone(solution.selectCell("two", 1, 2))
        self.assertEqual(solution.selectCell("two", 2, 2), "fifth")


if __name__ == '__main__':
    unittest.main()
