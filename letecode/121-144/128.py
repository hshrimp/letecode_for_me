#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-03 10:24
"""
"""128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。"""


class Solution:
    def longestConsecutive(self, nums) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n - 1 not in nums:
                cur = n
                cur_l = 1
                while cur + 1 in nums:
                    cur += 1
                    cur_l += 1
                res = max(res, cur_l)
        return res

    def longestConsecutive2(self, nums) -> int:
        d = {}
        res = 0
        for n in nums:
            if n not in d:
                left = d.get(n - 1, 0)
                right = d.get(n + 1, 0)
                print(d, n, left, right)
                cur = left + 1 + right
                res = max(res, cur)
                d[n] = cur
                d[n - left] = cur
                d[n + right] = cur
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive2([100, 4, 200, 1, 3, 2]))
