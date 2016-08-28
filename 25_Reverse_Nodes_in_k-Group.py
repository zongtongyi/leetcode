#! /usr/bin/env python
# -*- coding:utf-8 -*-

def prl(head):
    if not head: print head
    while head:
        print head.val
        head = head.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """


if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(8)
    c = ListNode(6)
    d = ListNode(1)
    e = ListNode(2)
    a.next, b.next, c.next, d.next = b, c, d, e

    l2 = Solution().reverseKGroup(a, k)
    prl(l2)

