#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/31 上午11:04
"""
"""224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。"""


class Solution:
    def calculate(self, s: str) -> int:
        def count(temp_s):
            res = int(temp_s[0])
            for i in range(1, len(temp_s), 2):
                if temp_s[i] == '+':
                    res += int(temp_s[i + 1])
                else:
                    res -= int(temp_s[i + 1])
            return str(res)

        stack = []
        last_is_num = False
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] != ')':
                if last_is_num and s[i].isdigit():
                    stack[-1] += s[i]
                else:
                    if not s[i].isdigit():
                        last_is_num = False
                    else:
                        last_is_num = True
                    stack.append(s[i])
            if s[i] == ')':
                temp = []
                while stack:
                    cur = stack.pop()
                    if cur != '(':
                        temp = [cur] + temp
                    else:
                        break
                stack.append(count(temp))
        return int(count(stack))


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("(1+(4+5+2)-3)+(6 +8)"))
