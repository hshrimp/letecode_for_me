#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-10 21:21
"""
"""233. 数字 1 的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6 
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        s = [str(i) for i in range(n + 1)]
        s = ''.join(s)
        return s.count('1')

    def countDigitOne2(self, n: int) -> int:
        if n < 1:
            return 0
        res = 0
        base = 1
        while n // base:
            cur = n // base % 10
            high = n // base // 10
            low = n % base
            if cur > 1:
                res += (high + 1) * base
            if cur == 1:
                res += low + 1 + high * base
            if cur < 1:
                res += high * base
            base *= 10
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(-113))
    print(sol.countDigitOne2(-13))
