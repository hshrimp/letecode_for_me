#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/20 下午2:43
"""
"""209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 
进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。"""


class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        length = len(nums)
        res = length + 1
        begin = 0
        count = 0
        for i in range(length):
            count += nums[i]
            if count >= s:
                while count >= s:
                    res = min(res, i - begin + 1)
                    count -= nums[begin]
                    begin += 1
        return res if res != length + 1 else 0


if __name__ == '__main__':
    sol = Solution()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(sol.minSubArrayLen(s, nums))
