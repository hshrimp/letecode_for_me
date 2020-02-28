#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/25 16:26
"""
"""面试题10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
提示：

0 <= n <= 100
注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/"""


class Solution:
    def numWays(self, n: int) -> int:
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numWays(7))
