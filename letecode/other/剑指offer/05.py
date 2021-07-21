#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/24 17:46
"""
"""面试题05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 
限制：

0 <= s 的长度 <= 10000"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.replace(' ', '%20')
        return s

    def replaceSpace2(self, s: str) -> str:
        p = ''
        for i, c in enumerate(s):
            if c == ' ':
                p += '%20'
            else:
                p += c
        return p


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceSpace2('i i  ewhihiu  ni'))
