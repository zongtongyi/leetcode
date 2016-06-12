#! /usr/bin/env python
# -*- coding:utf-8 -*-

from collections import OrderedDict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            t2 = target - x
            if t2 in nums[i+1:]:
                return i, nums.index(t2, i+1)


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    nums = [1, 7, 2, 11, 15]
    nums = [3,2,4]
    target = 6
    sol = Solution()
    print sol.twoSum(nums, target)

