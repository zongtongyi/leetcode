#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLastWord(self, s):
        if not s.strip(): return 0
        return len(s.strip().split()[-1])
