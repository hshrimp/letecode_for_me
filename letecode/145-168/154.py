#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/4 上午8:59
"""
"""154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？"""


class Solution:
    def findMin(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        else:
            return nums[0]
