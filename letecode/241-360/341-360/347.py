#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/8 下午6:10
"""
"""347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。"""

from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        res = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [k[0] for k in res[:k]]

    def topKFrequent2(self, nums, k: int):
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        res = heapq.nlargest(k, d.items(), key=lambda x: x[1])
        return [k[0] for k in res]


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(sol.topKFrequent2(nums=[1, 1, 1, 2, 2, 3], k=2))
