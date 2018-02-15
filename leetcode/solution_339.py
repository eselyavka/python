#!/usr/bin/env python

class Solution(object):

    @staticmethod
    def _rec(nestedList, depth=1):
        res = 0

        if not nestedList:
            return 0

        for element in nestedList:
            if isinstance(element, NestedInteger):
                if element.isInteger():
                    res += depth * element.getInteger()
                else:
                    res = res + Solution._rec(element.getList(), depth=depth+1)
            else:
                res = res + Solution._rec(nestedList[1:])
        return res

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return Solution._rec(nestedList)
