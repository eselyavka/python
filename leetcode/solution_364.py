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


class SolutionDict(object):
    def height(self, nestedList):
        for element in nestedList:
            if isinstance(element, int):
                continue
            return 1 + self.height(element)

        return 1

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        height = self.height(nestedList)
        mem = {i: 0 for i in range(1, height + 1)}

        def rec(lst, level):
            if level == 0:
                return
            for element in lst:
                if isinstance(element, int):
                    mem[level] += (element * level)
                    continue
                rec(element, level - 1)

        rec(nestedList, height)

        return sum(mem.values())


if __name__ == '__main__':
    NESTED_LIST = [[[[55]]], [[31]], [99], [], 75]
    SOLUTION_ARR = SolutionArr()

    assert SOLUTION_ARR.depthSumInverse([1, [4, [6]]]) == 17
    assert SOLUTION_ARR.depthSumInverse([[1, 1], 2, [1, 1]]) == 8
    assert SOLUTION_ARR.depthSumInverse(NESTED_LIST) == 714
    assert SOLUTION_ARR.depthSumInverse([[[-1]], [-1]]) == -3

    SOLUTION_DICT = SolutionDict()
    assert SOLUTION_DICT.depthSumInverse([1, [4, [6]]]) == 17
    assert SOLUTION_DICT.depthSumInverse([[1, 1], 2, [1, 1]]) == 8
    assert SOLUTION_DICT.depthSumInverse(NESTED_LIST) == 714
    assert SOLUTION_DICT.depthSumInverse([[[-1]], [-1]]) == -3
