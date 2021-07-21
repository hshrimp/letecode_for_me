#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-03 11:44
"""
"""516. 最长回文子序列
给定一个字符串s，找到其中最长的回文子序列，并返回该序列的长度。可以假设s的最大长度为1000。

示例 1:
输入:
"bbbab"
输出:
4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:
"cbbd"
输出:
2
一个可能的最长回文子序列为 "bb"。"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbb"))
