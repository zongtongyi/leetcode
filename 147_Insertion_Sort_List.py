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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        dummy = ListNode(0)
        p = dummy
        while head:
            # A little improvement for insert sort
            # else if it will cause TLE on Leetcode
            if p >= head.val: p = dummy

            p = dummy
            while p.next and p.next.val < head.val:
                p = p.next
            tmp = head.next
            head.next = p.next
            p.next = head
            head = tmp

        return dummy.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(6)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    l2 = Solution().insertionSortList(head)
    printlist(l2)

