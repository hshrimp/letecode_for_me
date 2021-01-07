#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/3 上午11:10
"""
"""438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        target = Counter(p)
        length = len(p)
        if len(s) < length:
            return []
        res = []
        cur = Counter(s[:length])
        if cur == target:
            res.append(0)
        for i in range(length, len(s)):
            cur[s[i - length]] -= 1
            if cur[s[i - length]] == 0:
                cur.pop(s[i - length])
            cur[s[i]] += 1
            if cur == target:
                res.append(i - length + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "abab"
    p = "ab"
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams(s, p))
