#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/8 下午3:09
"""
"""485. 最大连续1的个数
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        i = 0
        cur = 0
        while i < len(nums):
            if nums[i] == 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
            i += 1

        return max(res, cur)

    def findMaxConsecutiveOnes2(self, nums) -> int:
        nums = ''.join([str(n) for n in nums])
        nums = nums.split('0')
        return max([len(cur) for cur in nums])


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(sol.findMaxConsecutiveOnes2([1, 1, 0, 1, 1, 1]))
