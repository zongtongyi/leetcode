#! /usr/bin/env python
# -*- coding:utf-8 -*-
# step i, could compose by step i-1 by one step, and step i-2 by two steps.

class Solution(object):
    def climbStairs(self, n):
        if n in [0, 1]: return n

        nm2, nm1 = 1, 1
        for x in xrange(2, n):
            tmp = nm1
            nm1 = nm1 + nm2
            nm2 = tmp

        return nm1 + nm2


if __name__ == "__main__":
    print Solution().climbStairs(0)
    print Solution().climbStairs(1)
    print Solution().climbStairs(2)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
    print Solution().climbStairs(5)
