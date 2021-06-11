#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 上午10:12
"""
"""240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            if target < matrix[i][0]:
                return False
            else:
                if target in matrix[i]:
                    return True
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        x = len(matrix) - 1
        y = 0
        while x >= 0 and y <= len(matrix[0]):
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                x -= 1
            if matrix[x][y] < target:
                y += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(sol.searchMatrix(matrix, target))
    print(sol.searchMatrix2(matrix, target))
