#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n%2 == 1:
            return self.findKth(nums1, nums2, n/2+1)
        else:
            k1 = self.findKth(nums1, nums2, n/2)
            k2 = self.findKth(nums1, nums2, n/2+1)
            return (k1+k2)/2.0

    def findKth(self, nums1, nums2, k):
        if nums1==[]:
            return nums2[k-1]
        if nums2==[]:
            return nums1[k-1]
        if k==1:
            return min(nums1[0], nums2[0])
        a = nums1[k/2 - 1] if len(nums1)>=k/2 else None
        b = nums2[k/2 - 1] if len(nums2)>=k/2 else None
        
        if b is None or (a is not None and a<b):
            return self.findKth(nums1[k/2:], nums2, k-k/2)
        else:
            return self.findKth(nums1, nums2[k/2:], k-k/2)


if __name__ == "__main__":
    l1, l2 = [], [1]
    # l1, l2 = [1], [1]
    # l1, l2 = [1, 2, 3, 4], [5, 6, 7]
    # l1, l2 = [1, 2, 8, 10], [5, 6, 7]
    # l1, l2 = [1, 2, 4, 8], [5, 6, 8, 10]
    l1, l2 = [1], [2, 3, 4, 5, 6]
    print Solution().findMedianSortedArrays(l1, l2)
