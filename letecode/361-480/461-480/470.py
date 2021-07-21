#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/13 下午6:27
"""
"""470. 用 Rand7() 实现 Rand10()
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]
 
提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。
 
进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?"""


# The rand7() API is already defined for you.
def rand7():
    # @return a random integer in the range 1 to 7
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        first = rand7() + (rand7() - 1) * 7
        while first > 40:
            first = rand7() + (rand7() - 1) * 7
        return first % 10 + 1
