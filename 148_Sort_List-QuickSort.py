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
    def sortList(self, head):
        if not head or not head.next: return head

        # TODO, try random pivot
        val = head.val
        # "dummy_equay", split list at every recursion. In case 3,2,1 scenario.
        dummy_lower, dummy_equay, dummy_higher = ListNode(0), ListNode(0), ListNode(0)
        lower, equay, higher = dummy_lower, dummy_equay, dummy_higher
        while head:
            if val < head.val:
                higher.next = head
                higher = higher.next
            elif val> head.val:
                lower.next = head
                lower = lower.next
            else:
                equay.next = head
                equay = equay.next
            head = head.next

        lower.next = higher.next = equay.next = None
        dummy_lower  = self.sortList(dummy_lower.next)
        dummy_higher = self.sortList(dummy_higher.next)

        lower = self.getTail(dummy_lower)
        if lower:
            lower.next = dummy_equay.next
        else:
            dummy_lower = dummy_equay.next
        dummy_equay.next.next = dummy_higher

        return dummy_lower

    def getTail(self, head):
        if not head or not head.next: return head

        while head.next:
            head = head.next

        return head


if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(6)
    c = ListNode(8)
    d = ListNode(2)
    e = ListNode(1)
    a.next, b.next, c.next, d.next = b, c, d, e

    l2 = Solution().sortList(a)
    prl(l2)
