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
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(59))
