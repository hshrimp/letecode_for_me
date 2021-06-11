#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-10 20:39
"""
"""172. 阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            res += n // 5
            n = n//5
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.trailingZeroes(50))
