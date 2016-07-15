#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

# Solution 2: Normal match
# Solution 3: KMP (Good time complexity)
# Solution 4: using suffix array, add into prefix trie, then search the trie (clean)
# Solution 5: Boyer-Moore (Better)
#  http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html

if __name__ == "__main__":
    s1 = "0123456789"
    s2 = "2345"
    print Solution().strStr(s1, s2)
