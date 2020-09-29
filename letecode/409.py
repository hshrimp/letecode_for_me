#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/23 上午10:29
"""
"""409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = 0
        flag = 0
        for k, v in d.items():
            if v % 2 == 0:
                res += v
            elif v > 2:
                res += v - 1
                flag = 1
            elif v > 0 and not flag:
                flag = 1
        return res + flag


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('cccccdd'))
