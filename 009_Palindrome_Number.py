#! /usr/bin/env python
# -*- coding:utf-8 -*-
# by mac 2016-06-28 08:40:50

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if x == 0: return True
        
        res, x0 = 0, x
        while x > 0:
            res = res*10 + x%10
            x /= 10
            
        if res == x0:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])


if __name__ == "__main__":
    print Solution().isPalindrome(123)
    print Solution().isPalindrome(-123)
    print Solution().isPalindrome(100)
    print Solution().isPalindrome(1020)
    print Solution().isPalindrome(1000000003)
