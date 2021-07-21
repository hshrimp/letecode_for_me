#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/4 下午5:08
"""
"""503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。"""


class Solution:
    def nextGreaterElements(self, nums):
        res = []
        length = len(nums)
        for i in range(length):
            cur = (i + 1) % length
            while i != cur:
                if nums[cur] > nums[i]:
                    res.append(nums[cur])
                    break
                cur = (cur + 1) % length
            else:
                res.append(-1)
        return res

    def nextGreaterElements2(self, nums):
        stack = []
        length = len(nums)
        res = [-1] * length
        for i in range(2 * length - 1):
            while stack and nums[stack[-1]] < nums[i % length]:
                res[stack.pop()] = nums[i % length]
            stack.append(i % length)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))
    print(sol.nextGreaterElements2([1, 2, 1]))
