#!/usr/bin/env python

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            head = head.next
            return head
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head



if __name__ == "__main__":
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # printlist(head)
    
    n = 1
    head = Solution().removeNthFromEnd(head, n)
    printlist(head)
        