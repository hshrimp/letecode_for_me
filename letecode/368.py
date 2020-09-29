#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/25 上午11:27
"""
"""368. 最大整除子集
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

示例 1:

输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)
示例 2:

输入: [1,2,4,8]
输出: [1,2,4,8]"""


class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        res = {nums[0]: [nums[0]]}
        for num in nums[1:]:
            l = [num]
            for v in res.values():
                if num % v[-1] == 0 and len(l) < len(v) + 1:
                    l = list(v) + [num]
            res[num] = l
        n = nums[0]
        ml = 1
        for k, v in res.items():
            if len(v) > ml:
                ml = len(v)
                n = k
        return res[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset([5, 9, 18, 54, 108, 540, 90, 180, 360, 720]))
