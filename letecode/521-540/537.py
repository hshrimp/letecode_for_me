#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/8 下午4:48
"""
"""537. 复数乘法
给定两个表示复数的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:

输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
示例 2:

输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
注意:

输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        _a, ai = a.split('+')
        _b, bi = b.split('+')
        first = str(int(_a) * int(_b) - int(ai[:-1]) * int(bi[:-1]))
        second = str(int(_a) * int(bi[:-1]) + int(_b) * int(ai[:-1]))
        return first + "+" + second + 'i'


if __name__ == '__main__':
    sol = Solution()
    print(sol.complexNumberMultiply("1+-1i", "1+-1i"))
