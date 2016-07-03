#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        if num==0: return 0

        res = []
        # nd = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        dc = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        dn = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for k,v in zip(dc, dn):
            if num >= v:
                n = num / v
                num %= v
                res.append(k*n)

        return ''.join(res)

if __name__ == "__main__":
    print Solution().intToRoman(3999)
    print Solution().intToRoman(1437)
    print Solution().intToRoman(99)
    print Solution().intToRoman(18)
