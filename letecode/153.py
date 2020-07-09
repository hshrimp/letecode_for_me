#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/4 上午8:53
"""
"""153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0"""


class Solution:
    def findMin(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        else:
            return nums[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))
