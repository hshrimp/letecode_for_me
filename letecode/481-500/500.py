#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/4 下午3:54
"""
"""500. 键盘行
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
American keyboard

示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]
 
提示：

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成"""


class Solution:
    def findWords(self, words):
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        res = []
        temp = []
        for cur_word in words:
            word = cur_word.lower()
            if word[0] in first:
                temp = first
            if word[0] in second:
                temp = second
            if word[0] in third:
                temp = third
            if any([c not in temp for c in word]):
                continue
            res.append(cur_word)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
