#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/7 下午3:32
"""
"""324. 摆动排序 II
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:

输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
示例 2:

输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？"""


class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)
        if length % 2 == 0:
            half = length // 2
            nums[:half], nums[half:] = nums[:half][::-1], nums[half:][::-1]
            for i in range(half):
                nums[2 * i + 1], nums[2 * i + 2:half + i + 1] = nums[half + i], nums[2 * i + 1:half + i]
        else:
            half = length // 2
            nums[:half + 1], nums[half + 1:] = nums[:half + 1][::-1], nums[half + 1:][::-1]
            for i in range(half):
                nums[2 * i + 1], nums[2 * i + 2:half + i + 2] = nums[half + i + 1], nums[2 * i + 1:half + i + 1]
        return nums

    def wiggleSort2(self, nums) -> None:
        nums.sort(reverse=True)
        mi = len(nums) - len(nums) // 2
        nums[::2], nums[1::2] = nums[mi:], nums[:mi]
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.wiggleSort(nums=[1, 2, 2, 3]))
    print(sol.wiggleSort2(nums=[1, 2, 2, 3]))
