#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/30 下午4:00
"""
"""502. IPO
假设 力扣（LeetCode）即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，
力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。
帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。

给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。
最初，你有 W 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。

示例：

输入：k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
 
提示：

假设所有输入数字都是非负整数。
表示利润和资本的数组的长度不超过 50000。
答案保证在 32 位有符号整数范围内。
"""


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits, Capital) -> int:
        from collections import defaultdict
        import bisect
        visited = set()
        d = defaultdict(list)
        for i, cap in enumerate(Capital):
            bisect.insort(d[cap], (Profits[i], i))
        d_cap = sorted(d.keys())
        while k > 0:
            index = bisect.bisect_right(d_cap, W)
            cur = 0
            point = -1
            for key in d_cap[:index]:
                li = d[key]
                for pro, i in li[::-1]:
                    if i not in visited:
                        if pro > cur:
                            cur = pro
                            point = i
                        break
            if point != -1:
                W += cur
                visited.add(point)
            k -= 1
        return W

    def findMaximizedCapital2(self, k: int, W: int, Profits, Capital) -> int:
        def bi(li):
            left = 0
            right = len(li)
            while left < right:
                mid = (left + right) // 2
                if li[mid][2] > W:
                    right = mid
                else:
                    left = mid + 1
            return left

        visited = set()
        data = []
        for i in range(len(Profits)):
            data.append((i, Profits[i], Capital[i]))
        cap_sort = sorted(data, key=lambda x: x[2])
        while k > 0:
            index = bi(cap_sort)
            # print(cap_sort, W, index)
            cur = cap_sort[:index]
            pro_sort = sorted(cur, key=lambda x: x[1], reverse=True)
            for i, pro, cap in pro_sort:
                if i not in visited:
                    W += pro
                    visited.add(i)
                    break
            k -= 1
        return W

    def findMaximizedCapital3(self, k: int, W: int, Profits, Capital) -> int:
        from heapq import nlargest

        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))
        length = len(Capital)
        for i in range(min(length, k)):
            index = -1
            for j in range(length):
                if W >= Capital[j]:
                    if index == -1:
                        index = j
                    elif Profits[j] > Profits[index]:
                        index = j
            if index == -1:
                break
            W += Profits[index]
            Capital[index] = float('inf')
        return W


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
    print(sol.findMaximizedCapital2(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
    print(sol.findMaximizedCapital3(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
