#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/9 上午11:27
"""
"""327. 区间和的个数
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3 
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。"""


class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        res = 0

        for i in range(length):
            dp[i][i] = nums[i]
            if lower <= dp[i][i] <= upper:
                res += 1
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                # print(dp)
                if lower <= dp[i][j] <= upper:
                    res += 1
        return res

    def countRangeSum2(self, nums, lower: int, upper: int) -> int:
        import bisect
        res, cur, s = 0, 0, [0]
        for n in nums:
            cur += n
            res += bisect.bisect_right(s, cur - lower) - bisect.bisect_left(s, cur - upper)
            bisect.insort_right(s, cur)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
    print(sol.countRangeSum2(nums=[-2, 5, -1], lower=-2, upper=2))
