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
    '''
    def oddEvenList(self, head):
        # if not head or not head.next: return head
        if not head: return head

        odd_head, even_head = head, head.next
        odd, even = odd_head, even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return odd_head
    '''
    '''
    def oddEvenList(self, head):
        if not head or not head.next: return head

        odd, even = head, head.next
        while even and even.next:
            tmp = odd.next
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            odd.next = tmp
            even = even.next

        return head
    '''
    def oddEvenList(self, head):
        if not head: return head

        odd, even = head, head.next
        while even and even.next:
            next_odd, next_even = odd.next, even.next
            even.next = next_even.next
            odd.next, next_even.next = next_even, next_odd
            odd, even = odd.next, even.next

        return head



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    l2 = Solution().oddEvenList(head)
    prl(l2)

