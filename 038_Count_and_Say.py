#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def count(self, s):
        ss, sn, sout = s[0], 1, ''
        for x in xrange(1, len(s)):
            if s[x]==ss:
                sn += 1
            else:
                sout = sout + str(sn) + ss
                ss = s[x]
                sn = 1

        return sout + str(sn) + ss

    def countAndSay(self, n):
        s = '1'
        for x in xrange(2, n+1):
            s = self.count(s)
        return s


if __name__ == "__main__":
    n = 1211
    n = 11
    # n = 1
    print Solution().countAndSay(n)
