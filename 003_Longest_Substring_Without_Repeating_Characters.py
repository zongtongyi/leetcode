#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p_left, subs, r = 0, [], 0
        for i in range(len(s)):
            if s[i] in subs:
                p_left = s.index(s[i], p_left) + 1
                r = max(r, len(subs))
            subs = s[p_left:i+1]
        return max(r, len(subs))

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("bbbbbabc")
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("bbbb")

