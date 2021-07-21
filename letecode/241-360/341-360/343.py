#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/17 下午7:48
"""
"""343. 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        num, last = divmod(n, 3)
        if last == 0:
            return 3 ** num
        if last == 1:
            return 3 ** (num - 1) * 4
        if last == 2:
            return 3 ** num * 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerBreak(11))
