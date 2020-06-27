#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-08 09:52
"""
"""131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]"""


class Solution:
    def partition(self, s: str):
        res = [[s[0]]]
        for i in range(1, len(s)):
            for li in res[:len(res)]:
                print(res)
                if len(li) > 1 and li[-2] == s[i]:
                    res.append(li[:-2] + [li[-2] + li[-1] + s[i]])
                if li[-1] == s[i]:
                    res.append(li[:-1] + [li[-1] + s[i]])
                li.append(s[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition("aab"))
