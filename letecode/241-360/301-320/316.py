#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/8 下午2:15
"""
"""316. 去除重复字母
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
 

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        stack = []
        visited = set()
        count = Counter(s)
        for c in s:
            if c not in visited:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                    visited.discard(stack.pop())
                stack.append(c)
                visited.add(c)
            count[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('cbacdcbc'))
