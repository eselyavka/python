import heapq
import unittest


class SmallestInfiniteSet(object):

    def __init__(self):
        self.h = [i + 1 for i in range(1000)]
        self.dups = set(self.h)

    def popSmallest(self):
        """
        :rtype: int
        """
        item = heapq.heappop(self.h)
        if item in self.dups:
            self.dups.remove(item)
        return item

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.dups:
            heapq.heappush(self.h, num)
            self.dups.add(num)
        return


class TestSolution(unittest.TestCase):
    def test_smallestInfiniteSet(self):
        solution = SmallestInfiniteSet()
        solution.addBack(2)
        actual = [solution.popSmallest() for _ in range(3)]
        self.assertListEqual(actual, [1, 2, 3])
        solution.addBack(1)
        actual = [solution.popSmallest() for _ in range(3)]
        self.assertListEqual(actual, [1, 4, 5])


if __name__ == '__main__':
    unittest.main()
