#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/15 下午5:48
"""
"""374. 猜数字大小
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
 
示例 1：

输入：n = 10, pick = 6
输出：6
示例 2：

输入：n = 1, pick = 1
输出：1
示例 3：

输入：n = 2, pick = 1
输出：1
示例 4：

输入：n = 2, pick = 2
输出：2
 
提示：

1 <= n <= 231 - 1
1 <= pick <= n
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

import random


class Solution:
    def __init__(self, n):
        self.pick = random.randint(0, n)

    def guess(self, num: int) -> int:
        if num == self.pick:
            return 0
        if num > self.pick:
            return 1
        if num < self.pick:
            return -1

    def guessNumber(self, n: int) -> int:
        def g(left, right):
            if right - left == 1:
                return left + 1
            mid = left + (right - left) // 2
            num = self.guess(mid)
            if num == 0:
                return mid
            if num == -1:
                return g(left, mid)
            if num == 1:
                return g(mid, right)

        return g(-1, n + 1)
