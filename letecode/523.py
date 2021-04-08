#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/29 下午4:01
"""
"""523. 连续的子数组和
给定一个包含 非负数 的数组和一个目标 整数 k ，编写一个函数来判断该数组是否含有连续的子数组，
其大小至少为 2，且总和为 k 的倍数，即总和为 n * k ，其中 n 也是一个整数。

示例 1：

输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 

说明：

数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。"""


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(2)]
        dp[1][-1] = nums[-1]
        for i, n in enumerate(nums[:-1][::-1], 2):
            for j in range(1, i):
                dp[0][-j] = dp[1][-j] + n
                if k == 0:
                    if dp[0][-j] == 0:
                        return True
                if k != 0 and dp[0][-j] % k == 0:
                    return True
            dp[1] = list(dp[0])
            dp[1][-i] = n
        return False

    def checkSubarraySum2(self, nums, k: int) -> bool:
        d = {0: -1}
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            if k != 0:
                cur = cur % k
            if cur in d:
                if i - d[cur] > 1:
                    return True
            else:
                d[cur] = i

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkSubarraySum([4, 6, -7, 7], k=0))
    print(sol.checkSubarraySum2([0, 0], k=0))
