#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-19 10:08
"""
"""给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from functools import lru_cache


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        count = 0
        for i, c in enumerate(num1[::-1]):
            for j, v in enumerate(num2[::-1]):
                count += int(c) * int(v) * (10 ** (i + j))
        return str(count)

    def multiply2(self, num1: str, num2: str) -> str:
        return str(eval(num1 + '*' + num2))

    def multiply3(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        # 将num反转，每一位转成int,例 "2347"--》[7,4,3,2]
        n1 = list(map(int, num1[::-1]))
        n2 = list(map(int, num2[::-1]))

        res = [0] * (len(num1) + len(num2))
        for i, val1 in enumerate(n1):
            cur = 0
            for j, val2 in enumerate(n2):
                # temp = 当前的两个一位数相乘+上一位的进位+之前在当前位已有的数
                temp = val1 * val2 + cur + res[i + j]
                # 当前位 = temp对10取余
                res[i + j] = temp % 10
                # 进位 = temp除以10取整
                cur = temp // 10
            # 进位
            res[i + j + 1] += cur
        res = res[::-1]
        # 去掉前缀的0
        begin = 0
        for i in range(len(res)):
            if res[i]:
                begin = i
                break
        return ''.join([str(val) for val in res[begin:]])


if __name__ == '__main__':
    num1 = "1234567890987654321"
    num2 = "4561234567890987654321234567878990"
    sol = Solution()
    print(sol.multiply(num1, num2))
    print(sol.multiply2(num1, num2))
    print(sol.multiply3('0', '0'))
