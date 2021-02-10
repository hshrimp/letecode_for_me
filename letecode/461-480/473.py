#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/5 上午10:34
"""
"""473. 火柴拼正方形
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。
不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
注意:

给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。"""

from collections import defaultdict


class Solution:
    def makesquare(self, nums) -> bool:
        def find(side_l, begin):
            print(side_l, begin)
            for i, l in enumerate(que[begin:], begin):
                if l > side_l:
                    continue
                if l == side_l:
                    if num2count[l] > 0:
                        num2count[l] -= 1
                        return True
                if l < side_l:
                    if num2count[l] > 0:
                        num2count[l] -= 1
                        if find(side_l - l, i):
                            return True
                        else:
                            num2count[l] += 1
            return False

        count = sum(nums)
        length = count / 4
        if count % 4 != 0 or max(nums) > length:
            return False
        num2count = defaultdict(int)
        for num in nums:
            num2count[num] += 1
        que = sorted(nums, reverse=True)
        side = 4
        while side:
            if find(length, 0):
                side -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
