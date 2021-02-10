#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/11 上午11:07
"""
"""462. 最少移动次数使数组元素相等 II
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]"""


class Solution:
    def minMoves2(self, nums) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            left += 1
            right -= 1
        return sum([abs(n - nums[left]) for n in nums])

    def minMoves22(self, nums) -> int:
        """
        中位数，a<x<b,那么移动的次数为x-a+b-x=b-a，x在a,b之间任意值，
        这题不用想什么中位数：设 a <= x <= b，将 a 和 b 都变化成 x 为最终目的，则需要步数为 x-a+b-x = b-a，
        即两个数最后相等的话步数一定是他们的差，x 在 a 和 b 间任意取；
        所以最后剩的其实就是中位数；
        :param nums:
        :return:
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            res += nums[right] - nums[left]
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMoves2([1, 2, 3]))
    print(sol.minMoves22([1, 2, 3]))
