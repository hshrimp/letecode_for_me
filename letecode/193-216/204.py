#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/16 下午4:30
"""
"""204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。"""


class Solution:
    def countPrimes(self, n: int) -> int:
        val = [1] * n
        val[0] = val[1] = 0
        for i in range(1, int(n ** 0.5) + 1):
            if val[i]:
                val[i * i::i] = [0] * len(val[i * i::i])
        return sum(val)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(5))
