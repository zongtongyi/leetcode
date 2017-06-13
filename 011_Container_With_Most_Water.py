#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(height)-1
        while i < j:
            max_area = max( max_area, min(height[j],height[i])*(j-i) )
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    height = [1, 0, 0, 7, 2, 11, 15]
    sol = Solution()
    print sol.maxArea(height)

