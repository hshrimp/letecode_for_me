#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/7 上午11:26
"""
"""289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。
每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，
其中细胞的出生和死亡是同时发生的。

示例：

输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
 
进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
通过次数37,063提交次数49,847"""


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count(i, j):
            c = 0
            for p, q in dir:
                if 0 <= i + p < row and 0 <= j + q < col and board[i + p][j + q] == 1:
                    c += 1
            return c

        if not board or not board[0]:
            return
        dir = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
        row = len(board)
        col = len(board[0])
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                num = count(i, j)
                if board[i][j] == 0:
                    if num == 3:  # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                        res[i][j] = 1
                else:
                    if num < 2:
                        res[i][j] = 0  # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                    if 2 <= num <= 3:  # 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
                        res[i][j] = 1
                    if num > 3:  # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                        res[i][j] = 0
        for i in range(row):
            board[i][:] = res[i][:]
        return board

    def gameOfLife2(self, board) -> None:
        def count(i, j):
            c = 0
            for p, q in dir:
                if 0 <= i + p < row and 0 <= j + q < col and (board[i + p][j + q] == 1 or board[i + p][j + q] == -1):
                    c += 1
            # print(i, j, c)
            return c

        if not board or not board[0]:
            return
        dir = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                num = count(i, j)
                if board[i][j] == 0:
                    if num == 3:  # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                        board[i][j] = 2
                else:
                    if num < 2:
                        board[i][j] = -1  # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                    if num > 3:  # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                        board[i][j] = -1
        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        return board

    def gameOfLife4show(self, board) -> None:
        def count(i, j):
            c = 0
            for p, q in dir:
                if 0 <= i + p < row and 0 <= j + q < col and (board[i + p][j + q] == 1 or board[i + p][j + q] == -1):
                    c += 1
            # print(i, j, c)
            return c

        dir = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                num = count(i, j)
                if board[i][j] == 0:
                    if num == 3:  # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                        board[i][j] = 2
                else:
                    if num < 2:
                        board[i][j] = -1  # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                    if num > 3:  # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                        board[i][j] = -1
        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        return board


def show():
    import time
    import os  # 导入os模块
    import numpy as np
    board = np.random.randint(0, 1, (30, 100))
    board[0][2], board[1][0], board[1][2], board[2][1], board[2][2] = 1, 1, 1, 1, 1
    while True:
        board = sol.gameOfLife4show(board)
        for i in range(len(board)):
            print(''.join('*' if j == 1 else ' ' for j in board[i]))
        print('-----------------------------------------------------------------------------------------------------')
        time.sleep(0.5)
        os.system('clear')


if __name__ == '__main__':
    sol = Solution()
    # board = [[0] * 50 for _ in range(20)]

    # print(sol.gameOfLife(board))
    # print(sol.gameOfLife2(board))
    show()
