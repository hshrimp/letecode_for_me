#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/6 下午5:43
"""
"""279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9."""


class Solution:
    def numSquares(self, n: int) -> int:
        def get(li, p):
            if li >= res[0]:
                return
            if p == 0:
                res[0] = li
            for i in range(int(p ** 0.5), 0, -1):
                num = p // (i ** 2)
                get(li + num, p - (i ** 2) * num)

        res = [n]
        get(0, n)
        return res[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(6666))
