#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/8 下午4:29
"""
"""581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：

输入：nums = [1,2,3,4]
输出：0
示例 3：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？"""


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        left, right = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[left] == min(nums[i:]):
                left += 1
            else:
                break
        for j in range(len(nums) - 1, left - 1, -1):
            if nums[right] == max(nums[:right + 1]):
                right -= 1
            else:
                break
        return right - left + 1

    def findUnsortedSubarray2(self, nums) -> int:
        left, right = 0, -1
        s = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != s[i]:
                left = i
                break
        for j in range(len(nums) - 1, left - 1, -1):
            if nums[j] != s[j]:
                right = j
                break
        return right - left + 1

    def findUnsortedSubarray3(selfself, nums):
        length = len(nums)
        max_num = nums[0]
        min_num = nums[length - 1]
        l = 0
        r = -1
        for i in range(length):
            if max_num > nums[i]:
                r = i
            else:
                max_num = nums[i]
            if min_num < nums[length - i - 1]:
                l = length - i - 1
            else:
                min_num = nums[length - i - 1]

        return r - l + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([2, 9, 10, 15]))
    print(sol.findUnsortedSubarray2([2, 10, 9, 15]))
    print(sol.findUnsortedSubarray3([2, 10, 9, 15]))
