#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/26 上午11:26
"""
"""795. 区间子数组个数
给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。

求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。

例如 :
输入: 
A = [2, 1, 4, 3]
L = 2
R = 3
输出: 3
解释: 满足条件的子数组: [2], [2, 1], [3].
注意:

L, R  和 A[i] 都是整数，范围在 [0, 10^9]。
数组 A 的长度范围在[1, 50000]。"""


class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            if left <= nums[i] <= right:
                l, r = i - 1, i
                while l >= 0 and nums[l] < nums[i]:
                    l -= 1
                while r < length and nums[r] <= nums[i]:
                    r += 1
                ln = max(i - l - 1, 0)
                rn = max(r - i - 1, 0)
                count += ln + rn + 1 + ln * rn
                print(i, nums[i], count, l, r, ln, rn)
        return count

    def numSubarrayBoundedMax2(self, nums, left: int, right: int) -> int:
        lastcount = 0
        lastbreak = -1
        ans = 0
        for cur in range(len(nums)):
            if nums[cur] > right:
                lastbreak = cur
                lastcount = 0
            elif nums[cur] < left:
                ans += lastcount
            else:
                lastcount = cur - lastbreak
                ans += lastcount
        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
    L = 32
    R = 69
    print(sol.numSubarrayBoundedMax(A, L, R))
    print(sol.numSubarrayBoundedMax2(A, L, R))
