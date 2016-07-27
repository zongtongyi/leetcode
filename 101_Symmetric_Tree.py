#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Pre-Order Traversal
# In-Order Traversal
# Post-Order Traversal
# Level-Order Traversal
# Morris Traversal
# Non-recursive Traversal


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root: return True

        lt, rt = root.left, root.right
        return self.isSym(lt, rt)

    def isSym(self, lt, rt):

        if not lt and not rt: return True
        if not lt or not rt: return False
        if lt.val != rt.val: return False

        if lt.val == rt.val:
            return self.isSym(lt.left, rt.right) and self.isSym(rt.left, lt.right)


if __name__ == "__main__":
    p       = TreeNode(1)
    p.left  = TreeNode(2)
    p.left.left  = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right = TreeNode(2)
    p.right.left  = TreeNode(4)
    p.right.right = TreeNode(3)
    print Solution().isSymmetric(p)
