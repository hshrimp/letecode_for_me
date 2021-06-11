#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/1 下午4:15
"""
"""228. 汇总区间
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。"""


class Solution:
    def summaryRanges(self, nums):
        res = []
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
                continue
            if stack:
                if nums[i] == stack[-1] + 1:
                    stack.append(nums[i])
                else:
                    if len(stack) == 1:
                        res.append(str(stack[0]))
                    else:
                        res.append(str(stack[0]) + '->' + str(stack[-1]))
                    stack = [nums[i]]
        if stack:
            if len(stack) == 1:
                res.append(str(stack[0]))
            else:
                res.append(str(stack[0]) + '->' + str(stack[-1]))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges([0,2,3,4,6,8,9]))
