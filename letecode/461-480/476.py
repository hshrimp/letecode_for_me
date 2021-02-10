# !/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/14 上午11:17
"""
"""476. 数字的补数
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

示例 1:

输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2:

输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
 
注意:

给定的整数保证在 32 位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同"""


class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** (len(bin(num)) - 2) - num - 1

    def findComplement2(self, num: int) -> int:
        res = ''
        num = bin(num)[2:]
        for n in num:
            if n == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(5))
    print(sol.findComplement2(5))
