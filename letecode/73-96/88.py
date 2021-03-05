#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-25 09:49
"""
"""给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(n):
            while j < m:
                print(nums1, m, nums2, n, i, j)
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    j += 1
                    m += 1
                    nums1.pop()
                    break
                elif nums2[i] > nums1[j]:
                    j += 1
            else:
                nums1[m] = nums2[i]
                m += 1
        return nums1

    def merge2(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1


if __name__ == '__main__':
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(sol.merge(nums1, m, nums2, n))
    print(sol.merge2(nums1, m, nums2, n))
