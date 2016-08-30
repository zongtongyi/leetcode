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
        if not head or not head.next: return head

        bHead = False
        pre = ListNode(0)
        pre.next, first = head, head
        while True:
            i = k
            p1, p2 = first, first
            while i>1:
                p2 = p2.next
                if not p2: return head
                i -= 1

            last = p2.next
            first = last
            while p1 != p2:
                tmp = p1.next
                p1.next = last
                last = p1
                p1 = tmp
            p2.next = last
            pre.next = p2

            if not bHead:
                head = p2
                bHead = True

            i = k
            while i>0:
                pre = pre.next
                i -= 1





if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e

    l2 = Solution().reverseKGroup(a, 2)
    prl(l2)

