#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/30 下午3:52
"""
"""215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums, k: int) -> int:
        from heapq import heappush, heapreplace
        heap = []
        for i in range(len(nums)):
            if i < k:
                heappush(heap, nums[i])
            else:
                if heap[0] < nums[i]:
                    heapreplace(heap, nums[i])
        return heap[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], k=2))
    print(sol.findKthLargest2([3, 2, 1, 5, 6, 4], k=2))
