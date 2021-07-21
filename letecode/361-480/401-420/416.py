#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/8 上午10:17
"""
"""416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集."""


class Solution:
    def canPartition(self, nums) -> bool:
        count = sum(nums)
        if count % 2 != 0:
            return False
        targrt = count // 2
        dp = []
        for num in nums:
            if num > targrt:
                return False
            if not dp:
                if num == targrt:
                    return True
                dp.append(num)
                continue
            for i in range(len(dp)):
                if dp[i] + num == targrt:
                    return True
                if dp[i] + num < targrt:
                    dp.append(dp[i] + num)
        return False

    def canPartition2(self, nums) -> bool:
        count = sum(nums)
        if count % 2 != 0:
            return False
        targrt = count // 2
        dp = set()
        for num in nums:
            if num > targrt:
                return False
            if not dp:
                if num == targrt:
                    return True
                dp.add(targrt - num)
                continue
            for n in list(dp):
                if n == num:
                    return True
                if n - num > 0:
                    dp.add(n - num)
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([2, 2, 3, 5]))
