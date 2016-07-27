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
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
            
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    p       = TreeNode(1)
    p.left  = TreeNode(2)
    p.right = TreeNode(2)
    q       = TreeNode(1)
    q.left  = TreeNode(2)
    q.right = TreeNode(2)
    print Solution().isSameTree(p, q)
