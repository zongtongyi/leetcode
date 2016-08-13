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
    def isPalindrome(self, head):
        if not head: return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next

        last = None
        while slow:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp

        p = head
        while last:
            if p.val == last.val:
                p, last = p.next, last.next
            else:
                return False

        return True


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    #l1.next.next = ListNode(3)
    l1.next.next = ListNode(1)
    # l1.next.next.next = ListNode(1)

    print Solution().isPalindrome(l1)
