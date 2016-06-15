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
            return findKth(nums1, nums2, n/2+1)
        else:
            k1 = findKth(nums1, nums2, n/2)
            k2 = findKth(nums1, nums2, n/2+1)
            return (k1+k2)/2.0

    def findKth():
        pass


if __name__ == "__main__":
    # l1, l2 = [], [1]
    # l1, l2 = [1], [1]
    l1, l2 = [1, 2, 3, 4], [5, 6, 7]
    # l1, l2 = [1, 2, 8, 10], [5, 6, 7]
    # l1, l2 = [1, 2, 4, 8], [5, 6, 8, 10]
    print Solution().findMedianSortedArrays(l1, l2)
