#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/29 下午4:53
"""
"""493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。"""


class Solution:
    def reversePairs(self, nums) -> int:
        res = 0
        length = len(nums)
        for i, n in enumerate(nums[::-1], 1):
            cur = n * 2
            res += sum([nums[k] > cur for k in range(length - i)])
        return res

    def reversePairs2(self, nums) -> int:
        if not nums:
            return 0
        import bisect
        res = 0
        sorted_nums = [nums[0]]
        l = 1
        for n in nums[1:]:
            index = bisect.bisect_right(sorted_nums, n * 2)
            res += l - index
            bisect.insort(sorted_nums, n)
            l += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.reversePairs([2, 4, 3, 5, 1]))
    print(sol.reversePairs2([2, 4, 3, 5, 1]))
