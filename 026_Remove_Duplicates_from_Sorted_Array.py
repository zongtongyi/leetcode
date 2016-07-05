#! /usr/bin/env python
# -*- coding:utf-8 -*-
# One Slow pointer, one Traversal pointer

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0

        # Slow move, point to Current Max nunmber, 
        # its Next position is Update position
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == "__main__":
    nums = [1, 2]
    #nums = [1, 1, 2]
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 6]
    nums = [1]

    print nums
    n = Solution().removeDuplicates(nums)
    print "n:", n
    print nums[:n]
