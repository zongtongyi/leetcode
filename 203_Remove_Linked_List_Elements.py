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
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
        # p, prev = head, dummy
        # while p:
        #     if p.val == val:
        #         prev.next = p.next
        #     else:
        #         prev = p
        #     p = p.next
        # return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(3)
    
    l = Solution().removeElements(l1, 3)
    
    printlist(l)
