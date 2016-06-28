#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if len(s)==0: return 0
        
        valid_s = [str(x) for x in range(10)]
        def get_numbers(s1):
            num_s = []
            for x in s1:
                if x in valid_s:
                    num_s.append(x)
                else:
                    break
            if not num_s: return 0
            else: return int( ''.join(num_s) )
        
        def fix1(num):
            if num>2**31: return (2**31)-1
            if num<-2**31: return -2**31
            return num

        s = s.strip()
        if '-' == s[0]:
            s = s[1:]
            return fix1( get_numbers(s).__neg__() )
        elif '+' == s[0]:
            s = s[1:]
            return fix1( get_numbers(s) )
        else:
            return fix1( get_numbers(s) )




if __name__ == "__main__":
    s1 = "123"
    s1 = "1"
    s1 = "2147483648"
    print Solution().myAtoi(s1)
    pass

