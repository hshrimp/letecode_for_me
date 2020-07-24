#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/21 下午3:11
"""
"""212. 单词搜索 II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。"""


class Solution:
    def findWords2(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[1] = 1

        def find(x, y, root, pre, visited):
            if 1 in root:
                res.add(pre)
            for i, j in dir:
                if 0 <= x + i < row and 0 <= y + j < col and board[x + i][y + j] in root and (
                        x + i, y + j) not in visited:
                    find(x + i, y + j, root[board[x + i][y + j]], pre + board[x + i][y + j],
                         visited.union([(x + i, y + j)]))

        if not board or not board[0]:
            return []
        dir = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        res = set()
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] in trie:
                    find(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)

    def findWords(self, board, words):
        def find(visit, word, x, y):
            # print(visit, word)
            if not word:
                return True
            for i, j in dir:
                if 0 <= x + i < row and 0 <= y + j < col and board[x + i][y + j] == word[0] and (
                        x + i, y + j) not in visit:
                    if find(visit.union([(x + i, y + j)]), word[1:], x + i, y + j):
                        return True
            else:
                return False

        if not board or not board[0]:
            return []
        dir = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        res = []
        row = len(board)
        col = len(board[0])

        for word in words:
            break2 = False
            for i in range(row):
                for j in range(col):
                    if board[i][j] == word[0]:
                        if find({(i, j)}, word[1:], i, j):
                            res.append(word)
                            break2 = True
                            break
                if break2:
                    break
        return res


if __name__ == '__main__':
    sol = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    # board = [["a", "a"]]
    # words = ["aaa"]
    board = [["a", "b"], ["a", "a"]]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
    board = [["a", "b", "c"],
             ["a", "e", "d"],
             ["a", "f", "g"]]
    words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
    print(sol.findWords(board, words))
    print(sol.findWords2(board, words))

