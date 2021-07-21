#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/15 下午3:59
"""
"""542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。


示例 1：

输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

输出：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
示例 2：

输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]

输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

提示：

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。"""

from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        visited = set()
        stack = deque()
        dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    stack.append((i, j, 0))
                    visited.add((i, j))
        while stack:
            x, y, level = stack.popleft()
            for i, j in dir:
                tempx = x + i
                tempy = y + j
                if 0 <= tempx < row and 0 <= tempy < col and (tempx, tempy) not in visited:
                    matrix[tempx][tempy] = level + 1
                    stack.append((tempx, tempy, level + 1))
                    visited.add((tempx, tempy))
        return matrix


if __name__ == '__main__':
    sol = Solution()
    m = [[0, 0, 0],
         [0, 1, 0],
         [1, 1, 1]]
    print(sol.updateMatrix(m))
