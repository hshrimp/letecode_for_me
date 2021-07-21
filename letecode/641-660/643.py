#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/20 下午4:57
"""
"""643. 子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

提示：

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        return max([sum(nums[i:i + k]) / k for i in range(0, len(nums) - k + 1)])

    def findMaxAverage2(self, nums, k: int) -> float:
        length = len(nums)
        res = sum(nums[:k])
        temp = res
        for i in range(1, length - k + 1):
            temp = temp - nums[i - 1] + nums[i + k - 1]
            res = max(res, temp)
        return res / k


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], k=4))
    print(sol.findMaxAverage2([0, 4, 0, 3, 2], 1))
