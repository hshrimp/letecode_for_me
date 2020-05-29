#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-27 15:20
"""
"""140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]"""

from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict):
        def track_back(li, last):
            if last in wordDict:
                res.append(' '.join(li + [last]))
                # return
            for i in range(1, len(last)):
                if last[:i] in wordDict:
                    track_back(li + [last[:i]], last[i:])

        res = []
        track_back([], s)
        return res

    def wordBreak2(self, s: str, wordDict):
        def track_back(li, last):
            if last in wordDict:
                res.append(' '.join(li + [last]))
            for l in d:
                if l <= len(last) and last[:l] in d[l]:
                    track_back(li + [last[:l]], last[l:])

        res = []
        d = {}
        max_word = 0
        for w in wordDict:
            length = len(w)
            l = d.get(length, set())
            l.add(w)
            d[length] = l
            max_word = max(max_word, length)
        max_word += 1
        track_back([], s)
        return res

    def wordBreak3(self, s: str, wordDict: List[str]) -> List[str]:
        size = len(s)

        # 题目中说非空字符串，以下 assert 一定通过
        assert size > 0

        # 预处理，把 wordDict 放进一个哈希表中
        word_set = {word for word in wordDict}

        # dp[i] 表示长度为 i 的 s，满足题意
        # 0 表示 False ，1 表示 True
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1

        for i in range(1, size + 1):
            # i 表示 s 子串的长度
            for j in range(i):
                # j 表示后子串的起始位置，最多到 i-1
                # j 也正正好表示前子串的长度
                # dp[j] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
                if dp[j] and s[j:i] in word_set:
                    dp[i] = 1
                    break

        res = []
        # 如果有解，才有必要回溯
        if dp[-1]:
            queue = deque()
            self.__dfs(s, size, word_set, res, queue, dp)
        return res

    def __dfs(self, s, length, word_set, res, path, dp):
        print(s, length, word_set, res, path, dp)
        if length == 0:
            res.append(' '.join(path))
            return
        for i in range(length):
            if dp[i]:
                suffix = s[i:length]
                if suffix in word_set:
                    path.appendleft(suffix)
                    self.__dfs(s, i, word_set, res, path, dp)
                    path.popleft()

    def wordBreak4(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(length, li):
            if length == 0:
                res.append(' '.join(li))
            for i in range(length):
                if dp[i]:
                    suffix = s[i:length]
                    if suffix in wordDict:
                        li.appendleft(suffix)
                        dfs(i, li)
                        li.popleft()

        n = len(s)
        res = []
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True
        if dp[-1]:
            queue = deque()
            dfs(n, queue)
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "aaaaaaa"
    # wordDict = ["aaaa", "aa", "a"]
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    # print(sol.wordBreak(s, wordDict))
    print(sol.wordBreak4(s, wordDict))
