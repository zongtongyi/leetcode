#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 1. List Algorithm always have a dummy head node, and keep the dummy head
# 2. Multi pointer will be helpful (Fast & Slow / Gap Pointer)

def printlist(head):
    print head.val
    while head.next:
        head = head.next
        print head.val
    print "----"
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

        # printlist(dummy.next)
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    printlist(l1)

    Solution().swapPairs(l1)

