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


import random

class Solution(object):
    def __init__(self, head):
        self.vals = []
        p = head
        while p:
            self.vals.append(p.val)
            p = p.next
        self.len = len(self.vals)
    
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = random.randint(0, self.len-1)
        return self.vals[i]


if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    print Solution(a).getRandom()
