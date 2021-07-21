#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/8 下午10:44
"""
"""349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 
说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""


class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = (nums1 | nums2) - (nums1 - nums2) - (nums2 - nums1)
        return list(res)

    def intersection2(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = nums1 - (nums1 - nums2)
        return list(res)

    def intersection3(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    print(sol.intersection2(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    print(sol.intersection3(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
