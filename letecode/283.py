#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-01 15:52
"""
"""283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            zero = nums.index(0)
        else:
            return
        right = zero + 1
        while right < len(nums):
            print(nums, zero, right)
            if nums[right] != 0:
                nums[zero], nums[right] = nums[right], nums[zero]
                zero += nums[zero:].index(0)
            right += 1
        return nums

    def moveZeroes2(self, nums) -> None:
        count = nums.count(0)
        for i in range(len(nums) - count):
            while nums[i] == 0:
                print(nums, i)
                nums[i:] = nums[i + 1:] + [0]
        return nums

    def moveZeroes3(self, nums) -> None:
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.moveZeroes3([1, 2, 0, 3, 12]))
