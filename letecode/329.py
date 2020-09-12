#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/9 下午3:35
"""
"""329. 矩阵中的最长递增路径
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。"""
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        @lru_cache(None)
        def dfs(i, j):
            best = 1
            for x, y in dir:
                if 0 <= i + x < row and 0 <= j + y < col and matrix[i + x][j + y] < matrix[i][j]:
                    best = max(best, dfs(i + x, j + y) + 1)
            return best

        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dir = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i, j))
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    print(sol.longestIncreasingPath(nums))
