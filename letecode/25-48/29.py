#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-04 09:43
"""
"""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        p = False
        if dividend < 0:
            p = not p
            dividend = -dividend
        if divisor < 0:
            p = not p
            divisor = -divisor
        count = 0
        while divisor <= dividend:
            temp = divisor
            c = 0
            while temp <= dividend:
                t = temp
                if temp == divisor:
                    c = 1
                else:
                    c += c
                temp += temp
            count += c
            dividend -= t
        if p:
            if -count<-2**31:
                return 2**31
            else:
                return -count
        else:
            if count>2**31-1:
                return 2**31-1
            else:
                return count
