#! /usr/bin/env python
# -*- coding:utf-8 -*-
# continue of leetcode 206

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
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head

        pre1, p1 = dummy, head
        while m>1:
            pre1 = pre1.next
            p1 = p1.next
            m -= 1

        p2 = head
        while n>1:
            p2 = p2.next
            n -= 1

        tail = p2.next
        while p1!=p2:
            tmp = p1.next
            p1.next = tail
            tail = p1
            p1 = tmp

        p2.next = tail
        pre1.next = p2

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next = ListNode(8)
    
    # Solution().reverseBetween(l1, 2, 4)
    l = Solution().reverseBetween(l1, 2, 5)
    
    printlist(l)
