#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/18 下午3:10
"""
"""301. 删除无效的括号
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]"""


class Solution:
    def removeInvalidParentheses(self, s: str):
        def valid(s):
            flag = 0
            for i in range(len(s)):
                if s[i] == '(':
                    flag += 1
                if s[i] == ')':
                    flag -= 1
                if flag < 0:
                    return False
            return flag == 0

        res = {s}
        while True:
            temp = list(filter(valid, res))
            print(res, temp)
            if temp:
                return temp
            temp_res = set()
            for r in res:
                for i in range(len(r)):
                    if r[i] in '()':
                        temp_res.add(r[:i] + r[i + 1:])
            res = temp_res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeInvalidParentheses(")("))
