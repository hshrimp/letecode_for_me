#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/8 下午5:31
"""
"""583. 两个字符串的删除操作
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 
提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        dp = [[0] * (length1 + 1) for _ in range(length2 + 1)]
        for i in range(length1 + 1):
            dp[0][i] = i
        for j in range(length2 + 1):
            dp[j][0] = j
        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance("eaa", "eata"))
