#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/21 下午3:49
"""
"""658. 找到 K 个最接近的元素
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
 

示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
 

提示：

1 <= k <= arr.length
1 <= arr.length <= 104
数组里的每个元素与 x 的绝对值不超过 104"""


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - 1
        while r - l > k - 1:
            if x - arr[l] <= arr[r] - x:
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
