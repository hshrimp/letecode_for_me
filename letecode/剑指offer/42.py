#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-04-10 10:02
"""
"""面试题42. 连续子数组的最大和
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/"""


class Solution:
    def maxSubArray(self, nums) -> int:
        res = -1
        n = nums[0]
        for i in range(len(nums)):
            n = max(n + nums[i], nums[i])
            res = max(n, res)
        return res

    def maxSubArray2(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
