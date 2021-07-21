#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 下午5:18
"""
"""268. 缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
 
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?"""


class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if abs(nums[i]) == n:
                nums.append(-1)
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
        if n == len(nums):
            return n
        for i in range(n):
            if nums[i] > 0:
                return i
        return nums.index(0)

    def missingNumber2(self, nums) -> int:
        return sum(i for i in range(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([2, 0]))
    print(sol.missingNumber2([9,6,4,2,3,5,7,0,1]))
