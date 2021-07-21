#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/25 下午4:39
"""
"""600. 不含连续1的非负整数
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释: 
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 109"""


class Solution:
    def findIntegers(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            if '11' not in bin(i):
                count += 1
        return count

    def findIntegers2(self, n: int) -> int:
        string = bin(n)[2:]
        length = len(string)
        dp = [[0] * (length + 1) for _ in range(2)]
        dp[0][1] = 1
        dp[1][1] = 1
        for k in range(2, length + 1):
            dp[0][k] = dp[0][k - 1] + dp[1][k - 1]
            dp[1][k] = dp[0][k - 1]
        dp2 = [dp[0][i] + dp[1][i] for i in range(length + 1)]
        dp2[0] = 1
        res = 0
        for k in range(length):
            if string[k] == '1' and '11' not in string[:k]:
                res += dp2[length - k - 1]
        if '11' not in string:
            res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findIntegers2(4))
