#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        pass


# Solution 2: bitmap
# Solution 3: N-Queen

if __name__ == "__main__":
    board = [".87654321",
            "2........",
            "3........",
            "4........",
            "5........",
            "6........",
            "7........",
            "8........",
            "9........"]
    print Solution().isValidSudoku(board)
