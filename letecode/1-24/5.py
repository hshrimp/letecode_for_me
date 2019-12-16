#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-16 10:04
"""
"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        fi = ''
        for i in range(len(s) - 1):
            m = search(s, i, i)
            n = search(s, i, i + 1)
            if len(m) > len(fi):
                fi = m
            if len(n) > len(fi):
                fi = n
        return fi


def search(s, i, j):
    if s[i] == s[j]:
        if i - 1 >= 0 and j + 1 < len(s):
            return search(s, i - 1, j + 1)
        else:
            return s[i:j + 1]
    else:
        return s[i + 1:j]
