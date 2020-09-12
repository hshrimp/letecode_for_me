#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/1 下午5:59
"""
"""309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]"""


class Solution:
    def maxProfit(self, prices) -> int:
        """
        dp[i]表示第i 天结束之后的最大收益
        dp[i][0]表示持有状态的最大收益
        dp[i][1]表示冻结期状态的最大收益
        dp[i][2]表示非冻结期且不持有的最大收益
        :param prices:
        :return:
        """
        if not prices:
            return 0
        length = len(prices)
        dp = [[0] * 3 for _ in range(length)]
        dp[0][0] = -prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1][1:])

    def maxProfit2(self, prices) -> int:
        """
        dp表示第i 天结束之后的最大收益
        dp[0]表示持有状态的最大收益
        dp[1]表示冻结期状态的最大收益
        dp[2]表示非冻结期且不持有的最大收益
        :param prices:
        :return:
        """
        if not prices:
            return 0
        length = len(prices)
        dp = [0] * 3
        dp[0] = -prices[0]
        for i in range(1, length):
            dp[0], dp[1], dp[2] = max(dp[0], dp[2] - prices[i]), dp[0] + prices[i], max(dp[1], dp[2])
        return max(dp[1:])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1, 2, 0, 2]))
    print(sol.maxProfit2([1, 2, 0, 2]))

