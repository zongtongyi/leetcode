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
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return slow

        return None

    def detectCycle(self, head):
        # First, find the first collisionSpot
        collisionSpot = self.hasCycle(head)
        if not collisionSpot: return None

        # Second, find the second collisionSpot
        # which is the joint spot
        while True:
            if collisionSpot == head: return head

            collisionSpot, head = collisionSpot.next, head.next



if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(6)
    node3 = ListNode(3)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print Solution().detectCycle(node1).val
