#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/31 下午3:21
"""
"""227. 基本计算器 II
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。"""


class Solution:
    def calculate(self, s: str) -> int:
        is_num = False
        length = len(s)
        stack = []
        for i in range(length):
            if s[i] == ' ':
                continue
            if is_num and s[i].isdigit():
                stack[-1] = stack[-1] * 10 + int(s[i])
            else:
                if s[i].isdigit():
                    is_num = True
                    stack.append(int(s[i]))
                else:
                    is_num = False
                    stack.append(s[i])
        stack2 = []
        j = 0
        while j < len(stack):
            if stack[j] == '*':
                stack2[-1] = stack2[-1] * stack[j + 1]
                j += 2
            elif stack[j] == '/':
                stack2[-1] = stack2[-1] // stack[j + 1]
                j += 2
            else:
                stack2.append(stack[j])
                j += 1

        count = stack2[0]
        for i in range(1, len(stack2), 2):
            if stack2[i] == '+':
                count += stack2[i + 1]
            else:
                count -= stack2[i + 1]
        return count

    def calculate2(self, s: str) -> int:
        flag, stack, num = '+', [], 0
        length = len(s)
        for i in range(length):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == length - 1:
                if flag == '+':
                    stack.append(num)
                if flag == '-':
                    stack.append(-num)
                if flag == '*':
                    stack[-1] *= num
                if flag == '/':
                    stack[-1] = int(stack[-1] / num)
                num = 0
                flag = s[i]
        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("1*2-3/4+5*6-7*8+9/10"))
    print(sol.calculate2("1*2-3/4+5*6-7*8+9/10"))
