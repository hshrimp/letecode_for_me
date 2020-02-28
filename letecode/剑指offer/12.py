#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/25 16:50
"""
"""面试题12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/"""


class Solution:

    def exist(self, board, word: str) -> bool:
        def trackback(m, index, i, j):
            if index == len(word) - 1:
                return word[-1] == board[i][j]
            if word[index] == board[i][j]:
                m[i][j] = True
                for x, y in direction:
                    newx = i + x
                    newy = j + y
                    if 0 <= newx < row and 0 <= newy < col and not m[newx][newy] and trackback(m, index + 1, newx,
                                                                                               newy):
                        return True
                m[i][j] = False
            return False

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(board)
        if not row:
            return False
        col = len(board[0])
        mark = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if trackback(mark, 0, i, j):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]

    print(sol.exist(board, 'ABCES'))
