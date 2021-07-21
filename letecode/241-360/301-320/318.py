#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/4 上午10:27
"""
"""318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。
你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。"""


class Solution:
    def maxProduct(self, words) -> int:
        def check(s1, s2):
            if s1 - s2 == s1:
                return True
            return False

        d = {}
        for word in words:
            d[word] = [len(word), set(word)]
        length = len(d)
        keys = list(d.keys())
        res = 0
        for i in range(length - 1):
            for j in range(1, length):
                if check(d[keys[i]][1], d[keys[j]][1]):
                    res = max(res, d[keys[i]][0] * d[keys[j]][0])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct(["a","aa","aaa","aaaa"]))
