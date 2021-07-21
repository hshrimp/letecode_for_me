#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/7 下午2:31
"""
"""322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 
说明:
你可以认为每种硬币的数量是无限的。"""


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def track(num, last):
            if last == 0:
                res[0] = min(res[0], num)
                return
            if num >= res[0]:
                return
            for c in coins:
                if last >= c:
                    track(num + 1, last - c)

        coins.sort(reverse=True)
        res = [amount + 1]
        track(0, amount)
        if res[0] < amount + 1:
            return res[0]
        else:
            return -1

    def coinChange2(self, coins, amount: int) -> int:
        if not amount:
            return 0
        coins.sort()
        dp = [-1] * (amount + 1)
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(coins[0], amount + 1):
            if dp[i] == -1:
                temp = [dp[i - j] for j in coins if i - j > 0 and dp[i - j] != -1]
                if temp:
                    dp[i] = min(temp) + 1
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.coinChange([186, 419, 83, 408], 6249))
    print(sol.coinChange(coins=[5], amount=11))
    print(sol.coinChange2([186, 419, 83, 408], 6249))
