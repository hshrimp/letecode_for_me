#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-19 11:03
"""
"""680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            temp = s[:i] + s[i + 1:]
            if temp[::-1] == temp:
                return True
        else:
            return False

    def validPalindrome2(self, s: str) -> bool:
        end = len(s) - 1
        start = 0
        while end > start:
            if s[start] != s[end]:
                temp1 = s[:start] + s[start + 1:]
                if temp1 == temp1[::-1]:
                    return True
                temp2 = s[:end] + s[end + 1:]
                if temp2 == temp2[::-1]:
                    return True
                return False
            end -= 1
            start += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPalindrome2('abca'))
