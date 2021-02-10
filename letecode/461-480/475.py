#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/25 下午8:20
"""
"""475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3
 
提示：

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
"""


class Solution:
    def findRadius(self, houses, heaters) -> int:
        heaters.sort()
        houses_set = set(houses)
        res = 0
        if min(houses) < heaters[0]:
            res = heaters[0] - houses[0]
        if max(houses) > heaters[-1]:
            res = max(res, houses[-1] - heaters[-1])
        for i, h in enumerate(heaters[1:], 1):
            before = heaters[i - 1]
            cur = 0
            for num in range(before + 1, h):
                if num in houses_set:
                    this = min(num - before, h - num)
                    cur = max(cur, this)

            res = max(res, cur)
        return res

    def findRadius2(self, houses, heaters) -> int:
        res = 0
        for house in houses:
            cur = float('inf')
            for heater in heaters:
                cur = min(cur, abs(house - heater))
            res = max(res, cur)
        return res

    def findRadius3(self, houses, heaters) -> int:
        import bisect
        heaters.sort()
        res = 0
        length = len(heaters)
        for house in houses:
            index = bisect.bisect(heaters, house)
            if index == 0:
                res = max(res, heaters[0] - house)
            elif index == length:
                res = max(res, house - heaters[-1])
            else:
                res = max(res, min(heaters[index] - house, house - heaters[index - 1]))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius(houses=[1, 5], heaters=[2]))
    print(sol.findRadius2(houses=[1, 5], heaters=[2]))
    print(sol.findRadius3(houses=[1, 5], heaters=[2]))
