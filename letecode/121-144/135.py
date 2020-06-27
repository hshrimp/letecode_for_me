#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-01 16:52
"""
"""135. 分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""


class Solution:
    def candy(self, ratings) -> int:
        length = len(ratings)
        dp = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        for j in range(length - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                dp[j] = max(dp[j+1] + 1, dp[j])
        return sum(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1, 2, 2]))

if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([29, 51, 87, 87, 72, 12]))
