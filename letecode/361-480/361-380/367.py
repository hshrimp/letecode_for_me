#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/3 下午5:58
"""
"""367. 有效的完全平方数
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (int(num ** 0.5)) ** 2 == num


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPerfectSquare(14))
