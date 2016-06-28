#! /usr/bin/env python
# -*- coding:utf-8 -*-
# by mac 2016-06-28 08:40:50

INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution(object):
    def reverse(self, x):
        sig = 1
        if x < 0:
            sig, x = -1, abs(x)

        res = 0
        while x > 0:
            res = res*10 + x%10
            x /= 10

        res *= sig
        if res > 2**31 - 1 or res < -2**31:
            return 0

        return res

class Solution(object):
    def reverse(self, x):
        sig = 1
        if x < 0:
            sig, x = -1, abs(x)

        sx = str(x)
        sx = sx[::-1]
        ix = int(sx)

        ix *= sig
        if ix > 2**31 - 1 or ix < -2**31:
            return 0

        return ix


if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(100)
    print Solution().reverse(1020)
    print Solution().reverse(1000000003)
