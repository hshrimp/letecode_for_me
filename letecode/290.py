#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/5 上午10:22
"""
"""290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    """


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        d = {}
        d2 = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            elif s[i] != d[pattern[i]]:
                return False

            if s[i] not in d2:
                d2[s[i]] = pattern[i]
            elif d2[s[i]] != pattern[i]:
                return False
        return True

    def wordPattern2(self, pattern: str, str: str) -> bool:
        s = str.split()
        d = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in d:
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
            else:
                if d[pattern[i]] != s[i]:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern(pattern="abba", str="dog cat cat fish"))
    print(sol.wordPattern2(pattern="abba", str="dog cat cat fish"))
