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
            n += 1
            head = head.next
        return n

    def recusive(self, head, n):
        if n==1:
            return head.next, True
        if n==0:
            return head, True

        node, ret = self.recusive(head.next, n-2)
        if not ret or not node:
            return None, False
        if head.val == node.val:
            return node.next, True
        else:
            return None, False

    def isPalindrome(self, head):
        if not head or not head.next: return True

        n = self.llength(head)

        _, ret = self.recusive(head, n)
        return ret


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(1)
    #l1.next.next.next = ListNode(1)
    #l1.next.next.next.next = ListNode(1)

    print Solution().isPalindrome(l1)
