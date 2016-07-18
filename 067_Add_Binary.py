#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def addBinary(self, a, b):
        return "{0:b}".format( int(a,2) + int(b,2) )


if __name__ == "__main__":
    a, b = '0', '0'
    a, b = '11', '1'
    print Solution().addBinary(a, b)
