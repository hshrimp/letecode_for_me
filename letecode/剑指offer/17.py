#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/28 17:22
"""
"""面试题17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 
说明：

用返回一个整数列表来代替打印
n 为正整数"""


class Solution:
    def printNumbers(self, n: int):
        num = int('9' * n)
        return [i for i in range(1, num + 1)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.printNumbers(3))
