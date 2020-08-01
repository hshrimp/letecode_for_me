#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/1 下午4:36
"""
"""229. 求众数 II
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]"""


class Solution:
    def majorityElement(self, nums):
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        length = len(nums) // 3 + 1
        return [k for k, v in d.items() if v >= length]

    def majorityElement2(self, nums):
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                if len(d) < 2:
                    d[n] = 1
                else:
                    for k in list(d):
                        if d[k] == 1:
                            d.pop(k)
                        else:
                            d[k] -= 1
        length = len(nums) // 3 + 1
        return [k for k in d if nums.count(k) >= length]


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
    print(sol.majorityElement2([1, 1, 1, 3, 3, 2, 2, 2]))
