#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/8 下午7:45
"""
"""321. 拼接最大数
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]"""


class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        def get(li, num):
            length = len(li)
            remove_num = length - num
            stack = []
            for i in range(length):
                while remove_num and stack and stack[-1] < li[i]:
                    stack.pop()
                    remove_num -= 1
                stack.append(li[i])
            return stack[:num]

        def combine(li1, li2):
            seq = []
            while li1 or li2:
                big = li1 if li1 > li2 else li2
                seq.append(big[0])
                big.pop(0)
            return seq

        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(k + 1):
            if i <= len1 and k - i <= len2:
                s1 = get(nums1, i)
                s2 = get(nums2, k - i)
                print(i, k - i, s1, s2)
                res = max(res, combine(s1, s2))
        return res


if __name__ == '__main__':
    sol = Solution()

    nums1 = [2, 5, 6, 4, 4, 0]
    nums2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]

    k = 15
    print(sol.maxNumber(nums1, nums2, k))
