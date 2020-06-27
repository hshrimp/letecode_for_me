#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-25 10:46
"""
"""137. 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99"""


class Solution:
    def singleNumber(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[:i] + nums[i + 1:]:
                return nums[i]

    def singleNumber2(self, nums) -> int:
        return int((sum(set(nums)) * 3 - sum(nums)) / 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber2([0, 1, 0, 1, 0, 1, 99]))
