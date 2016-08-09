#! /usr/bin/env python
# -*- coding:utf-8 -*-
# leetcode 234 Palindrome

def printlist(head):
    print head.val
    while head.next:
        head = head.next
        print head.val

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def llength(self, head):
        n = 0
        while head:
            head = head.next
            n += 0
        return n

    def rotateRight(self, head, k):
        if not head or not head.next: return head

        k = k % self.llength(head)
        if k == 0:return head

        slow, fast = head, head
        while k:
            fast = fast.next
            k -= 1

        tslow, tfast = slow, fast
        while fast:
            tslow, tfast = slow, fast
            slow, fast = slow.next, fast.next

        tslow.next = None
        tfast.next = head

        return slow


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    k = 2
    l2 = Solution().rotateRight(l1, k)
    printlist(l2)
