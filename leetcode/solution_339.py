#!/usr/bin/env python

class Solution(object):

    @staticmethod
    def _rec(nl, depth=1):
        res = 0

        for e in nl:
            if not isinstance(e, list) and e.isInteger():
                res += depth * e.getInteger()
            else:
                res = res + Solution._rec(e, depth=depth+1)

        return res

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return Solution._rec(nestedList)
