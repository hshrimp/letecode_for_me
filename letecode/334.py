#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/10 下午3:59
"""
"""334. 递增的三元子序列
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false"""


class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False
        dp = [1]
        for n in nums[1:]:
            dp.append(max([dp[i] + 1 for i in range(len(dp)) if n > nums[i]] + [1]))
            if dp[-1] == 3:
                return True
        return False

    def increasingTriplet2(self, nums) -> bool:
        length = len(nums)
        if length < 3:
            return False
        small = [nums[0]]
        big = [nums[-1]]
        for i in range(1, length):
            small.append(min(nums[i], small[-1]))
            big.append(max(big[-1], nums[length - 1 - i]))
        big = big[::-1]
        for i in range(1, length - 1):
            if small[i - 1] < nums[i] < big[i + 1]:
                return True
        return False

    def increasingTriplet3(self, nums) -> bool:
        r1, r2 = float('inf'), float('inf')
        for n in nums:
            if n < r1:
                r1 = n
            elif n < r2:
                r2 = n
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.increasingTriplet([1, 4, 4, 4, 3]))
    print(sol.increasingTriplet2([1, 4, 3, 4, 3]))
    print(sol.increasingTriplet3([1, 4, 3, 4, 3]))
