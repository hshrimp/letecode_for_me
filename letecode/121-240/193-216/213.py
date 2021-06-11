#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-29 15:59
"""
"""213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。"""


class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        dp2 = [0] * (n - 1)
        dp2[0] = nums[1]
        dp2[1] = nums[1] if nums[1] > nums[2] else nums[2]
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 2] + nums[i + 1], dp2[i - 1])
        return max(dp[-1], dp2[-1])

    def rob2(self, nums) -> int:
        def my(nums):
            pre, cur = 0, 0
            for n in nums:
                cur, pre = max(pre + n, cur), cur
            return cur

        return max(my(nums[:-1]), my(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == '__main__':
    sol = Solution()
    s = [1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]
    print(sol.rob(s))

    print(sol.rob2(s))
