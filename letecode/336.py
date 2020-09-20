#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/17 下午3:11
"""
"""336. 回文对
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1：

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]] 
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]] 
解释：可拼接成的回文串为 ["battab","tabbat"]"""

from functools import lru_cache


class Solution:
    def palindromePairs(self, words):
        res = []
        length = len(words)
        for i in range(length):
            for j in range(length):
                if i != j:
                    temp = words[i] + words[j]
                    if temp == temp[::-1]:
                        res.append([i, j])
        return res

    def palindromePairs2(self, words):
        @lru_cache(None)
        def check(a):
            if a[:] == a[::-1]:
                return True
            return False

        res = []
        length = len(words)
        for i in range(length):
            cur_length = len(words[i])
            for j in range(length):
                if i != j:
                    jl = len(words[j])
                    if cur_length >= jl:
                        if words[i][:jl] == words[j][::-1] and check(words[i][jl:]):
                            res.append([i, j])
                    else:
                        if words[j][jl - cur_length:] == words[i][::-1] and check(words[j][:jl - cur_length]):
                            res.append([i, j])

        return res

    def palindromePairs3(self, words):
        res = []
        word_dict = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]
                if left[::-1] in word_dict and word_dict[left[::-1]] != i and right == right[::-1]:
                    res.append([i, word_dict[left[::-1]]])
                if j > 0 and right[::-1] in word_dict and word_dict[right[::-1]] != i and left == left[::-1]:
                    res.append([word_dict[right[::-1]], i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(sol.palindromePairs2(["a", ""]))
    print(sol.palindromePairs3(["abcd", "dcba", "lls", "s", "sssll"]))
