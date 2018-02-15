#!/usr/bin/env python

class Solution(object):

    @staticmethod
    def heigh(nestedList):
        res = 1

        if not nestedList:
            return 0

        for element in nestedList:
            if not element.isInteger():
                res = max(res, 1 + Solution.heigh(element.getList()))
            else:
                continue
        return res

    @staticmethod
    def _rec(nestedList, depth):
        res = 0
        if not nestedList:
            return 0

        for element in nestedList:
            if element.isInteger():
                res += depth * element.getInteger()
            else:
                res = res + Solution._rec(element.getList(), depth-1)
        return res

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        height = Solution.heigh(nestedList)

        return Solution._rec(nestedList, height)

class SolutionArr(object):

    @staticmethod
    def heigh(nestedList):
        res = 1

        if not nestedList:
            return 0

        for element in nestedList:
            if isinstance(element, list):
                res = max(res, 1 + SolutionArr.heigh(element))
            else:
                continue
        return res

    @staticmethod
    def _rec(nestedList, depth):
        res = 0

        if not nestedList:
            return 0

        for element in nestedList:
            if not isinstance(element, list):
                res += depth * element
            else:
                res = res + SolutionArr._rec(element, depth-1)
        return res

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        height = SolutionArr.heigh(nestedList)

        return SolutionArr._rec(nestedList, height)

if __name__ == '__main__':
    NESTED_LIST = [[[[55]]], [[31]], [99], [], 75]
    SOLUTION_ARR = SolutionArr()

    assert SOLUTION_ARR.depthSumInverse(NESTED_LIST) == 714
    assert SOLUTION_ARR.depthSumInverse([[[-1]], [-1]]) == -3
