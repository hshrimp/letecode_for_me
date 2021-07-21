#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/24 下午6:00
"""
"""357. 计算各个位数不同的数字个数
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10**n 。

示例:

输入: 2
输出: 91 
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        res = 10
        mul = 9
        for i in range(1, min(n, 10)):
            mul *= 10 - i
            res += mul
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(3))
