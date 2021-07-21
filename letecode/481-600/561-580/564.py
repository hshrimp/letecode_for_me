#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/25 下午5:04
"""
"""564. 寻找最近的回文数
给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。

“最近的”定义为两个整数差的绝对值最小。

示例 1:

输入: "123"
输出: "121"
注意:

n 是由字符串表示的正整数，其长度不超过18。
如果有多个结果，返回最小的那个。
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n) + 1
        if n < '10' or int(n[::-1]) == 1:
            return str(int(n) - 1)
        if n == '11':
            return '9'
        if set(n) == {'9'}:
            return str(int(n) + 2)

        a, b = n[:length // 2], n[length // 2:]
        temp = [str(int(a) - 1), a, str(int(a) + 1)]
        print(a, b, temp)
        temp = [cur + cur[-len(b):][::-1] for cur in temp]
        print(temp)
        return min(temp, key=lambda x: abs(int(n) - int(x) or float('inf')))


if __name__ == '__main__':
    sol = Solution()
    print(sol.nearestPalindromic('88'))
