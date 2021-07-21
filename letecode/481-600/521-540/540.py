#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/15 下午3:40
"""
"""540. 有序数组中的单一元素
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。"""


class Solution:
    def singleNonDuplicate(self, nums) -> int:
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNonDuplicate([3, 3, 7, 7, 11, 11, 12]))
