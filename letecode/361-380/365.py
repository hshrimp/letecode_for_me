#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/22 下午3:12
"""
"""365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        visited = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in visited:
                continue
            visited.add((remain_x, remain_y))
            # 把x灌满
            stack.append((x, remain_y))
            # 把y灌满
            stack.append((remain_x, y))
            # 把x倒光
            stack.append((0, remain_y))
            # 把y倒光
            stack.append((remain_x, 0))
            # 把x中的倒进y，倒满y或者倒光x
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把y中的倒进x，倒满x或者倒光y
            stack.append((remain_x + min(x - remain_x, remain_y), remain_y - min(x - remain_x, remain_y)))
        return False

    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        import math
        return z % math.gcd(x, y) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.canMeasureWater(3, 5, 4))
    print(sol.canMeasureWater2(3, 5, 4))
