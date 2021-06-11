#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-09 10:15
"""
"""132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。"""


class Solution:
    def minCut(self, s: str) -> int:
        lis = [[s[0]]]
        for i in range(1, len(s)):
            for j in lis[:len(lis)]:
                if len(j) > 1 and j[-2] == s[i]:
                    lis.append(j[:-2] + [j[-2] + j[-1] + s[i]])
                if j[-1] == s[i]:
                    lis.append(j[:-1] + [s[i] * 2])
                j.append(s[i])
        return min([len(i) for i in lis]) - 1

    def minCut2(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            print(dp)
            if s[:i + 1] == s[:i + 1][::-1]:
                dp[i] = 0
            else:
                dp[i] = min([dp[j] + 1 for j in range(i) if s[j + 1:i + 1] == s[j + 1:i + 1][::-1]])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut2('aab'))
