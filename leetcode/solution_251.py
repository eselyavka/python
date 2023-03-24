import unittest


class Vector2D(object):

    def __init__(self, vec):
        """
        :type vec: List[List[int]]
        """
        acc = []

        def rec(lst):
            for item in lst:
                if isinstance(item, list):
                    rec(item)
                else:
                    acc.append(item)

        rec(vec)

        self.it = iter(acc)
        self.len = len(acc)

    def next(self):
        """
        :rtype: int
        """
        self.len -= 1
        return next(self.it)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.len > 0


class TestSolution(unittest.TestCase):
    def test_vector2d(self):
        solution = Vector2D([[1, 2], [3], [4]])
        self.assertListEqual([solution.next() for _ in range(3)], [1, 2, 3])
        self.assertTrue(solution.hasNext())
        self.assertTrue(solution.hasNext())
        self.assertEqual(solution.next(), 4)
        self.assertFalse(solution.hasNext())


if __name__ == '__main__':
    unittest.main()
