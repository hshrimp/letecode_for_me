#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/18 下午3:18
"""
"""592. 分数加减运算
给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。 这个结果应该是不可约分的分数，即最简分数。 
如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。

示例 1:

输入:"-1/2+1/2"
输出: "0/1"
 示例 2:

输入:"-1/2+1/2+1/3"
输出: "1/3"
示例 3:

输入:"1/3-1/2"
输出: "-1/6"
示例 4:

输入:"5/3+1/3"
输出: "2/1"
说明:

输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。"""


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def add(a1, a2, b1, b2):
            print(a1, a2, b1, b2)
            if a2 == 0:
                return b1, b2
            kid = a1 * b2 + b1 * a2
            mom = a2 * b2
            for i in range(2, abs(kid) + 1):
                while kid % i == 0 and mom % i == 0:
                    kid = kid // i
                    mom = mom // i
            return kid, mom

        res_kid, res_mom = 0, 0
        left = 0
        for i in range(1, len(expression)):
            if expression[i] in {'-', '+'}:
                if res_mom == 0:
                    res_kid, res_mom = [int(v) for v in expression[:i].split('/')]
                else:
                    res_kid, res_mom = add(res_kid, res_mom, *[int(v) for v in expression[left:i].split('/')])
                left = i

        res_kid, res_mom = add(res_kid, res_mom, *[int(v) for v in expression[left:].split('/')])
        if res_kid == 0:
            res_mom = 1
        return str(res_kid) + '/' + str(res_mom)


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionAddition("-1/4-4/5-1/4"))
