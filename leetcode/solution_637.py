#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    @staticmethod
    def _traverse(root, val_by_levels, level=1):
        if root:
            if val_by_levels.has_key(level):
                val_by_levels[level].append(root.val)
            else:
                val_by_levels[level] = [root.val]
            Solution._traverse(root.left, val_by_levels, level=level + 1)
            Solution._traverse(root.right, val_by_levels, level=level + 1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        val_by_levels = dict()
        Solution._traverse(root, val_by_levels)
        res = list()

        for level in val_by_levels:
            res.append(sum(val_by_levels[level])/float(len(val_by_levels[level])))

        return res

if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(60)
    root.left.right = None
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(15)

    root2 = TreeNode(3)
    root2.left = TreeNode(0)
    root2.right = TreeNode(4)
    root2.left.left = None
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(1)
    root2.left.right.right = None

    avg1 = Solution().averageOfLevels(root)
    print avg1
    avg2 = Solution().averageOfLevels(root)
    print avg2
