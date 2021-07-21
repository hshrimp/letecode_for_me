#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/10 下午4:38
"""
"""282. 给表达式添加运算符
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []"""


class Solution:
    def addOperators(self, num: str, target: int):
        def check(n, tar, li):
            if not n:
                if tar == 0:
                    res.add(li[:-1])
                return
            if n[0] == '0':
                for p in op:
                    cur = li + n[:1]
                    check(n[1:], target - eval(cur), cur + p)
            else:
                for i in range(len(n)):
                    for p in op:
                        cur = li + n[:i + 1]
                        check(n[i + 1:], target - eval(cur), cur + p)

        op = {'+', '-', '*'}
        res = set()
        check(num, target, '')
        return list(res)

    def addOperators2(self, num: str, target: int):
        def check(n, li):
            if not n:
                if target == eval(li[:-1]):
                    res.add(li[:-1])
                return
            if n[0] == '0':
                cur = li + n[:1]
                for p in op:
                    check(n[1:], cur + p)
            else:
                for i in range(len(n)):
                    cur = li + n[:i + 1]
                    for p in op:
                        check(n[i + 1:], cur + p)

        if not num:
            return []
        op = {'+', '-', '*'}
        res = set()
        check(num, '')
        return list(res)

    def addOperators3(self, num: str, target: int):
        def check(n, li, pre, ans):
            if not n and target == ans:
                res.add(li)
            else:
                for i in range(1, len(n) + 1):
                    if i > 1 and n[0] == '0':
                        break
                    cur = int(n[:i])
                    if not li:
                        check(n[i:], n[:i], cur, cur)
                    else:
                        check(n[i:], li + '+' + n[:i], cur, ans + cur)
                        check(n[i:], li + '-' + n[:i], -cur, ans - cur)
                        check(n[i:], li + '*' + n[:i], cur * pre, ans - pre + pre * cur)

        if not num:
            return []
        res = set()
        check(num, '', 0, 0)
        return list(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addOperators3(num="232", target=8))
