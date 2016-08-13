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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next

        last = None
        while half:
            tmp = half.next
            half.next = last
            last = half
            half = tmp

        slow.next = None

        p = head
        while last:
            tmp = last.next
            last.next = p.next
            p.next = last

            p = last.next
            last = tmp



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    Solution().reorderList(head)
    printlist(head)

