#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/26 下午9:57
"""
"""214. 最短回文串
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd" """


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s)):
            if i == 0:
                if s == s[::-1]:
                    return s
            else:
                temp = s[:-i]
                if temp == temp[::-1]:
                    return s[-i:][::-1] + s


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPalindrome('a'))
