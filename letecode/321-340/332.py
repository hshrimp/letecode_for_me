#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/10 上午11:24
"""
"""332. 重新安排行程
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

提示：

如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次。
 
示例 1：

输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2：

输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。"""

import bisect
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        def dfs(li, last, citys):
            if last == 0:
                res[:] = li
                return True
            if li[-1] not in citys:
                return
            for city in citys[li[-1]]:
                print(li, city, last)
                temp = {k: list(v) for k, v in citys.items()}
                temp[li[-1]].remove(city)
                if dfs(li + [city], last - 1, temp):
                    return True

        city2city = defaultdict(list)
        for first, second in tickets:
            bisect.insort(city2city[first], second)
        res = []
        count = len(tickets)
        dfs(['JFK'], count, city2city)
        return res

    def findItinerary2(self, tickets):
        def dfs(first):
            while city2city[first]:
                dfs(city2city[first].pop(0))
            res.insert(0, first)

        city2city = defaultdict(list)
        for first, second in tickets:
            bisect.insort(city2city[first], second)
        res = []
        dfs('JFK')
        return res


if __name__ == '__main__':
    sol = Solution()
    ti = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(sol.findItinerary(ti))
    print(sol.findItinerary2(ti))
