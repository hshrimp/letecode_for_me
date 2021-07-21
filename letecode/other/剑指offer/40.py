#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-03-31 16:59
"""
"""面试题40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000"""


class Solution:
    def getLeastNumbers(self, arr, k: int):
        i = 0
        while i < k:
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
            i += 1
        return arr[0:k]

    def getLeastNumbers2(self, arr, k):
        i = 0
        while k > i:
            m = min(arr[i:])
            index = (arr[i:]).index(m)
            arr[i], arr[i + index] = arr[i + index], arr[i]
            i += 1
        return arr[:k]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getLeastNumbers2(arr=[0, 0, 1, 2, 4, 2, 2, 3, 1, 4], k=8))
