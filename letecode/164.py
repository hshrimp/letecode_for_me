#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/6 下午4:00
"""
"""164. 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。"""


class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        m = 0
        for i in range(1, len(nums)):
            m = max(m, nums[i] - nums[i - 1])
        return m

    def maximumGap2(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        buk_len = (max_num - min_num) // length + 1
        buks = [[float('inf'), -float('inf')] for _ in range(length)]
        for num in nums:
            index = (num - min_num) // buk_len
            buks[index][0] = min(buks[index][0], num)
            buks[index][1] = max(buks[index][1], num)
        gap = 0
        pre = buks[0][1]
        for i in range(length):
            if buks[i][1] < 0:
                continue
            gap = max(gap, buks[i][0] - pre)
            pre = buks[i][1]
        return gap


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([3, 6, 9, 1]))
    print(sol.maximumGap2([3, 3, 3]))
