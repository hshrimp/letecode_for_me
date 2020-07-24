#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/21 下午5:11
"""
"""220. 存在重复元素 III
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        def find(num):
            for p, q in d:
                if p <= num <= q:
                    return True
            return False

        d = []
        for i, num in enumerate(nums):
            if find(num):
                return True
            d.append((num - t, num + t))
            if len(d) > k:
                d = d[1:]
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k: int, t: int) -> bool:
        buck = {}
        if t < 0:
            return False
        for i in range(len(nums)):
            # print(buck)
            temp = nums[i] // (t + 1)
            if temp in buck:
                return True
            if temp - 1 in buck and nums[i] - buck[temp - 1] <= t:
                return True
            if temp + 1 in buck and buck[temp + 1] - nums[i] <= t:
                return True
            buck[temp] = nums[i]
            if i >= k:
                buck.pop(nums[i - k] // (t + 1))
        return False


if __name__ == '__main__':
    sol = Solution()

    print(sol.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(sol.containsNearbyAlmostDuplicate2([1, 2], 0, 1))
