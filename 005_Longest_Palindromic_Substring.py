#! /usr/bin/env python
# -*- coding:utf-8 -*-

# This submission is pretty slow, and could not pass the time limitation
# class Solution(object):
#     def longestPalindrome(self, s):
#         s2 = s[::-1]
#         s_suffix_array, s2_suffix_array = [], []
#         self.build_suffix_array(s_suffix_array, s)
#         self.build_suffix_array(s2_suffix_array, s2)
#         max_len, lcs = 0, ''
#         for i in range(len(s_suffix_array)):
#             for j in range(len(s2_suffix_array)):
#                 com_len = self.comlen(s_suffix_array[i], s2_suffix_array[j])
#                 max_len, lcs = (com_len, s_suffix_array[i]) if com_len>max_len else (max_len, lcs)
# 
#         # return max_len
#         return lcs[:max_len]
# 
#     def build_suffix_array(self, suffix_array, text_string):
#         for i in range(len(text_string)):
#             suffix_array.append(text_string[i:])
# 
#         suffix_array.sort()
# 
#     def comlen(self, str_i, str_i_next):
#         max_len = 0
#         for i in range(1, len(str_i)+1):
#             max_len = i if str_i[:i]==str_i_next[:i] else max_len
#     
#         return max_len


# This submission is slow too, only beats 15.26%, and cost almost 1570ms which many people only use less than 200ms.
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1 or not s: return s

        lcs = ''
        for i in range(len(s)):
            odd_lcs  = self.find_lcs(s, i, i)
            lcs = odd_lcs if len(odd_lcs) > len(lcs) else lcs
            even_lcs = self.find_lcs(s, i, i+1)
            lcs = even_lcs if len(even_lcs) > len(lcs) else lcs
        return lcs

    def find_lcs(self, s, i_forward, i_backward):
        while i_backward <= len(s)-1 and i_forward >= 0 and s[i_forward]==s[i_backward]:
            i_forward -= 1
            i_backward += 1
        return s[i_forward+1:i_backward]


if __name__ == '__main__':
    print Solution().longestPalindrome("12343")
    print Solution().longestPalindrome("123432")
    print Solution().longestPalindrome("222222223432")

