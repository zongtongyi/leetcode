#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i_m, i_n = m-1, n-1
        p = m+n-1
        while i_m>=0 and i_n>=0:
            if nums1[i_m]>nums2[i_n]:
                nums1[p] = nums1[i_m]
                i_m = i_m - 1
            else:
                nums1[p] = nums2[i_n]
                i_n = i_n - 1
            p = p - 1

        while i_n>=0:
            nums1[i_n] = nums2[i_n]
            i_n = i_n - 1

        # 如果第一个while因为i_n<0退出，即i_m>0，则nums1剩下部分不需要处理
        # while i_m>=0:


if __name__ == "__main__":
    # nums1, m = [1, 4, 7, 0, 0], 3
    # nums2, n = [2, 9], 2
    nums1, m = [7, 9, 0, 0, 0], 2
    nums2, n = [1, 2, 8], 3
    Solution().merge(nums1, m, nums2, n)
    print nums1
