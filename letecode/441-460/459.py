#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/7 下午4:27
"""
"""459. 重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(length // 2):
            times, last = divmod(length, i + 1)
            if last:
                continue
            if s == s[:i + 1] * times:
                return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        length = len(s)
        return (s + s).find(s, 1) != length


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern('abca'))
    print(sol.repeatedSubstringPattern2('abca'))
