#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/3 下午5:19
"""
"""389. 找不同
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。"""

from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = defaultdict(int)
        for c in s:
            ds[c] += 1
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        for k, v in dt.items():
            if k not in ds:
                return k
            if v != ds[k]:
                return k


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheDifference(s="abcd", t="abcde"))
