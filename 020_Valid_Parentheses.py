#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        tl = []
        dp = {'}':'{', ']':'[', ')':'('}
        for c in s:
            if not tl:
                tl.append(c)
            else:
                if c in dp and dp[c] == tl[-1]:
                    tl.pop()
                else:
                    tl.append(c)
        
        return False if tl else True


if __name__ == "__main__":
    print Solution().isValid('()')
    print Solution().isValid('{()}')
    print Solution().isValid('{()[]}')
    print Solution().isValid('{()[]{}}')
    print Solution().isValid('([)]')
