#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def convert(self, s, numRows):
        if len(s)<=numRows or numRows==1:
            return s

        reslists = [[] for x in range(numRows)]

        row, move = 0, 1
        for c in s:
            reslists[row].append(c)
            if row == numRows - 1:
                move = -1
            elif row == 0:
                move = 1
            row += move

        return ''.join( [x for l in reslists for x in l] )


if __name__ == "__main__":
    print Solution().convert('PAYPALISHIRING', 3)
    print Solution().convert('PAYPALISHIRING', 4)
