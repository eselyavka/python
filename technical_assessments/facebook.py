#!/usr/bin/env python

# open two csv files with format nameX,numberX | nameY,numberY
# sort both files by X,Y and produce name

import unittest
from io import StringIO
import tempfile
from contextlib import contextmanager
import os


@contextmanager
def tempinput(data):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(bytes(data, "utf-8"))
    temp.close()
    try:
        yield temp.name
    finally:
        os.unlink(temp.name)


class Solution(object):

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    @staticmethod
    def _process_file(payload, data_dict):
        for entry in payload:
            data = entry.strip().split(',')
            if len(data) != 2:
                continue

            name, number = data
            number = int(number)

            if number in data_dict:
                data_dict[number].append(name)
            else:
                data_dict[number] = [name]

    def sort_by_number(self):
        numbered_names = dict()
        with open(self.file1, 'r') as fh1, open(self.file2, 'r') as fh2:
            Solution._process_file(fh1.readlines(), numbered_names)
            Solution._process_file(fh2.readlines(), numbered_names)

        output = ''
        _keys = list(numbered_names.keys())
        _keys.sort()
        for num in _keys:
            names = numbered_names[num]
            names.sort()
            output += "\n".join(names)
            output += "\n"
        return output


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.payload1 = "name1,83\nname2,12\nname3,101\nbadname1,90,redundantfield"
        self.payload2 = "name4,53\nname5,12\nname6,1101\nbadname2,910,redundantfield"
        self.file1 = StringIO(self.payload1)
        self.file2 = StringIO(self.payload2)

    def test_process_file(self):
        solution = Solution(self.file1, self.file2)
        actual = dict()
        solution._process_file(self.file1.readlines(), actual)
        solution._process_file(self.file2.readlines(), actual)
        expected = {83: ['name1'], 12: ['name2', 'name5'], 101: ['name3'],
                    53: ['name4'], 1101: ['name6']}
        self.assertEqual(actual, expected)

    def test_sort_by_number(self):
        expected = "\n".join(['name2', 'name5', 'name4', 'name1', 'name3', 'name6', ''])
        with tempinput(self.payload1) as f_name1, tempinput(self.payload2) as f_name2:
            solution = Solution(f_name1, f_name2)
            actual = solution.sort_by_number()
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
