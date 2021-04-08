#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/31 下午4:42
"""
"""525. 连续数组
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

注意: 给定的二进制数组的长度不会超过50000。"""


class Solution:
    def findMaxLength(self, nums) -> int:
        count = 0
        d = {0: -1}
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                count -= 1
            if n == 1:
                count += 1
            if count not in d:
                d[count] = i
            else:
                res = max(res, i - d[count])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxLength([0, 0, 1, 1, 1, 0, 0, 1, 1]))
