#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-18 10:01
"""
"""给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


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
    # board = [["A", "A"]]

    print(sol.exist(board, 'ASA'))
