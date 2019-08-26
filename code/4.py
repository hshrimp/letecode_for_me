#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-07 14:29
"""
from _ast import List

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        point = 0
        for j in range(len(nums1)):
            # temp = nums2[point:]
            for i in range(point, len(nums2)):
                if nums1[j] <= nums2[i]:
                    nums2.insert(i, nums1[j])
                    point = i + 1
                    break
            else:
                nums2.extend(nums1[j:])
                break

        length = len(nums2)
        if length % 2 == 0:
            return (nums2[length // 2] + nums2[length // 2 - 1]) / 2
        else:
            return nums2[length // 2]


if __name__ == '__main__':
    nums1 = [3]
    nums2 = [-2,-1]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
