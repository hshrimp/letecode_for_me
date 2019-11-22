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


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        length = len(board[0])
        row = len(board)

        def track(i, j, index, b):
            print(i, j, word, b)
            if not word:
                res.append(1)
                return
            if 0 > i or i >= row or 0 > j or j >= length:
                # print(i, j)
                return
            # w = str(word)
            b = [list(l) for l in b]
            b[i][j] = ''
            try:
                if b[i - 1][j] == word[index]:
                    track(i - 1, j, index + 1, b)
            except:
                pass
            try:
                if b[i + 1][j] == word[index]:
                    track(i + 1, j, w[1:], b)
            except:
                pass
            try:
                if b[i][j - 1] == word[index]:
                    track(i, j - 1, w[1:], b)
            except:
                pass
            try:
                if b[i][j + 1] == word[index]:
                    track(i, j + 1, w[1:], b)
            except:
                pass

        res = []
        for i, l in enumerate(board):
            for j, v in enumerate(l):
                if v == word[0]:
                    track(i, j, word[1:], board)
                    if sum(res) > 0:
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
