#! /usr/bin/env python
# -*- coding:utf-8 -*-

def prl(head):
    if not head: print head
    while head:
        print head.val
        head = head.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA: return None
        if not headB: return None

        # Find headA's tail 
        fast = headA
        while fast.next:
            fast = fast.next

        # retain lists later
        tailA = fast

        # Find if there is a cycle
        # and locate the first collisionSpot
        fast.next = headB
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        # return None, if no cycle, which means
        # the two linked lists have no intersection at all
        if not fast or not fast.next:
            tailA.next = None
            return None

        # Locate the second collisionSpot,
        # which is the intersection Spot
        slow = headA
        while True:
            if fast == slow:
                tailA.next = None
                return fast
            slow, fast = slow.next, fast.next



if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e

    b1 = ListNode(2)
    c1 = ListNode(3)
    b1.next = c1

    intersectSpot = Solution().getIntersectionNode(c1, c1)
    print intersectSpot.val

