#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in reversed(xrange(len(digits))):
            if carry:
                n = digits[i] + 1
                if n==10:
                    digits[i], carry = 0, 1
                else:
                    digits[i], carry = n, 0

        if carry:
            digits.insert(0, 1)

        return digits



if __name__ == "__main__":
    # digits = [9, 9]
    # digits = [0]
    digits = [1, 2, 3]
    Solution().plusOne(digits)
    print digits

