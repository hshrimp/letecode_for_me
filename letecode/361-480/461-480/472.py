#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/20 下午4:22
"""
"""472. 连接词
给定一个 不含重复 单词的字符串数组 words ，编写一个程序，返回 words 中的所有 连接词 。

连接词 的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats"由"cats", "dog" 和 "cats"组成; 
     "dogcatsdog"由"dog", "cats"和"dog"组成; 
     "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]
 
提示：

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 6 * 105"""

from collections import defaultdict


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def find(li, l):
            print(li, l)
            if [l - 1, 0] in li:
                return True
            for i, cur in enumerate(li):
                if cur[0] == l - 1:
                    if find(li[i + 1:], cur[1]):
                        return True
                elif cur[0] < l - 1:
                    return False

        word2con = defaultdict(list)
        words.sort(key=lambda x: len(x), reverse=True)
        for i, cur in enumerate(words[:-2]):
            for word in words[i + 1:]:
                begin = 0
                length = len(word)
                while word in cur[begin:]:
                    left = cur.index(word, begin)
                    right = left + length - 1
                    word2con[cur].append([right, left])
                    begin = right + 1
        res = []
        for k, v in word2con.items():
            print(k, v)
            if find(sorted(v, reverse=True), len(k)):
                res.append(k)
        return res

    def findAllConcatenatedWordsInADict2(self, words):
        def find(word):
            if word in visited:
                return True
            for i in range(min_l, len(word) - min_l + 1):
                if word[:i] in visited and find(word[i:]):
                    return True

        visited = set()
        words.sort(key=len)
        min_l = max(1, len(words[0]))
        res = []
        for word in words:
            if find(word):
                res.append(word)
            visited.add(word)
        return res

    def findAllConcatenatedWordsInADict3(self, words):
        def dfs(S, s, step, tab):
            print(s, step, tab)
            if step == len(s):
                return True
            if step in tab:
                return tab[step]
            l = len(s) - 1 if step > 0 else len(s) - 2
            for i in range(l, step - 1, -1):
                if s[step:i + 1] in words and dfs(S, s, i + 1, tab):
                    tab[step] = True
                    return True
            tab[step] = False
            return False

        res = []
        words = set(words)
        for word in words:
            if len(word) > 1 and dfs(words, word, 0, {}):
                res.append(word)
        return res


if __name__ == '__main__':
    sol = Solution()
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(sol.findAllConcatenatedWordsInADict(words))
    print(sol.findAllConcatenatedWordsInADict2(words))
    print(sol.findAllConcatenatedWordsInADict3(words))
