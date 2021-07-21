#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/9 下午5:54
"""
"""419. 甲板上的战舰
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

X..X
...X
...X
在上面的甲板中有2艘战舰。

无效样例 :

...X
XXXX
...X
你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。

进阶:

你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？"""


class Solution:
    def countBattleships(self, board) -> int:
        if not board or not board[0]:
            return 0
        visited = set()
        res = 0
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    if (i - 1, j) not in visited and (i, j - 1) not in visited:
                        res += 1
                    visited.add((i, j))

        return res

    def countBattleships2(self, board) -> int:
        if not board or not board[0]:
            return 0
        res = 0
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    if (i - 1 >= 0 and board[i - 1][j] == 'X') or (j - 1 >= 0 and board[i][j - 1] == 'X'):
                        continue
                    else:
                        res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
    print(sol.countBattleships2([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
