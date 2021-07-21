#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/22 下午4:45
"""
"""552. 学生出勤记录 II
给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。

学生出勤记录是只包含以下三个字符的字符串：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

示例 1:

输入: n = 2
输出: 8 
解释：
有8个长度为2的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数超过一次。
注意：n 的值不会超过100000。

"""


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [0, 0, 1, 0, 1, 1]
        for i in range(1, n):
            dp = [dp[1], dp[2], sum(dp), dp[4], dp[5], sum(dp[3:])]
        # print(dp)
        return sum(dp) % (10 ** 9 + 7)

    def checkRecord2(self, n: int) -> int:
        mod_num = 10 ** 9 + 7
        a, b, c, d, e, f = 0, 0, 1, 0, 1, 1
        for i in range(1, n):
            a, b, c, d, e, f = b, c, (a + b + c + d + e + f) % mod_num, e, f, (d + e + f) % mod_num
        return (a + b + c + d + e + f) % mod_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkRecord(100000))
    print(sol.checkRecord2(100000))
