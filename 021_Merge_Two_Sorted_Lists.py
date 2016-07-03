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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = ListNode(0)
        res = l3
        while l1 and l2:
            l3.next = ListNode(0)
            l3 = l3.next
            if l1.val < l2.val:
                l3.val = l1.val
                l1 = l1.next
            else:
                l3.val = l2.val
                l2 = l2.next
        
        while l1:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = l1.val
            l1 = l1.next

        while l2:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = l2.val
            l2 = l2.next
            
        return res.next


if __name__ == "__main__":
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # 
    # l2 = ListNode(6)
    # l2.next = ListNode(7)
    # l2.next.next = ListNode(8)
    # l2.next.next.next = ListNode(9)
    l1 = ListNode(2)
    l2 = ListNode(1)
    l3 = Solution().mergeTwoLists(l1, l2)
    
    printlist(l3)