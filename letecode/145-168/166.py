#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/7 上午11:19
"""
"""166. 分数到小数
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = numerator * denominator
        if flag == 0:
            return '0'
        elif flag < 0:
            flag = '-'
        else:
            flag = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        n, pre = divmod(numerator, denominator)
        if pre == 0:
            return flag + str(n)
        res = str(n) + '.'
        length = len(res)
        yushu = {}
        while True:
            print(res, yushu)
            temp, pre = divmod(pre * 10, denominator)
            if pre == 0:
                return flag + res + str(temp)
            if pre in yushu and res[yushu[pre]] == str(temp):
                index = yushu[pre]
                return flag + res[:index] + '(' + res[index:] + ')'
            else:
                res += str(temp)
                yushu[pre] = len(res) - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(numerator=1, denominator=214748364))
