#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 下午3:38
"""
"""258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？"""


class Solution:
    def addDigits(self, num: int) -> int:
        count = 0
        while True:
            while num > 0:
                num, last = divmod(num, 10)
                count += last
            if count < 10:
                return count
            num = count
            count = 0

    def addDigits2(self, num: int) -> int:
        s = str(num)
        res = int(s[0])
        for i in s[1:]:
            temp = res + int(i)
            if temp >= 10:
                p, q = divmod(temp, 10)
                res = p + q
            else:
                res = temp
        return res

    def addDigits3(self, num: int) -> int:
        """数根"""
        return (num - 1) % 9 + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(318))
    print(sol.addDigits2(318))
    print(sol.addDigits3(318))
