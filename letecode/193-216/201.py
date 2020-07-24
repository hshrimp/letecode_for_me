#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/15 下午6:03
"""
"""201. 数字范围按位与
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        length = len(bin(n)) - 2
        tl = len(bin(m)) - 2
        res = ['0'] * (length - tl) + ['1'] * tl
        for num in range(m, n + 1):
            num = bin(num)[2:]
            for i in range(len(num)):
                if num[i] == '0' and res[length - len(num) + i] == '1':
                    res[length - len(num) + i] = '0'
                    tl -= 1
                    if tl == 0:
                        return 0
        return int('0b' + ''.join(res), 2)

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        for num in range(m, n):
            n &= num
            if n == 0:
                return 0
        return n

    def rangeBitwiseAnd3(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        from math import log2, floor
        nn = floor(log2(n))
        val_max = 2 ** nn
        if val_max > m:
            return 0
        elif val_max == m:
            return val_max
        else:
            for num in range(m, n):
                n &= num
                if int(bin(n)[3:], 2) == 0:
                    return n
            return n

    def rangeBitwiseAnd4(self, m: int, n: int) -> int:
        flag = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            flag += 1
        return m << flag

    def rangeBitwiseAnd5(self, m: int, n: int) -> int:
        """Brian Kernighan 算法"""
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return n


if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(0, 7))
    print(sol.rangeBitwiseAnd2(3, 7))
    print(sol.rangeBitwiseAnd3(9, 15))
    print(sol.rangeBitwiseAnd4(9, 15))

