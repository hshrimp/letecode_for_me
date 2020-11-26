#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/26 上午11:21
"""
"""405. 数字转换为十六进制数
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"
"""


class Solution:
    def toHex(self, num: int) -> str:
        res = ''
        if num < 0:
            num = (abs(num) ^ (2 ** 32 - 1)) + 1
        elif num == 0:
            return '0'
        while (num >> 4) > 0 or num > 0:
            a = str(num % 16)
            if a == '10':
                a = 'a'
            elif a == '11':
                a = 'b'
            elif a == '12':
                a = 'c'
            elif a == '13':
                a = 'd'
            elif a == '14':
                a = 'e'
            elif a == '15':
                a = 'f'
            res += a
            num = num >> 4
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.toHex(-26))