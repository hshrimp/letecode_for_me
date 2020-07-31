#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/21 下午4:30
"""
"""219. 存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false"""


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
            elif i - d[num] <= k:
                return True
        else:
            return False

    def containsNearbyDuplicate2(self, nums, k: int) -> bool:
        d = set()
        for i, num in enumerate(nums):
            if num not in d:
                d.add(num)
                if len(d) > k:
                    d.remove(nums[i - k])
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))
