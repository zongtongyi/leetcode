#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Reservoir sampling (水塘抽样)
# https://zh.wikipedia.org/wiki/%E6%B0%B4%E5%A1%98%E6%8A%BD%E6%A8%A3

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


from random import randint

class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        head, n, val = self.head, 0, None

        while head:
            if randint(0, n)==0:
                val = head.val
            n += 1
            head = head.next

        return val


if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    print Solution(a).getRandom()
