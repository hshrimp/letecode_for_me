#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 下午4:11
"""
"""522. 最长特殊序列 II
给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。

示例：

输入: "aba", "cdc", "eae"
输出: 3
 
提示：

所有给定的字符串长度不会超过 10 。
给定字符串列表的长度将在 [2, 50 ] 之间。"""


class Solution:
    def findLUSlength(self, strs) -> int:
        def find(string):
            cur = set()
            for c in string:
                this = set([p + c for p in cur])
                cur.update(this)
                cur.add(c)
            contain.update(cur)

        from collections import defaultdict
        d = defaultdict(int)
        for s in strs:
            d[s] += 1
        d = sorted(d.items(), key=lambda x: len(x[0]), reverse=True)
        contain = set()
        for k, v in d:
            if v > 1:
                find(k)
                continue
            if k in contain:
                continue
            return len(k)
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLUSlength(["aba", "cdc", "eae"]))
