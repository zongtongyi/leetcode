#! /usr/bin/env python
# -*- coding:utf-8 -*-

def printlist(head):
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
    def sortList(self, head):
        if not head or not head.next: return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(fast)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 else l2

        return dummy.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(6)
    c = ListNode(8)
    d = ListNode(3)
    e = ListNode(4)
    a.next, b.next, c.next, d.next = b, c, d, e

    l2 = Solution().sortList(a)
    printlist(l2)
