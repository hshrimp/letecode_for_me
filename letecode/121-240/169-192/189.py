#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/14 下午8:40
"""
"""189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。"""


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            temp = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = temp
            k -= 1

        return nums

    def rotate2(self, nums, k: int) -> None:
        k = k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp
        return nums

    def rotate3(self, nums, k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(sol.rotate(nums, k))
    nums = [1, 2, 3, 4, 5, 6, 7]

    print(sol.rotate2(nums, k))
    nums = [1, 2, 3, 4, 5, 6, 7]

    print(sol.rotate3(nums, k))
