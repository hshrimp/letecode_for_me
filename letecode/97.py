#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-08 10:27
"""
"""给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        res = set()

        def find(s1, s2, s3):
            print(s1, s2, s3, res)
            if 1 in res:
                return
            if not s1:
                if s2 == s3:
                    res.add(1)
                    return
                else:
                    res.add(0)
                    return
            if not s2:
                if s1 == s3:
                    res.add(1)
                    return
                else:
                    res.add(0)
                    return
            if s3:
                if s1[0] == s3[0]:
                    find(s1[1:], s2, s3[1:])
                if s2[0] == s3[0]:
                    find(s1, s2[1:], s3[1:])
                if s1[0] != s3[0] and s2[0] != s3[0]:
                    res.add(0)
                    return
            else:
                res.add(0)
                return

        find(s1, s2, s3)
        return sum(res) > 0

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l1 + 1) for _ in range(l2 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            dp[0][i] = dp[0][i - 1] and s1[i - 1] == s3[i - 1]
        for j in range(1, l2 + 1):
            dp[j][0] = dp[j - 1][0] and s2[j - 1] == s3[j - 1]
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(sol.isInterleave2(s1, s2, s3))
