#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def removeElement(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break

        return len(nums)



if __name__ == "__main__":
    nums = [3,2,2,3]
    val  = 3
    print Solution().removeElement(nums, val)
