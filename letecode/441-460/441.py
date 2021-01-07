#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/3 上午11:17
"""
"""441. 排列硬币
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3."""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        count = 0
        while count <= n:
            k += 1
            count += k
        return k - 1

    def arrangeCoins2(self, n: int) -> int:
        res = (2 * n + 0.25) ** 0.5 - 0.5
        return int(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrangeCoins(5))
    print(sol.arrangeCoins2(5))
