#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        rows = [[] for i in range(9)]
        colm = [[] for i in range(9)]
        subboard = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue

                if x in rows[i]:
                    return False
                if x in colm[j]:
                    return False
                rows[i].append(x)
                colm[j].append(x)

                si = i/3*3 + j/3
                if x in subboard[si]:
                    return False
                subboard[si].append(x)
        return True


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
