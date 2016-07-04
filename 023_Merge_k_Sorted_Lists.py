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

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return []
        
        heap = []
        td = {}
        ml = ListNode(0)
        tml = ml
        while True:
            if len(lists) == lists.count(None): break
            
            for i in range(len(lists)):
                node = lists[i]
                if not node: continue

                heapq.heappush(heap, node.val)
                td.setdefault(node.val, []).append(node)
                lists[i] = lists[i].next
            
            if not heap: return []
                
            val = heapq.heappop(heap)
            tml.next = ListNode(val)
            tml = tml.next
        
        while heap:
            val = heapq.heappop(heap)
            tml.next = ListNode(val)
            tml = tml.next
        
        return ml.next
        


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(6)
    l2.next = ListNode(7)
    l2.next.next = ListNode(8)
    l3 = ListNode(9)
    l3.next = ListNode(10)
    l3.next.next = ListNode(11)
    
    lists = [l1, l2, l3]
    lists = [[]]
    
    l = Solution().mergeKLists(lists)
    
    # printlist(l)
