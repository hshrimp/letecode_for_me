#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/28 14:12
"""
"""面试题14- II. 剪绳子 II
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 
提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        p, q = divmod(n, 3)
        if q == 0:
            res = 3 ** p
        elif q == 1:
            res = 3 ** (p - 1) * 4
        elif q == 2:
            res = 3 ** p * 2
        return res % 1000000007


if __name__ == '__main__':
    sol = Solution()
    print(sol.cuttingRope(10))
