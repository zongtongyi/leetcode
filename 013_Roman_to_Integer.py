#! /usr/bin/env python
# -*- coding:utf-8 -*-
# I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）

class Solution(object):
    def romanToInt(self, s):
        ROMAN = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        tc, res = 'I', 0
        for c in s[::-1]:
            if ROMAN[c] >= ROMAN[tc]:
                res, tc = res + ROMAN[c], c
            else:
                res, tc = res - ROMAN[c], c

        return res


if __name__ == "__main__":
    print Solution().romanToInt('XVIII') # 18
    print Solution().romanToInt('XCIX')  # 99
    print Solution().romanToInt('MCDXXXVII') # 1437
    pass
