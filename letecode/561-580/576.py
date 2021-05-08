#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/7 下午6:02
"""
"""576. 出界的路径数
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。
但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

示例 1：

输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6
解释:

示例 2：

输入: m = 1, n = 3, N = 3, i = 0, j = 1
输出: 12
解释:

说明:

球一旦出界，就不能再被移动回网格内。
网格的长度和高度在 [1,50] 的范围内。
N 在 [0,50] 的范围内。
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        from collections import defaultdict
        matrix = defaultdict(int)
        dir = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for i in range(m):
            for j in range(n):
                out_times = 0
                for x, y in dir:
                    if i + x < 0 or i + x >= m or j + y < 0 or j + y >= n:
                        out_times += 1
                matrix[(i, j)] = out_times
        stack = {(startRow, startColumn): 1}
        res = 0
        while maxMove:
            print(stack)
            for point in stack:
                res += matrix[point] * stack[point]
            temp = defaultdict(int)
            for i, j in stack:
                for x, y in dir:
                    if 0 <= i + x < m and 0 <= j + y < n:
                        temp[(i + x, j + y)] += stack[(i, j)]
            maxMove -= 1
            stack = temp
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPaths(7, 6, 13, 0, 2))
