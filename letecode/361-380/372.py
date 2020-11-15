#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/28 下午7:56
"""
"""372. 超级次方
你的任务是计算 a**b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

输入: a = 2, b = [3]
输出: 8
示例 2:

输入: a = 2, b = [1,0]
输出: 1024"""


class Solution:
    def superPow(self, a: int, b) -> int:
        base = 1337
        if not b:
            return 1
        cur = b.pop()
        part1 = a ** cur % base
        part2 = self.superPow(a, b) ** 10 % base
        return part1 * part2 % base


if __name__ == '__main__':
    sol = Solution()
    print(sol.superPow(a=2, b=[1, 0, 2]))
