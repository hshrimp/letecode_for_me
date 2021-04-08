#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 上午10:39
"""
"""506. 相对名次
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，
“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
提示:

N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。"""


class Solution:
    def findRelativeRanks(self, score):
        d = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        rank = sorted(score, reverse=True)
        for i in range(len(score)):
            index = rank.index(score[i]) + 1
            score[i] = d.get(index, str(index))
        return score

    def findRelativeRanks2(self, score):
        d = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        d2 = {}
        rank = sorted(score, reverse=True)
        for i, s in enumerate(rank, 1):
            d2[s] = i
        for i in range(len(score)):
            index = d2[score[i]]
            score[i] = d.get(index, str(index))
        return score


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRelativeRanks([5, 4, 3, 9, 1]))
    print(sol.findRelativeRanks2([5, 4, 3, 9, 1]))
