#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-04 10:51
"""
"""238. 除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）"""


class Solution:
    def productExceptSelf(self, nums):
        count = 1
        for i in nums:
            count *= i
        res = []
        for i in range(len(nums)):
            res.append(count // nums[i])
        return res

    def productExceptSelf2(self, nums):
        length = len(nums)
        left, right = [1] * (length + 1), [1] * (length + 1)
        left[1] = nums[0]
        right[1] = nums[-1]
        for i in range(2, length + 1):
            left[i] = left[i - 1] * nums[i - 1]
            j = length - i
            right[i] = right[i - 1] * nums[j]
        res = []
        for i in range(length):
            res.append(left[i] * right[length - i - 1])
        return res

    def productExceptSelf3(self, nums):
        length = len(nums)
        ans = [1] * length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]
        r = 1
        for i in range(length - 1, -1, -1):
            ans[i] = ans[i] * r
            r *= nums[i]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf2([1, 2, 3, 4]))
    print(sol.productExceptSelf3([1, 2, 3, 4]))
