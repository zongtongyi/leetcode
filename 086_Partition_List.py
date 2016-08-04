#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Given a linked list and a value x, partition it such that all nodes less than 
# x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the 
# two partitions.

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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_list = ListNode(0)
        after_list  = ListNode(0)
        before_list_head = before_list
        after_list_head  = after_list

        while head:
            Node = ListNode(head.val)
            if head.val >= x:
                after_list.next = Node
                after_list = after_list.next
            else:
                before_list.next = Node
                before_list = before_list.next

            head = head.next

        before_list.next = after_list_head.next

        return before_list_head.next



if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(6)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(11)
    l1.next.next.next.next.next = ListNode(4)

    x = 5

    l2 = Solution().partition(l1, x)
    printlist(l2)
