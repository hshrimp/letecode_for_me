#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/3 下午6:12
"""
"""371. 两整数之和
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        from math import log2
        num = 2 ** a * 2 ** b
        return int(log2(num))

    def getSum2(self, a: int, b: int) -> int:
        return sum([a, b])


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(-3, 2))
