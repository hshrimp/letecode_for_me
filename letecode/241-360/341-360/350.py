#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/8 下午10:55
"""
"""350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？"""

from collections import defaultdict


class Solution:
    def intersect(self, nums1, nums2):
        def create(li):
            d = defaultdict(int)
            for n in li:
                d[n] += 1
            return d

        d1 = create(nums1)
        d2 = create(nums2)
        res = list(set(nums1) & set(nums2))
        for i in range(len(res)):
            num = min(d1[res[i]], d2[res[i]]) - 1
            if num > 0:
                res += [res[i]] * num
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersect(nums1=[4, 9, 5, 4], nums2=[9, 4, 9, 8, 4]))
