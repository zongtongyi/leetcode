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
    def reverseKGroup(self, head, k):

        if not head or not head.next: return head

        bHead = False
        pre = ListNode(0)
        pre.next, first = head, head
        while True:
            i = k
            p1, p2 = first, first
            while i>1:
                p2 = p2.next
                if not p2: return head
                i -= 1

            last = p2.next
            first = last
            while p1 != p2:
                tmp = p1.next
                p1.next = last
                last = p1
                p1 = tmp
            p2.next = last
            pre.next = p2

            if not bHead:
                head = p2
                bHead = True

            i = k
            while i>0:
                pre = pre.next
                i -= 1

    def reverseKGroup(self, head, k):
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        p = head
        i = 0
        while p:
            i += 1
            if i%k == 0:
                pre = self.reverse(pre, p.next)
                p = pre.next
            else:
                p = p.next

        return dummy.next

    # Use a changeless pre or dummy node, to keep the two section connected
    # Use a changeless tail node, to break out reverse procedure
    # Use dummy node as pre node, and always has a pre node before the beginning of sub_list
    # the first node of sub_list is the next pre node, the pre node of next sub_list
    # k = 3
    # 0->1->2->3->4->5->6
    # |           |   
    # pre        next
    #
    # after calling pre = reverse(pre, next)
    # 
    # 0->3->2->1->4->5->6
    #          |  |
    #          pre next 
    def reverse(self, pre, tail):
        last = pre.next
        cur  = last.next

        while cur != tail:
            last.next = cur.next
            cur.next  = pre.next
            pre.next  = cur
            cur       = last.next

        return last




if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    h = ListNode(8)
    a.next, b.next, c.next, d.next = b, c, d, e
    e.next, f.next, g.next = f, g, h

    l2 = Solution().reverseKGroup(a, 3)
    prl(l2)

