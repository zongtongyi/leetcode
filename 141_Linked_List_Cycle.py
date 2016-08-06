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
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False

        p1, p2 = head, head.next.next
        while p2:
            if p1 == p2: return True

            try:
                p1, p2 = p1.next, p2.next.next
            except AttributeError as e:
                return False

        #return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(6)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node1

    print Solution().hasCycle(node1)
