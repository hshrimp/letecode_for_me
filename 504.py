#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 上午10:26
"""
"""504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = 0
        if num < 0:
            num = -num
            flag = 1
        res = ''
        while num:
            num, r = divmod(num, 7)
            res += str(r)
        if flag:
            return '-' + res[::-1]
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToBase7(-100))
