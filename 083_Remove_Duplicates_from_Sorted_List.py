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
    """def deleteDuplicates(self, head):
        # Solution for array, swap vals.
        # Slow move, point to Current Max nunmber, 
        # its Next position is Update position
        # 1 -> 2 -> 2 -> 2 -> 3 -> 4 -> 4
        if not head or not head.next: return head

        ht = head

        i, j = head, head.next
        while j:
            if i.val != j.val:
                i = i.next
                i.val = j.val
            j = j.next

        i.next = None

        return ht"""

    def deleteDuplicates(self, head):
        # Solution for LinkList, drop nodes.
        # Slow move, point to Current Max nunmber, 
        # its Next position is Update position
        # 1 -> 2 -> 2 -> 2 -> 3 -> 4 -> 4
        if not head or not head.next: return head

        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    # l1.next.next.next = ListNode(3)
    # l1.next.next.next.next = ListNode(3)
    # l1.next.next.next.next.next = ListNode(4)
    
    l = Solution().deleteDuplicates(l1)
    
    printlist(l)
