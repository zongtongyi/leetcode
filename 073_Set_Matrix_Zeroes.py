#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_column = set(), set()
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_column.add(j)

        for i in xrange(m):
            for j in xrange(n):
                if i in zero_row or j in zero_column:
                    matrix[i][j] = 0



def matrix_print(matrix):
    for l in matrix:
        print l

if __name__ == "__main__":
    matrix = [
            [1,2,3,4,5],
            [2,0,3,5,5],
            [3,2,3,0,9],
            ]
    Solution().setZeroes(matrix)
    matrix_print(matrix)
