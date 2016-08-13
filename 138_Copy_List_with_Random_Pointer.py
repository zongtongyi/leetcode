#! /usr/bin/env python
# -*- coding:utf-8 -*-

def printlist(head):
    if not head: print head

    while head:
        print 'label:%s, random:%s' % (head.label, head.random.label if head.random else head.random)
        head = head.next

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head: return head

        # Insert new nodes
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = node.next

        # Copy random
        p = head
        while p:
            p.next.random = p.random.next if p.random else p.random
            p = p.next.next

        # Split list
        dummy = RandomListNode(0)
        dummy.next = head
        p  = head
        p2 = dummy
        while p:
            p2.next = p2.next.next
            p.next = p.next.next
            p2 = p2.next
            p  = p.next


        return dummy.next




if __name__ == "__main__":
    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    d = RandomListNode(4)
    a.next = b
    b.next = c
    c.next = d
    a.random = d
    c.random = a
    d.random = a

    l2 = Solution().copyRandomList(a)
    printlist(l2)

