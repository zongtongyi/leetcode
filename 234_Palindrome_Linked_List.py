#! /usr/bin/env python
# -*- coding:utf-8 -*-

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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(6)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(11)
    l1.next.next.next.next.next = ListNode(4)

    print Solution.isPalindrome(head)
