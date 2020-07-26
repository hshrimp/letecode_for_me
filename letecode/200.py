#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/15 下午2:44
"""
"""200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。"""


class Solution:
    def numIslands(self, grid) -> int:
        def check(i, j):
            nonlocal row, col
            stack = [[i, j]]
            while stack:
                i, j = stack.pop()
                for p, q in dir:
                    if 0 <= i + p < row and 0 <= j + q < col:
                        if (i + p, j + q) not in visit and grid[i + p][j + q] == '1':
                            stack.append([i + p, j + q])
                            visit.add((i + p, j + q))

        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        dir = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        visit = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] == '1':
                    check(i, j)
                    print(visit)
                    res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(sol.numIslands(grid))
