#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/26 下午4:28
"""
"""628. 三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
 

提示：

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""


class Solution:
    def maximumProduct(self, nums) -> int:
        origin = sorted(nums)
        if origin[-1] <= 0 or origin[0] >= 0:
            return origin[-1] * origin[-2] * origin[-3]
        return max(origin[0] * origin[1] * origin[-1], origin[-1] * origin[-2] * origin[-3])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3, 4, -1, -5, -4]))
