#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-02 10:36
"""
"""188. 买卖股票的最佳时机 IV
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。"""


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        def get_dp(begin):
            # dp[begin] = [0] * length
            m = prices[begin]
            for i in range(begin + 1, length):
                if m > prices[i]:
                    m = prices[i]
                    dp[begin][i] = dp[begin][i - 1]
                else:
                    dp[begin][i] = max(dp[begin][i - 1], prices[i] - m)

        def track(deep, temp_res, begin):
            # print(deep, temp_res, begin)
            if deep <= k:
                if begin >= length - 1:
                    nonlocal res
                    res = max(res, temp_res)
                    return
                for i in range(begin + 1, length):
                    if dp[begin][i] > 0:
                        track(deep + 1, temp_res + dp[begin][i], i)

        length = len(prices)
        res = 0
        dp = [[0] * length for _ in range(length - 1)]
        list(map(get_dp, range(length - 1)))
        track(0, 0, 0)
        return res

    def maxProfit2(self, k: int, prices) -> int:
        length = len(prices)
        if k > length / 2:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(length)]
        for i in range(length):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, length):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]


if __name__ == '__main__':
    sol = Solution()
    k = 2
    p = [3, 3, 5, 0, 0, 3, 1, 4]
    print(sol.maxProfit(k, p))
    print(sol.maxProfit2(k, p))
