#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/16 下午5:10
"""
"""205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        visit = set()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
                if t[i] in visit:
                    return False
                visit.add(t[i])
            else:
                if d[s[i]] != t[i]:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "paper"
    t = "tiwlw"
    print(sol.isIsomorphic(s, t))
