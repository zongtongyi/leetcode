#! /usr/bin/env python
# -*- coding:utf-8 -*-

def printlist(head):
    if not head: return None

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
    def deleteDuplicates(self, head):
        # Solution for LinkList, drop nodes.
        # Slow move, point to Current Max nunmber, 
        # its Next position is Update position
        # 1 -> 2 -> 2 -> 2 -> 3 -> 4 -> 4
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur.next:
            dup = False
            while cur.next.next and cur.next.next.val == cur.next.val:
                cur.next.next = cur.next.next.next
                dup = True
            if dup:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    # l1.next.next.next.next = ListNode(3)
    # l1.next.next.next.next.next = ListNode(4)
    
    l = Solution().deleteDuplicates(l1)
    
    printlist(l)
