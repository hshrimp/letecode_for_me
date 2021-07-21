#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/20 下午4:04
"""
"""640. 求解方程
求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。

如果方程没有解，请返回“No solution”。

如果方程有无限解，则返回“Infinite solutions”。

如果方程中只有一个解，要保证返回值 x 是一个整数。

示例 1：

输入: "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: "x=x"
输出: "Infinite solutions"
示例 3:

输入: "2x=x"
输出: "x=0"
示例 4:

输入: "2x+3x-6x=x+2"
输出: "x=-1"
示例 5:

输入: "x=x+2"
输出: "No solution"
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        def check(equ):
            x_num = 0
            other = 0

            def deal(s):
                x_num = 0
                other = 0
                flag = 1
                if s[0] == '-':
                    flag = 0
                    s = s[1:]
                s = s.split('-')
                if 'x' in s[0]:
                    if len(s[0]) > 1:
                        if flag:
                            x_num += float(s[0][:-1])
                        else:
                            x_num -= float(s[0][:-1])
                    else:
                        if flag:
                            x_num += 1
                        else:
                            x_num -= 1
                else:
                    if flag:
                        other += float(s[0])
                    else:
                        other -= float(s[0])
                for val in s[1:]:
                    if 'x' in val:
                        if len(val) > 1:
                            x_num -= float(val[:-1])
                        else:
                            x_num -= 1
                    else:
                        other -= float(val)
                return x_num, other

            equ = equ.split('+')
            for e in equ:
                x, o = deal(e)
                x_num += x
                other += o
            return x_num, other

        equ1, equ2 = equation.split('=')
        x_num, other = check(equ1)
        x, o = check(equ2)
        x_num -= x
        other -= o
        if x_num == 0:
            if other == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return 'x=' + str(int(-other // x_num))


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveEquation("-x=2x+6"))
