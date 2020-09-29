#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/27 下午4:23
"""
"""375. 猜数字大小 II
我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。

"""

from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                dp[i][j] = min(
                    m + 1 + max(dp[i][m - 1] if m - 1 >= i else 0, dp[m + 1][j] if j >= m + 1 else 0) for m in
                    range((j - i) // 2 + i, j + 1))
        return dp[0][-1]

    def getMoneyAmount2(self, n: int) -> int:
        @lru_cache(None)
        def sol(left, right):
            if right - left == 2:
                return left
            if right - left <= 1:
                return 0
            return min(i + max(sol(left, i), sol(i + 1, right)) for i in range(left + (right - 1 - left) // 2, right))

        return sol(1, n + 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMoneyAmount(100))
    print(sol.getMoneyAmount2(100))
