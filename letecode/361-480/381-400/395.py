#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/17 下午3:21
"""
"""395. 至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = Counter(s)
        li = [s]
        temp = []
        flag = True
        for key, v in c.items():
            if v < k:
                for l in li:
                    temp.extend(l.split(key))
                li, temp = temp, []
                flag = False
        if flag:
            return len(s)

        return max([self.longestSubstring(l, k) for l in li])


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubstring(s="ababbc", k=2))
