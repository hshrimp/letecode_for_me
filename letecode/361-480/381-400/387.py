#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/15 下午7:40
"""
"""387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 
提示：你可以假定该字符串只包含小写字母。"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar("loveleetcode"))
