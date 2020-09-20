#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/15 下午8:40
"""
"""541. 反转字符串 II
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 
示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
 
提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        i = 0
        while i < length:
            if i + 2 * k < length:
                s = s[:i] + s[i:i + k][::-1] + s[i + k:]
                i += 2 * k
            elif i + k < length:
                s = s[:i] + s[i:i + k][::-1] + s[i + k:]
                return s
            else:
                s = s[:i] + s[i:][::-1]
                return s


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseStr(s="abcdefg", k=2))
