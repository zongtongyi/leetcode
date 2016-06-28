#! /usr/bin/env python
# -*- coding:utf-8 -*-
# by mac 2016-06-28 08:40:50

INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution(object):
    def reverse(self, x):
        sig, res = 1, 0
        if x < 0:
            sig = -1

        while x>0:
            res = res*10 + x%10
            x /= 10

        return sig * res

class Solution(object):
    def reverse(self, x):
        sx = str(x)
        sx = sx[::-1]
        ix = int(sx)

if __name__ == "__main__":
    Solution().reverse(123)
    Solution().reverse(-123)
    Solution().reverse(100)
    Solution().reverse(1000000003)
