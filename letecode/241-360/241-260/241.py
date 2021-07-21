#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 上午10:24
"""
"""241. 为运算表达式设计优先级
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10"""


class Solution:
    def diffWaysToCompute(self, input: str):
        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        if input[i] == '+':
                            res.append(l + r)
                        if input[i] == '-':
                            res.append(l - r)
                        if input[i] == '*':
                            res.append(l * r)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.diffWaysToCompute("2*3-4*5"))
