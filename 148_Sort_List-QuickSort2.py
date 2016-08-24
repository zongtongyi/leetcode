#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Quick Sort
# but will TLE on leetcode, cause of worst time complexity

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

        self.qsort(head, None)

        return head

    def qsort(self, head, tail):
        if not head or not head.next: return
        if head == tail: return
        if head.next == tail: return

        slow, fast = head.next, head.next
        preslow = head
        while fast!=tail:
            if fast.val < head.val:
                slow.val, fast.val = fast.val, slow.val
                slow, preslow = slow.next, preslow.next
            fast = fast.next

        preslow.val, head.val = head.val, preslow.val

        self.qsort(head, preslow)
        self.qsort(preslow.next, tail)



if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(8)
    c = ListNode(6)
    d = ListNode(1)
    e = ListNode(2)
    a.next, b.next, c.next, d.next = b, c, d, e

    l2 = Solution().sortList(a)
    prl(l2)
