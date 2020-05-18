#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-18 10:09
"""
"""130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。"""


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        dir = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        row = len(board)
        col = len(board[0])
        out = [(0, i) for i in range(col)] + [(j, 0) for j in range(1, row)] + [(row - 1, i) for i in range(1, col)] + [
            (j, col - 1) for j in range(1, row - 1)]
        temp = set(out)
        while out:
            x, y = out.pop()
            for d in dir:
                if 0 <= x + d[0] < row and 0 <= y + d[1] < col and (x + d[0], y + d[1]) not in temp and board[x][y] == 'O':
                    temp.add((x + d[0], y + d[1]))
                    out.append((x + d[0], y + d[1]))
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'O' and (i, j) not in temp:
                    board[i][j] = 'X'
        return board


if __name__ == '__main__':
    sol = Solution()
    b = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
    print(sol.solve(b))
